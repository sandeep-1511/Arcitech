# Arcitech

Here is a comprehensive guide to completing the task.

## 1. Set Up an EC2 Instance
Launch EC2 Instance:

Sign in to the AWS Management Console.
Navigate to EC2 Dashboard.
Click "Launch Instance".
Choose the Ubuntu AMI (e.g., "Ubuntu Server 20.04 LTS (HVM), SSD Volume Type").
Select the instance type t2.micro.
Configure instance details, add storage, and configure security groups (allow SSH and HTTP/port 80).
Review and launch the instance. Download the key pair for SSH access.
SSH into the Instance:

Open your terminal and SSH into the instance using the key pair:
sh
Copy code
ssh -i "path_to_key_pair.pem" ubuntu@your_instance_public_dns
Install Necessary Software:

sh
Copy code
sudo apt update
sudo apt install -y python3 python3-pip git nginx
## 2. Deploy a Simple Web Application
Create a Simple Flask Application:

Create a new directory and a file for the Flask app:
sh
Copy code
mkdir flask
cd flask
python3 -m venv venv
source venv/bin/activate
pip install flask gunicorn

nano hellopy
Add the following code to hello.py:
python
Copy code

         from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


Set Up Gunicorn:

Install Gunicorn:
sh
Copy code
pip3 install gunicorn flask
Test the Flask app with Gunicorn:
sh
Copy code
gunicorn --bind 0.0.0.0:8000 hello:app

## Configure Nginx:

Create an Nginx configuration for your Flask app:
sh


sudo nano /etc/nginx/sites-available/myapp
Add the following configuration:
nginx
Copy code


server {
    listen 80;
    server_name your_domain_or_public_IP;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

Enable the configuration and restart Nginx:
sh
Copy code
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx

## 3. Configure S3 for Static File Hosting
Create an S3 Bucket:

Navigate to the S3 console and create a bucket named devops-assignment-sandeep.
Upload a File:

Upload a file (introduction.txt) to the bucket.
Set permissions to make the file publicly accessible.

## 4. Set Up a CI/CD Pipeline
Create a GitHub Repository:

Create a new repository on GitHub and clone it to your local machine.
Add the Flask App to the Repository:

Initialize a Git repository and push the Flask app:
sh
Copy code
git init
git remote add origin your_repo_url
git add .
git commit -m "Initial commit"
git push -u origin branch name 

## 5. Manage Access and Permissions
Set Up IAM Roles and Policies:

Create an IAM role with S3 access and attach it to the EC2 instance.
Configure Security Groups:

Ensure the EC2 security group allows HTTP (port 80) and SSH (port 22) traffic.
## 6. Automation and Scheduling
Write a Cron Job Script:

Create a health check script:
sh
Copy code
nano flascheck_app_health.sh
Add the following code:
sh
Copy code
#!/bin/bash
if curl -s --head  --request GET http://localhost | grep "200 OK" > /dev/null; then 
    echo "The application is running" 
else 
    echo "The application is NOT running" 
fi
Make it executable:
sh
Copy code
chmod +x flascheck_app_health.sh
Set Up Cron Job:

Edit the crontab file:
sh
Copy code
crontab -e
Add the following line to run the script every 5 minutes:
sh
Copy code
*/5 * * * * /path_to_script/flascheck_app_health.sh >> /path_to_log/health_check.log 2>&1
Schedule EC2 Start/Stop:

Create Lambda functions and CloudWatch Events to start/stop the instance at specified times.

Every thing I have done we can see them in files .

## challenges faced 

1.I faced many challenges while setting up flask . when i installed it it picking globally which makes flask unavialble for the venu environment .
2. when i setting it in jenkins file for cicd it asking sudo password and new tab to run .
3. I faced when lambda fuction running the ip address dynamically changing that has to be reflected on the file.

