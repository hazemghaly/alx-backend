import redis from 'redis';

const client = redis.createClient()

  client.on('error', ERROR_MESSAGE  => console.log(`Redis client not connected to the server: ${ERROR_MESSAGE }`))
  client.on('connect', () => {
    console.log('Redis client connected to the server')})

async function publishMessage(message, time) {
  await new Promise(resolve => setTimeout(resolve, time)); // Wait for the specified time
  
  if (client.connected) {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  } else {
    console.error('Redis client not connected. Cannot publish message.');
  }
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
