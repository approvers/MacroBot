from MacroBot.MacroHolder import MacroHolder
from MacroBot.Write.EditMacroHolder import EditMacroHolder
from MacroBot.Write.MacroCommand.MacroCommand import MacroCommand
from MacroBot.Write.MacroCommand.MacroCommandMessage import MacroCommandMessage



class MacroEditCommand(MacroCommand):
    COMMADN = "del"
    ARGUMENT_ERROR = "マクロ名が指定されてないよカス"
    UNDEFINED_ERROR = "そのマクロは未定義だよカス"
    RESULT = "マクロ\"{}\"を編集対象にしたよ\n[event]```{}```[code]```python\n{}```"



    class MacroEditCommandMessage(MacroCommandMessage):
        def has_name(self) -> bool:
            return self.words_length >= 3

        def get_name(self) -> str:
            return self.words[2]

        async def send_argument_error(self):
            await self.channel.send(MacroEditCommand.ARGUMENT_ERROR)
        async def send_undefined_error(self):
            await self.channel.send(MacroEditCommand.UNDEFINED_ERROR)
        async def send_result(self, name:str, event:str, code:str):
            await self.channel.send(MacroEditCommand.RESULT.format(name, event, code))


    def __init__(self,macros:MacroHolder, edit_macro:EditMacroHolder):
        super().__init__(macros)
        self.edit_macro = edit_macro
        

    async def run(self, message:MacroCommandMessage):
        message.__class__ = MacroEditCommand.MacroEditCommandMessage
        if not message.has_name():
            await message.send_argument_error()
            return

        name = message.get_name()
        if not self.macros.has_macro(name):
            await message.send_undefined_error()
            return

        macro = self.macros.get_macro(name)
        event = macro.event
        code = macro.code
        self.edit_macro.set_macro(macro)
        await message.send_result(name, event, code)