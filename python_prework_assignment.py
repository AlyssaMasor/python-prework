#Question 1
#Greets a user

def hello_name(user_name):
    print("Hello_" + user_name.upper() + "!")

#Question 2
#Prints odd numbers 1-100

def first_odds():
    numbers = list(range(1,100,2))
    print(numbers)

#Question 3
#Return the max number of a given list
def max_num_in_list(a_list):
    a_list = numbers
numbers = [1,2,3,4,5]
max_number = max(numbers)
print(max_number)

#Question 4
#Tells you if the given year is a leap year

def is_leap_year(a_year):
    if int(a_year) % 4 == 0 and int(a_year) % 100 == 0 and int(a_year) % 400 == 0:
        return True
    elif int(a_year) % 4 == 0 and int(a_year) % 100 != 0 and int(a_year) % 400 != 0:
        return True
    else:
        return False

#Question 5
#Checks if all numbers in a list are consecutive numbers
#All the others I solved totally on my own.  I was really stuck on this so I found this solution on the internet. But supposedly, that's what coding is all about?

def is_consecutive(a_list):
   if len(a_list) < 1:
      return False
   min_val = min(a_list)
   max_val = max(a_list)
   if max_val - min_val + 1 == len(a_list):
      for i in range(len(a_list)):
         if a_list[i] < 0:
            j = -a_list[i] - min_val
         else:
            j = a_list[i] - min_val
            if a_list[j] > 0:
               a_list[j] = -a_list[j]
            else:
               return False
      return True
   return False
a_list = [6, 8, 3, 5, 4, 7]
print(is_consecutive(a_list))