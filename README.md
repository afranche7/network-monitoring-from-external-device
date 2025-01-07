# Network Monitoring using MQTT broker and Influx database

The goal of this project is to have the publisher service run on an external device (or the same one) and 
to periodically monitor the network and forward the data to the MQTT broker.
Then, the subscriber service will consume the MQTT message and store it as time series data in the influx database.

## Ping Metrics in InfluxDB UI
### All metrics graph
![Capture 3](https://github.com/user-attachments/assets/8a570601-7ce1-4bb2-9c0e-8c28577aa3fc)
### Jitter
![Capture 4](https://github.com/user-attachments/assets/96929308-725d-4de3-bd3d-6a2abb0379be)
### Latency
![Capture 5](https://github.com/user-attachments/assets/7eca44db-5b2d-4afd-be24-5dc7ae984539)


## How it works
Every 5 seconds the publisher service will start a NetworkMonitor to measure ping metrics.
To collect ping metrics, the NetworkMonitor will ping 3 times each of these sites:
"google.com", "facebook.com", "twitter.com", "youtube.com", "amazon.com".

The three metrics collected are latency, jitter and packet loss, which are calculated as follows:
- Average latency = sum of latency values / total number of latency data points
- Average jitter = maximum latency - minimum latency
- Average Packet loss % = (loss count / (number of pings per site * number of sites) * 100)

Once the metrics are collected, the publisher will send the metrics to the topic of the MQTT broker.

The subscriber service will listen to the topic, collect metrics and insert them in the influx database.
The metrics are inserted in the bucket "network-metrics" as "ping_metrics" measurement with fields "avg_latency", "avg_packet_loss" and "avg_jitter".

## How to run project on one host
1. In the root of the project run "docker compose build"
2. In the root of the project run "docker compose up"
3. Access influx database UI at http://localhost:8086/ (username "admin" and password "Admin1234!")
4. Navigate to "Data Explorer" tab, then the bucket "network-metrics", finally under measurement "ping_metrics" the three metric fields will be available to select / query.
