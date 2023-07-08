import random

from telegram import Update
from telegram.ext import CallbackContext

import TashriRobot.modules.truth_and_dare_string as truth_and_dare_string
from TashriRobot import dispatcher
from TashriRobot.modules.disable import DisableAbleCommandHandler


def truth(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


def dare(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)

__help__ = """
*ᴛʀᴜᴛʜ & ᴅᴀʀᴇ*
 ❍ /truth  *:* sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴛʀᴜᴛʜ sᴛʀɪɴɢ.
 ❍ /dare  *:* sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴅᴀʀᴇ sᴛʀɪɴɢ.

☆............𝙱𝚈 » [Tashri](https://t.me/Tashri2342)............☆
"""
__mod_name__ = "⚡ꜰᴜɴ⚡"
