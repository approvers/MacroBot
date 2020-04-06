from MacroBot.MacroHolder import MacroHolder
from MacroBot.Write.MacroCommand.MacroCommandMessage import MacroCommandMessage



class MacroCommand:
    COMMADN = None


    def __init__(self, macros:MacroHolder):
        self.macros = macros

    
    def command_is(self, commad:str) -> bool:
        return self.COMMADN == commad


    async def run(self, *args, **kwargs):
        pass