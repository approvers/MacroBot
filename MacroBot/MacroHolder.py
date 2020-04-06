from MacroBot.Macro import Macro



class MacroHolder:
    def __init__(self):
        self.macros = {}

    
    def has_macro(self, name) -> bool:
        return name in self.macros


    def add_macro(self, name):
        self.macros[name] = Macro()

    def del_macro(self, name):
        del self.macros[name]

    def set_macro(self, name, macro:Macro):
        self.macros[name] = macro

    def get_macro(self, name) -> Macro:
        return self.macros[name]