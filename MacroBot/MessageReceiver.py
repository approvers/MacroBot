import discord

from MacroBot.MacroHolder import MacroHolder
from MacroBot.WriteFlagHolder import WriteFlagHolder
from MacroBot.NormalCommandReceiver import NormalCommandReceiver
from MacroBot.MacroWriter import MacroWriter



class MessageReceiver:
    def __init__(self, macros:MacroHolder):
        self.write_flag = WriteFlagHolder()
        self.command_receiver = NormalCommandReceiver(self.write_flag)
        self.macro_writer = MacroWriter(self.write_flag)

    async def receive(self, message:discord.Message):
        if message.author.bot:
            return

        await self.macro_writer.write(message)
            
        await self.command_receiver.receive(message)