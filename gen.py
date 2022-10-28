import asyncio
from pyrogram import Client
import os

os.system("pip3 install -U pip")
os.system("pip3 install pyrogram==1.3.6")
os.system("clear")

async def main():
    api_id = 19358020
    api_hash = "de33bd71c8d49212c32af0bc10d67617"
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        await app.send_message(
            "me",
            "**Stringiniz**:\n\n"
            f"`{await app.export_session_string()}`"
        )
        print(
            "Telegram Kayıtlı Mesajlara Bakabilirsiniz ! ! !"
        )

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
