# B6 - Write a function called is_prime() that accepts a number and return True or False if the number of prime or not


def is_prime(num):
  count = 0

  for i in range(2, num):
      if(num % i == 0):
          count = count + 1
          break

  if (count == 0 and num != 1):
      print(str(num) + " is a Prime Number")
      return True
  else:
      print(str(num) +" is not a Prime Number")
      return False

is_prime(6)
is_prime(99)
is_prime(83)