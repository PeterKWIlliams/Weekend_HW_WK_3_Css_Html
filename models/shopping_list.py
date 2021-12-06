from models.Items import *


item1 = Items("linguine",1.00,2,False)
item2 = Items("tinned tomatoes",0.80,4,False)
item3 = Items("parsley",1.00,1,False)
item4 = Items("basil",1.00,1,False)
item5 = Items("special K bran flakes",6.00,2,False)
item6 = Items("orange juice",2.00,2,False)


items =[item1,item2,item3,item4,item5,item6]

def add_new_item(item):
    items.append(item)

# def delete_item(item_name):
#     item_to_delete = None
#     for item in items:
#         if item.name == item_name:
#             item_to_delete = item
#     items.remove(item_to_delete)
