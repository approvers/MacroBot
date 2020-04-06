from MacroBot.Write.MacroEdit.MacroEditorCommand import MacroEditorCommand
from MacroBot.Write.MacroEdit.MacroEditorMessage import MacroEditorMessage
from MacroBot.Write.MacroEdit.VariablesEditor import VariablesEditor


class VarCommand(MacroEditorCommand):
    HEAD = "var"
    ARGUMENT_ERROR = "コマンドが指定されてないよカス"
    RESULT = "[event]\n```{}```"


    class VarCommandMessage(MacroEditorMessage):
        def has_command(self) -> bool:
            return self.words_length >= 2

        async def send_argument_error(self):
            await self.channel.send(VarCommand.ARGUMENT_ERROR)


    def __init__(self, edit_macro):
        super().__init__(edit_macro)
        self.edit_vars = {}
        self.editor = VariablesEditor(self.edit_vars)

    
    async def run(self, message:MacroEditorMessage):
        message.__class__ = VarCommand.VarCommandMessage

        if not message.has_command():
            await message.send_argument_error()
            return

        edit_macro = self.edit_macro.get_macro()
        self.edit_vars = edit_macro.vars
        self.editor.edit(message)