# Network Monitoring

The goal of this project is to have the publisher service run on an external device (or the same one) and to periodically monitor the network and forward the data to the MQTT broker.
Then, the subscriber service will consume the MQTT message and store it as time series data.
