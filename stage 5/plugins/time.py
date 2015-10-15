from datetime import datetime
import base

class Time(base)
    def __init__(self, *args, **kwargs):
        super(Time, self).__init__(*args, **kwargs)
        self.command = "time"
    
    def message_received(self, status, msg):
        msg.Chat.SendMessage("The time is {}".format(datetime.now())
    