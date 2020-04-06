from MacroBot.Write.MacroEdit.VariablesEdit.VariablesEditCommand import VariablesEditCommand
from MacroBot.Write.MacroEdit.VariablesEdit.VariablesEditMessage import VariablesEditMessage

        

class VariablesGetCommand(VariablesEditCommand):
    COMMAND = "get"
    ARGUMENT_ERROR = "変数名が指定されてないよカス"
    UNDEFINED_ERROR = "その変数は未定義だよカス"
    RESULT = "変数の情報だよ\n```python\n{} : {}\n```"


    class VariablesGetCommandMessage(VariablesEditMessage):
        def has_name(self) -> bool:
            return self.words_length >= 3
        
        def get_name(self) -> str:
            return self.words[3]

        async def send_argument_error(self):
            await self.channel.send(VariablesGetCommand.ARGUMENT_ERROR)
        async def send_undefined_error(self):
            await self.channel.send(VariablesGetCommand.UNDEFINED_ERROR)
        async def send_result(self, name:str, value:str):
            await self.channel.send(VariablesGetCommand.RESULT.format(name, value))
        

    async def run(self, message:VariablesEditMessage):
        message.__class__ = VariablesGetCommand.VariablesGetCommandMessage
        if not message.has_name():
            await message.send_argument_error()
            return

        name = message.get_name()
        if not self.edit_vars.has_var(name):
            await message.send_undefined_error()
            return

        value = self.edit_vars[name]
        await message.send_result(name, value)