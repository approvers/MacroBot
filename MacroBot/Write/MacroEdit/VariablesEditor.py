import discord

from MacroBot.Vars import Vars
from MacroBot.Write.MacroEdit.VariablesEdit.VariablesEditMessage import VariablesEditMessage
from MacroBot.Write.MacroEdit.VariablesEdit.VariablesAddCommand import VariablesAddCommand
from MacroBot.Write.MacroEdit.VariablesEdit.VariablesDelCommand import VariablesDelCommand
from MacroBot.Write.MacroEdit.VariablesEdit.VariablesSetCommand import VariablesSetCommand
from MacroBot.Write.MacroEdit.VariablesEdit.VariablesGetCommand import VariablesGetCommand



class VariablesEditor:
    def __init__(self, edit_vars):
        self.edit_vars = edit_vars
        self._add = VariablesAddCommand(self.edit_vars)
        self._del = VariablesDelCommand(self.edit_vars)
        self._set = VariablesSetCommand(self.edit_vars)
        self._get = VariablesGetCommand(self.edit_vars)


    async def edit(self, message:discord.Message):
        message.__class__ = VariablesEditMessage
        command = message.command_word

        if command is None:
            return

        if self._add.command_is(command):
            await self._add.run(message)
            
        if self._del.command_is(command):
            await self._del.run(message)
            
        if self._set.command_is(command):
            await self._set.run(message)
            
        if self._get.command_is(command):
            await self._get.run(message)