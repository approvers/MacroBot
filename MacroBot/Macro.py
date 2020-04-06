from discord import Message

from MacroBot.Vars import Vars



class Macro:
    message_globals = {}
    message_globals["Message"] = globals()["Message"]


    def __init__(self):
        self.event = ""
        self.code = ""
        self.vars = Vars({})