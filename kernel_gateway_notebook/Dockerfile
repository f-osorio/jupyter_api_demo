# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
FROM jupyter/all-spark-notebook:15a66513da30

EXPOSE 9001

# Install Kernel Gateway and modules
RUN pip install jupyter_kernel_gateway
RUN pip install mysql-connector-python

# Configure container startup
ENTRYPOINT ["tini", "--", "jupyter", "kernelgateway"]


CMD [ \
        "--KernelGatewayApp.api=notebook-http", \
        "--KernelGatewayApp.seed_uri=/srv/notebooks/metrics_api.ipynb", \
        "--KernelGatewayApp.allow_methods='GET'", \
        "--KernelGatewayApp.allow_headers='accept, accept-language, content-type'", \
        "--KernelGatewayApp.ip=0.0.0.0" \
    ]

ADD metrics_api.ipynb /srv/notebooks/

