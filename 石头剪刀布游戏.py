import random

# 出拳
punches = ['石头','剪刀','布']
computer_choice = random.choice(punches)
user_choice = ''
user_choice = input('请出拳：（石头、剪刀、布）')  # 请用户输入选择
while user_choice not in punches:  # 当用户输入错误，提示错误，重新输入
    print('输入有误，请重新出拳')
    user_choice = input()

# 亮拳
print('————战斗过程————')
print('电脑出了：%s' % computer_choice)
print('你出了：%s' % user_choice)

# 胜负
win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
print('—————结果—————')
if user_choice == computer_choice:
    print('\033[32;1m平局\033[0m')
elif [user_choice,computer_choice] in win_list:
    print('\033[31;1m你赢了You WIN!!!\033[0m')
else:
    print('\033[31;1m你输了You LOSE!!!\033[0m')