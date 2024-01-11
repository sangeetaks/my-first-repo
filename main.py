from game_data import data
from art import logo
from art import vs
import random

print(logo)
first_data ={}
second_data ={}
first_data = random.choice(data)
second_data = random.choice(data)
score =0


def compare(dict_1,dict_2,option):
  global score
  if dict_1['follower_count'] >= dict_2['follower_count'] and option =='A':
    score+=1
    wining = True
    print(f"You're correct ,current score {score}")
    first_data = dict_1
    second_data = random.choice(data)
    #get_data()
  elif dict_2['follower_count'] >= dict_1['follower_count'] and option =='B':
    score+=1
    wining = True
    print(f"You're correct ,current score {score}")
    first_data = dict_2
    second_data = random.choice(data)
    
    #get_data()
  elif dict_1['follower_count'] >= dict_2['follower_count'] and option =='B':
    score+=0
    wining = False
    print(f"Sorry thats wrong final score {score}")
    first_data ={}
    second_data ={}
  else:
    wining = False
    score+=0
    print(f"Sorry thats wrong final score {score}")
    first_data ={}
    second_data ={}
  return first_data, second_data , wining

wining = True
while wining:
  print(f"Compare A : {first_data['name']} ,a {first_data['description']} ,from {first_data['country']} ")
  print(vs)
  print(f"Compare B : {second_data['name']} ,a {second_data['description']} ,from {second_data['country']} ")
#   print(first_data['follower_count'])
#   print(second_data['follower_count'])
  choice = input("Who has more followers type 'A' or 'B' ")
  first_data, second_data ,wining = compare(first_data,second_data,choice)