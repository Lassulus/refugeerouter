# Introduction  

The **Refugeerouter** software helps volunteers of a German refugee initiative to pick up Ukrainian refugees at the Polish border in Chelm, bring them to Berlin temporarily and find available long-term accommodation for them. The current software to match housing requests and offers consists mainly of Excel files. Refugeerouter aims to simplify that and eventually replace the previous solution. It relies on the open-source Django framework written in Python. More information [here](https://github.com/Lassulus/refugeerouter/docs/).  

# Installation guide  

This is a pretty standard django app, install should be like this (tested on Ubuntu 20.04):  

\# Fork this app in your own Github repository, using the "Fork" button on Github  

\# Then clone this app from your repo  
**git clone https://github.com/\<yourrepo\>/refugeerouter.git**  

\# Enter cloned repo locally  
**cd refugeerouter**  

\# Install python3-venv if not available (if the next command fails)  
**sudo apt install python3-venv**

\# Configure venv  
**python3 -m venv venv**

\# Active venv environment (a '(venv)' prompt will show up)  
**. venv/bin/activate**

\# Install required libs and dependencies  
\# This has to repeat if you update the repo later  
**pip3 install -r requirements.txt**

\# Adapt/update your Django model  
\# This has to repeat if you update your repo later  
**./manage.py migrate**

\# Create a superuser for the admin interface  
**./manage.py createsuperuser**

\# Run the server  
**./manage.py runserver**  

**Now you can use your browser to access the user interface on http://127.0.0.1:8000**  
**For the admin interface, use http://127.0.0.1:8000/admin**

\# Deactivate the virtual environment after testing  
**deactivate**  


Or the same with Nix:  
\# start nix-shell  
**./manage.py migrate**  
**./manage.py createsuperuser**  
**./mange.py runserver**
