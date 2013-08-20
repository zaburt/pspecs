
from comar.service import *

serviceType = "local"
serviceConf = "pam_usb"
serviceDefault = "conditional"

serviceDesc = _({"en": "Pam_usb",
                 "tr": "Pam_usb"})

@synchronized
def start():
    startService(command="/usr/sbin/pam_usb",
                 args = config.get("args", "destroy"),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/pam_usb",
                donotify=True)

def ready():
    import os
    status = is_on()
    if status == "on" or (status == "conditional" and os.path.exists("/sys/coffee/ready")):
        start()

def status():
    return checkDaemon("/var/run/pam_usb.pid")

