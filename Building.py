import Elevator


class Building:
    def __init__(self, minfloor, maxfloor, elevarr):
        self.elevarr = elevarr
        self.minfloor = minfloor
        self.maxfloor = maxfloor

    def getelev(self, index) -> Elevator:
        for x in self.elevarr:
            if x.serialnum == index:
                return x
        return 0
