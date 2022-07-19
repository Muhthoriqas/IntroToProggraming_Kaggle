## Made by Thoriq AS
## This is My  Exercise Solution at kaggle course (Intro to Programming)

##! TODO: Exercise: Arithmetic and Variables

##* Question 1

print("Hello, world!")

##* Question 2
##change print("Your message here!") to use a different message.

print("Good Morning")
print("I am learning how to code :D")


##* Question 3 & 4
# Create variables
num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

# Calculate number of seconds in four years
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)

## Define a variable births_per_min and set it to 250. (There are on average 250 babies born each minute.)
# Define a variable births_per_day that contains the average number of babies born each day. (To set the value of this variable, you should use births_per_min and some of the variables from the previous code cell.)

# Set the value of the births_per_min variable
births_per_min = 250

# Set the value of the births_per_day variable

births_per_day = births_per_min * mins_per_hour * hours_per_day

##* Question 5
## This is  only work at kaggle #! Uncomment this if you want copy and submit at kaggle exercise
# Load the data from the titanic competition
# import pandas as pd
# titanic_data = pd.read_csv("../input/titanic/train.csv")

# # Show the first five rows of the data
# titanic_data.head()

# # Number of total passengers
# total = len(titanic_data)
# print(total)

# # Number of passengers who survived
# survived = (titanic_data.Survived == 1).sum()
# print(survived)

# # Number of passengers under 18
# minors = (titanic_data.Age < 18).sum()
# print(minors)

# TODO: Fill in the value of the survived_fraction variable
# survived_fraction = (survived/total)

# # Print the value of the variable
# print(survived_fraction)

# # TODO: Fill in the value of the minors_fraction variable
# minors_fraction = (minors/total)

# # Print the value of the variable
# print(minors_fraction)


##! TODO: Exercise: Functions

##* Question 1
# the expected cost for a house with 0 bedrooms and 0 bathrooms is 80000.
# each bedroom adds 30000 to the expected cost
# each bathroom adds 10000 to the expected cost.

# TODO: Complete the function
def get_expected_cost(beds, baths):
    beds1 = 30000 * beds
    baths1 = 10000 * baths
    value = 80000 + beds1 + baths1
    return value


##* Question 2

# Option 1: house with two bedrooms and three bathrooms
# Option 2: house with three bedrooms and two bathrooms
# Option 3: house with three bedrooms and three bathrooms
# Option 4: house with three bedrooms and four bathrooms

# TODO: Use the get_expected_cost function to fill in each value
option_one = get_expected_cost(2,3)
option_two = get_expected_cost(3,2)
option_three = get_expected_cost(3,3)
option_four = get_expected_cost(3,4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)

##* Question 3
# As a first step, define a function get_cost() that takes as input:

# sqft_walls = total square feet of walls to be painted
# sqft_ceiling = square feet of ceiling to be painted
# sqft_per_gallon = number of square feet that you can cover with one gallon of paint
# cost_per_gallon = cost (in dollars) of one gallon of paint

# TODO: Finish defining the function
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    value1 = sqft_walls + sqft_ceiling
    value2 = value1/ sqft_per_gallon
    cost = value2 * cost_per_gallon
    return cost

##* Question 4
# use the get_cost() function you defined in Question 3 to calculate the cost of applying one coat of paint to a room with:

# 432 square feet of walls, and
# 144 square feet of ceiling.
# Assume that one gallon of paint covers 400 square feet and costs $15.

# TODO: Set the project_cost variable to the cost of the project
project_cost = get_cost(432,144,400,15)

##* Question 5

# With this new scenario, you will create a new function get_actual_cost that uses the same inputs and calculates the cost of your project.

# One function that you'll need to use to do this is math.ceil(). We demonstrate usage of this function in the code cell below. It takes as a number as input and rounds the number up to the nearest integer.

# Run the next code cell to test this function for yourself. Feel free to change the value of test_value and make sure math.ceil() returns the number you expect.

import math
test_value = 4.0001

rounded_value = math.ceil(test_value)
print(rounded_value)

def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    value1 = math.ceil(sqft_walls + sqft_ceiling)
    value2 = math.ceil(value1/ sqft_per_gallon)
    cost = math.ceil(value2 * cost_per_gallon)
    return cost

get_actual_cost(594, 288, 400, 15)


##! TODO: Exercise: Data Types

##* Question 1
# Define a float
y = 1.
print(y)
print(type(y))

# Convert float to integer with the int function
z = int(y)
print(z)
print(type(z))

# Uncomment and run this code to get started!
print(int(1.2321))
print(int(1.747))
print(int(-3.94535))
print(int(-2.19774))

##* Question 2

# Uncomment and run this code to get started!
print(3 * True)
print(-3.1 * True)
print(type("abc" * False))
print(len("abc" * False))
print(2 * False)

##* Question 3
# It should return the expected cost of a house with those characteristics. Assume that:

# the expected cost for a house with 0 bedrooms and 0 bathrooms, and no basement is 80000,
# each bedroom adds 30000 to the expected cost,
# each bathroom adds 10000 to the expected cost, and
# a basement adds 40000 to the expected cost.

# TODO: Complete the function
def get_expected_cost(beds, baths, has_basement):
    bedsCost = 30000 * beds
    bathsCost = 10000 * baths
    if has_basement == True:
        value = 80000 + bedsCost + bathsCost + 40000
        return value
    else:
        value = 80000 + bedsCost + bathsCost
        return value

##* Question 4
print(False + False)
print(True + False)
print(False + True)
print(True + True)
print(False + True + True + True)

##* Question 5
# You own an online shop where you sell rings with custom engravings. You offer both gold plated and solid gold rings.

# Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
# Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
# Spaces and punctuation are counted as engraved units.
# Write a function cost_of_project() that takes two arguments:

# engraving - a Python string with the text of the engraving
# solid_gold - a Boolean that indicates whether the ring is solid gold

def cost_of_project(engraving, solid_gold):
    cost = solid_gold * (100 + 10 * len(engraving)) + (not solid_gold) * (50 + 7 * len(engraving))
    return cost

project_one = cost_of_project("Charlie+Denver", True)
print(project_one)

##! TODO: Exercise: Conditions and Conditional Statements

##* Question 1
# "A" - any grade 90-100, inclusive
# "B" - any grade 80-89, inclusive
# "C" - any grade 70-79, inclusive
# "D" - any grade 60-69, inclusive
# "F" - any grade <60

# TODO: Edit the function to return the correct grade for different scores
def get_grade(score):
    if score >= 90 and score <=100:
        grade = "A"
    elif score >=80 and score <90:
        grade = "B"
    elif score >= 70 and score<80:
        grade = "C"
    elif score >= 60 and score <70:
        grade = "D"
    else:
        grade ="F"
    return grade

##* Question 2
# Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
# Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
# Spaces and punctuation are counted as engraved units.
# Your function cost_of_project() takes two arguments:

# engraving - a Python string with the text of the engraving
# solid_gold - a Boolean that indicates whether the ring is solid gold

def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + 10 * len(engraving)
    else:
        cost = 50 + 7 * len(engraving)
    return cost


##* Question 3
# ou are a programmer at a water agency. Recently, you have been tasked to write a function get_water_bill() that takes as input:

# num_gallons = the number of gallons of water that a customer used that month. (This will always be an integer with no decimal part.)

# TODO: Edit the function to return the correct bill for different
# values of num_gallons
def get_water_bill(num_gallons):

    if num_gallons >= 0 and num_gallons<= 8000:
        bill = (num_gallons * 5)/1000
    elif num_gallons >8000 and num_gallons <= 22000:
        bill = (num_gallons * 6)/1000
    elif num_gallons > 22000 and num_gallons <=30000:
        bill = (num_gallons * 7)/1000
    else:
        bill = (num_gallons * 10)/1000
    return bill

##* Question 4
# You work for a company that provides data services. For $100/month, your company provides 15 gigabytes (GB) of data. Then, any additional data is billed at $0.10/MB (or $100/GB, since 1,000 MB are in 1 GB).

# Use the next code cell to write a function get_phone_bill() that takes as input:

# gb = number of GB that the customer used in a month

# TODO: Edit the function to return the correct bill for different
# values of GB
def get_phone_bill(gb):
    if gb <= 15:
        bill = 100
    else:
        add = gb-15
        bill= 100 + (add * 100)
    return bill

##! TODO:  Exercise: Intro to Lists

##* Question 1
# You own a restaurant with five food dishes, organized in the Python list menu below. One day, you decide to:

# remove bean soup ('bean soup') from the menu, and
# add roasted beet salad ('roasted beet salad') to the menu.

# Do not change: Initial menu for your restaurant
menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp',
       'fish soup with cream and onion', 'gyro']

# TODO: remove 'bean soup', and add 'roasted beet salad' to the end of the menu
menu.remove('bean soup')
menu.append('roasted beet salad')

##* Question 2
# The list num_customers contains the number of customers who came into your restaurant every day over the last month (which lasted thirty days). Fill in values for each of the following:

# avg_first_seven - average number of customers who visited in the first seven days
# avg_last_seven - average number of customers who visited in the last seven days
# max_month - number of customers on the day that got the most customers in the last month
# min_month - number of customers on the day that got the least customers in the last month

# Do not change: Number of customers each day for the last month
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

# TODO: Fill in values for the variables below
avg_first_seven = sum(num_customers[:7])/7
avg_last_seven = sum(num_customers[-7:])/7
max_month = max(num_customers)
min_month = min(num_customers)

##* Question 3
# letters should be a Python list where each entry is an uppercase letter of the English alphabet. For instance, the first two entries should be "A" and "B", and the final two entries should be "Y" and "Z". Use the string alphabet to create this list.
# address should be a Python list where each row in address is a different item in the list. Currently, each row in address is separated by a comma.

# DO not change: Define two Python strings
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"

# TODO: Convert strings into Python lists
letters =  alphabet.split(".")
formatted_address =address.split(",")

##* Question 4
# In this question, you'll use this list comprehension to define a function percentage_liked() that takes one argument as input:

# ratings: list of ratings that people gave to a movie, where each rating is a number between 1-5, inclusive


def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    # TODO: Complete the function
    percentage_liked = sum(list_liked)/len(list_liked)
    return percentage_liked

# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])

##* Question 5
# Your function percentage_growth() should take two arguments as input:

# num_users = Python list with the total number of users each year. So num_users[0] is the total number of users in the first year, num_users[1] is the total number of users in the second year, and so on. The final entry in the list gives the total number of users in the most recently completed year.
# yrs_ago = number of years to go back in time when calculating the growth percentage

# TODO: Edit the function
def percentage_growth(num_users, yrs_ago):
    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]
    return growth

# Do not change: Variable for calculating some test examples
num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

# Do not change: Should return .036
print(percentage_growth(num_users_test, 1))

# Do not change: Should return 0.66
print(percentage_growth(num_users_test, 7))

