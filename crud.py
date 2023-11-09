items_list = {
    'Jhon' : 20,
    'Daniel' : 12, 
    'Bob' : 2, 
    'Mark' : 42, 
    'Paul' : 30, 
}

def get_items() -> dict:
    global items_list
    return items_list


def post_items(set):
    global items_list 
    items_list = dict(set)
    return

def put_item(item_id, data):
    global items_list
    items_list[item_id] = data
    return

def delete_item(key:str): 
    global items_list
    if not items_list.keys().__contains__(key):
        raise Exception
    items_list.pop(key)
    return

def update_item(item_id, data): 
    global items_list
    for k in items_list.keys():
        if item_id == k:
            items_list[k] = data
    return
    
