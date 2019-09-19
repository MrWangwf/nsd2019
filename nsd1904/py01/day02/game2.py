import random

all_choices = ['石头', '剪刀', '布']
# 将玩家赢的三种情况放到列表中
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
computer = random.choice(all_choices)
player = input('请出拳(石头/剪刀/布): ')

print("Your choice: %s, Computer's choice: %s" % (player, computer))
# 人机选择一样为平
if player == computer:
    print('\033[32;1m平局\033[0m')
# 人机组成的列表是win_list中的一项为胜
elif [player, computer] in win_list:
    print('\033[31;1mYou WIN!!!\033[0m')
# 未平未赢则为输
else:
    print('\033[31;1mYou LOSE!!!\033[0m')
