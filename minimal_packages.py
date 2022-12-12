def minimal_number_of_packages(items, available_large_packages, available_small_packages):
    if(items>available_large_packages*5+available_small_packages):
        return -1
    possible_large = (int(items/5))
    if(available_large_packages>=possible_large):
        count = possible_large
        possible_small = items - 5*count 
        count += possible_small
    else:
        count = available_large_packages
        possible_small = items - 5*count
        count+=possible_small

    return count
    
print(minimal_number_of_packages(16, 2, 10))