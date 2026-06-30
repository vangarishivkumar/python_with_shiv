my_list = [9, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
uniqu=[]
for elem in my_list:          # travers thru all list elements
    if elem not in uniqu:     # check element is in unique list if not add in unique list
        uniqu.append(elem)    # if not add element in unique list and continue 
print("The list with unique elements only:")
print(uniqu)
print(my_list)
###### original order by kept as is

################
### approach 1
################

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unique_list = list(set(my_list))

print(unique_list)
##### original order can change in output.



######
## approach 2
######
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unique_list = list(dict.fromkeys(my_list))

print(unique_list)
#### we get sorted output
