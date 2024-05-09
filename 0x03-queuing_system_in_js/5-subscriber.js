import redis from 'redis';

const client = redis.createClient()

  client.on('error', ERROR_MESSAGE  => console.log(`Redis client not connected to the server: ${ERROR_MESSAGE }`))
  client.on('connect', () => {
    console.log('Redis client connected to the server')})

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
