from __future__ import print_function
import Skype4Py

class SkypeBot(object):
    def __init__(self):
        self.tag = "@"
        self.client = Skype4Py.Skype(Events=self)

    def MessageStatus(self, msg, status):      
        if status == Skype4Py.cmsReceived and msg.Body[0] == self.tag:                    
            command = msg.Body.split(" ")[1:]
            if command == "help":
                msg.Chat.SendMessage("Welcome to beaker skype bot help")
            if command == "commands":
                msg.Chat.SendMessage("Help, Commands")
            if "cloud" in msg.Body:
                msg.Chat.SendMessage(msg.Body.replace("cloud", "butt")
            else:
                msg.Chat.SendMessage(msg.Body)


if __name__ == "__main__":
    bot = SkypeBot()
    bot.client.Attach()
    while 1:
        pass
        


