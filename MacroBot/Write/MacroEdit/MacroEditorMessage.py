import discord



class MacroEditorMessage(discord.Message):
    def __init__(self, message:discord.Message):
        super().__setattr__()
        self.words = self.content.split()
        self.words_length = len(self.words)
        self.head_word = self.words[0]