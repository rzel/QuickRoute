from Packages import get_total_distance
from Simulator import get_hash_map
import datetime

# CLI application to interact with the simulator
class Main:
    print("\nQuickRoute")
    print('All packages delivered in', "{0:.2f}".format(get_total_distance(), 2), 'miles.')

    # CLI main menu
    print("\nMAIN MENU --------------------------------------------------")
    print("| 1 | Check status of package by ID")
    print("| 2 | Check status of all packages")
    print("------------------------------------------------------------")
    start = input("Enter 1 or 2: ")

    # User is asked for a package ID, then a timestamp to display the delivery status
    # Time complexity is 0(n)
    if start == '1':
        try:
            print("\nPACKAGE LOOKUP by ID ---------------------------------------")
            count = input('Enter package ID: ')
            departure_time = get_hash_map().get(str(count))[9]
            delivered_time = get_hash_map().get(str(count))[10]
            package_status_time = input('Enter time (HH:MM:SS): ')
            print('------------------------------------------------------------')
            # Converts users timestamp input to the package status time
            (h, m, s) = package_status_time.split(':')
            package_status_timestamp = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            # Converts users timestamp input to the truck departure time
            (h, m, s) = departure_time.split(':')
            departure_timestamp = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            # Converts users timestamp input to the package delivered time
            (h, m, s) = delivered_time.split(':')
            delivered_timestamp = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

            # Checks if package has left the hub
            if departure_timestamp >= package_status_timestamp:
                get_hash_map().get(str(count))[9] = departure_time
                get_hash_map().get(str(count))[10] = 'AT HUB'
                print('Package ID:', get_hash_map().get(str(count))[0],
                      '\t\t\t\tWeight:', get_hash_map().get(str(count))[7], 'lbs.',
                      '\nDeliver By:', get_hash_map().get(str(count))[6],
                      '\nTruck leaves at', get_hash_map().get(str(count))[9],
                      '\t\tStatus:', get_hash_map().get(str(count))[10],
                      '\nTo:',
                      '\t', get_hash_map().get(str(count))[2], '\n\t', get_hash_map().get(str(count))[3],
                      '\n\t', get_hash_map().get(str(count))[4] + ',', get_hash_map().get(str(count))[5])

            # Checks if package is in route
            elif departure_timestamp <= package_status_timestamp:
                if package_status_timestamp < delivered_timestamp:
                    get_hash_map().get(str(count))[9] = departure_time
                    get_hash_map().get(str(count))[10] = 'IN TRANSIT'
                    print('Package ID:', get_hash_map().get(str(count))[0],
                          '\t\t\t\tWeight:', get_hash_map().get(str(count))[7], 'lbs.',
                          '\nDeliver By:', get_hash_map().get(str(count))[6],
                          '\nTruck left at', get_hash_map().get(str(count))[9],
                          '\t\tStatus:', get_hash_map().get(str(count))[10],
                          '\nTo:',
                          '\t', get_hash_map().get(str(count))[2], '\n\t', get_hash_map().get(str(count))[3],
                          '\n\t', get_hash_map().get(str(count))[4] + ',', get_hash_map().get(str(count))[5])

                # Displays the delivery time if package has already been delivered by the users timestamp input
                else:
                    get_hash_map().get(str(count))[10] = delivered_time
                    get_hash_map().get(str(count))[9] = departure_time
                    print('Package ID:', get_hash_map().get(str(count))[0],
                          '\t\t\t\tWeight:', get_hash_map().get(str(count))[7], 'lbs.',
                          '\nDeliver By:', get_hash_map().get(str(count))[6],
                          '\nTruck left at', get_hash_map().get(str(count))[9],
                          '\t\t\tStatus: DELIVERED at', get_hash_map().get(str(count))[10],
                          '\nTo:',
                          '\t', get_hash_map().get(str(count))[2], '\n\t', get_hash_map().get(str(count))[3],
                          '\n\t', get_hash_map().get(str(count))[4] + ',', get_hash_map().get(str(count))[5])
        except ValueError:
            print('Invalid entry')

    # User is asked for a timestamp, then all packages display their status at that time
    # Time complexity is 0(n)
    if start == '2':
        try:
            print("\nLOOKUP ALL PACKAGES ----------------------------------------")
            package_status_time = input('Enter time (HH:MM:SS): ')
            print('------------------------------------------------------------')
            # Converts users timestamp input to the package status time
            (h, m, s) = package_status_time.split(':')
            package_status_timestamp = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            for count in range(1, 41):
                try:
                    departure_time = get_hash_map().get(str(count))[9]
                    delivered_time = get_hash_map().get(str(count))[10]
                    # Converts users timestamp input to the truck departure time
                    (h, m, s) = departure_time.split(':')
                    departure_timestamp = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    # Converts users timestamp input to the package delivered time
                    (h, m, s) = delivered_time.split(':')
                    delivered_timestamp = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                except ValueError:
                    pass

                # Checks if package has left the hub
                if departure_timestamp >= package_status_timestamp:
                    get_hash_map().get(str(count))[10] = 'AT HUB'
                    get_hash_map().get(str(count))[9] = departure_time
                    print('Package ID:', get_hash_map().get(str(count))[0],
                          '\t\t\t\tWeight:', get_hash_map().get(str(count))[7], 'lbs.',
                          '\nDeliver By:', get_hash_map().get(str(count))[6],
                          '\nTruck leaves at', get_hash_map().get(str(count))[9],
                          '\t\tStatus:', get_hash_map().get(str(count))[10],
                          '\nTo:',
                          '\t', get_hash_map().get(str(count))[2], '\n\t', get_hash_map().get(str(count))[3],
                          '\n\t', get_hash_map().get(str(count))[4] + ',', get_hash_map().get(str(count))[5],
                          '\n------------------------------------------------------------')

                # Checks if package is in route
                elif departure_timestamp <= package_status_timestamp:
                    if package_status_timestamp < delivered_timestamp:
                        get_hash_map().get(str(count))[10] = 'IN TRANSIT'
                        get_hash_map().get(str(count))[9] = departure_time
                        print('Package ID:', get_hash_map().get(str(count))[0],
                              '\t\t\t\tWeight:', get_hash_map().get(str(count))[7], 'lbs.',
                              '\nDeliver By:', get_hash_map().get(str(count))[6],
                              '\nTruck left at', get_hash_map().get(str(count))[9],
                              '\t\t\tStatus:', get_hash_map().get(str(count))[10],
                              '\nTo:',
                              '\t', get_hash_map().get(str(count))[2], '\n\t', get_hash_map().get(str(count))[3],
                              '\n\t', get_hash_map().get(str(count))[4] + ',', get_hash_map().get(str(count))[5],
                              '\n------------------------------------------------------------')

                    # Displays the delivery time if package has already been delivered by the users timestamp input
                    else:
                        get_hash_map().get(str(count))[10] = delivered_time
                        get_hash_map().get(str(count))[9] = departure_time
                        print('Package ID:', get_hash_map().get(str(count))[0],
                              '\t\t\t\tWeight:', get_hash_map().get(str(count))[7], 'lbs.',
                              '\nDeliver By:', get_hash_map().get(str(count))[6],
                              '\nTruck left at', get_hash_map().get(str(count))[9],
                              '\t\t\tStatus: DELIVERED at', get_hash_map().get(str(count))[10],
                              '\nTo:',
                              '\t', get_hash_map().get(str(count))[2], '\n\t', get_hash_map().get(str(count))[3],
                              '\n\t', get_hash_map().get(str(count))[4] + ',', get_hash_map().get(str(count))[5],
                              '\n------------------------------------------------------------')
        except IndexError:
            print(IndexError)

        except ValueError:
            print('Invalid entry')
