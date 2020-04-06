from MacroBot.Write.MacroEdit.VariablesEdit.VariablesEditCommand import VariablesEditCommand
from MacroBot.Write.MacroEdit.VariablesEdit.VariablesEditMessage import VariablesEditMessage



class VariablesAddCommand(VariablesEditCommand):
    COMMAND = "add"
    ARGUMENT_ERROR = "変数名が指定されてないよカス"
    DEFINED_ERROR = "その変数は定義済みだよカス"
    RESULT = "```python\n{} = {}\n```"


    class VariablesAddCommandMessage(VariablesEditMessage):
        def has_name(self) -> bool:
            return self.words_length >= 3
        def has_value(self) -> bool:
            return self.words_length >= 4
        
        def get_name(self) -> str:
            return self.words[3]
        def get_value(self) -> str:
            index = len(VariablesAddCommand.HEAD) + len(VariablesAddCommand.COMMAND) + 2
            return self.content[index:]

        async def send_argument_error(self):
            await self.channel.send(VariablesAddCommand.ARGUMENT_ERROR)
        async def send_defined_error(self):
            await self.channel.send(VariablesAddCommand.DEFINED_ERROR)
        async def send_result(self, name:str, value:str):
            await self.channel.send(VariablesAddCommand.RESULT.format(name, value))
        

    async def run(self, message:VariablesEditMessage):
        message.__class__ = VariablesAddCommand.VariablesAddCommandMessage
        if not message.has_name():
            await message.send_argument_error()
            return

        name = message.get_name()
        if self.edit_vars.has_var(name):
            await message.send_defined_error()
            return

        value = None
        if message.has_value():
            value = message.get_value()

        self.edit_vars[name] = value
        await message.send_result(name, value)