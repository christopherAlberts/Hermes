import telebot
import time
import os
from telebot import TeleBot

def config_handler(start_text, end_text, config_file):

    # The following code is designed to import text from a config file.
    # It's designed to do this line by line.
    # start_text: The program will start importing after this point.
    # end_text: The program will stop importing when it reaches this point.
    # config_file: location where config file is stored.

    fr = open(config_file, 'r')
    text = fr.read()
    start = text.find(start_text) + len(start_text + "\n")
    end = text.find("\n" + end_text)
    substring = text[start:end]
    fr.close()

    return substring


def hedwig_protocol(listen_or_take, file_name, take_this):

    # THERE ARE TWO PARTS TO THIS FUNCTION:
    # -------------------------------------------------------------------------------------
    #
    # LISTEN:
    # This code is ment to be placed in a continues while loop.
    # If "listen" is selected the code will monitors a specific folder.
    # If there are text files inside, it will choose the oldest one and return the output.
    # Following this it will also remove the file.
    #
    # listen_or_take = "listen"
    # filename = The file path of the file you are monitoring.
    # take_this = ""
    #
    # -------------------------------------------------------------------------------------
    #
    # TAKE:
    # Code creates a file with text inside.
    #
    # listen_or_take = "take"
    # filename = The file path of the file you want to create.
    # take_this = The text you want to write to the file.
    #
    # -------------------------------------------------------------------------------------

    if listen_or_take == "listen":

        try:

            # Counts number of files in folder.
            file_count = sum([len(files) for r, d, files in os.walk(file_name)])

            if file_count > 0:
                # The following code is used to determine the oldest file in the folder.
                path = file_name
                os.chdir(path)
                files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

                oldest_file = files[0]
                # newest_file = files[-1]

                # now do something with the oldes file....
                fr = open(oldest_file)
                text = fr.read()
                fr.close()

                os.remove(oldest_file)  # Removes oldest file.

                return text

        except:
            # When a file is being copied while the Hedwig_protocol is running
            # it can cause and error, a delay helps with this.
            time.sleep(1)

    elif listen_or_take == "take":

        # WRITE TO A FILE
        fw = open(file_name, 'w')
        fw.write(take_this)
        fw.close()


def log_history(file_name, take_this):

    # The following method is used through out the code.
    # It's met to log every message that is sent and received to a "ChatHistoryLog" file.
    # It also does not replace text in the file but rather appends it.

    # Append text to a file
    fw = open(file_name, 'a')
    fw.write("\n" + take_this)
    fw.close()


def talaria(From_Hermes, To_Hermes):  # This is the main daddy function!

    # This function will first wait to receive the initiate "/start" command.
    # Once this is sent through the bot is live.
    # The bot will then listen for incoming messages.
    # Once a message is received the bot will first check if the correct notation was used.

    # ALL MESSAGES SHOULD BE IN THIS FORMAT:
    # first the exchange number followed by "#" and then your message.

    #       0# Hello Venus

    # The function will then insure it gets delivered to the right exchange.
    # Once the message is delivered the function will wait to receive the response.
    # IT MUST RECEIVE A RESPONSE TO CONTINUE.

    # Once the function receives the response, it will then sent it through to the user.

    # After the response is sent through the function will go through all the response files from all the exchanges.
    # To check if there are any additional information the might have come through.

    @bot.message_handler(commands=['start', 'wakeup', 'areyoualive?', 'areyoualive'])
    def send_welcome(message):
        bot.reply_to(message, "I'm alive")

        @bot.message_handler(content_types=['text'])
        def handle_text(message):

            string = message.text
            chat_id = message.chat.id

            # This will keep a history of all the text sent
            log_history(History,string)

            if "#" in string: # Check if the strinng contains "#".

                PO_Num = string.split('#', 1)[0]
                parcel = string.split('#', 1)[1]

                a = 0

                try:
                    PO_Num = int(PO_Num)  # Check to see if the first characters that were typed in were digest.

                    for line in From_Hermes:

                        if PO_Num == a:

                            new_file = line + "\\" + str(a) + ".txt"

                            b = a

                            while os.path.exists(new_file):

                                b = b + 1
                                new_file = line + "\\" + str(b) + ".txt"

                            hedwig_protocol("take", new_file, parcel)

                            # Now the parcel is sent, so we have to wait for a response.

                            c = 0
                            for secondline in To_Hermes:

                                if PO_Num == c:

                                    hp = None

                                    while hp is None:
                                        hp = hedwig_protocol("listen", secondline, "")

                                    bot.send_message(chat_id, hp)
                                    log_history(History, hp)
                                c = c + 1

                        a = a + 1

                except:
                    bot.send_message(message.chat.id, "Error: OP_Num not Int")
                    log_history(History, "Error: OP_Num not Int")
                    string = None

            else:
                bot.send_message(message.chat.id, "Error: No '#' in OP_Num")
                log_history(History, "Error: No '#' in OP_Num")
                string = None


            # The following code will go through each PO.Box and send remaining messages through.
            for thirdline in To_Hermes:

                hp = not None
                while hp is not None:

                    hp = hedwig_protocol("listen", thirdline, "")

                    if hp is not None:
                        bot.send_message(chat_id, hp)
                        log_history(History, hp)


config_file = "HermesConfig.txt"
token = config_handler("Hermes_Bot_Token:", "Hermes Chat History File:", config_file)
URL = "https://api.telegram.org/bot{}/".format(token)
bot = telebot.TeleBot(token=token)
History = config_handler("Hermes Chat History File:", "Hermes 2 Exchange:", config_file)
From_Hermes_Config = list(config_handler("Hermes 2 Exchange:", "Exchange 2 Hermes:", config_file).split("\n"))
To_Hermes_Config = list(config_handler("Exchange 2 Hermes:", "End of Config", config_file).split("\n"))

# -------------------------------------------------------------------------------------
# Running Protocol
# -------------------------------------------------------------------------------------
talaria(From_Hermes_Config, To_Hermes_Config)

try:
    bot.polling(none_stop=True)
    # ConnectionError and ReadTimeout because of possible timeout of the requests library
    # maybe there are others, therefore Exception
except Exception:
    time.sleep(2)
