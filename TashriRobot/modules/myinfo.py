import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from TashriRobot import telethn as bot
from TashriRobot import telethn as tgbot
from TashriRobot.events import register

edit_time = 5
""" =======================❦Tashri࿐​​​​​​​​​​  𝐑𝐨𝐛𝐨𝐭====================== """
file1 = "https://te.legra.ph/file/95b4d7a9a6cc9c7a191ac.jpg"
file2 = "https://te.legra.ph/file/d5f6796456709ff9ec758.jpg"
file3 = "https://te.legra.ph/file/b7ce8731d34ad225d72d3.jpg"
file4 = "https://te.legra.ph/file/bea1baad55af57a7e7f2f.jpg"
file5 = "https://te.legra.ph/file/dd94180292e8e6e4cda4c.jpg"
""" =======================❦Tashri࿐​​​​​​​​​​  𝐑𝐨𝐛𝐨𝐭====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("information", data="informations")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"Hey {firstname}, \n Click on the button below \n to get info about you",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        LILIE = "ᴘᴏᴡᴇʀᴇᴅ ʙʏ ❦Tashri࿐​​​​​​​​​​  𝐑𝐨𝐛𝐨𝐭\n\n"
        LILIE += f"ғɪʀsᴛ ɴᴀᴍᴇ: {PRO.first_name} \n"
        LILIE += f"ʟᴀsᴛ ɴᴀᴍᴇ: {PRO.last_name}\n"
        LILIE += f"ʏᴏᴜ ʙᴏᴛ : {PRO.bot} \n"
        LILIE += f"ʀᴇsᴛʀɪᴄᴛᴇᴅ : {PRO.restricted} \n"
        LILIE += f"ᴜsᴇʀ ɪᴅ: {boy}\n"
        LILIE += f"ᴜsᴇʀɴᴀᴍᴇ : {PRO.username}\n"
        await event.answer(LILIE, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__command_list__ = ["myinfo"]
__mod_name__ = "📍ɪɴғᴏ📍"
__help__ = """
 /myinfo  ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ɪɴғᴏ 

☆............𝙱𝚈 » [Tashri](https://t.me/Tashri2342)............☆"""
