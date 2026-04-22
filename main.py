from telethon import TelegramClient
api_id = 123456
api_hash = ""

client = TelegramClient ("session", api_id, api_hash)
async def main():
  print("Bot is running...")
with client:
  client.loop.run_until_complete(main())
