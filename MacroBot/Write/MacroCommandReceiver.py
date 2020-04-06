import discord

from MacroBot.MacroHolder import MacroHolder
from MacroBot.Write.EditMacroHolder import EditMacroHolder
from MacroBot.Write.MacroCommand.MacroAddCommand import MacroAddCommand
from MacroBot.Write.MacroCommand.MacroDelCommand import MacroDelCommand
from MacroBot.Write.MacroCommand.MacroEditCommand import MacroEditCommand
from MacroBot.Write.MacroCommand.MacroCommandMessage import MacroCommandMessage


class MacroCommandReceiver:
    HEAD = "macro"


    def __init__(self, macros:MacroHolder, edit_macro:EditMacroHolder):
        self.macros = macros
        self.edit_macro = edit_macro
        self._add = MacroAddCommand(self.macros)
        self._del = MacroDelCommand(self.macros)
        self._edit = MacroEditCommand(self.macros, self.edit_macro)

    
    async def receive(self, message:discord.Message):
        message.__class__ = MacroCommandMessage

        head = message.head_word
        if head != MacroCommandReceiver.HEAD:
            return

        command = message.command_word
        if command is None:
            return

        if self._add.command_is(command):
            await self._add.run(message)
            return

        if self._del.command_is(command):
            await self._del.run(message)
            return

        if self._edit.command_is(command):
            await self._edit.run(message)
            return