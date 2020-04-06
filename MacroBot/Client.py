import discord
from discord.ext import tasks
import os

from MacroBot.MacroHolder import MacroHolder
from MacroBot.MessageReceiver import MessageReceiver



class Client(discord.Client):
    __TOKEN = os.environ["TOKEN"]


    def __init__(self):
        super().__init__()

        self.macros = MacroHolder()
        self.message_receiver = MessageReceiver(self.macros)

    
    def run(self):
        super().run(Client.__TOKEN)

    # async def on_ready(self):
    #     self.minute_loop.start()

    async def on_message(self, message):
        await self.message_receiver.receive(message)

    @tasks.loop(seconds=60)
    async def minute_loop(self):
        pass