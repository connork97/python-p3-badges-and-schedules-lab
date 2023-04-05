def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names): 
    return [f"Hello, my name is {name}." for name in names]
    # badge_list = []
    # for name in names:
    #     badge_list.append(f"Hello, my name is {name}.")
    # return badge_list
    # return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    rooms_names_list = []
    i = 1
    while (i <= 7):
        for name in names:
            # print(f"Hello, {name}! You'll be assigned to room {i}!")
            rooms_names_list.append(f"Hello, {name}! You'll be assigned to room {i}!")
            i += 1
        return rooms_names_list


def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room in assign_rooms(names):
        print(room)

printer(["a", "b", "c", "d"])