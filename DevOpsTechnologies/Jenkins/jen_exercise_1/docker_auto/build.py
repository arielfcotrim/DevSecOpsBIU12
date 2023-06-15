import os

image_name = os.environ.get("IMAGE_NAME")
image_version = os.environ.get("IMAGE_VERSION")

os.system(f'docker build -t {image_name}:{image_version} .')