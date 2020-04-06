import discord

from MacroBot.WriteFlagHolder import WriteFlagHolder



class NormalCommand:
    COMMAND = None


    def command_is(self, content:str) -> bool:
        return self.COMMAND == content


    async def run(self):
        pass


class WriteCommand(NormalCommand):
    COMMAND = "!write"
    TEXT = "†writeモードに変更しました†"


    def __init__(self, write_flag:WriteFlagHolder):
        self.write_flag = write_flag

    async def run(self, channel:discord.TextChannel):
        new_mode = not self.write_flag.get_flag()
        self.write_flag.set_flag(new_mode)
        await channel.send(WriteCommand.TEXT)


class UserIdCommand(NormalCommand):
    COMMAND = "!user_id"


    async def run(self, message:discord.Message):
        channel:discord.TextChannel = message.channel
        author_id:int = message.author.id
        await channel.send(author_id)


class ChannelIdCommand(NormalCommand):
    COMMAND = "!channel_id"


    async def run(self, message:discord.Message):
        channel:discord.TextChannel = message.channel
        channel_id:int = message.channel.id
        await channel.send(channel_id)



class NormalCommandReceiver:
    def __init__(self, write_flag:WriteFlagHolder):
        self.write = WriteCommand(write_flag)
        self.user_id = UserIdCommand()
        self.channel_id = ChannelIdCommand()
        

    async def receive(self, message:discord.Message):
        command = message.content

        if self.write.command_is(command):
            await self.write.run(message.channel)

        if self.user_id.command_is(command):
            await self.user_id.run(message)

        if self.channel_id.command_is(command):
            await self.channel_id.run(message)