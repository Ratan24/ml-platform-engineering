# base image - layer
FROM python:3.10-slim-bookworm
# setting the working directory - layer
WORKDIR /app 

# updating the base image - layer 
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    build-essential \
    && apt-get clean && rm -rf /tmp/* /var/tmp/* 

# copy requirements.txt to the working directory - layer 
COPY requirements.txt /app/requirements.txt 
# upgrade pip - layer 
RUN pip3 install --upgrade pip 
# install dependencies - layer 
RUN pip3 install --no-cache-dir -r requirements.txt 

# copy the application code - layer 
COPY . /app 

# expose the port - layer
EXPOSE 8083 

# set the python path - layer
ENV PYTHONPATH="/app" 

# change the permissions of the entrypoint script - layer 
RUN chmod +x /app/entrypoint.sh 

# set the entrypoint - layer 
ENTRYPOINT ["/app/entrypoint.sh"] 

# docker follows layer caching.