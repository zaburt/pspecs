
from comar.service import *

serviceType = "local"
serviceConf = "mongoose"
serviceDefault = "conditional"

serviceDesc = _({"en": "Mongoose",
                 "tr": "Mongoose"})

@synchronized
def start():
    startService(command="/usr/sbin/mongoose",
                 args = config.get("args", "destroy"),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/mongoose",
                donotify=True)

def ready():
    import os
    status = is_on()
    if status == "on" or (status == "conditional" and os.path.exists("/sys/coffee/ready")):
        start()

def status():
    return checkDaemon("/var/run/mongoose.pid")

