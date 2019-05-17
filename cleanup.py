from subprocess import call
from kubernetes import config, client
import os

NAMESPACE = os.environ['NAMESPACE']
config.load_incluster_config()

kubernetescorev1 = client.CoreV1Api()

succeeded_pods = kubernetescorev1.list_namespaced_pod(NAMESPACE, field_selector='status.phase=Succeeded').items
failed_pods = kubernetescorev1.list_namespaced_pod(NAMESPACE, field_selector='status.phase=Failed').items
for pod in succeeded_pods + failed_pods:
    print('Deleted succeeded pod %s in namespace %s' % (pod.metadata.name, NAMESPACE))
    kubernetescorev1.delete_namespaced_pod(pod.metadata.name,NAMESPACE)
