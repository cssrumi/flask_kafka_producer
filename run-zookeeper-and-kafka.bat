@ECHO OFF
cd D:\Kafka\kafka_2.11-2.0.0\bin\windows\
start "" zookeeper-server-start.bat "..\..\config\zookeeper.properties"
timeout /t 7 /nobreak
start "" kafka-server-start.bat "..\..\config\server.properties"
exit 0