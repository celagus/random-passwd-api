# Intro

This is a RESTful API for random password generation.

You can input th number of lowercase chars, uppercase chars, digits and the password length you wish, then the API returns a random password.

## Requisites to run

1. Clone repo

2. Install Python requirements

```
pip install -r requirements.txt
```

3. Run API Server (by default it runs in localhost:5000)

```
python random-passwd-api.py
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

## Restrictions

* Total number of password characters cannot be less than 30
* The number of lowercase letters cannot be lower than 10
* The number of uppercase letters cannot be lower than 10
* The number of digits cannot be lower than 10
