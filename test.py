import random

# 出拳
punches = ['石头','剪刀','布']
computer_choice = random.choice(punches)
user_choice = random.choice(punches)
iii=punches.index(user_choice)
jjj=punches.index(computer_choice)
print(type(iii))
print(type(jjj))