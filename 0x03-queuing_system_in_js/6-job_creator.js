import kue from 'kue';

const queue = kue.createQueue({ name: 'push_notification_code' });

const job = queue.create('push_notification_code', {
  phoneNumber: '01239',
  message: 'Acc',
});

job.on('enqueue', () => {
  console.log('Notification job created:', job.id);
  }).on('failed attempt', () => {
  	console.log('Notification job failed');
	}).on('complete', () => {
		console.log('Notification job completed');
	});
job.save();
