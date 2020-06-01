#Code to omit Duplicate Numbers from the list:

given_numbers= [1,6,20,20,5,6,9,5,10]
new_list=given_numbers.copy()
for x in given_numbers:
    new_variable= given_numbers.count(x)
    if new_variable==2:
        new_list.remove(x)
    else:
        new_list
print(new_list)