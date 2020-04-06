from MacroBot.Write.MacroEdit.MacroEditorCommand import MacroEditorCommand
from MacroBot.Write.MacroEdit.MacroEditorMessage import MacroEditorMessage



class EventCommand(MacroEditorCommand):
    HEAD = "event"
    ARGUMENT_ERROR = "eventが指定されてないよカス"
    RESULT = "[event]```{}```"


    class EventCommandMessage(MacroEditorMessage):
        def has_event(self) -> bool:
            return self.words_length >= 2

        def get_event(self) -> str:
            index = len(EventCommand.HEAD) + 1
            return self.content[index:]

        async def send_argument_error(self):
            await self.channel.send(EventCommand.ARGUMENT_ERROR)

        async def send_result(self, event:str):
            await self.channel.send(EventCommand.RESULT.format(event))

    
    async def run(self, message:MacroEditorMessage):
        message.__class__ = EventCommand.EventCommandMessage
        if not message.has_event():
            await message.send_argument_error()
            return

        macro = self.edit_macro.get_macro()
        event = message.get_event()
        macro.event = event
        await message.send_result(event)