# ---------------------------------------------------------------------------------
# Name: PicSearcher
# Commands:
# .pic
# ---------------------------------------------------------------------------------


__version__ = (0, 0, 2)
# module by:
# █▀ █▄▀ █ █░░ █░░ ▀█
# ▄█ █░█ █ █▄▄ █▄▄ █▄
#        /\_/\
#       ( o.o )
#        > ^ <
# █▀▄▀█ █▀▀ █▀█ █░█░█
# █░▀░█ ██▄ █▄█ ▀▄▀▄▀
#   you can edit this module
#            2022
# 🔒 Licensed under the AGPL-3.0
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# meta developer: @serafim_shedko
import random
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import Message

from .. import loader, utils


class PicSearcherMod(loader.Module):
    """search a picture in @pic"""

    strings = {"name": "PicSearcher"}

    async def piccmd(self, event):
        "<pic name>"
        args = utils.get_args_raw(event)
        result = await event.client.inline_query("pic", args)
        await result [random.randint(0, 19)].click(event.to_id)
        await event.delete()