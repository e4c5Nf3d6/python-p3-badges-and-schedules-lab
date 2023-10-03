def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names]

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room_assignment in assign_rooms(names):
        print(room_assignment)
