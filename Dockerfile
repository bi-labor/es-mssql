# Use the official Elasticsearch Docker image as base
FROM docker.elastic.co/elasticsearch/elasticsearch-oss:6.6.0

# Set the environmert variables required by Elasticsearch
ENV cluster.name=bilab-cluster
ENV discovery.type=single-node

# Install python 3.5 and the elasticsearch module
RUN yum install -q -y https://centos7.iuscommunity.org/ius-release.rpm && \
    yum install -q -y python35u python35u-pip && \
    yum clean -q all && \
    python3.5 -m pip install -q elasticsearch==6.3.1

# Copy the (slightly modified) entrypoint shell script
COPY --chown=1000:0 ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

# Copy initializer files and the evaluator tests into the container
COPY ["./evaluator", "/tmp/evaluator"]
WORKDIR "/tmp/evaluator"

# Initialize the 'salaries' index in Elasticsearch
RUN /usr/local/bin/docker-entrypoint.sh eswrapper &> /dev/null && \
    python3.5 ./init.py 2>/dev/null && \
    ES_PID=$(cat /tmp/elasticsearch-pid) && \
    kill -15 $ES_PID && \
    while $(kill -0 $ES_PID 2>/dev/null); do sleep 1; done;

ENTRYPOINT /usr/local/bin/docker-entrypoint.sh eswrapper &> /dev/null && \
           python3.5 -m unittest discover -c -v && \
           ES_PID=$(cat /tmp/elasticsearch-pid) && \
           kill -15 $ES_PID && \
           while $(kill -0 $ES_PID 2>/dev/null); do sleep 1; done;
