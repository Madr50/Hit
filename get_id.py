from telethon import TelegramClient

# معلوماتك من الصورة
API_ID = 24044141
API_HASH = '3de21516f69614b183a96dbf1846aae5'

client = TelegramClient('my_session', API_ID, API_HASH)

async def get_channels():
    async for dialog in client.iter_dialogs():
        if dialog.is_channel:
            print(f"اسم القناة: {dialog.name} | الـ ID: {dialog.id}")

with client:
    client.loop.run_until_complete(get_channels())
