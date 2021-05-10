import logging
from FacebookAutomater import *
from AudioProcessor import *
from SpeechHandling import *
import requests
import json
import pyttsx3
import gi
from detect import *
from get_posts import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
flag = 0

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

fb = FacebookAutomater()
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    intro_text = "Welcome to Vision! This is a speech operated bot and that means you don't have to type anything. Just speak!\n"
    intro_text += "Listen to the instructions for using the bot carefully.\n"
    intro_text += "1. For opening facebook, please say something like log me into facebook making sure the sentence has facebook in it.\n"
    intro_text += "2. For logging in please say your number or email followed by the password.\n"
    intro_text += "3. For making a post on facebook, please say a sentence that should have the word post in it.\n"
    intro_text += "4. For reading your recent posts, say something like read posts.\n"
    intro_text += "5. Finally, if you want to check whether you are safe while speaking passwords or anytime. Please say something like Am I safe or check if I am safe etc.\n"
    intro_text += "6. Please note that we are not saving anything so nothing is being compromised.\n"
    intro_text += "We hope that you have a great time!"
    """Send a message when the command /start is issued."""
    update.message.reply_text(intro_text)


    context.job_queue.run_repeating(callback_minute, interval=10, first=20,
                                    context=update.message.chat_id)

def callback_minute(context):
    text = RecognizeSpeech("audio1.wav")
    global flag
    if(("facebook" in text.lower() or "into facebook" in text.lower())and flag == 0):
        fb.initiate_chrome()
        fb.page_load()
        speak("Loaded facebook")
        flag = 1
        time.sleep(20)
        speak("Please speak your number and password")
        speakEmailAndPassword()
    elif(text.lower() == "add post"):
        speak("Please speak your message")
        post = RecognizeSpeech("post.wav")
        print("Recognized post")
        fb.page_posting(post)
    elif("safe" in text.lower()):
        checkFaces()
    elif("get posts" in text.lower()):
        get_posts()

def speakEmailAndPassword():
    text =  RecognizeSpeech('speech.wav')
    words = text.split()
    number=""
    i = 0
    for word in words:
        if(i==10):
            break
        if(word=="one"):
            number+=str(1)
        elif(word=="zero"):
            number+=str(0)
        elif(word=="two"):
            number+=str(2)
        elif(word=="three"):
            number+=str(3)
        elif(word=="four"):
            number+=str(4)
        elif(word=="five"):
            number+=str(5)
        elif(word=="six"):
            number+=str(6)
        elif(word=="seven"):
            number+=str(7)
        elif(word=="eight"):
            number+=str(8)
        elif(word=="nine"):
            number+=str(9)
        i+=1
    password = words[-1]
    print(password)
    print(number)
    if(fb.do_login(number,password)):
        speak("You have successfully logged in!")
        return 1
    else:
        print("error")
        return 0        






def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
def login(update, context):
    update.message.reply_text("Opening facebook!")
    


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start",start, pass_job_queue=True))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("login",login))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))



    # log all errors
    dp.add_error_handler(error)
    

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
