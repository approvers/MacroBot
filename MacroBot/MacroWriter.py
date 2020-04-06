import discord

from MacroBot.WriteFlagHolder import WriteFlagHolder
from MacroBot.MacroHolder import MacroHolder
from MacroBot.Write.EditMacroHolder import EditMacroHolder
from MacroBot.Write.MacroCommandReceiver import MacroCommandReceiver
from MacroBot.Write.MacroEditor import MacroEditor


class MacroWriter:
    def __init__(self, write_flag:WriteFlagHolder):
        self.write_flag = write_flag
        self.macros = MacroHolder()
        self.edit_macro = EditMacroHolder()
        self.receiver = MacroCommandReceiver(self.macros, self.edit_macro)
        self.editor = MacroEditor(self.edit_macro)

    
    async def write(self, message:discord.Message):
        if self.write_flag.is_false():
            return

        if self.edit_macro.is_edit_mode():
            await self.receiver.receive(message)
            return

        #ここ嫌い
        await self.editor.edit(message)