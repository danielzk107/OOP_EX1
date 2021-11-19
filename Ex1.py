import Elevator
import Building
import CallForElevator
import json
import csv
import sys


def allocate(building, call) -> int:
    mintime = float('inf')
    output = 0
    for x in building.elevarr:
        temp = x.gettimeforcall(call)
        if temp < mintime:
            mintime = temp
            call.elev = x
            output = x.serialnum
    building.getelev(output).setcall(call)
    return abs(output)


def main(num1, num2, newname):
    elevarr = list()
    for x in num1['_elevators']:
        elevarr.append(Elevator.Elevator(x['_id'], x['_speed'], x['_stopTime'], x['_startTime'], x['_openTime'], x['_closeTime']))
    b = Building.Building(int(num1['_minFloor']), int(num1['_maxFloor']), elevarr)
    index = 0
    with open(newname, 'w', newline="") as new_file:
        writer = csv.writer(new_file)
        for line in num2:
            temp = (line[0],  line[1], line[2], line[3], line[4], allocate(b, CallForElevator.CallForElevator(float(line[2]), float(line[3]), float(line[1]), b, index)))
            index += 1
            writer.writerow(temp)


if __name__ == '__main__':
    input_json = open(str(sys.argv[1]), 'r')
    input_csv = open(str(sys.argv[2]), 'r')
    input_name = str(sys.argv[3])
    # input_json = open("B5.json", 'r')
    # input_csv = open("Calls_d.csv", 'r')
    # input_name = "out.csv"
    a = json.load(input_json)
    b = csv.reader(input_csv)
    input_json.close()
    main(a, b, input_name)
    input_csv.close()
