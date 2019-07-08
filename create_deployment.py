from os import path

import yaml

from kubernetes import client, config

DEPLOYMENT_NAME = "nginx"


def create_deployment_object():
    # Configureate Pod template container
    container = client.V1Container(
        name="nginx",
        image="nginx",
        ports=[client.V1ContainerPort(container_port=80)])
    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "nginx"}),
        spec=client.V1PodSpec(containers=[container]))
    # Create the specification of deployment
    spec = client.ExtensionsV1beta1DeploymentSpec(
        replicas=1,
        template=template,
        selector = client.V1LabelSelector(match_labels={"app": "nginx"})
        )
    # Instantiate the deployment object
    deployment = client.ExtensionsV1beta1Deployment(
        api_version="extensions/v1beta1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=DEPLOYMENT_NAME),
        spec=spec)

    return deployment


def create_deployment(api_instance, deployment):
    # Create deployement
    api_response = api_instance.create_namespaced_deployment(
        body=deployment,
        namespace="default")
    print("Deployment created. status='%s'" % str(api_response.status))

if __name__ == '__main__':
    config.load_kube_config()
    extensions_v1beta1 = client.ExtensionsV1beta1Api()
    # Create a deployment object with client-python API.
    deployment = create_deployment_object()

    create_deployment(extensions_v1beta1, deployment)

