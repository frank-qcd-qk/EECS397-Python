"""
Author: "Frank" Chude Qian 
Email: CXQ41@case.edu
"""
import time #! Not used for active writing code, but just for evaluation
import random #! Not used for active writing code, but just for evaluation
import string #! Not used for active writing code, but just for evaluation


#! Control Tag for debug and testing
DEBUG = False
MINIMAL = False

def customPrint(input_str, level=0):
    """
    Parameters
    ----------
    input_str : str
        The text string you want to print it out. It must be a string.

    level : int
        The information level of the string.
    """
    message = str(input_str)
    if level == 0:
        if DEBUG:
            print("[DEBUG]"+message)
    elif level == 1:
        if not MINIMAL: ## Resolve Conflict
            print("[INFO]"+message)
    elif level == 2:
        print("[WARNING]"+message)
    elif level == 3:
        print("[ERROR]"+message)
    elif level == 4:
        print("[CRITICAL]"+message)
    elif level == 5:
        print("[FATAL]"+message)
    else:
        print(message)

# Implement this function:
def store_checkout(inventory_tuple_list, item_purchase_list):
    """
        inventory_tuple_list: 
            A list of tuples. Each tuple has a string representing an
            item name, an int representing a price, and a string representing
            a description.

            Example: [("A", 5, "shiny new A"), ("B", 10, "big heavy B")]

            ! [("ID STRING",int price,"Description"),("ID STRING",int price,"Description")]

        item_purchase_list:
            A list of strings. Each string represents an item name.

            Example: ["A", "A", "B", "C"]


        Return the total price of the items in item_purchase_list by using
        prices from the provided inventory_tuple_list. If an item does not
        have a price, it is free. The descriptions are extra, useless
        information for this function.

        The example inputs here would have a total cost of:
        5 + 5 + 10 + 0 = 20 
    """
    
    """
    Design: Inventory tuple list should be interpreted as dictionary
    Use lookup for each in iten purchase list.
    """
    if (item_purchase_list is None):
        customPrint("Fatal Error, itemlist null!",5)
        return 0 
    if (len(item_purchase_list) == 0):
        customPrint("Fatal Error, empty list!",5)
        return 0
    if (inventory_tuple_list is None):
        customPrint("Fatal Error, price list null!",5)
        return 0 
    if (len(inventory_tuple_list) == 0):
        customPrint("Fatal Error, empty price list list!",5)
        return 0

    #! Create an inventory dictionary
    inventoryDict = {a:b for a,b,c in inventory_tuple_list}
    customPrint("Inventory List: ")
    customPrint(str(inventoryDict))
    sumVal = 0
    for item in item_purchase_list:
        sumVal+=inventoryDict.get(item,0)
    return sumVal


# Implement this function:
def highest_frequency_count(item_list):
    """
        item_list:
            A list of strings. Each string represents an item name.

            Example: ["A", "A", "B", "B" , "C", "A", "B", "B"]


        Find and return a count for the most frequently occurring item
        in item_list.

        In the example, "A" and "B" each appear 3 times, while "C" appears 
        only 1 time. Therefore, expected return value would be 3.
    """
    if (item_list is None):
        customPrint("Fatal Error, itemlist null!",5)
        return 0 

    if (len(item_list) == 0):
        customPrint("Fatal Error, empty list!",5)
        return 0

    counting_dict = {}
    #?: Using dictionary.get function: if exist, return value, otherwise, return 0 which in either way we are going to iterate and udpate it in the dictionary.
    # refer python collection class, counter class
    for item in item_list:
        counting_dict[item]=counting_dict.get(item,0)+1
    customPrint("Current Listing Dictionary: "+str(counting_dict))
    #?: Utilizes python 3.7 feature of sort dictionary 
    # refer: https://thispointer.com/python-how-to-sort-a-dictionary-by-key-or-value/
    newdick = dict(sorted(counting_dict.items(),key=lambda x: x[1],reverse=True))
    customPrint("Sorted Dictionary: "+str(newdick))
    #? How to safely output a value?
    # refer https://stackoverflow.com/questions/3097866/access-an-arbitrary-element-in-a-dictionary-in-python
    return next(iter(newdick.values()))

def lagtest():
    start = time.perf_counter_ns()
    returnval = store_checkout([(str(i), i, str(i)) for i in range(100_000)], [str(i) for i in range(100_000)])
    end = time.perf_counter_ns()
    customPrint("store_checkout function: time in ms: "+str((end-start)/1000000)+" val: "+str(returnval),1)
    start = time.perf_counter_ns()
    returnval = highest_frequency_count([str(i) for i in range(1_000_000)])
    end = time.perf_counter_ns()
    customPrint("highest_frequency_count function: time in ms: "+str((end-start)/1000000)+" val: "+str(returnval),1)
    return

#! Ahhhh I am bored....
def frequencyTest():
    inputList = []
    start = time.perf_counter_ns()
    for i in range(1_000_000):
        inputList.append(str(random.choice(string.ascii_letters)))
    end = time.perf_counter_ns()
    customPrint("Generation Done: time in ms: "+str((end-start)/1000000))
    start = time.perf_counter_ns()
    returnval = highest_frequency_count(inputList)
    end = time.perf_counter_ns()
    customPrint("highest_frequency_count function: time in ms: "+str((end-start)/1000000)+" val: "+str(returnval),1)

def minimaltest():
    returnval = store_checkout([("A", 5, "shiny new A"), ("B", 10, "big heavy B")],["A", "A", "B", "C"])
    customPrint("store_checkout function: val: "+str(returnval),1)
    returnval = highest_frequency_count(["B","B","B","B","A","A","A","A","A","A","A","A","A", "A", "B", "B", "C", "A", "B", "B"])
    customPrint("highest_frequency_count function: val: "+str(returnval),1)


#minimaltest()
#lagtest()
#frequencyTest()