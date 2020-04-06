import discord



class MacroCommandMessage(discord.Message):
    def __init__(self):
        super().__init__()
        self.words = self.content.split()
        self.words_length = len(self.words)
        self.head_word = self.words[0]
        self.command_word = self.words[1] if self.words_length >= 2 else None