from abc import ABCMeta, abstractmethod


class Plugin(object):
    __metaclass__ = ABCMeta

    def __init__(self, skype, command=""):
        self.skype = skype
        self.command = command

    @abstractmethod
    def message_received(self, status, msg):
        pass

    def help(self, msg):
        text = "{} Has not implemented a help function".format(self.__class__.__name__)
        msg.Chat.SendMessage(text)

    def __repr__(self):
        return str(self.command)

    def __eq__(self, b):
        if isinstance(b, basestring):
            return self.command == b
        else:
            return self.command == b.command

    def __ne__(self, b):
        if isinstance(b, basestring):
            return self.command != b
        else:
            return self.command != b.command

