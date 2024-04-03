#!/usr/bin/env python3
'''task 2'''


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''get page'''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''get page'''
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        dataset = self.dataset()
        total_pages = len(dataset) // page_size + (
            1 if len(dataset) % page_size != 0 else 0)
        data = dataset[start_index:end_index]
        next_page = page + 1 if end_index < len(dataset) else None
        prev_page = page - 1 if start_index > 0 else None
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
