import datetime
class checkTime():
    def __init__(self):
        pass
    def getTimeSpr(self, func, args):
        pre = datetime.datetime.now()
        exec(func+"("+args+")")
        after = datetime.datetime.now()
        print(after-pre)

import time
class timer(checkTime):
    def __init__(self):
        self.getTimeSpr("self.sleeptime","3")
    def sleeptime(self, times):
        time.sleep(times)

a = timer()