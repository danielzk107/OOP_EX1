class Elevator:
    def __init__(self, serialnum, speed, stopspeed, startspeed, openspeed, closespeed):
        self.serialnum = serialnum
        self.speed = speed
        self.stopspeed = stopspeed
        self.startspeed = startspeed
        self.openspeed = openspeed
        self.closespeed = closespeed
        self.flag = "rest"
        self.call_log = list()
        self.call_log_size = 0
        self.call_time_log = {}  #A dictionary that keeps the time it would take for the elevator to finish each call.

    def setcall(self, call):
        temp = self.gettimeforcall(call)
        self.call_time_log[call.key] = temp
        self.call_log.append(call)
        self.call_log_size += 1

    def gettimeforcall(self, call) -> float:  #Returns the approximated time it would take for the elevator to finish handling the call
        time = call.timeofcall + abs(call.src-call.dest)*self.speed + self.closespeed + self.openspeed + self.startspeed + self.stopspeed
        if self.call_log_size > 0:
            temp = self.call_log.pop(self.call_log_size-1)
            time += abs(call.src-temp.dest)*self.speed + self.call_time_log[temp.key]
            for x in self.call_log:
                if call.timeofcall < self.call_time_log[x.key] and x.between(call):
                    time += abs(call.src-x.src) * self.speed + abs(call.dest-x.dest) * self.speed + 2 * (self.closespeed + self.openspeed + self.startspeed + self.stopspeed)
                else:
                    time += self.call_time_log[x.key]
            self.call_log.append(temp)
        return time

    def removecall(self, call):
        self.call_log.remove(call)
