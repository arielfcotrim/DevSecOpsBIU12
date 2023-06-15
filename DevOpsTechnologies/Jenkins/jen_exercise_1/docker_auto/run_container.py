from build import image_name, image_version
import os

host_port = os.environ.get('HOST_PORT')
container_port = os.environ.get('CONTAINER_PORT')

os.system(f'docker run -p {host_port}:{container_port} --name{input("Enter a name for the container: ")} -d {image_name}:{image_version}')
