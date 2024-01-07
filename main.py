


def sorting_list(elements_to_sort):
    """
    Take in a list of elements and return a sorted list of the elements
    """  

    char_elements = []

    if type(elements_to_sort[0]) is int:        
        elements_to_sort.sort()        
    else:        
        for element in elements_to_sort:            
            char_elements.append(element.title())
        char_elements.sort()
        return char_elements
    
    return elements_to_sort

    

elements = ["Neat", "Blue", "three", "Ant", "caramel", "Star"]
# elements = [5, 8, 4, 1, 9, 6, 2]

print(sorting_list(elements))


