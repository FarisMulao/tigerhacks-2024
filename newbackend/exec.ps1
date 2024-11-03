docker build -t auth0-python-web-01-login .
docker run -m 2048m --env-file .env -p 5000:5000 -it auth0-python-web-01-login
