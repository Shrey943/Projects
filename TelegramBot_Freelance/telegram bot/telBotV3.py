from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler, Filters, MessageHandler, Updater
import time
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
import asyncio
import threading


updater = Updater(
    "1907704934:AAHOolKyKfB6JvYON12oAbn4-ZwUmpss7-0", use_context=True)
message = "Working..."
api_id = 0
api_hash = ''
session_id = 0
id_list = []

storage = {}
phone = 0
code = 0
have_code = False
time_interval = 5
code_hash = ''
status = True
connected_loop = True
connected = 0
return_from_phone = 0
storage_string = []
API_ID, HASH_ID, PHONE, CODE, CMD, MSG, TIME, STOP, ADD = range(9)
dispatcher = updater.dispatcher
loop = asyncio.get_event_loop()


async def connect_client_to_server(update: Update, context: CallbackContext):
    global phone, connected
    print("REACHED CONNECT")
    client = TelegramClient('session'+str(session_id),
                            api_id, api_hash, loop=loop)
    await client.connect()
    if not (await client.is_user_authorized()):
        update.message.reply_text(
            "Phone number verification required when accessing first time.\n\nEnter your phone number (with country code)\n# To enter api_id and hash_id enter '/change'.")
        await client.disconnect()
        connected = 0
        return PHONE

    update.message.reply_text("Connected Successfully !")
    update.message.reply_text(
        """Hello, \n1. Enter "/add" to add and remove groups\n2. Enter "/message" to set message\n3. Enter "/time" to set time interval\n4. Enter "/send" to start sending messages.\n3. Enter "/stop" to stop sending messages.\n\nNOTE :Enter "/change" to login with different account.""")

    await client.disconnect()

    print("returned CMD")
    return CMD


async def send_code(update: Update, context: CallbackContext):
    global code_hash, have_code, connected, connected_loop, return_from_phone
    print("reached sendCode")
    client = TelegramClient('session'+str(session_id),
                            api_id, api_hash, loop=loop)
    await client.connect()
    try:
        a = await client.send_code_request(phone, force_sms=True)
        return_from_phone = 1
        while not have_code:
            print("InPass")
            time.sleep(2)

            # code_hash = a.phone_code_hash
            # wait client.sign_in(phone, code,phone_code_hash=code_hash)
        have_code = False
        try:
            await client.sign_in(phone, code)
            update.message.reply_text("Connected Successfully....")
            update.message.reply_text(
                """Hello, \n1. Enter "/add" to add and remove groups\n2. Enter "/message" to set message\n3. Enter "/time" to set time interval\n4. Enter "/send" to start sending messages.\n3. Enter "/stop" to stop sending messages.\n\nNOTE :Enter "/change" to login with different account.""")
            await client.disconnect()
            # print("returned CMD")

            connected = 1
            connected_loop = False
            return
        except Exception as e:
            print("Exception : ", e)
            update.message.reply_text(
                """Wrong code entered.\nDO NOT enter code more than 3 times\n\n# To change phone number enter "/phone". """)
            await client.disconnect()
            print("CODE : ", code)
            connected = 3
            t1 = threading.Thread(target=go2, args=(update, context,))
            t1.start()
            connected_loop = False
            return

    except Exception as e:
        print("Exception : ", e)
        return_from_phone = 3
        update.message.reply_text(
            "Problem sending the verification code.\nMake sure API ID, HASH ID and Phone Number is of same account and are correct.\n\nNOTE : You can not send more than 3 codes from one account on same day. ")
        update.message.reply_text(
            "Enter the phone number again and remember to put country code.\n\n# To Change API id or hash id, enter '/change'. ")
        return


# async def add_groups(update: Update, context: CallbackContext):
#     global connected
#     print("REACHED ADD")
#     client = TelegramClient('session'+str(session_id),
#                             api_id, api_hash, loop=loop)
#     await client.connect()
#     if not (await client.is_user_authorized()):
#         update.message.reply_text(
#             "Phone number verification required when accessing first time.\n\nEnter your phone number (with country code)")
#         await client.disconnect()
#         connected = 0
#         return PHONE
#     update.message.reply_text(
#         """To add groups send "Join" message on the required group.\nTo remove group send "Remove" message to the group you want to remove.\n\nIMPORTANT : To stop adding groups enter "Done" or "/done". """)

#     @client.on(events.NewMessage(outgoing=True))
#     async def handler(event):
#         if ((event.raw_text == "Join" or event.raw_text == "join") and event.chat_id not in id_list):
#             a = await event.get_chat()
#             print(a.title)
#             update.message.reply_text("Added Group : " + a.title)
#             id_list.append(event.chat_id)
#             print(id_list)
#         elif((event.raw_text == "Remove" or event.raw_text == "remove") and event.chat_id in id_list):
#             a = await event.get_chat()
#             print(a.title)
#             update.message.reply_text("Removed Group : " + a.title)
#             id_list.remove(event.chat_id)
#             print(id_list)

#         elif(event.raw_text == "done" or event.raw_text == "Done" or event.raw_text == "/done"):
#             update.message.reply_text("Groups saved.")
#             update.message.reply_text(
#                 """1. Enter "/add" to add and remove groups\n2. Enter "/message" to set message\n3. Enter "/time" to set time interval\n4. Enter "/send" to start sending messages.\n3. Enter "/stop" to stop sending messages.\n\nNOTE :Enter "/start" to login with different account.""")

#             await client.disconnect()
#             return CMD

#     await client.start()
#     await client.run_until_disconnected()
#     return


async def send_function(update: Update, context: CallbackContext):
    global connected, status , connected_loop
    print("REACHED SEND")
    client = TelegramClient('session'+str(session_id),
                            api_id, api_hash, loop=loop)
    await client.connect()
    if not (await client.is_user_authorized()):
        update.message.reply_text(
            "Phone number verification required when accessing first time.\n\nEnter your phone number (with country code)")
        await client.disconnect()
        connected = 4
        connected_loop = False
        return 
    connected_loop = False
    update.message.reply_text(
        """Sending Messages.......\nTo stop sending messages, enter 'stop' or '/stop'.""")
    message_temp = message
    id_list_temp = id_list
    time_interval_temp = time_interval
    while status:
        for i in id_list_temp:
            try:
                await client.send_message(i, message_temp)
                time.sleep(time_interval_temp)
            except Exception as e:
                print("Exception : ", e)
                update.message.reply_text(
                    "Stoped sending messages.Please check the inputs and try again.")
                update.message.reply_text(
                    """Enter "/stop" or "Stop".""")
                await client.disconnect()
                return
    await client.start()
    await client.disconnect()
    status = True
    return


def go(update: Update, context: CallbackContext):
    return asyncio.run(connect_client_to_server(update, context))


def go2(update: Update, context: CallbackContext):
    print("reached go2")
    return asyncio.run(send_code(update, context))


# def go3(update: Update, context: CallbackContext):
#     print("reached go3")
#     return asyncio.run(verify_code(update, context))

# def go4(update: Update, context: CallbackContext):
#     print("reached go4")
#     return asyncio.run(add_groups(update, context))


def go5(update: Update, context: CallbackContext):
    print("reached go5")
    return asyncio.run(send_function(update, context))


def start_function(update: Update, context: CallbackContext):
    # global api_id, api_hash
    print("FROM USER : ", update.message.from_user)

    update.message.reply_text("Hello, Please enter your API ID")
    return API_ID


def stop_function(update: Update, context: CallbackContext):
    global status
    print("REASCHED STOP")
    if (update.message.text == "Stop" or update.message.text == "/stop" or update.message.text == "stop"):
        status = False
        update.message.reply_text("Stoped sending messages.")
        update.message.reply_text(
            """1. Enter "/add" to add and remove groups\n2. Enter "/message" to set message\n3. Enter "/time" to set time interval\n4. Enter "/send" to start sending messages.\n3. Enter "/stop" to stop sending messages.\n\nNOTE : IF YOU HAD LOGGED IN WITH OTHER ACCOUNT ON ANY DEVICE THEN PLEASE RELOGIN BY ENTERING "/change". """)

        return CMD

    else:
        update.message.reply_text(
            "If you want to stop sending messages, enter 'Stop' or '/stop'. ")
        return STOP


def get_api_function(update: Update, context: CallbackContext):
    global api_id

    try:

        api_id = int(update.message.text)
        update.message.reply_text("Now please enter HASH ID")
        print("API ID : ", api_id)

        return HASH_ID
    except Exception as e:
        print("Exception : ", e)
        update.message.reply_text("Please enter correct API ID.")
        print("API ID : ", api_id)
        return API_ID


def get_hash_function(update: Update, context: CallbackContext):
    global api_hash, session_id
    # if (api_id != int(update.message.text)):
    session_id += 1
    print("SESSION NUMBER : ", session_id)
    api_hash = update.message.text
    update.message.reply_text("Connecting to the server.....")
    print("HASH ID : ", api_hash)

    return go(update, context)


def get_phone_function(update: Update, context: CallbackContext):
    global phone, return_from_phone
    print("REACHED PHONE")
    phoneTemp = update.message.text
    if(phoneTemp == "/change" or phoneTemp == "Change" or phoneTemp == "change"):
        return start_function(update, context)
    elif(len(phoneTemp) > 13):
        update.message.reply_text("Enter correct number")
        return PHONE
    else:
        phone = phoneTemp
        t1 = threading.Thread(target=go2, args=(update, context,))
        t1.start()
        while return_from_phone == 0:
            time.sleep(1)
        if (return_from_phone == 1):
            update.message.reply_text(
                "Enter the verification code sent on phone\nNOTE: If no response is received then try sending code with 'a' before code for example : a23XXX ")
            return_from_phone = 0
            return CODE
        else:
            return_from_phone = 0
            return PHONE
        # return go2(update,context)
    print("Phone : ", phone)
    # return


def get_code_function(update: Update, context: CallbackContext):
    global code, have_code, connected, connected_loop
    print("CODE :", update.message.text)
    codeTemp = update.message.text
    if(codeTemp == "/phone" or codeTemp == "Phone" or codeTemp == "phone"):
        update.message.reply_text(
            "Phone number verification required when accessing first time.\n\nEnter your phone number (with country code)")
        return PHONE
    else:
        code = codeTemp
        have_code = True
        while connected_loop:
            print("IN connected loop")
            time.sleep(1)
        connected_loop = True
        if (connected == 1):
            connected = 0
            return CMD
        elif(connected == 3):
            connected = 0
            return CODE
        # return None


def check_function(update: Update, context: CallbackContext):
    global connected_loop, connected
    print("reached check")
    if (update.message.text == "/add" or update.message.text == "add"):
        if (len(storage)==0):
            update.message.reply_text("No groups in storage.")
        else:
            # for index,i in enumerate(list(storage.keys):)
                
            update.message.reply_text("Groups stored are :- \n\n" + "\n".join(storage_string))
        update.message.reply_text("""1. Enter "/addall" to select all stored groups.\n2. Enter "/removeall" to remove all the selected groups.
                                      \n3. Enter 'Remove group_id' to remove one selected group. (format : Remove 1000011 or -1000011)
                                      \n4. To add new groups or select perticular groups, Enter group id and group name in this format : '10001001-group name'.\n\nEnter "/done when done adding groups.""")
        return ADD
        # return go4(update, context)
    elif(update.message.text == "/message" or update.message.text == "message"):
        update.message.reply_text("Enter the message you want to send.")
        return MSG
    elif(update.message.text == "/time" or update.message.text == "time" or update.message.text == "Time"):
        update.message.reply_text(
            "Enter the time interval between two messages.")
        return TIME
    elif(update.message.text == "/send" or update.message.text == "send" or update.message.text == "Send"):
        t1 = threading.Thread(target=go5, args=(update, context,))
        t1.start()
        while connected_loop:
            time.sleep(1)
        connected_loop = True
        if (connected == 4):
            connected = 0 
            return connect_client_to_server(update,context)
        else:
            return STOP
    elif(update.message.text == "/change"):
        return start_function(update, context)
    elif(update.message.text == "/done" or update.message.text == "done" or update.message.text == "Done"):
        return CMD
    else:
        update.message.reply_text("Enter a valid command.")
        return CMD

def msg_function(update: Update, context: CallbackContext):
    global message
    message = update.message.text
    update.message.reply_text(
        "Message saved.\nTo change message enter '/message' again.\nEnter '/time' to set time interval.")
    return CMD


def time_function(update: Update, context: CallbackContext):
    global time_interval
    try:
        time_interval = int(update.message.text)
        update.message.reply_text(
            "Time interval saved.\nTo change time enter '/time' again.\nEnter '/send' to start sending messages.")
        return CMD
    except Exception as e:
        print("Exception : ", e)
        update.message.reply_text("Enter only numbers")
        return TIME

def add_function(update: Update, context: CallbackContext):
    global id_list,storage,storage_string
    text = update.message.text
    if (text == "/addall" or text == "Addall"):
        if (len(storage) == 0 ):
            update.message.reply_text("Storage empty,try adding groups.")
            return ADD
        id_list = list(storage.keys())
        update.message.reply_text("Selected groups : " + ", ".join(list(map(str,id_list))))
        return ADD
    elif (text == "/removeall" or text == "Removeall"):
        id_list.clear()
        update.message.reply_text("No group selected.")
        return ADD
    elif ("Remove" in text or "remove" in text):
        l = text.strip().split()
        for i in l :
            if i == "remove":
                pass
            else:
                try:
                    if int("-"+i) not in id_list:
                        update.message.reply_text("id : " + i + "\nNo such id selected.") 
                    else:
                        id_list.remove(int("-"+i))
                except ValueError:
                    update.message.reply_text("Make sure id are correct, do not contain letters and in correct format.\nProblem with id : " + i )
                
        # remove_id  = text[6:len(text)]
        # remove_id = remove_id.strip()
        # try:
        # if (int(remove_id) not in id_list):
        #     update.message.reply_text("No such group selected.")
        #     return ADD
        # id_list.remove(int(remove_id))
        update.message.reply_text("Groups removed.\nCurrent selected groups : " + ", ".join(list(map(str,id_list))))
        return ADD
    elif ("-" in text):
        l = text.split("\n")
        print(l)
        for i in l:
            l2 = i.split("-")
            if ('' in l2):
                l2.remove('')
            try:
                if (int("-"+l2[0]) not in list(storage.keys())):
                    storage[int("-"+l2[0])] = l2[1]
                    storage_string.append(i)
                if (int("-"+l2[0]) not in id_list):
                    id_list.append(int("-"+l2[0]))
            except ValueError:
                update.message.reply_text("Make sure id are correct, do not contain letters and in correct format.\nProblem with id : " + l2[0] )
                
            # if(i not in list(storage.keys())):
            #     l2 = i.split("-")
            #     for j in 
            #     full_list.append(i.split("-"))
        print(storage)
        update.message.reply_text("Selected groups : "+ ", ".join(list(map(str,id_list))))
        return ADD
    elif (text == "/done" or text == "Done"):
        update.message.reply_text("Groups saved.")
        update.message.reply_text(
            """1. Enter "/add" to add and remove groups\n2. Enter "/message" to set message\n3. Enter "/time" to set time interval\n4. Enter "/send" to start sending messages.\n3. Enter "/stop" to stop sending messages.\n\nNOTE : IF YOU HAD LOGGED IN WITH OTHER ACCOUNT ON ANY DEVICE THEN PLEASE RELOGIN BY ENTERING "/change". """)

        return CMD
    else:
        update.message.reply_text("Enter valid Command\nEnter '/done' to stop adding groups.")
        return ADD
    
        

def cancel(update: Update, context: CallbackContext):
    pass


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start_function)],
    states={

        API_ID: [MessageHandler(Filters.text & ~Filters.command, get_api_function)],
        HASH_ID: [MessageHandler(Filters.text & ~Filters.command, get_hash_function)],
        PHONE: [MessageHandler(Filters.text, get_phone_function)],
        CODE: [MessageHandler(Filters.text, get_code_function)],
        CMD: [MessageHandler(Filters.text, check_function)],
        MSG: [MessageHandler(Filters.text & ~Filters.command, msg_function)],
        TIME: [MessageHandler(Filters.text & ~Filters.command, time_function)],
        STOP: [MessageHandler(Filters.text, stop_function)],
        ADD: [MessageHandler(Filters.text, add_function)],

    },
    fallbacks=[CommandHandler('cancelXYZ', cancel)],
)

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()