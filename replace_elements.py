my_list = [10, 1, 8, 3, 5]
length = len(my_list)
##replace only 1,2 with 4,5 and keep 3rd elements as is
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

###out put [5, 3, 8, 1, 10]
