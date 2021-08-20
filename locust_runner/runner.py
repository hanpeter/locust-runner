# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
import yaml
from locust import HttpUser, TaskSet, between


class Config(dict):
    def __init__(self, config_file):
        # Call super class and be a good Python class
        super(Config, self).__init__()

        with open(config_file) as f:
            self.update(yaml.safe_load(f))


def task_builder(url, config):
    def task(locust):
        locust.client.request(
            method=config.get('method', 'GET'),
            url=url,
            headers=config.get('headers', {}),
            params=config.get('params', {}),
            auth=config.get('auth', None)
        )

    return task


config = Config(config_file=os.path.join(os.path.dirname(__file__), '..', 'config.yaml'))
domain = next(key for key in config.keys() if key != 'min_wait' and key != 'max_wait' and key != 'ssl')

task_list = []
for url, config in config[domain].items():
    task_list.append(task_builder(url, config))

attributes = {
    'tasks': task_list,
    'wait_time': between(
        config.get('min_wait', 1), config.get('max_wait', 1)
    ),
    'host': ('https://' if config.get('ssl', True) else 'http://') + domain,
}

User = type('User', (HttpUser,), attributes)
