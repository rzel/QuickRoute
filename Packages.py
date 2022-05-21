import datetime
from Distance import get_address
from Distance import get_distance
from Distance import get_current_distance
from Distance import get_shortest_route
from Distance import get_time_truck1
from Distance import get_time_truck2
from Distance import get_time_truck3
from Distance import truck1_index_optimized
from Distance import truck2_index_optimized
from Distance import truck3_index_optimized
from Distance import truck1_list_optimized
from Distance import truck2_list_optimized
from Distance import truck3_list_optimized
from Simulator import get_hash_map
from Simulator import get_truck1_trip1
from Simulator import get_truck1_trip2
from Simulator import get_truck2_trip1

# Time the truck departs from the hub
departure_time1 = '8:00:00'
# Converts departure timestamp to timedelta
(h, m, s) = departure_time1.split(':')
hub_departure_time1 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

# Time the truck departs from the hub
departure_time2 = '9:10:00'
# Converts departure timestamp to timedelta
(h, m, s) = departure_time2.split(':')
hub_departure_time2 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

# Time the truck departs from the hub
departure_time3 = '11:00:00'
# Converts departure timestamp to timedelta
(h, m, s) = departure_time3.split(':')
hub_departure_time3 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

# first delivery list, truck 1
delivery_list1 = []
# distance list, truck 1
truck1_distance_list = []
# Time complexity is 0(n)
i = 0
for value in get_truck1_trip1():
    get_truck1_trip1()[i][9] = departure_time1
    delivery_list1.append(get_truck1_trip1()[i])
    i += 1

try:
    first_variable_count = 0
    for k in delivery_list1:
        for j in get_address():
            if k[2] == j[2]:
                truck1_distance_list.append(j[0])
                delivery_list1[first_variable_count][1] = j[0]
        first_variable_count += 1
except IndexError:
    pass

# Sorts the deliveries into the most efficient order
get_shortest_route(delivery_list1, 1, 0)
first_truck_total_distance = 0
first_truck_package_id = 0

for index in range(len(truck1_index_optimized())):
    try:
        first_truck_total_distance = get_distance(int(truck1_index_optimized()[index]),
                                                  int(truck1_index_optimized()[index + 1]),
                                                  first_truck_total_distance)
        deliver_package = get_time_truck1(get_current_distance(int(truck1_index_optimized()[index]),
                                                               int(truck1_index_optimized()[index + 1])))
        truck1_list_optimized()[first_truck_package_id][10] = (str(deliver_package))
        get_hash_map().update(int(truck1_list_optimized()[first_truck_package_id][0]), delivery_list1)
        first_truck_package_id += 1
    except IndexError:
        pass

# second delivery list, truck 2
delivery_list2 = []
# distance list, truck 2
truck2_distance_list = []
# Time complexity is 0(n)
i = 0
for value in get_truck2_trip1():
    get_truck2_trip1()[i][9] = departure_time2
    delivery_list2.append(get_truck2_trip1()[i])
    i += 1

try:
    second_variable_count = 0
    for k in delivery_list2:
        for j in get_address():
            if k[2] == j[2]:
                truck2_distance_list.append(j[0])
                delivery_list2[second_variable_count][1] = j[0]
        second_variable_count += 1
except IndexError:
    pass

# Sorts the deliveries into the most efficient order
get_shortest_route(delivery_list2, 2, 0)
second_truck_total_distance = 0
second_truck_package_id = 0

for index in range(len(truck2_index_optimized())):
    try:
        second_truck_total_distance = get_distance(int(truck2_index_optimized()[index]),
                                                   int(truck2_index_optimized()[index + 1]),
                                                   second_truck_total_distance)
        deliver_package = get_time_truck2(get_current_distance(int(truck2_index_optimized()[index]),
                                                               int(truck2_index_optimized()[
                                                                                 index + 1])))
        truck2_list_optimized()[second_truck_package_id][10] = (str(deliver_package))
        get_hash_map().update(int(truck2_list_optimized()[second_truck_package_id][0]), delivery_list2)
        second_truck_package_id += 1
    except IndexError:
        pass

# third delivery list, truck 1 second trip
delivery_list3 = []
# distance list, truck 3
truck3_distance_list = []
# Time complexity is 0(n)
i = 0
for value in get_truck1_trip2():
    get_truck1_trip2()[i][9] = departure_time3
    delivery_list3.append(get_truck1_trip2()[i])
    i += 1

try:
    third_variable_count = 0
    for k in delivery_list3:
        for j in get_address():
            if k[2] == j[2]:
                truck3_distance_list.append(j[0])
                delivery_list3[third_variable_count][1] = j[0]
        third_variable_count += 1
except IndexError:
    pass

# Sorts the deliveries into the most efficient order
get_shortest_route(delivery_list3, 3, 0)
third_truck_total_distance = 0
third_truck_package_id = 0

# Time complexity is 0(n)
for index in range(len(truck3_index_optimized())):
    try:
        third_truck_total_distance = get_distance(int(truck3_index_optimized()[index]),
                                                  int(truck3_index_optimized()[index + 1]),
                                                  third_truck_total_distance)
        deliver_package = get_time_truck3(get_current_distance(int(truck3_index_optimized()[index]),
                                                               int(truck3_index_optimized()[index + 1])))
        truck3_list_optimized()[third_truck_package_id][10] = (str(deliver_package))
        get_hash_map().update(int(truck3_list_optimized()[third_truck_package_id][0]), delivery_list3)
        third_truck_package_id += 1
    except IndexError:
        pass


# Time complexity is 0(1)
def get_total_distance():
    total_distance = first_truck_total_distance + second_truck_total_distance + third_truck_total_distance
    return total_distance
