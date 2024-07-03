from typing import List, Optional 

def binary_search(lista: List[int], item: int) -> Optional[int]:
    # defines the low and high part of list to track the part of the list that is being searched.
    
    low: int = 0 
    high: int = len(lista) - 1
    
    while low <= high: # while still haven't come up with a single element
        mid: int = int((low + high) / 2) # central element of the list
        guess: int = lista[mid]
        
        if guess == item: 
            return mid # return if found the item
        
        if guess > item: # the guess was high
            high = mid - 1
            continue # continue and try again
        
        # the guess was low
        low = mid + 1
    
    return # item not found

print(binary_search([l for l in range(0, 100000)], 52123)) # example

