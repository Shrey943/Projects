# importing all required libraries
import time
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events


# get your api_id, api_hash, token
# from telegram as described above

# api_id = int(input("\nEnter API ID : "))
api_id = 7246436
# api_hash = input("\nEnter API HASH ID : ")
api_hash = '60d6c9dc987363673fbfc54a74f9014a'
IDlist = ['-1596216426']
message = "working..."
timeInterval = 2000

# creating a telegram session and assigning
# it to a variable client
# try:
client = TelegramClient('session', api_id, api_hash)
    # connecting and building the session

client.connect()

# in case of script ran first time it will
# ask either to input token or otp sent to
# number or sent or your telegram id

if not client.is_user_authorized():

    print("\nPhone number verification required when accessing first time.")
    phone = '+916266827746'
    # phone = input("\nEnter your phone number (with country code) : ")

    if ("+" not in phone):
        phone = "+" + phone

    client.send_code_request(phone)

    # signing in the client
    client.sign_in(phone, input('\nEnter the code: '))


# IDlist = list(map(int, input(
#     "\n\nEnter group ids with space between two ID : ").strip().split()))
print(IDlist)
# message = input("\nEnter message to be sent : ")
message = "Working..."

# timeInterval = int(input("\nEnter time interval in seconds : "))
timeInterval = 2


status = input("\n\nPress Enter to start sending messages : ")

print("\nSending messages.......\n\nClose the window to stop.")

while True:
    # for i in IDlist:
        entity = client.get_entity('https://t.me/idguhajvsku')
        client.send_message(entity=entity,message=message)
        time.sleep(timeInterval)
       

# disconnecting the telegram session

client.start()
client.run_until_disconnected()
# except Exception as e:
#    print ("Ooops! ",e.message," Occured ")
#    input("Press enter to close")
