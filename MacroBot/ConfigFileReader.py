import configparser
from MacroBot.Singleton import Singleton



class ConfigFileReader(Singleton):
    FILE ="MacroBot/config.ini"


    def set_up(self):
        self._config = configparser.ConfigParser()
        self._config.read(ConfigFileReader.FILE)


    def get(self, *args, **kwargs):
        self._config.get(*args, **kwargs)