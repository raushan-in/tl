### Introduction
This repository hosts the code for Cryptocurrency Price Tracker. Written in Python and using Django rest framework.

### Technical Stack
- Python 3
- Django Rest Framework (DRF) 3.13.0+
- Docker (for building image)


## Steps to start server

- create an .env file.
- add these variables into .env
```
USER_EMAIL=""
MIN_PRICE_LIMIT=100
MAX_PRICE_LIMIT=500

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = ''
```
- Run these command
```
docker compose run web
```
```
docker compose up
```

- Open `http://127.0.0.1:8000/admin/` in browser.
- Endpoint: GET /api/prices/btc?date=DD-MM-YYYY

## Author

[Raushan Kumar](https://www.linkedin.com/in/raushan-in/)
