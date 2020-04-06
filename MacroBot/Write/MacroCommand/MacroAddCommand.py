from MacroBot.Write.MacroCommand.MacroCommand import MacroCommand
from MacroBot.Write.MacroCommand.MacroCommandMessage import MacroCommandMessage



class MacroAddCommand(MacroCommand):
    COMMADN = "add"
    ARGUMENT_ERROR = "マクロ名が指定されてないよカス"
    DEFINED_ERROR = "そのマクロは定義済みだよカス"
    RESULT = "マクロ\"{}\"を定義したよ"



    class MacroAddCommandMessage(MacroCommandMessage):
        def has_name(self) -> bool:
            return self.words_length >= 3

        def get_name(self) -> str:
            return self.words[2]

        async def send_argument_error(self):
            await self.channel.send(MacroAddCommand.ARGUMENT_ERROR)
        async def send_defined_error(self):
            await self.channel.send(MacroAddCommand.DEFINED_ERROR)
        async def send_result(self, name:str):
            await self.channel.send(MacroAddCommand.RESULT.format(name))
        

    async def run(self, message:MacroCommandMessage):
        message.__class__ = MacroAddCommand.MacroAddCommandMessage
        if not message.has_name():
            await message.send_argument_error()
            return

        name = message.get_name()
        if self.macros.has_macro(name):
            await message.send_defined_error()
            return

        self.macros.add_macro(name)
        await message.send_result(name)