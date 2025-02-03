def unique_elements():
    lst = list(map(int, input().split()))
    unique_lst = []
    
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    
    print()( unique_lst)

unique_elements()
