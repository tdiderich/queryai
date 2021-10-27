import os
import time
from client.client import Client
from datetime import datetime, timedelta

client = Client()


def run_standard_workflow_with_relative_lookback(workflow: str, platform_alias: str, relative_lookback_minutes: int):
    path = 'workflow'
    currentEpochTime = datetime.utcnow()
    relativeEpochTime = currentEpochTime - \
        timedelta(minutes=relative_lookback_minutes)
    payload = {
        "workflow": workflow,
        "aliases": platform_alias,
        "start_time": str(relativeEpochTime.timestamp()),
        "end_time": str(currentEpochTime.timestamp()),
        "org_name": os.environ['org_name'],
        "timeout": 300
    }
    workflow_results = client.post(path=path, payload=payload)
    return workflow_results


def check_async_workflow_status(tracking_id: str):
    gathering_results = True
    while gathering_results:
        workflow_results = client.get(path='workflow_async', params={
                                      'tracking_id': tracking_id})
        if workflow_results.json()['status'] == 'SUCCESS':
            gathering_results = False
        else:
            time.sleep(5)
    return workflow_results


def run_async_workflow_with_relative_lookback(workflow: str, platform_alias: str, relative_lookback_minutes: int):
    path = 'workflow_async'
    currentEpochTime = datetime.utcnow()
    relativeEpochTime = currentEpochTime - \
        timedelta(minutes=relative_lookback_minutes)
    payload = {
        "workflow": workflow,
        "alias": platform_alias,
        "start_time": str(relativeEpochTime.timestamp()),
        "end_time": str(currentEpochTime.timestamp()),
        "org_name": os.environ['org_name'],
        "timeout": 300
    }
    start_workflow = client.post(path, payload)
    tracking_id = start_workflow.json()['tracking_id']
    workflow_results = check_async_workflow_status(tracking_id)
    return workflow_results


if __name__ == '__main__':
    workflow = "New Elastic Summary"
    platform_alias = "elastic_us"
    workflow_results = run_async_workflow_with_relative_lookback(
        workflow=workflow, platform_alias=platform_alias, relative_lookback_minutes=30)
    print(workflow_results.json())
