from subprocess import call
from kubernetes import config, client
import os

NAMESPACE = os.environ['NAMESPACE']
config.load_incluster_config()

kubernetescorev1 = client.CoreV1Api()

for pod in kubernetescorev1.list_namespaced_pod(NAMESPACE, field_selector='status.phase=Succeeded').items:
    print('Deleted succeeded pod %s in namespace %s' % (pod.metadata.name, NAMESPACE))
    kubernetescorev1.delete_namespaced_pod(pod.metadata.name,NAMESPACE)
