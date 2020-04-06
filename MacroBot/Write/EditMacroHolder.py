from MacroBot.Macro import Macro



class EditMacroHolder:
    def __init__(self, macro:Macro=None):
        self.edit_macro = macro


    def is_edit_mode(self) -> bool:
        return not self.edit_macro is None

    def get_macro(self) -> Macro:
        return self.edit_macro
    
    def set_macro(self, macro:Macro):
        self.edit_macro = macro

    def exit(self):
        self.edit_macro = None