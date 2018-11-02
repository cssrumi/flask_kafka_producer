# flask_kafka_producer
On windows:
1. To send message:
curl -i -X POST -H "Content-Type: application/json" -d "{\\"user\\":\\"username\\",\\"token\\":\\"token\\"}" http://127.0.0.1:5000/api/message/producer

2. To set user name and get token
curl -i -X GET -H "Content-Type: application/json" -d "{\\"user\\":\\"username\\"}" http://127.0.0.1:5000/api/message/producer

3. To check if user is existing:
curl -i -X GET -H "Content-Type: application/json" -d "{\\"user\\":\\"username\\"}" http://127.0.0.1:5000/api/user/is_exist

4. To check if user token is valid (or if he is authorized)
curl -i -X GET -H "Content-Type: application/json" -d "{\\"user\\":\\"username\\",\\"token\\":\\"token\\"}" http://127.0.0.1:5000/api/user/is_auth

On Linux:
1. To send message:
curl -i -X POST -H "Content-Type: application/json" -d "{"user":"username","token":"token"}" http://127.0.0.1:5000/api/message/producer

2. To set user name and get token
curl -i -X GET -H "Content-Type: application/json" -d "{"user":"username"}" http://127.0.0.1:5000/api/message/producer

3. To check if user is existing:
curl -i -X GET -H "Content-Type: application/json" -d "{"user":"username"}" http://127.0.0.1:5000/api/user/is_exist

4. To check if user token is valid (or if he is authorized)
curl -i -X GET -H "Content-Type: application/json" -d "{"user":"username","token":"token"}" http://127.0.0.1:5000/api/user/is_auth
