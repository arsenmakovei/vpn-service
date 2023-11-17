# VPN Service 

This project is a simple VPN service implemented as a web application using Django. 
It allows users to register, access their personal profile, edit personal information, 
and view statistics related to VPN usage. Additionally, users can create and navigate 
to custom sites through an internal routing system acting as a proxy server.

## Installation & Getting started
Python 3.10 must be already installed

1. Clone project and create virtual environment
   ```shell
   git clone https://github.com/arsenmakovei/vpn-servise.git
   cd vpn_service
   python -m venv venv
   Windows: venv\Scripts\activate
   Linux, Unix: source venv/bin/activate
   pip install -r requirements.txt
   ```
   
2. Make migrations and run server
   ```shell
   python manage.py migrate
   python manage.py runserver
   ```

3. You can create superuser using command `python manage.py createsuperuser` and visit admin panel at /admin/

## Run with Docker

1. Docker should be installed and running
   ```shell
   docker-compose up --build
   ```
   
2. You can create superuser in Docker or run other `python manage.py` command if needed
   ```shell
   docker exec -it vpn_service-web-1 python manage.py createsuperuser 
   ```