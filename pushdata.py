import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import time
from datetime import datetime
import json


token = 'L5kqdkWZRdb6wCuGEmTzn5v6faNjQEn9859sxdkvJcGOsyHeMIC59pUUJt706SkD47sQ2MY5hS1a3IsU8wXXDg=='
org = "organization"
url = "http://localhost:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

json_open = open('./weather20240203.json', 'r')
json_load = json.load(json_open)

bucket="temp"
write_api = write_client.write_api(write_options=SYNCHRONOUS)

for key in json_load:
    try:
        print(key,":",json_load[key]['temp'][0])
        p = (
            Point("ap_mesurement")
            .tag("location", key)
            .field("low_temp", json_load[key]['temp'][0])
            .field("high_temp", json_load[key]['temp'][1])
        )

        write_api.write(bucket=bucket, record=p)

    except:
        print("error:",key)

