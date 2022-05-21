import csv
import datetime

# Reads data from CSV file
with open('Data/distance_data.csv') as distance_file:
    read_distances = csv.reader(distance_file, delimiter=',')
    read_distances = list(read_distances)

# Reads data from CSV file
with open('Data/address_data.csv') as address_file:
    read_addresses = csv.reader(address_file, delimiter=',')
    read_addresses = list(read_addresses)

    # Time that the trucks leave the hub
    first_time_list = ['8:00:00']
    second_time_list = ['9:10:00']
    third_time_list = ['11:00:00']

    # Gets package address data
    # Time-complexity is 0(n)
    def get_address():
        return read_addresses

    # Gets total distance from distance data
    # Time-complexity is 0(1)
    def get_distance(row_value, column_value, sum_of_distance):
        distance = read_distances[row_value][column_value]
        if distance == '':
            distance = read_distances[column_value][row_value]

        sum_of_distance += float(distance)
        return sum_of_distance

    # Gets current distance from distance data
    # Time-complexity is 0(n)
    def get_current_distance(row_value, column_value):
        distance = read_distances[row_value][column_value]
        if distance == '':
            distance = read_distances[column_value][row_value]
        return float(distance)

    # Gets timestamp for truck 1
    # Time-complexity is 0(n)
    def get_time_truck1(distance):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        first_time_list.append(final_time)
        total = datetime.timedelta()
        for i in first_time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            total += d
        return total

    # Gets timestamp for truck 2
    # Time-complexity is 0(n)
    def get_time_truck2(distance):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        second_time_list.append(final_time)
        total = datetime.timedelta()
        for i in second_time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            total += d
        return total

    # Gets timestamp for truck 3
    # Time-complexity is 0(n)
    def get_time_truck3(distance):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        third_time_list.append(final_time)
        total = datetime.timedelta()
        for i in third_time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            total += d
        return total

    # Lists represent sorted trucks in order of efficiency
    first_truck = []
    first_truck_indices = []
    second_truck = []
    second_truck_indices = []
    third_truck = []
    third_truck_indices = []

    # Algorithm uses a 'greedy approach' to determine the best location to deliver to next based on the
    # current location.

    # Uses three parameters:
    # (1) list of packages on a truck that has not been optimized yet
    # (2) truck numbers
    # (3) the current location that is updated each time the truck moves

    # To find the shortest route, the first 'for loop' will cycle until the lowest value is found.
    # Once the lowest value is decided, the second 'for loop' will check which truck the package is associated with.
    # When all possible routes have been searched, the package is added to the truck. Once the list is empty, the call
    # will end.

    # Time complexity is 0(n^2)
    def get_shortest_route(truck_distance_list, truck_number, current_location):
        if len(truck_distance_list) == 0:
            return truck_distance_list
        else:
            try:
                lowest_value = 50.0
                new_location = 0
                for index in truck_distance_list:
                    if get_current_distance(current_location, int(index[1])) <= lowest_value:
                        lowest_value = get_current_distance(current_location, int(index[1]))
                        new_location = int(index[1])

                for index in truck_distance_list:
                    if get_current_distance(current_location, int(index[1])) == lowest_value:
                        if truck_number == 1:
                            first_truck.append(index)
                            first_truck_indices.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = new_location
                            get_shortest_route(truck_distance_list, 1, current_location)

                        elif truck_number == 2:
                            second_truck.append(index)
                            second_truck_indices.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = new_location
                            get_shortest_route(truck_distance_list, 2, current_location)

                        elif truck_number == 3:
                            third_truck.append(index)
                            third_truck_indices.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = new_location
                            get_shortest_route(truck_distance_list, 3, current_location)
            except IndexError:
                pass

    # Insert zero for the first index of the lists
    first_truck_indices.insert(0, '0')
    second_truck_indices.insert(0, '0')
    third_truck_indices.insert(0, '0')

    # Functions that return a value
    # Time Complexity is O(1)
    def truck1_index_optimized():
        return first_truck_indices

    def truck1_list_optimized():
        return first_truck

    def truck2_index_optimized():
        return second_truck_indices

    def truck2_list_optimized():
        return second_truck

    def truck3_index_optimized():
        return third_truck_indices

    def truck3_list_optimized():
        return third_truck
