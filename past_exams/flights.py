


def flights(*args):

    result = ""
    flight_dict = {}

    for i in range(0,len(args),2):
        if args[i] == "Finish":
            break
        else:
            if args[i] not in flight_dict.keys():
                flight_dict[args[i]] = int(args[i+1])
            else:
                flight_dict[args[i]] += int(args[i+1])

    return (flight_dict)



print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
