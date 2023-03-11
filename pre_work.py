#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    # My code
    print("Hello, " + user_name + "!")
hello_name("Alice")


#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
#my code
    for num in range(1, 101, 2):
        print(num)
#You can call this function simply by typing first_odds()
#first_odds()


#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
  #my code
    max_num = a_list[0]  # start by assuming the first element is the maximum
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num
#numbers = [5, 8, 2, 10, 3, 100, 76, 54, 172]
#print(max_num_in_list(numbers))

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    #my code
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2022))  # False
print(is_leap_year(2024))  # True


#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    #my code

    # Sort the list
    sorted_list = sorted(a_list)

    # Check if each pair of adjacent numbers differ by 1
    for i in range(len(sorted_list)-1):
        if sorted_list[i+1] - sorted_list[i] != 1:
            return False

    # If all pairs of adjacent numbers differ by 1, the list is consecutive
    return True
print(is_consecutive([2,3,4,5,6,7]))  # True
print(is_consecutive([1,2,4,5]))     # False
print(is_consecutive([1,2,3,3,4,5])) # False
print(is_consecutive([1,2,3,4,5]))   # True
