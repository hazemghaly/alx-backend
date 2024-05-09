import { createClient } from 'redis';

const client = createClient()

  client.on('error', ERROR_MESSAGE  => console.log(`Redis client not connected to the server: ${ERROR_MESSAGE }`))
  client.on('connect', () => {
    console.log('Redis client connected to the server')})

function setNewSchool(schoolName,value){
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error('Error setting school value:', err);
    } else {
      console.log(`Replay: ${reply}`);
    }
  });}

function displaySchoolValue(schoolName){
  client.get(schoolName, (err, value) => {
    if (err) {
      console.error('Error getting school value:', err);
    } else {
      console.log(value);
    }
  });}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
