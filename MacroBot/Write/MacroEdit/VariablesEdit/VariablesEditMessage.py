from MacroBot.Write.MacroEdit.MacroEditorMessage import MacroEditorMessage



class VariablesEditMessage(MacroEditorMessage):
    def __init__(self):
        super().__init__()
        self.command_word = self.words[1] if self.words_length >= 2 else None