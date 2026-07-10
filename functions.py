def hi(name):                   # one argument function
    print("Hi,", name)

hi("Greg")                      #function call

#### two arguments functions.
def hi(n1,n2):
    print("hi,",n1,n2,sep='\n')

hi("name1","name2")       # function call

#op
#hi,
#name1
#name2

## positional arguments
def addr(st,ct,pc):
    print('your address is :- ', st,ct,pc)

s=input("street:- ")
#street:- pune
pc=input("postal code:- ")
#postal code:- 411052
c=input("city:- ")
#maharashtra

print("positional argument check")
###  funtion call
addr(s,pc,c)         ## positional arguments passing

#op 
#your address is :-  pune 411052 maharashtra

#########
##### keyword agruments passing

s=input("street:- ")
#street:- hollywod
pc=input("postal code:- ")
#postal code:- 111111
c=input("city:- ")
#citynew york

## call function
print("keyword argument check")
addr(st=s,ct=c,pc=pc)           ## pass arguments using keyword
#your address is :-  hollywod new york 111111



##### sum of list values
#### we can pass a list to a functions

def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s

print("additoina is : ",list_sum([4,2,1,]))

#### to automate the list creation process

print("automate list of 5 elements in desc order:")
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))

# list creation in order

print("automate list of 5 elements in order:")
def strange_list_fun(n):
    strange_list = []
    c_list = []
    
    for i in range(0, n):
        strange_list.insert(0,i)
        c_list.append(i)
    return strange_list,c_list

print(strange_list_fun(5))


## to check year is even leap or not.

def is_year_leap(year):
    #print('year is',year)
    if year %2 == 0:
        return True
    else:
        return False


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	#if result == test_results[i]:
	if result:
		print("OK")
	else:
		print("Failed")
