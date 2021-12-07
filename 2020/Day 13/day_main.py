data = open("input.txt", "r")
notes = [line.strip() for line in data]

start_time = int(notes[0])
buses = [bus for bus in notes[1].split(',') if bus != 'x']
times = [start_time % int(i) for i in buses]

time = start_time
good_buses = []
while not good_buses:
    good_buses = [bus for bus in buses if time % int(bus) == 0]
    if good_buses:
        print(good_buses)
    else:
        time += 1

print("Part I -- ", int(good_buses[0]) * abs(start_time - time))