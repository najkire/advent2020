with open('input.txt', 'r') as input_file:
    timestamp = int(input_file.readline().strip())
    bus_ids = [int(i) for i in input_file.readline().strip().split(',') if i != 'x']

ttd = {bus_id: bus_id - timestamp % bus_id for bus_id in bus_ids}
first_id = min(ttd, key=ttd.get)
print(first_id * ttd[first_id])