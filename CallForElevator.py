class CallForElevator:
    def __init__(self, src, dest, timeofcall, building, key):
        if src > building.maxfloor or src < building.minfloor or dest > building.maxfloor or dest < building.minfloor:
            print("One of the calls had illegal floor numbers")
            return
        self.src = src
        self.key = key
        self.dest = dest
        self.timeofcall = timeofcall
        if src > dest:
            self.flag = "down"
        else:
            self.flag = "up"
        self.elev = -1
        self.building = building

    def between(self, other) -> bool:
        return self.src < other.flag < self.dest or self.src > other.flag > self.dest
