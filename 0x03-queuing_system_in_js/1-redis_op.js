import redis from 'redis';

const client = redis.createClient()

  client.on('error', ERROR_MESSAGE  => console.log(`Redis client not connected to the server: ${ERROR_MESSAGE }`))
  client.on('connect', () => {
    console.log('Redis client connected to the server')})

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
  }

function displaySchoolValue(schoolName){
    client.get(schoolName, (err, value) => {
      console.log(`${value}`)
    });}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
