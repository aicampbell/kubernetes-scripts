from kubernetes import client, config

NAMESPACE='jhub'

def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_namespaced_pod(namespace=NAMESPACE, watch=False)
    for i in ret.items:
        print("%s\t%s\t%s\t%s" %
              (i.status.pod_ip, i.status.host_ip, i.metadata.namespace, i.metadata.name))


if __name__ == '__main__':
    main()
