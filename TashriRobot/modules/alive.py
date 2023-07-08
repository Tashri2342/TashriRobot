import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from TashriRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID

PHOTO = [
    "https://te.legra.ph/file/95b4d7a9a6cc9c7a191ac.jpg",
    "https://te.legra.ph/file/d5f6796456709ff9ec758.jpg",
    "https://te.legra.ph/file/b7ce8731d34ad225d72d3.jpg",
    "https://te.legra.ph/file/bea1baad55af57a7e7f2f.jpg",
    "https://te.legra.ph/file/dd94180292e8e6e4cda4c.jpg",
]

Tashri = [
    [
        InlineKeyboardButton(text="📍𝐎𝐰𝐧𝐞𝐫📍", url=f"tg://user?id={OWNER_ID}"),
        InlineKeyboardButton(text="🍒𝐆𝐫𝐨𝐮𝐩🍒", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="α∂∂ мє ιη уσυ ¢нαт🎈",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

lol = "https://te.legra.ph/file/d5f6796456709ff9ec758.jpg"


@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.5)
    await accha.edit("Radhe Radhe..")
    await asyncio.sleep(0.5)
    await accha.edit("Radhe Krishna......")
    await asyncio.sleep(0.5)
    await accha.edit("Krishna Radhe..")
    await asyncio.sleep(0.5)
    await accha.edit("Krishna Krishna......")
    await accha.delete()
    await asyncio.sleep(0.5)
    umm = await m.reply_sticker(
        "CAACAgUAAxkDAAJHbmLuy2NEfrfh6lZSohacEGrVjd5wAAIOBAACl42QVKnra4sdzC_uKQQ"
    )
    await umm.delete()
    await asyncio.sleep(0.8)
    await m.reply_photo(
        lol,
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ♥️ 『[❦Tashri࿐​​​​​​​​​​ ](f"t.me/{BOT_USERNAME}")』**
   ♥️💛💚💜🧡♥️💜💛💚💛♥️💛
  » ᴍʏ ᴏᴡɴᴇʀ : [Tashri](https://t.me/Tashri2342)
  
  
  » ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : {tver}
  
  » ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : {pver}
  
  » ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : {pyver()}
   ♥️💛💚💜🧡♥️💜💛💚💛♥️💛""",                                                
        reply_markup=InlineKeyboardMarkup(Tashri),
    )
__mod_name__ = "♨️ᴀʟɪᴠᴇ♨️"
__help__ = """

*ᴜsᴇʀ ᴄᴏᴍᴍᴀɴᴅs*:
» /alive*:* ᴛᴏ ᴄʜᴇᴀᴋ ❓  ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ?

☆............©️𝙱𝚈 » [Tashri](https://t.me/Tashri2342)............☆"""
