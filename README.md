# OakCodeFest-Newb_c0ders

This is the official repository for our project in the oakwood hackathon. This project mainly aims to nudge people into doing more environmentally friendly things by indirectly giving them environmental facts while they talk to the chatbot.

## Installation and usage

To use this code you must download RASA. It is advised to download RASA on a virtual environment with the latest version of pip (For me it's 21.3.1). To install RASA do this :-
```bash 
pip install --upgrade pip
# Upgrading pip to the most recent on mac

pip install rasa
# Installing rasa

```
After getting rasa, you need to run a custom actions server. To do this you can do :
```bash
rasa run actions

```
After the actions are registered, copy the adress from the action server and add it to endpoints.yml. Note that the server will mostly be localhost. 
```
# Adding server to endpoints.yml

action_endpoint:
  url: "http://localhost:5055/webhook"


```
After running the server we can simply use the rasa shell to communicate with the bot using the following command : 

```bash

rasa shell

```

## Integrating the bot with telegram 

To integrate the bot with telegram you might need to install ngrok. First create a telegram bot from the bot father in telegram. Then get the access token and the name of the bot to help verify the bot. We must now add the token and name to credentials.yml .
```
telegram:
  access_token: <Access token of the bot>
  verify: <Name of the bot>
  webhook_url: 

```
Note: You can install ngrok from this link --> https://ngrok.com/download
Now we can use ngrok to make requests and communicate with the telegram api. This can be done by:
```bash 
ngrok http 5005

```
After we run the command we get a url and then we add that url to the webhook section in the credentials.yml

```
webhook: <url>/webhooks/telegram/webhook
```

Now to run the bot on telegram we can simply do:
```bash
rasa run --enable-api --cors "*"
```

