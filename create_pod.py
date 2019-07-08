import hashlib
import string
import random
import logging
import yaml
import sys,os, time
from kubernetes import client, config, utils
import kubernetes.client
from kubernetes.client.rest import ApiException

def id_generator(size=12, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# Set logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# Setup K8 configs
config.load_kube_config()
configuration = kubernetes.client.Configuration()
api_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(configuration))

# Scipy notebook
container_image = "jupyter/scipy-notebook"
container_name = id_generator()

# Set the hardware requirements for the container
# Requests are the minimum hardware requirements
# Limits are the maximum hardware requirements
# Always requests <= limits
resource = client.V1ResourceRequirements(requests={'cpu':'2', 'memory': '4Gi'}, limits={'cpu':'4', 'memory': '8Gi'})
container = client.V1Container(name=container_name, image=container_image, resources=resource)

body = client.V1Pod()
body.spec = client.V1PodSpec(containers=[container])
body.metadata = client.V1ObjectMeta(namespace='default', name=container_name)

api_instance.create_namespaced_pod(namespace='default',body=body)

