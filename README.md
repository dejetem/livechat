## Getting Started the first thing to do is to clone the repository:

```bash
$ git clone https://github.com/dejetem/livechat.git
$ cd livechat
```

## Create a virtual environment to install dependencies in and activate it:

```bash
$ python3 -m venv env
$ source env/bin/activate  # On Windows use `env\Scripts\activate`
$ cd livechat
```

## Then install the dependencies:

```bash
(env)$ pip install -r requirements.txt
```


Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by venv

## .env

```bash
$ create .env file and add
$ APP_CERTIFICATE
$ APP_ID
$ SECRET_KEY
```

## run the server:

```bash
(env)$ python manage.py runserver
```
Open your a tab on your browser and input this url 
## http://127.0.0.1:8000/ 