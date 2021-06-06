# Intro

This is a RESTful API built in Flask for random password generation.

You can input th number of lowercase chars, uppercase chars, digits and the password length you wish, then the API returns a random password.

## Running from cli

1. Clone repo

2. Install Python requirements

```
$ pip install -r requirements.txt
```

3. Run API Server (by default it runs in localhost:5000)

```
$ python random-passwd-api.py
```

4. Call the API specifying the input variables in this way:

```
$ curl -X GET "http://127.0.0.1:5000/generate-password/?lowercase=10&uppercase=10&digits=10&length=38
```
Expected output:
```
HTTP/1.1" 200 -
{"password":"py1B2a3zHsD|C0kJbK9u8Smd7hPt\\:TO45u6Qe"}
```
(if length is grather than the sum of three differents char types you input, the API full them with random printables)

## Running from Docker Hub

```
$ docker pull celagus/random-passwd-api
...
...
...
$ docker run -ti -p 5000:5000 celagus/random-passwd-api
```

## Building from Dockerfile
From the root path for this repo please introduce commands below

```
$ docker build -t celagus/random-passwd-api .
...
...
...
$ docker run -ti -p 5000:5000 celagus/random-passwd-api
```

## Restrictions

* Total number of password characters cannot be less than 8 or the sum of all other params
* The number of lowercase letters cannot be lower than 2
* The number of uppercase letters cannot be lower than 2
* The number of digits cannot be lower than 2
