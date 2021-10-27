import os
import time
from client.client import Client
from datetime import datetime, timedelta

client = Client()

def run_standard_search_with_relative_lookback(query: str, platform_aliases: str, relative_lookback_minutes: int):
    path = 'search'
    currentEpochTime = datetime.utcnow()
    relativeEpochTime = currentEpochTime - timedelta(minutes=relative_lookback_minutes)
    payload = {
        "query": query,
        "aliases": platform_aliases,
        "start_time": str(relativeEpochTime.timestamp()),
        "end_time": str(currentEpochTime.timestamp()),
        "org_name": os.environ['org_name'],
        "timeout": 300
        }
    search_results = client.post(path=path, payload=payload)
    return search_results

def check_async_search_status(tracking_id: str):
    gathering_results = True
    while gathering_results:
        search_results = client.get(path='search_async', params={'tracking_id': tracking_id})
        if search_results.json()['status'] == 'SUCCESS':
            gathering_results = False
        else:
            time.sleep(5)
    return search_results

def run_async_search_with_relative_lookback(query: str, platform_aliases: str, relative_lookback_minutes: int):
    path = 'search_async'
    currentEpochTime = datetime.utcnow()
    relativeEpochTime = currentEpochTime - timedelta(minutes=relative_lookback_minutes)
    payload = {
        "query": query,
        "aliases": platform_aliases,
        "start_time": str(relativeEpochTime.timestamp()),
        "end_time": str(currentEpochTime.timestamp()),
        "org_name": os.environ['org_name'],
        "timeout": 300
        }
    start_search = client.post(path, payload)
    tracking_id = start_search.json()['tracking_id']
    search_results = check_async_search_status(tracking_id)
    return search_results

if __name__ == '__main__':
    query = "Alert = *"
    platform_aliases = "S3_CarbonBlack, Splunk_au"
    search_results = run_async_search_with_relative_lookback(query=query, platform_aliases=platform_aliases, relative_lookback_minutes=30)
    print(search_results.json())