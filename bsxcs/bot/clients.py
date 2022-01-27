# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import Client
from asyncio import Queue
from ..vars import Var

StreamBot = Client(
    session_name= 'bsxcs',
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)
StreamQu = Queue()
for x in range(4):
    StreamQu.put_nowait(x)
MultiQu1 = None
MultiQu2 = None
MultiQu3 = None
MultiQu4 = None
MultiCli1 = None
MultiCli2 = None
MultiCli3 = None
MultiCli4 = None
if Var.MULTI_CLIENT:
    if str(Var.MULTI_TOK1).lower() != "none":
        MultiCli1 = Client(
            session_name= ':memory:',
            api_id=Var.API_ID,
            api_hash=Var.API_HASH,
            bot_token=Var.MULTI_TOK1,
            sleep_threshold=Var.SLEEP_THRESHOLD,
            no_updates=True
        )
        MultiQu1 = Queue()
        for x in range(4):
            MultiQu1.put_nowait(x)
    if MultiCli1 and str(Var.MULTI_TOK2).lower() != "none":
        MultiCli2 = Client(
            session_name= ':memory:',
            api_id=Var.API_ID,
            api_hash=Var.API_HASH,
            bot_token=Var.MULTI_TOK2,
            sleep_threshold=Var.SLEEP_THRESHOLD,
            no_updates=True
        )
        MultiQu2 = Queue()
        for x in range(4):
            MultiQu2.put_nowait(x)
    if MultiCli2 and str(Var.MULTI_TOK3).lower() != "none":
        MultiCli3 = Client(
            session_name= ':memory:',
            api_id=Var.API_ID,
            api_hash=Var.API_HASH,
            bot_token=Var.MULTI_TOK3,
            sleep_threshold=Var.SLEEP_THRESHOLD,
            no_updates=True
        )
        MultiQu3 = Queue()
        for x in range(4):
            MultiQu3.put_nowait(x)
    if MultiCli3 and str(Var.MULTI_TOK4).lower() != "none":
        MultiCli4 = Client(
            session_name= ':memory:',
            api_id=Var.API_ID,
            api_hash=Var.API_HASH,
            bot_token=Var.MULTI_TOK4,
            sleep_threshold=Var.SLEEP_THRESHOLD,
            no_updates=True
        )
        MultiQu4 = Queue()
        for x in range(4):
            MultiQu4.put_nowait(x)
