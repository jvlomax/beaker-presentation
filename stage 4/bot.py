from __future__ import print_function
import Skype4Py

from plugins import time, quote

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
            if command == "time":
                time.give_time(msg)   
            if command == "quote":
                quote.give_quote(msg)         
            else:
                msg.Chat.SendMessage(msg.Body)


if __name__ == "__main__":
    bot = SkypeBot()
    bot.client.Attach()
    while 1:
        pass
        


