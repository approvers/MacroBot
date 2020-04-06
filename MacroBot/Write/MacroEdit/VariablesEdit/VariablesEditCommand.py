from MacroBot.Vars import Vars



class VariablesEditCommand:
    HEAD = "var"
    COMMAND = None


    def __init__(self, _vars:Vars):
        self.edit_vars = _vars


    def command_is(self, command) -> bool:
        return self.COMMAND == command

    
    async def run(self, *args, **kwargs):
        pass