# Installation guide

This is a pretty standard django app, install should be like this (tested on Ubuntu 20.04):  

\# Install python3-venv if not available  
**sudo apt install python3-venv**

\# Configure venv  
**python3 -m venv venv**

\# Active venv environment (a '(venv)' propmt will show up)  
**. venv/bin/activate**

\# Install required libs and dependencies  
**pip3 install -r requirements.txt**

\# Adapt/update your Django model  
**./manage.py migrate**

\# Create a superuser for the admin interface  
**./manage.py createsuperuser**

\# Run the server  
**./manage.py runserver**  

**Now you can use your browser to access the server on http://127.0.0.1:8000**

Or the same with Nix:  
\# start nix-shell  
**./manage.py migrate**  
**./manage.py createsuperuser**
**./mange.py runserver**
