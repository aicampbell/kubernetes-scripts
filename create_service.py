from kubernetes import client, config
config.load_kube_config()
api_instance = client.CoreV1Api()
service = client.V1Service()



service.api_version = "v1"
service.kind = "Service"
service.metadata = client.V1ObjectMeta(name="nginx")

spec = client.V1ServiceSpec()
spec.selector = {"app": "nginx"}
spec.ports = [client.V1ServicePort(protocol="TCP", port=80, target_port=80)]
spec.type = 'NodePort'
service.spec = spec

api_instance.create_namespaced_service(namespace="default", body=service)
