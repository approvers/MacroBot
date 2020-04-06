from MacroBot.Write.MacroCommand.MacroCommand import MacroCommand
from MacroBot.Write.MacroCommand.MacroCommandMessage import MacroCommandMessage



class MacroDelCommand(MacroCommand):
    COMMADN = "del"
    ARGUMENT_ERROR = "マクロ名が指定されてないよカス"
    UNDEFINED_ERROR = "そのマクロは未定義だよカス"
    RESULT = "マクロ\"{}\"を削除したよ\n[event]```{}```[code]```python\n{}```"



    class MacroDelCommandMessage(MacroCommandMessage):
        def has_name(self) -> bool:
            return self.words_length >= 3

        def get_name(self) -> str:
            return self.words[2]

        async def send_argument_error(self):
            await self.channel.send(MacroDelCommand.ARGUMENT_ERROR)
        async def send_undefined_error(self):
            await self.channel.send(MacroDelCommand.UNDEFINED_ERROR)
        async def send_result(self, name:str, event:str, code:str):
            await self.channel.send(MacroDelCommand.RESULT.format(name, event, code))
        

    async def run(self, message:MacroCommandMessage):
        message.__class__ = MacroDelCommand.MacroDelCommandMessage
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
        self.macros.del_macro(name)
        await message.send_result(name, event, code)