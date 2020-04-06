from MacroBot.Write.MacroEdit.MacroEditorCommand import MacroEditorCommand
from MacroBot.Write.MacroEdit.MacroEditorMessage import MacroEditorMessage



class ExitCommand(MacroEditorCommand):
    HEAD = "exit"
    RESULT = "マクロの編集を終了したよ\n[event]```{}```[code]```python\n{}```"

    
    class ExitCommandMessage(MacroEditorMessage):
        async def send_result(self, event:str, code:str):
            await self.channel.send(ExitCommand.RESULT.format(event, code))


    async def run(self, message:MacroEditorMessage):
        message.__class__ = ExitCommand.ExitCommandMessage
        
        macro = self.edit_macro.get_macro()
        code = macro.code
        event = macro.event
        
        self.edit_macro.exit()
        await message.send_result(event, code)