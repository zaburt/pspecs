
from comar.service import *

serviceType = "server"
serviceConf = "redis"
serviceDefault = "off"

serviceDesc = _({"en": "Redis Server",
                 "tr": "Redis Sunucu"})

EXEC = "/usr/sbin/redis-server"
REDIS_PID = config.get("REDIS_PID", "/var/run/redis/redis.pid")
REDIS_USER = config.get("REDIS_USER", "redis")
REDIS_GROUP = config.get("REDIS_GROUP", "redis")
REDIS_CONF = config.get("REDIS_CONF", "/etc/redis.conf")
REDIS_OPTS = config.get("REDIS_OPTS", "redis")

@synchronized
def start():
    startService(command=EXEC,
                 args = "%s %s" % (REDIS_CONF, REDIS_OPTS),
                 pidfile = REDIS_PID,
                 chuid = REDIS_USER,
                 detach = True,
                 makepid = True,
                 donotify = True)

@synchronized
def stop():
    stopService(command = EXEC,
                 chuid = REDIS_USER,
                 donotify = True)

def status():
    return isServiceRunning(REDIS_PID)

