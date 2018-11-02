# flask_kafka_producer
On windows:
<<<<<<< HEAD
1. To send message if token is valid (and to refresh token authentication time):
=======
1. To send message:
>>>>>>> b054f92f29677cffd63b3606f4b3fe39c94aada2
curl -i -X POST -H "Content-Type: application/json" -d "{\\"user\\":\\"username\\",\\"token\\":\\"token\\",\\"message\\":\\"message\\"}" http://127.0.0.1:5000/api/message/producer

2. To set user name and get token:
curl -i -X GET -H "Content-Type: application/json" -d "{\\"user\\":\\"username\\"}" http://127.0.0.1:5000/api/message/producer

3. To check if user is existing:
curl -i -X GET -H "Content-Type: application/json" -d "{\\"user\\":\\"username\\"}" http://127.0.0.1:5000/api/user/is_exist

4. To check if user token is valid (or if he is authorized):
curl -i -X GET -H "Content-Type: application/json" -d "{\\"user\\":\\"username\\",\\"token\\":\\"token\\"}" http://127.0.0.1:5000/api/user/is_auth

On Linux:
1. To send message:
curl -i -X POST -H "Content-Type: application/json" -d "{"user":"username","token":"token","message":"message"}" http://127.0.0.1:5000/api/message/producer

2. To set user name and get token:
curl -i -X GET -H "Content-Type: application/json" -d "{"user":"username"}" http://127.0.0.1:5000/api/message/producer

3. To check if user is existing:
curl -i -X GET -H "Content-Type: application/json" -d "{"user":"username"}" http://127.0.0.1:5000/api/user/is_exist

4. To check if user token is valid (or if he is authorized):
curl -i -X GET -H "Content-Type: application/json" -d "{"user":"username","token":"token"}" http://127.0.0.1:5000/api/user/is_auth
