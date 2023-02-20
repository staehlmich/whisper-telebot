# Telegram whisper bot
This python script allows you to run a telegram bot to perform automatic speech recognition (ASR) on telegram voice messages.  
The script uses the [telebot](https://github.com/eternnoir/pyTelegramBotAPI) and [whisper](https://github.com/openai/whisper) python library to connect to telegram and perform ASR respectively.

## Step 1: Register new bot
Follow [these instructions](https://mattrighetti.medium.com/build-your-first-telegram-bot-using-python-and-heroku-79d48950d4b0) to register a new bot on telegram.  
Save the API token in config.py.

## Step 2: Deploy bot to Heroku
In order for the bot to run in a serverless manner, we need to deploy it to a service.  
Follow [these instructions](https://devcenter.heroku.com/articles/getting-started-with-python) to create a Heroku account and deploy the bot.
Check that your python packages in requirements.txt match the latest [pytorch](https://pytorch.org/get-started/locally/) release and [heroku stack](https://devcenter.heroku.com/categories/stacks). 
Install pytorch cpu package, to meet the required slug-size by heroku.
