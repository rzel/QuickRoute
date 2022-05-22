import csv
from HashTable import HashTable

# Reads data from CSV file
with open('package_data.csv') as package_file:
    read_packages = csv.reader(package_file, delimiter=',')

    # Creates a hashmap object
    insert_into_hash_table = HashTable()

    # Empty list for truck 1, trip 1
    truck1_trip1 = []

    # Empty list for truck 2, trip 1
    truck2_trip1 = []

    # Empty list for truck 1, trip 2
    truck1_trip2 = []

    # Makes key-value pairs for the hash table dictionary
    # Time complexity is 0(n)
    for row in read_packages:
        package_ID = row[0]
        key = package_ID
        address_ID = row[1]
        street = row[2]
        city = row[3]
        state = row[4]
        zipcode = row[5]
        deliver_by = row[6]
        weight = row[7]
        deliver_start = ''
        address_location = ''
        deliver_status = 'At hub'
        iterate_value = [package_ID, address_location, address_ID, street, city, state, zipcode, deliver_by, weight,
                         deliver_start, deliver_status]

        key = package_ID
        value = iterate_value

        # Constraints that determines which packages are loaded into each truck
        if value[6] != 'EOD':
            if 'Must' in value[8] or 'None' in value[8]:
                truck1_trip1.append(value)
        if 'Can only be' in value[8]:
            truck2_trip1.append(value)
        if 'Delayed' in value[8]:
            truck2_trip1.append(value)

        # Changes incorrect address
        if '84104' in value[5] and '10:30' not in value[6]:
            truck1_trip2.append(value)
        if 'Wrong address listed' in value[8]:
            value[2] = '410 S State St'
            value[5] = '84111'
            truck1_trip2.append(value)

        if value not in truck1_trip1 and value not in truck2_trip1 and value not in truck1_trip2:
            if len(truck2_trip1) > len(truck1_trip2):
                truck1_trip2.append(value)
            else:
                truck2_trip1.append(value)
        insert_into_hash_table.add(key, value)

    # Gets all values
    def get_hash_map():
        return insert_into_hash_table

    # Gets the packages that are loaded onto truck1
    def get_truck1_trip1():
        return truck1_trip1

    # Gets the packages that are loaded onto truck2
    def get_truck2_trip1():
        return truck2_trip1

    # Gets the packages that are loaded onto truck3
    def get_truck1_trip2():
        return truck1_trip2
