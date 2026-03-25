def new_list():
    new_list = {
        'elements': [],
        'size': 0
    }
    return new_list
    
def add_first(my_list, element):
    
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list    
    
    
def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    
    return my_list


def size(my_list):
    return my_list["size"]


def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False


def first_element(my_list):
    if is_empty(my_list) == True:
        return "IndexError: list index out of range"
    else:
        return my_list["elements"][0]


def last_element(my_list):
    if is_empty(my_list) == True:
        return "IndexError: list index out of range"
    else:
        last_index = size(my_list)-1
        return my_list["elements"][last_index]


def get_element(my_list, pos):
    if pos > size(my_list):
        return "IndexError: list index out of range"
    else:
        return my_list["elements"][pos]


def remove_last(my_list):
    if is_empty(my_list) == False:
        new_list = my_list["elements"].pop()
        my_list["size"] -= 1
        return new_list
    
    else:
        return "IndexError: list index out of range"


def remove_first(my_list):
    if is_empty(my_list) == False:
        new_list = my_list['elements'].pop(0)
        my_list['size'] -= 1
        return new_list
    
    else:
        return "IndexError: list index out of range"


def delete_element(my_list, pos):
    if size(my_list) > pos:
        my_list['elements'].pop(pos)
        my_list['size'] -= 1
        return my_list
    
    else:
        return "IndexError: list index out of range"


def insert_element(my_list, element, pos):
    if size(my_list) >= pos:
        my_list['elements'].insert(pos, element)
        my_list['size'] += 1
        return my_list
    
    else:
        return "IndexError: list index out of range"
    
def is_present(my_list, element,cmp_function):
    for i in range(size(my_list)):
        if cmp_function(element, get_element(my_list, i)) == 0:
            return i
    return 0   


def change_info(my_list, pos, new_info):
    if size(my_list) >= pos:
        my_list['elements'][pos] = new_info
        return my_list
    
    else:
        return "IndexError: list index out of range"


def exchange(my_list, pos_1, pos_2):
    if (pos_1 or pos_2) < size(my_list):
        elem_1 = my_list['elements'][pos_1]
        elem_2 = my_list['elements'][pos_2]
        my_list['elements'][pos_1] = elem_2
        my_list['elements'][pos_2] = elem_1
        return my_list
    
    else:
        return "IndexError: list index out of range"


def sub_list(my_list, pos_i, num_elements):
    new_sub_list = new_list()
    pos_f = pos_i + num_elements
    if pos_f < size(my_list):
        for i in range(pos_i, pos_f):
            elem = get_element(my_list, i)
            add_last(new_sub_list, elem)
        return new_sub_list
    
    else:
        return "IndexError: list index out of range"
    
    
def cmp_function(element_1, element_2):
    if element_1 == element_2:
        return 0
    elif element_1 < element_2:
        return True
    else:
        return False   
    
    
def default_sort_criteria(element_1, element_2):
    """
    Función de comparación por defecto para ordenar elementos.
    
    Parameters:
        element_1 (any): Primer elemento a comparar.
        element_2 (any): Segundo elemento a comparar.
    
    Returns:
        bool: True si el primer elemento es menor que el segundo, False en caso contrario.
    """
    return element_1 < element_2



def selection_sort(my_list, sort_crit = cmp_function):
    """Ordena la lista usando Selection Sort"""
    n = size(my_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if sort_crit(get_element(my_list, j), get_element(my_list, min_index)):
                min_index = j
        if min_index != i:
            exchange(my_list, i, min_index)
    return my_list



def insertion_sort(my_list, sort_crit=default_sort_criteria):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento Insertion Sort.
    
    Parameters:
        my_list (dict): Lista a ordenar (debe contener las claves "elements" y "size").
        sort_crit (function): Función de comparación.
    
    Returns:
        dict: Lista ordenada.
    """
    my_list_copy = my_list["elements"]

    for i in range(1, len(my_list_copy)):
        key = my_list_copy[i]
        j = i - 1
        while j >= 0 and sort_crit(key, my_list_copy[j]):
            my_list_copy[j + 1] = my_list_copy[j]
            j -= 1
        my_list_copy[j + 1] = key

    
    my_list["elements"] = my_list_copy
    my_list["size"] = len(my_list_copy)  

    return my_list

def shell_sort(my_list, sort_crit=default_sort_criteria):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento Shell Sort.
    
    Parameters:
        my_list (dict): Lista a ordenar (debe contener las claves "elements" y "size").
        sort_crit (function): Función de comparación.
    
    Returns:
        dict: Lista ordenada.
    """
    my_list_copy = my_list["elements"]

    n = len(my_list_copy)
    parte = n // 2
    while parte > 0:
        for i in range(parte, n):
            temp = my_list_copy[i]
            j = i
            while j >= parte and sort_crit(temp, my_list_copy[j - parte]):
                my_list_copy[j] = my_list_copy[j - parte]
                j -= parte
            my_list_copy[j] = temp
        parte //= 2

    
    my_list["elements"] = my_list_copy
    my_list["size"] = len(my_list_copy)  

    return my_list


def merge_sort(my_list, sort_crit=default_sort_criteria):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento Merge Sort.
    
    Parameters:
        my_list (dict): Lista a ordenar (debe contener las claves "elements" y "size").
        sort_crit (function): Función de comparación.
    
    Returns:
        dict: Lista ordenada.
    """
    my_list_copy = my_list["elements"]

    def _merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = _merge_sort(arr[:mid])
        right_half = _merge_sort(arr[mid:])

        return _merge(left_half, right_half, sort_crit)

    def _merge(left, right, sort_crit):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if sort_crit(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    
    my_list["elements"] = _merge_sort(my_list_copy)
    my_list["size"] = len(my_list["elements"]) 

    return my_list


def quick_sort(my_list, sort_crit=default_sort_criteria):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento Quick Sort.
    
    Parameters:
        my_list (dict): Lista a ordenar (debe contener las claves "elements" y "size").
        sort_crit (function): Función de comparación.
    
    Returns:
        dict: Lista ordenada.
    """
    my_list_copy = my_list["elements"]

    def _quick_sort(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if sort_crit(x, pivot)]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if not sort_crit(x, pivot) and x != pivot]

        return _quick_sort(left) + middle + _quick_sort(right)

    # Ordenar y actualizar la lista
    my_list["elements"] = _quick_sort(my_list_copy)
    my_list["size"] = len(my_list["elements"])  # Actualizar el tamaño

    return my_list