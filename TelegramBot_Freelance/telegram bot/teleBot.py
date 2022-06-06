from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler, Filters, MessageHandler, Updater
import telebot
import time
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
import asyncio
import threading


# bot = Bot("1907704934:AAHOolKyKfB6JvYON12oAbn4-ZwUmpss7-0")
updater = Updater(
    "1907704934:AAHOolKyKfB6JvYON12oAbn4-ZwUmpss7-0", use_context=True)
message = "Working..."
api_id = 0
api_hash = ''
client = ''
id_list = []
phone = 0
API_ID, HASH_ID, PHONE, CODE = range(4)
dispatcher = updater.dispatcher
loop = asyncio.get_event_loop()
async def connect_client_to_server(update: Update, context: CallbackContext):
    global client
    print("REACHED CONNECT")
    client = TelegramClient('session', api_id, api_hash, loop=loop)
    await client.connect()
    # print("phone number : ", update.message.from_user)
    if not (await client.is_user_authorized()):
        update.message.reply_text(
            "Phone number verification required when accessing first time.\n\nEnter your phone number (with country code)")
        return PHONE

        # await client.send_code_request('+916266827746')
        # await client.start()
        # await client.run_until_disconnected()
        # phone = update.message.text
        # print("\nPhone number verification required when accessing first time.")

        # phone = input("\nEnter your phone number (with country code) : ")
        # client.send_code_request(phone)
        # update.message.reply_text("Enter the verification code sent on phone")
        # client.sign_in(phone, input('\nEnter the code: '))
        # signing in the client
    # @client.on(events.NewMessage(outgoing=True))
    # async def handler(event):
    #     pass
    update.message.reply_text("Connected Successfully !")
    update.message.reply_text(
        """Hello, \n1. Enter "/add" to add and remove groups\n2. Enter "/message" to set message\n3. Enter "/time" to set time interval\n4. Enter "/send" to start sending messages.\n3. Enter "/stop" to stop sending messages.""")
    # while True:
    #     for i in id_list:
    #         try:
    #             client.send_message(i, message)
    #             time.sleep(4)

    #         except Exception as e:
    #             print ("Ooops! ",e.message," Occured ")
    #             input("Press enter to close")
    return
async def send_code(update: Update, context: CallbackContext):
    print("reached sendCode")
    print(client)
    await client.send_code_request('+916266827746')
    # await client.send_code_request(phone)
    update.message.reply_text("Enter the verification code sent on phone")
    return CODE

def go(update: Update, context: CallbackContext):
    return asyncio.run(connect_client_to_server(update, context))


def go2(update: Update, context: CallbackContext):
    print("reached go2")
    return asyncio.run(send_code(update, context))


def go3(update: Update, context: CallbackContext, code):
    print("reached go3")
    return asyncio.run(verify_code(update, context, code))


# threading.Thread(target=go2).start
# @client.on(events.NewMessage(outgoing=True))
# async def handler(event):
#     if (event.raw_text == "join_group"):
#         print(event.chat_id)
#         # id_list.append(event.chat_id)
# try:
#     timeInterval = int(input("Enter Time interval between messages : "))
# except:
#     print("\nEnter only numbers.")
#     timeInterval = int(input("Enter Time interval between messages : "))


def start_function(update: Update, context: CallbackContext):
    global api_id, api_hash
    print("FROM USER : ", update.message.from_user)
    # bot.send_message(chat_id = update.effective_chat.id,text = """Hello, Please enter your API ID""",)
    update.message.reply_text("Hello, Please enter your API ID")
    return API_ID
    # api_id = update.message.text
    # api_id = context.args[2]
    # print("\nAPI ID : ", api_id)
    # update.message.reply_text("Please enter Hash ID")
    # api_hash = update.message.text
    # print("\nAPI Hash : ",api_hash)
    # connect_client_to_server()


def get_api_function(update: Update, context: CallbackContext):
    global api_id
    try:
        api_id = int(update.message.text)
        update.message.reply_text("Now please enter HASH ID")
        print("API ID : ", api_id)
        return HASH_ID
    except:
        update.message.reply_text("Please enter correct API ID.")
        print("API ID : ", api_id)
        return API_ID


def get_hash_function(update: Update, context: CallbackContext):
    global api_hash
    api_hash = update.message.text
    update.message.reply_text("Connecting to the server.....")
    print("HASH ID : ", api_hash)
    return go(update, context)
    # return connect_client_to_server(update,context)

    # return server().connecting()


def get_phone_function(update: Update, context: CallbackContext):
    global phone
    phone = update.message.text
    print("Phone : ", phone)
    return go2(update, context)





def get_code_function(update: Update, context: CallbackContext):
    code = update.message.text
    print("CODE : ", code)
    return go3(update, context, code)


async def verify_code(update: Update, context: CallbackContext, code):

    try:
        await client.sign_in(phone, code)
        return update.message.reply_text("Successful")
    except:
        update.message.reply_text("Enter correct code")
        print("CODE : ", code)
        return CODE
    # return connect_client_to_server


def msg_function(update: Update, context: CallbackContext):
    code = update.message.text
    try:
        # client.sign_in(phone, code)
        print("CODE : ", code)
        return
    except:
        update.message.reply_text("Enter correct code")
        print("CODE : ", code)
        return CODE


def time_function(update: Update, context: CallbackContext):
    code = update.message.text
    try:
        # client.sign_in(phone, code)
        print("CODE : ", code)
        return
    except:
        update.message.reply_text("Enter correct code")
        print("CODE : ", code)
        return CODE


def cancel(update: Update, context: CallbackContext):
    pass
    # bot.send_message(chat_id=update.effective_chat.id, text="""Hello, \n1. Enter "/add" to  add groups\n2. Enter "/send" to start sending messages.\n3. Enter "/stop" to stop sending messages.""",)
    # await client.send_message('me', 'Hello, myself!')


# def add_function(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         """"Send "Join" message to groups you want to add.""")
#     # bot.send_message(chat_id=update.effective_chat.id,
#     #                  text="""Enter group ids one by one""",)
#     # print(bot.getMe().id)

#     @client.on(events.NewMessage(outgoing=True))
#     async def handler(event):
#         print(event)
#         if (event.raw_text == "Join" and event.chat_id not in id_list):
#             id_list.append(event.chat_id)
#             # update.message.reply_text(f"Added Group : {event.cha}",)
#         print(id_list)
    #     if (event.chat_id == bot.getMe().id):
    #         if ("/" in event.raw_text):
    #             pass
    #         elif (event.raw_text not in id_list ):
    #             try:
    #                 id_list.append(int(event.raw_text))
    #                 print(id_list)
    #             except:
    #                 bot.send_message(chat_id=update.effective_chat.id,
    #                              text="""Enter correct group id .""",)

    #     print("event id ", event.chat_id)
    #     print("update chat id ", update.effective_chat.id)
    #     print("raw chat ", event.raw_text)
    #     if (event.chat_id == bot.getMe().id and event.raw_text not in id_list and '/' not in event.raw_text):
    #         id_list.append(event.raw_text)
    #         print(id_list)
    #     elif("/" in event.raw_text):
    #         # client.start()
    #         client.disconnected()

    #         raise Exception("Boo!")

    # @client.on(events.NewMessage(outgoing=True))
    # async def handler(event):
    #     if ("-" in event.raw_text and event.raw_text not in id_list):
    #         id_list.append(event.raw_text)
    #         print(id_list)
    #     # await client.send_message('me', 'Hello, myself!')


# def message_function(update: Update, context: CallbackContext):

#     bot.send_message(chat_id=update.effective_chat.id,
#                      text="""Enter Message to be sent.""",)

#     @client.on(events.NewMessage(outgoing=True))
#     async def handler(event):
#         if (event.chat_id == bot.getMe().id and "/" not in event.raw_text):
#             message = event.raw_text
#             print("Message : ", message)
#         elif("/" in event.raw_text):
#             raise Exception("Boo!")
#         print("Message : ", event.raw_text)


# def time_function(update: Update, context: CallbackContext):
#     bot.send_message(chat_id=update.effective_chat.id,
#                      text="""Enter Time Interval in seconds .""",)

#     @client.on(events.NewMessage(outgoing=True))
#     async def handler(event):
#         print("TIME : ", event.raw_text)
#         if (event.chat_id == bot.getMe().id):
#             if ("/" in event.raw_text):
#                 raise Exception("Boo!")
#             elif (event.raw_text.isdigit()):
#                 timeInterval = int(event.raw_text)
#             else:
#                 bot.send_message(chat_id=update.effective_chat.id,
#                                  text="""Enter only numbers .""",)


# def send_function(update: Update, context: CallbackContext):
#     bot.send_message(chat_id=update.effective_chat.id,
#                      text="""Sending messages.....""",)
#     while status:
#         for i in id_list:
#                 await client.send_message(i, message)
#         time.sleep(timeInterval)

# def stop_function(update: Update, context: CallbackContext):
#     bot.send_message(chat_id=update.effective_chat.id,
#                      text="""Stoping messages.....""",)
#     status = False

conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start_function)],
        states={
            # GENDER: [MessageHandler(Filters.regex('^(Boy|Girl|Other)$'), gender)],
            # PHOTO: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
            # LOCATION: [
            #     MessageHandler(Filters.location, location),
            #     CommandHandler('skip', skip_location),
            # ],
        
            API_ID: [MessageHandler(Filters.text & ~Filters.command, get_api_function)],
            HASH_ID: [MessageHandler(Filters.text & ~Filters.command, get_hash_function)],
            PHONE: [MessageHandler(Filters.text & ~Filters.command, get_phone_function)],
            CODE: [MessageHandler(Filters.text & ~Filters.command, get_code_function)],
            # MSG: [MessageHandler(Filters.text & ~Filters.command, msg_function)],
            # TIME: [MessageHandler(Filters.text & ~Filters.command, time_function)],
            # SERVER: [MessageHandler(Filters.text & ~Filters.command, connect_client_to_server)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
dispatcher.add_handler(conv_handler)
# start_value = CommandHandler('start', start_function)
# start_value2 = MessageHandler(Filters.text & ~Filters.command, get_api_function)
# start_value2 = CommandHandler('add', add_function)
# # start_value3 = CommandHandler('message', message_function)
# # start_value4 = CommandHandler('time', time_function)
# start_value5 = CommandHandler('send', send_function)
# start_value6 = CommandHandler('stop', stop_function)

# dispatcher.add_handler(start_value)
# dispatcher.add_handler(start_value2)
# dispatcher.add_handler(start_value2)
# # dispatcher.add_handler(start_value3)
# # dispatcher.add_handler(start_value4)
# dispatcher.add_handler(start_value5)
# dispatcher.add_handler(start_value6)

# dispatcher.add_handler(start_value3)

updater.start_polling()
updater.idle()
