# Telegram whisper bot
This python script allows you to run a telegram bot to perform automatic speech recognition (ASR) on telegram voice messages.  
The script uses the [telebot](https://github.com/eternnoir/pyTelegramBotAPI) and [whisper](https://github.com/openai/whisper) python library to connect to telegram and perform ASR respectively.
## Step 1: Register new bot
Follow these instructions to register a new bot on telegram.  
Save the API token in config.py

## Step 2: Deploy bot to Heroku
In order for the bot to run in a serverless manner, we need to deploy it to a service.  
Follow [these instructions](https://devcenter.heroku.com/articles/getting-started-with-python) to create a Heroku account and deploy the bot.
