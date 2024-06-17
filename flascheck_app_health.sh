#!/bin/bash

# Get the public IP address of the EC2 instance
instance_ip=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4)

# Perform HTTP request to the web app and check the response
response=$(curl -s -o /dev/null -w "%{http_code}" http://${instance_ip}:8000)

# Log the status
echo "$(date '+%Y-%m-%d %H:%M:%S') - Application status: $response" >> /var/log/app_health.log
