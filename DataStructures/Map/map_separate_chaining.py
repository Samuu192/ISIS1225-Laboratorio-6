import random
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as al


def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(int(num_elements / load_factor))

    table = {"prime": prime,
             "capacity": capacity,
             "scale": random.randint(1, prime - 1),
             "shift": random.randint(0, prime - 1),
             "table": None,
             "current_factor": 0,
             "limit_factor": load_factor,
             "size": 0}

    # Cada slot es un ArrayList vacío (la cadena)
    table["table"] = al.new_list()
    for _ in range(capacity):
        chain = al.new_list()
        al.add_last(table["table"], chain)

    return table


def put(my_map, key, value):
    hash_index = mf.hash_value(my_map, key)
    slot = (hash_index % my_map["capacity"]) + 1
    chain = al.get_element(my_map["table"], slot)

    # Buscar si la llave ya existe en la cadena
    entry = default_compare(key, chain)

    if entry is not None:
        # Llave encontrada: actualizar valor
        me.set_value(entry, value)
    else:
        # Llave nueva: agregar al final de la cadena
        new_entry = me.new_map_entry(key, value)
        al.add_last(chain, new_entry)
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

        if my_map["current_factor"] > my_map["limit_factor"]:
            rehash(my_map)

    return my_map


def get(my_map, key):

    hash_index = mf.hash_value(my_map, key)
    slot = (hash_index % my_map["capacity"]) + 1
    chain = al.get_element(my_map["table"], slot)

    entry = default_compare(key, chain)
    if entry is not None:
        return me.get_value(entry)
    return None


def contains(my_map, key):
    
    hash_index = mf.hash_value(my_map, key)
    slot = (hash_index % my_map["capacity"]) + 1
    chain = al.get_element(my_map["table"], slot)

    return default_compare(key, chain) is not None


def remove(my_map, key):

    hash_index = mf.hash_value(my_map, key)
    slot = (hash_index % my_map["capacity"]) + 1
    chain = al.get_element(my_map["table"], slot)

    for i in range(1, al.size(chain) + 1):
        entry = al.get_element(chain, i)
        if me.get_key(entry) == key:
            # Reemplazar con el último elemento y reducir tamaño
            last = al.get_element(chain, al.size(chain))
            chain["elements"][i] = last
            chain["size"] -= 1
            my_map["size"] -= 1
            my_map["current_factor"] = my_map["size"] / my_map["capacity"]
            break

    return my_map


def size(my_map):

    return my_map["size"]


def is_empty(my_map):

    return my_map["size"] == 0


def key_set(my_map):

    keys = al.new_list()
    for i in range(1, my_map["capacity"] + 1):
        chain = al.get_element(my_map["table"], i)
        for j in range(1, al.size(chain) + 1):
            entry = al.get_element(chain, j)
            al.add_last(keys, me.get_key(entry))
    return keys


def value_set(my_map):

    values = al.new_list()
    for i in range(1, my_map["capacity"] + 1):
        chain = al.get_element(my_map["table"], i)
        for j in range(1, al.size(chain) + 1):
            entry = al.get_element(chain, j)
            al.add_last(values, me.get_value(entry))
    return values


# ---------------------------------------------------------------
# Funciones auxiliares
# ---------------------------------------------------------------

def default_compare(key, chain):

    for i in range(1, al.size(chain) + 1):
        entry = al.get_element(chain, i)
        if me.get_key(entry) == key:
            return entry
    return None


def rehash(my_map):

    # Guardar todas las entradas actuales
    old_entries = []
    for i in range(1, my_map["capacity"] + 1):
        chain = al.get_element(my_map["table"], i)
        for j in range(1, al.size(chain) + 1):
            entry = al.get_element(chain, j)
            old_entries.append((me.get_key(entry), me.get_value(entry)))

    # Nueva capacidad
    new_capacity = mf.next_prime(my_map["capacity"] * 2)
    my_map["capacity"] = new_capacity
    my_map["size"] = 0
    my_map["current_factor"] = 0

    # Reiniciar tabla con cadenas vacías
    my_map["table"] = al.new_list()
    for _ in range(new_capacity):
        chain = al.new_list()
        al.add_last(my_map["table"], chain)

    # Reinsertar todas las entradas
    for key, value in old_entries:
        put(my_map, key, value)

    return my_map