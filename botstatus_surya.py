from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    name = "botstatus_surya",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

async def main_surya():
    async with app:
            while True:
                print("Checking...")
                xxx_surya = f"📊 | 𝗟𝗜𝗩𝗘 𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗨𝗦"
                for bot in BOT_LIST:
                    try:
                        yyy_surya = await app.send_message(bot, "/start")
                        aaa = yyy_surya.id
                        await asyncio.sleep(10)
                        zzz_surya = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_surya:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_surya += f"\n\n🤖  @{bot}\n        └ **Down** ❌"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"🚨 **Oops !This @{bot} is down currently** ❌")
                                except Exception:
                                    pass
                            await app.read_chat_history(bot)
                        else:
                            xxx_surya += f"\n\n🤖  @{bot}\n        └ **Alive** ✅"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_surya += f"\n\n✔️ Last checked on: {last_update} ({TIME_ZONE})\n\n**♻️ Refreshes automatically - Powered By @SuryaBots**"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_surya)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(6300)
                        
app.run(main_surya())
