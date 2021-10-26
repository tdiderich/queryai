import os
import time
from client.client import Client
from datetime import datetime, timedelta

client = Client()

def run_standard_command_with_relative_lookback(query, platform_alias, relative_lookback_minutes):
    path = 'command'
    currentEpochTime = datetime.utcnow()
    relativeEpochTime = currentEpochTime - timedelta(minutes=relative_lookback_minutes)
    payload = {
        "query": query,
        "alias": platform_alias,
        "start_time": str(relativeEpochTime.timestamp()),
        "end_time": str(currentEpochTime.timestamp()),
        "org_name": os.environ['org_name'],
        "timeout": 300
        }
    command_results = client.post(path=path, payload=payload)
    return command_results

def check_async_command_status(tracking_id):
    gathering_results = True
    while gathering_results:
        command_results = client.get(path='command_async', params={'tracking_id': tracking_id})
        if command_results.json()['status'] == 'SUCCESS':
            gathering_results = False
        else:
            time.sleep(5)
    return command_results

def run_async_command_with_relative_lookback(query, platform_alias, relative_lookback_minutes):
    path = 'command_async'
    currentEpochTime = datetime.utcnow()
    relativeEpochTime = currentEpochTime - timedelta(minutes=relative_lookback_minutes)
    payload = {
        "query": query,
        "alias": platform_alias,
        "start_time": str(relativeEpochTime.timestamp()),
        "end_time": str(currentEpochTime.timestamp()),
        "org_name": os.environ['org_name'],
        "timeout": 300
        }
    start_command = client.post(path, payload)
    tracking_id = start_command.json()['tracking_id']
    command_results = check_async_command_status(tracking_id)
    return command_results

if __name__ == '__main__':
    query = "<command> cs-falcon-search-device"
    platform_alias = "crowdstrike_falcon"
    command_results = run_async_command_with_relative_lookback(query, platform_alias, 30)
    print(command_results.json())