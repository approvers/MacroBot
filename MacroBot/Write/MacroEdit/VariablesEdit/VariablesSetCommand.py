from MacroBot.Write.MacroEdit.VariablesEdit.VariablesEditCommand import VariablesEditCommand
from MacroBot.Write.MacroEdit.VariablesEdit.VariablesEditMessage import VariablesEditMessage



class VariablesSetCommand(VariablesEditCommand):
    COMMAND = "set"
    ARGUMENT_NAME_ERROR = "変数名が指定されてないよカス"
    ARGUMENT_VALUE_ERROR = "値が指定されてないよカス"
    UNDEFINED_ERROR = "その変数は未定義済みだよカス"
    RESULT = "値を更新したよ\n```python\n{} = {}\n```"


    class VariablesSetCommandMessage(VariablesEditMessage):
        def has_name(self) -> bool:
            return self.words_length >= 3
        def has_value(self) -> bool:
            return self.words_length >= 4
        
        def get_name(self) -> str:
            return self.words[3]
        def get_value(self) -> str:
            index = len(VariablesSetCommand.HEAD) + len(VariablesSetCommand.COMMAND) + 2
            return self.content[index:]

        async def send_argument_name_error(self):
            await self.channel.send(VariablesSetCommand.ARGUMENT_NAME_ERROR)
        async def send_argument_value_error(self):
            await self.channel.send(VariablesSetCommand.ARGUMENT_VALUE_ERROR)
        async def send_undefined_error(self):
            await self.channel.send(VariablesSetCommand.UNDEFINED_ERROR)
        async def send_result(self, name:str, value:str):
            await self.channel.send(VariablesSetCommand.RESULT.format(name, value))
        

    async def run(self, message:VariablesEditMessage):
        message.__class__ = VariablesSetCommand.VariablesSetCommandMessage
        if not message.has_name():
            await message.send_argument_name_error()
            return

        if not message.has_value():
            await message.send_argument_value_error()
            return

        name = message.get_name()
        if not self.edit_vars.has_var(name):
            await message.send_undefined_error()
            return

        value = message.get_value()

        self.edit_vars[name] = value
        await message.send_result(name, value)