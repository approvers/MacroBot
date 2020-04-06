from MacroBot.Write.MacroEdit.MacroEditorCommand import MacroEditorCommand
from MacroBot.Write.MacroEdit.MacroEditorMessage import MacroEditorMessage



class CodeCommand(MacroEditorCommand):
    HEAD = "code"
    ARGUMENT_ERROR = "codeが指定されてないよカス"
    RESULT = "[code]```python\n{}```"

    
    class CodeCommandMessage(MacroEditorMessage):
        def has_code(self) -> bool:
            return self.words_length >= 2

        def get_code(self) -> str:
            index = len(CodeCommand.HEAD) + 1
            return self.content[index:]

        async def send_argument_error(self):
            await self.channel.send(CodeCommand.ARGUMENT_ERROR)

        async def send_result(self, code:str):
            await self.channel.send(CodeCommand.RESULT.format(code))


    async def run(self, message:MacroEditorMessage):
        message.__class__ = CodeCommand.CodeCommandMessage
        if not message.has_code():
            await message.send_argument_error()
            return

        macro = self.edit_macro.get_macro()
        code = message.get_code()
        macro.code = code
        await message.send_result(code)