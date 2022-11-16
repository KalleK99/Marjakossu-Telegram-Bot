# A telegram bot that keeps a leaderboard for a group chat.
# Further details can be found in the readme
from telegram.ext import *
import database as db


API_token = "5749827068:AAHWG1QUhdBvwsNYse5c5OhNxo47Gdnrw60"
updater = Updater(API_token, use_context=True)
dispatcher = updater.dispatcher


# Returns the word following the /Pj command in a message text
def extract_chair_name(message):
    word_list = message.split()
    pj_name =""

    for i in range(len(word_list)):
        if word_list[i] == "/Pj":
            pj_name = word_list[i+1]
    return pj_name

# Fetch the chair's name from the user's message and handle the database
def Pj_command(update, context):
    Pj_name = extract_chair_name(update.message.text)
    db.add_data(Pj_name)
dispatcher.add_handler(CommandHandler("Pj", Pj_command))

# Execute the leaderboard command by calling db.print_top10 function
def leaderboard_command(update, context):
    top10 = db.print_top10()
    update.message.reply_text(top10)
dispatcher.add_handler(CommandHandler("leaderboard", leaderboard_command))

def main():
    print("Bot running!")
    updater.start_polling()
    updater.idle()

main()

