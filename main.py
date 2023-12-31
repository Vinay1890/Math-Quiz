# Function to greet the user
def greet_user(user_name):
  welcome_message = "HELLO, " + user_name + "! Welcome to the math quiz."
  print(welcome_message)


# Function to create a qiestion in the correct format.
def print_question(num1, num2, op):
  question = "What is " + str(num1) + op + str(num2) + "?"
  print(question)


# Function to bid farewell to the user and provide the result.
def print_result(user_name, score):
  farewell_message = farewell_message = "Thanks for giving the quiz, " + user_name + ". Your score is " + str(
      score) + " out of 5."
  print(farewell_message)


# Function to choose the operator based on the random choice integer genrated.
def choose_operator(op_n):
  if op_n == 1:
    return "-"
  elif op_n == 2:
    return "+"
  elif op_n == 3:
    return "*"
  else:
    return "/"


def calculate_answer(n1, n2, op):
  if op == "-":
    return n1 - n2
  elif op == "+":
    return n1 + n2
  elif op == "*":
    return n1 * n2
  elif op == "/":
    return int(n1 / n2)
  else:
    return "Not a valid operation"


# Take input from the user and save it in a variable.
user_name = input("Please enter your name: ")

# Make a cusomized greeting for the userand print it.
greeting = greet_user(user_name)

score = 0
total = 0

while total < 5:
  # importing the random module

  import random

  # using the randint function

  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)

  # Randomly choose the operator
  op_num = random.randint(1, 4)
  op = choose_operator(op_num)

  print_question(num1, num2, op)
  user_answer = int(input("Ans: "))
  correct_answer = calculate_answer(num1, num2, op)

  # check answer and update score.
  if user_answer == correct_answer:
    print("Correct_answer.")
    score = score + 1
  else:
    print("Oops, that's not correct. The correct answer is:", correct_answer)

  total = total + 1

# Make a customized farewell message and print it.
print_result(user_name, score)
import os

current_directory = os.getcwd()
print("Current working directory:", current_directory)