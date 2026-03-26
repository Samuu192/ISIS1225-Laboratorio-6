import random
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as al


def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(int(num_elements / load_factor))

    table = {
        "prime": prime,
        "capacity": capacity,
        "scale": random.randint(1, prime - 1),
        "shift": random.randint(0, prime - 1),
        "table": al.new_list(),
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
    }

    for _ in range(capacity):
        entry = me.new_map_entry(None, None)
        al.add_last(table["table"], entry)

    return table


def put(my_map, key, value):
    hash_index = mf.hash_value(my_map, key)
    slot = find_slot(my_map, key, hash_index)
    entry = al.get_element(my_map["table"], slot)

    if me.get_key(entry) == key:
        me.set_value(entry, value)
    else:
        me.set_key(entry, key)
        me.set_value(entry, value)
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

        if my_map["current_factor"] > my_map["limit_factor"]:
            rehash(my_map)

    return my_map


def get(my_map, key):
    hash_index = mf.hash_value(my_map, key)
    slot = find_slot(my_map, key, hash_index)
    entry = al.get_element(my_map["table"], slot)

    if me.get_key(entry) == key:
        return me.get_value(entry)
    return None


def contains(my_map, key):
    hash_index = mf.hash_value(my_map, key)
    slot = find_slot(my_map, key, hash_index)
    entry = al.get_element(my_map["table"], slot)
    return me.get_key(entry) == key


def remove(my_map, key):
    hash_index = mf.hash_value(my_map, key)
    slot = find_slot(my_map, key, hash_index)
    entry = al.get_element(my_map["table"], slot)

    if me.get_key(entry) == key:
        me.set_key(entry, "__EMPTY__")
        me.set_value(entry, None)
        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    return my_map


def size(my_map):
    return my_map["size"]


def is_empty(my_map):
    return my_map["size"] == 0


def key_set(my_map):
    keys = al.new_list()
    for i in range(my_map["capacity"]):
        entry = al.get_element(my_map["table"], i)
        key = me.get_key(entry)
        if key is not None and key != "__EMPTY__":
            al.add_last(keys, key)
    return keys


def value_set(my_map):
    values = al.new_list()
    for i in range(my_map["capacity"]):
        entry = al.get_element(my_map["table"], i)
        key = me.get_key(entry)
        if key is not None and key != "__EMPTY__":
            al.add_last(values, me.get_value(entry))
    return values


def is_available(my_map, slot):
    entry = al.get_element(my_map["table"], slot)
    key = me.get_key(entry)
    return key is None or key == "__EMPTY__"


def find_slot(my_map, key, hash_index):
    capacity = my_map["capacity"]
    slot = hash_index % capacity
    first_available = None

    for _ in range(capacity):
        entry = al.get_element(my_map["table"], slot)
        current_key = me.get_key(entry)

        if current_key == key:
            return slot
        elif current_key is None:
            return first_available if first_available is not None else slot
        elif current_key == "__EMPTY__":
            if first_available is None:
                first_available = slot

        slot = (slot + 1) % capacity

    return first_available if first_available is not None else 0


def rehash(my_map):
    old_entries = []

    for i in range(my_map["capacity"]):
        entry = al.get_element(my_map["table"], i)
        key = me.get_key(entry)
        if key is not None and key != "__EMPTY__":
            old_entries.append((key, me.get_value(entry)))

    new_capacity = mf.next_prime(my_map["capacity"] * 2)
    my_map["capacity"] = new_capacity
    my_map["size"] = 0
    my_map["current_factor"] = 0
    my_map["table"] = al.new_list()

    for _ in range(new_capacity):
        entry = me.new_map_entry(None, None)
        al.add_last(my_map["table"], entry)

    for key, value in old_entries:
        put(my_map, key, value)

    return my_map


def default_compare(key, entry):
    entry_key = me.get_key(entry)
    if key == entry_key:
        return 0
    elif key > entry_key:
        return 1
    return -1