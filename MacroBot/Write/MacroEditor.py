import discord

from MacroBot.Write.EditMacroHolder import EditMacroHolder
from MacroBot.Write.MacroEdit.MacroEditorMessage import MacroEditorMessage
from MacroBot.Write.MacroEdit.EventCommand import EventCommand
from MacroBot.Write.MacroEdit.CodeCommand import CodeCommand
from MacroBot.Write.MacroEdit.VarCommand import VarCommand
from MacroBot.Write.MacroEdit.ExitCommand import ExitCommand



class MacroEditor:
    def __init__(self, edit_macro:EditMacroHolder):
        self.edit_macro = edit_macro
        self.event = EventCommand(self.edit_macro)
        self.code = CodeCommand(self.edit_macro)
        self.var = VarCommand(self.edit_macro)
        self.exit = ExitCommand(self.edit_macro)
        

    async def edit(self, _message:discord.Message):
        message = MacroEditorMessage(_message)
        head = message.head_word

        if self.event.head_is(head):
            await self.event.run(message)
            return
            
        if self.code.head_is(head):
            await self.code.run(message)
            return
            
        if self.var.head_is(head):
            await self.var.run(message)
            return

        if self.exit.head_is(head):
            await self.exit.run(message)
            return