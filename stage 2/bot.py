from __future__ import print_function
import Skype4Py

class SkypeBot(object):
    def __init__(self):

        self.client = Skype4Py.Skype(Events=self)

    def MessageStatus(self, msg, status):
        print(status)        
        if status == Skype4Py.cmsReceived:        
              
            msg.Chat.SendMessage(msg.Body)

if __name__ == "__main__":
    bot = SkypeBot()
    bot.client.Attach()
    while 1:
        pass
        


