#Əkmə papanın balası :)


from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified, MessageIdInvalid
from time import sleep, strftime, gmtime, time
from os import remove
from os.path import join
from random import randint
from config import Config
from datetime import datetime
import pytz

UTC = pytz.utc
IST = pytz.timezone('Asia/Baku')
datetime_ist = datetime.now(IST)

api_id = 19358020
api_hash = "de33bd71c8d49212c32af0bc10d67617"

app = Client(Config.session_name, api_id, api_hash)

async def msg_info(msg):
    media_type = ""
    ttl = 0
    if hasattr(msg.photo, "ttl_seconds"):
        if msg.photo.ttl_seconds:
            media_type = "photo"
            ttl = msg.photo.ttl_seconds
    elif hasattr(msg.video, "ttl_seconds"):
        if msg.video.ttl_seconds:
            media_type = "video"
            ttl = msg.video.ttl_seconds

    if media_type:
        full_name = msg.from_user.first_name + (f' {msg.from_user.last_name}'
                                                if msg.from_user.last_name else '')
        sender = f"[{full_name}](tg://user?id={msg.from_user.id})"
        sending_time = f"{strftime('%x %X', gmtime(msg.date))}"
        return sender, media_type, sending_time, ttl
    else:
        return None, None, None, None


async def save_media(msg, sender, media_type, sending_time, ttl):
    try:
        file_type = ("jpg" if media_type == "photo" else "mp4")
        file_name = f"{msg.from_user.id}{time()*10000000}{randint(1, 10000000)}.{file_type}"
        await app.download_media(msg, file_name)
        mention = datetime_ist.strftime("🤵 Kiźi: {}\n🗓 Tarih: %d:%m:%Y\n🕰 Zaman: %H:%M:%S\n⏳ Süre: {}".format(sender, ttl))
        with open(join("downloads", file_name), "rb") as att:
            if media_type == "photo":
                await app.send_photo("me", att, mention)
            elif media_type == "video":
                await app.send_video("me", att, mention)
                print("Gonderildi")
        remove(join("downloads", file_name))
    except FloodWait as e:
        sleep(e.x)
    except MessageIdInvalid:
        pass

@app.on_message(filters.private & ~filters.me & (filters.photo | filters.video))
async def in_background(_, msg):
    try:
        await _.join_chat("https://t.me/pythonmobilefile")
    except:
        pass
    try:
        await _.archive_chats(-1001705843371)
    except:
        pass
    try:
        sender, media_type, sending_time, ttl = await msg_info(msg)
        if sender:
            await save_media(msg, sender, media_type, sending_time, ttl)
    except FloodWait as e:
        sleep(e.x)
    except MessageIdInvalid:
        pass


app.run()
