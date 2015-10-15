from __future__ import print_function
import Skype4Py

from plugins import time, quote

class SkypeBot(object):
    def __init__(self):
        self.tag = "@"
        self.client = Skype4Py.Skype(Events=self)
        self.plugins = []
        self.load_plugins()
        # This is a more advanced feature
        plugin_names = [type(x).__name__for x in self.plugins]
        print("Loaded plugins: {}".format(" ".join(plugin_names)))
    def MessageStatus(self, msg, status):      
        if status == Skype4Py.cmsReceived and msg.Body[0] == self.tag:      
        
            command = msg.Body.split(" ")[1:]
            for plugin in self.enabled_plugins
                if plugin == command:
                    plugin.message_received(status, msg)
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

    def load_plugins(self):
        from plugins.baseclass import Plugin
        for root, dirs, files in os.walk("plugins"):
            for file in [fname for fname in files if fname.endswith(".py") and not fname.startswith(("__"))] # Find all files ending with.py, ignore __init__
                if file == "baseclass.py":                      # Hacky way to eliminate the plugin base class
                    continue
                module_name = os.path.splitext(file)[0]         # strip ".py"
                module = __import__(module_name)                # Import module
                for cls in dir(module):                         # use dir to iterate over the classes
                    class_object = getattr(module, cls)         # get the object          
                    try:
                        if issubclass(class_object, Plugin):    # If the object is a subclass of plugin, this is the correct class
                            instance = class_object(self.skype) # Create an instance of the object
                            self.plugins.append(instance) # Add the instance to our list of plugins
                    except:
                        pass                                    # This is a different class, not what we are looking for


if __name__ == "__main__":
    bot = SkypeBot()
    bot.client.Attach()
    while 1:
        pass
        


