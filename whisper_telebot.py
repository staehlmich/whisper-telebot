
import telebot
import whisper

import config

#Step 1: Perform ASR with whisper

def whisper_transcribe(filepath: str, model="tiny") -> str:
    """
    Function to perform ASR on a .mp3 file
    :param filepath: Path to the .mp3 audiofile.
    :param model: Set the model type for whisper
    ["tiny", "base", "small", "medium", "large"].
    Larger model means more parameters, higher memory requirements and
    slower speed.
    :return: transcribed audio.
    """
    # Choose tiny model for faster output.
    model = whisper.load_model(model)
    result = model.transcribe(filepath)

    return result["text"]

#Step 2: Create Telegram Bot and programm the basic commands.

bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    """
    Send a welcome message to user on command '/hello'
    :param message: Message sent by user.
    :return:
    """
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['help'])
def help_command(message):
    """
    Display available commands in the bot
    :param message:
    :return:
    """
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(
    'Message the developer', url='telegram.me/artiomtb'))
    bot.send_message(
       message.chat.id,
       '/help - display commands \n' +
       '/hello - display welcome message \n' +
       '/listen - start listening for voice messages ',
       reply_markup=keyboard
    )

@bot.message_handler(commands=['listen'])
def listen(message):
    """
    Send a message to the user to prompt for audio input
    :param message: Message sent by user.
    :return:
    """
    bot.send_message(chat_id=message.chat.id, text='Please send an audio file')

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    """
    Function to send transcription of audio message to user
    :param message: Message with audio file sent by user.
    :return: Transcribed message as string.
    """
    # Retrieve file id.
    file_id = message.voice.file_id
    # Get url to audio file.
    file_path = bot.get_file_url(file_id)

    # Transcribe the audio using Whisper AI
    response = whisper_transcribe(file_path)
    text = response

    # Send the transcribed text to the user
    bot.send_message(chat_id=message.chat.id, text=text)


if __name__ == '__main__':
    bot.polling()