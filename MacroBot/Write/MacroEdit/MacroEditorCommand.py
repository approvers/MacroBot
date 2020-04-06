from MacroBot.Write.EditMacroHolder import EditMacroHolder
        


class MacroEditorCommand:
    HEAD = None


    def __init__(self, edit_macro:EditMacroHolder):
        self.edit_macro = edit_macro


    def head_is(self, head:str) -> bool:
        return self.HEAD == head


    async def run(self, *args, **kwargs):
        pass