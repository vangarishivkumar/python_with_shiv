def is_prime(num):
    if num==2:
        return True
    for i in range (2,num):
        if num%i != 0 :   ## check prime or not?
          return True
        else:
            return False

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")

## or call function for any number
#e.g print(is_prime(2))   --> True
