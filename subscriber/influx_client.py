import os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


bucket = os.getenv("INFLUXDB_BUCKET")
org = os.getenv("INFLUXDB_ORG")
token = os.getenv("INFLUXDB_TOKEN")


def insert_measurements(ping_metrics_json):
    with InfluxDBClient(url="http://influxdb:8086", token=token, org=org) as client:
        point = Point("ping_metrics") \
            .field("avg_latency", ping_metrics_json["avg_latency"]) \
            .field("avg_packet_loss", ping_metrics_json["avg_packet_loss"]) \
            .field("avg_jitter", ping_metrics_json["avg_jitter"])
        write_api = client.write_api(write_options=SYNCHRONOUS)

        write_api.write(bucket=bucket, record=point)
