# This is a Work in Progress! 
# Samples and Code Snippets coming soon!

import os

import wrapt

from kubernetes.client.configuration import Configuration
from kubernetes.config.incluster_config import load_incluster_config
from kubernetes.client.api_client import ApiClient
from kubernetes.client.rest import ApiException
from openshift.dynamic import DynamicClient


load_incluster_config()

import urllib3
urllib3.disable_warnings()
instance = Configuration()
instance.verify_ssl = False
Configuration.set_default(instance)
