import os 
from pyrogram import Client, filters

API_HASH = "f9dd1efc1781f1476c53afa04d76b234"
API_ID = 11619572
API_TOKEN = "5467986140:AAG9J8Puem-1r9xWdC31oUe0qjgiaKmEhsc"

py = Client(
  "Pyrob0t",
  api_id=API_ID, api_hash=API_HASH , bot_token=API_TOKRN
  )

async def main():

    async with py:



        # Send a message, Markdown is enabled by default

        await py.send_message("me", "Hi there! I'm using **Pyrogram**")

py.run(main())

print("[pyrogram] : im live ..!")
