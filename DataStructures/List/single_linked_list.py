def new_list():
    
    new_list = {
        'first': None,
        'last': None,
        'size': 0
    }
    return new_list

def add_first(my_list, element):

    new_node = {
        "info": element,
        "next": my_list["first"]  
    }
    
    my_list["first"] = new_node
  
    if my_list["size"] == 0:
        my_list["last"] = new_node

    my_list["size"] += 1
    
def add_last(my_list, element):

    new_node = { 
        "info": element, 
        "next": None
    }
    
    if my_list["size"] == 0: 
        my_list["first"] = new_node
        my_list["last"] = new_node
        
    else: 
        
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node
        
    my_list["size"] += 1    
    
def first_element(my_list):
    
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    else: 
        return my_list["first"]    


def is_empty(my_list):
    if my_list['size'] > 0:
        return False
    else:
        return  True
    
def size(my_list):
    
    return my_list["size"]    


def last_element(my_list):
    
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    else:
        return my_list["last"]
    

def delete_element(my_list, pos):

    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    
    if pos == 0:
        my_list["first"] = my_list["first"]["next"]
        my_list["size"] -= 1
        
        if my_list["size"] == 0:
            my_list["last"] = None
        return my_list

   
    prev = my_list["first"]
    for _ in range(pos - 1):
        prev = prev["next"]

    
    to_delete = prev["next"]

   
    prev["next"] = to_delete["next"]

   
    if to_delete == my_list["last"]:
        my_list["last"] = prev

   
    my_list["size"] -= 1

    return my_list
    
    
    
    
def remove_first(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    
    eliminado = my_list["first"]["info"]
    
    my_list["first"] = my_list["first"]["next"]
    
    if my_list["first"] is None: 
        my_list["last"] = None 
        
        
    my_list["size"] -= 1 
    
    return eliminado    


def remove_last(my_list):
    
    if my_list["size"] == 1:
        
        eliminado = my_list["last"]["info"]
        
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] -= 1 
        return eliminado
        
    actual = my_list["first"]
    
    while actual["next"] != my_list["last"]:
        actual = actual["next"]

    eliminado = my_list["last"]["info"]
    
    actual["next"] = None
    my_list["last"] = actual
    
    my_list["sizw"] -= 1 
    
    return eliminado 

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0 
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else: 
            temp = temp["next"]
            count += 1 
            
    if not is_in_array:
        count = -1
    return count


def insert_element(my_list, element, pos):
    
    if pos < 0 or pos > size(my_list):  
        raise Exception('IndexError: list index out of range')
    
    if pos == 0:
        
        add_first(my_list, element)
        return my_list
    
    if pos == my_list["size"]:
        
        add_last(my_list, element)
        return my_list
    
    nuevo_nodo = {"info": element, "next": None}
    
    curr = my_list["first"]
    for _ in range(pos - 1):
        curr = curr["next"]
        
    nuevo_nodo["next"] = curr["next"]
    
    curr["next"] = nuevo_nodo
    
    my_list["size"] += 1 
    
    return my_list

def get_element(my_list, pos):
    
    if pos < 0 or pos >= my_list["size"]:
        raise Exception('IndexError: list index out of range')
    
    current = my_list["first"]
    
    for _ in range(pos):
        current = current["next"]
        
    return current["info"]


def change_info(my_list, pos, new_info):
    
    if pos < 0 or pos >= my_list["size"]:  
        raise Exception('IndexError: list index out of range')
    
    current = my_list["first"]
    for _ in range(pos):
        current = current["next"]
        
    current["info"] = new_info
    
    return my_list


def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= my_list["size"] or pos_2 < 0 or pos_2 >= my_list["size"]:
        raise IndexError("Una de las posiciones está fuera de rango")

    if pos_1 == pos_2:  #
        return my_list

    
    current_1 = my_list["first"]
    for _ in range(pos_1):
        current_1 = current_1["next"]

    current_2 = my_list["first"]
    for _ in range(pos_2):
        current_2 = current_2["next"]

    
    current_1["info"], current_2["info"] = current_2["info"], current_1["info"]

    return my_list


def sub_list(my_list, start, end):
    if start < 0 or start >= my_list["size"] or end <= start:
        return {"first": None, "last": None, "size": 0}  
    if end > my_list["size"]:
        end = my_list["size"]  

    sublist = {"first": None, "last": None, "size": 0}
    current = my_list["first"]
    

    for _ in range(start):
        current = current["next"]

    
    while start < end:
        new_node = {"info": current["info"], "next": None}

        if sublist["first"] is None:
            sublist["first"] = new_node
            sublist["last"] = new_node
        else:
            sublist["last"]["next"] = new_node
            sublist["last"] = new_node
        
        current = current["next"]
        start += 1
        sublist["size"] += 1

    return sublist 


def default_sort_criteria(x_1,x_2):
    
    if x_1 > x_2: #caso_1 (mayor que) 
        return False
    
    elif x_1 < x_2: #caso_2 (menor que)  
        return True
    
    else: #caso_3 (iguales) 
        return 0



def selection_sort(my_list, sort_crit=default_sort_criteria):
    """
    Ordena una lista enlazada simple utilizando el algoritmo de Selection Sort.
    
    Parameters:
        my_list (dict): Lista enlazada simple (debe contener "first", "last" y "size").
        sort_crit (function): Función de comparación (por defecto, default_function).
    
    Returns:
        dict: Lista ordenada.
    """
    if my_list["size"] <= 1:
        return my_list

    current = my_list["first"]
    while current is not None:
        min_node = current
        next_node = current["next"]
        while next_node is not None:
            if sort_crit(next_node["info"], min_node["info"]) == -1:
                min_node = next_node
            next_node = next_node["next"]
        # Intercambiar los valores de los nodos
        current["info"], min_node["info"] = min_node["info"], current["info"]
        current = current["next"]

    return my_list


def insertion_sort(my_list, sort_crit=default_sort_criteria):
    """
    Ordena una lista enlazada simple utilizando el algoritmo de Insertion Sort.
    
    Parameters:
        my_list (dict): Lista enlazada simple (debe contener "first", "last" y "size").
        sort_crit (function): Función de comparación (por defecto, default_function).
    
    Returns:
        dict: Lista ordenada.
    """
    if my_list["size"] <= 1:
        return my_list

    sorted_list = new_list()
    current = my_list["first"]

    while current is not None:
        next_node = current["next"]
        if sorted_list["size"] == 0:
            add_first(sorted_list, current["info"])
        else:
            actual = sorted_list["first"]
            prev = None
            while actual is not None and sort_crit(actual["info"], current["info"]) == -1:
                prev = actual
                actual = actual["next"]
            if prev is None:
                add_first(sorted_list, current["info"])
            else:
                new_node = {"info": current["info"], "next": actual}
                prev["next"] = new_node
                sorted_list["size"] += 1
        current = next_node

    my_list["first"] = sorted_list["first"]
    my_list["last"] = sorted_list["last"]
    my_list["size"] = sorted_list["size"]

    return my_list

def shell_sort(my_list, sort_crit=default_sort_criteria):
    """
    Ordena una lista enlazada simple utilizando el algoritmo de Shell Sort.
    
    Parameters:
        my_list (dict): Lista enlazada simple (debe contener "first", "last" y "size").
        sort_crit (function): Función de comparación (por defecto, default_function).
    
    Returns:
        dict: Lista ordenada.
    """
    if my_list["size"] <= 1:
        return my_list

    # Convertir la lista enlazada en una lista de Python para facilitar el acceso por índices
    elements = []
    current = my_list["first"]
    while current is not None:
        elements.append(current["info"])
        current = current["next"]

    n = len(elements)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = elements[i]
            j = i
            while j >= gap and sort_crit(elements[j - gap], temp) == 1:
                elements[j] = elements[j - gap]
                j -= gap
            elements[j] = temp
        gap //= 2

    # Actualizar la lista enlazada con los elementos ordenados
    current = my_list["first"]
    for element in elements:
        current["info"] = element
        current = current["next"]

    return my_list



def merge_sort(my_list, sort_crit=default_sort_criteria):
    """
    Ordena una lista enlazada simple utilizando el algoritmo de Merge Sort.
    
    Parameters:
        my_list (dict): Lista enlazada simple (debe contener "first", "last" y "size").
        sort_crit (function): Función de comparación (por defecto, default_function).
    
    Returns:
        dict: Lista ordenada.
    """
    if my_list["size"] <= 1:
        return my_list

    # Función auxiliar para dividir la lista en dos mitades
    def split_list(head):
        slow = head
        fast = head["next"]
        while fast is not None and fast["next"] is not None:
            slow = slow["next"]
            fast = fast["next"]["next"]
        mid = slow["next"]
        slow["next"] = None
        return head, mid

    # Función auxiliar para mezclar dos listas ordenadas
    def merge(left, right):
        dummy = {"info": None, "next": None}
        tail = dummy

        while left is not None and right is not None:
            if sort_crit(left["info"], right["info"]) == -1:
                tail["next"] = left
                left = left["next"]
            else:
                tail["next"] = right
                right = right["next"]
            tail = tail["next"]

        if left is not None:
            tail["next"] = left
        if right is not None:
            tail["next"] = right

        return dummy["next"]

    # Función recursiva para Merge Sort
    def _merge_sort(head):
        if head is None or head["next"] is None:
            return head

        left, right = split_list(head)
        left = _merge_sort(left)
        right = _merge_sort(right)
        return merge(left, right)

    # Ordenar la lista
    my_list["first"] = _merge_sort(my_list["first"])

    # Actualizar el último nodo
    current = my_list["first"]
    while current["next"] is not None:
        current = current["next"]
    my_list["last"] = current

    return my_list



def quick_sort(my_list, sort_crit=default_sort_criteria):
    """
    Ordena una lista enlazada simple utilizando el algoritmo de Quick Sort.
    
    Parameters:
        my_list (dict): Lista enlazada simple (debe contener "first", "last" y "size").
        sort_crit (function): Función de comparación (por defecto, default_function).
    
    Returns:
        dict: Lista ordenada.
    """
    if my_list["size"] <= 1:
        return my_list

    # Función auxiliar para obtener el último nodo
    def get_tail(head):
        while head is not None and head["next"] is not None:
            head = head["next"]
        return head

    # Función auxiliar para particionar la lista
    def partition(head, tail):
        pivot = tail["info"]
        prev = None
        current = head
        new_head = head

        while current != tail:
            if sort_crit(current["info"], pivot) == -1:
                if new_head == current:
                    new_head = current["next"]
                if prev is not None:
                    prev["next"] = current["next"]
                temp = current["next"]
                current["next"] = None
                tail["next"] = current
                tail = current
                current = temp
            else:
                prev = current
                current = current["next"]

        return new_head, tail

    # Función recursiva para Quick Sort
    def _quick_sort(head, tail):
        if head is None or head == tail:
            return head

        new_head, pivot = partition(head, tail)
        if new_head != pivot:
            temp = new_head
            while temp["next"] != pivot:
                temp = temp["next"]
            temp["next"] = None
            new_head = _quick_sort(new_head, temp)
            temp = get_tail(new_head)
            temp["next"] = pivot

        pivot["next"] = _quick_sort(pivot["next"], tail)
        return new_head

    # Ordenar la lista
    my_list["first"] = _quick_sort(my_list["first"], my_list["last"])

    # Actualizar el último nodo
    current = my_list["first"]
    while current["next"] is not None:
        current = current["next"]
    my_list["last"] = current

    return my_list