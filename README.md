## Project Name

Live Chat

## Introduction

- Author - [Simon Jonathan](https://www.linkedin.com/in/simon-jonathan-844b1719a/)
- Deployed Web App - [Live Chat](https://livechat-production-9c6c.up.railway.app/)
- Blog - [Project blog article](https://medium.com/@enyeoluwarotimisimon/live-chat-app-305f300dab31)


# Installation
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

## Usage

<img
  src="https://github.com/dejetem/livechat/blob/main/static/images/start.png"
  alt="Home page"
  title="Home page"
  style="display: inline-block; margin: 0 auto; max-width: 300px"
>

<img
  src="https://github.com/dejetem/livechat/blob/main/static/images/join.png"
  alt="Start or Join"
  title="Start or Join Live page"
  style="display: inline-block; margin: 0 auto; max-width: 300px"
>
## Contributing
As I use this for my own projects, I know this might not be the perfect approach for all the projects out there. If you have any ideas, just [open an issue](https://github.com/dejetem/livechat/issues/new) and tell me what you think.
If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## Related projects


## Licensing
This project is licensed under Unlicense license. This license does not require you to take the license with you to your project.