# howto start

this is a pretty standard django app, install should be like this:

- python -m venv venv
- venv/bin/activate
- pip install -r requirements.txt
- ./manage.py migrate
- ./manage.py createsuperuser
- ./mange.py runserver


or with nix:
- nix-shell
- ./manage.py migrate
- ./manage.py createsuperuser
- ./mange.py runserver
