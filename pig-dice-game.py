from random import randint, choice
from time import sleep

# 게임 시작 함수
def game_start():
  player_num = int(input('플레이 인원 수를 정해주세요 (1~3) >> '))
  print('컴퓨터를 포함해 총 {}명이 플레이합니다.'.format(player_num + 1))
  print(f'모든 게임의 시작은 컴퓨터가 합니다.')
  print("=" * 30)

  global turn
  global order
  global order_limit
  global bank
  global score

  turn = ['com']
  bank = [0]  # 임시점수(누적 가능)
  score = [0]   # 총합점수
  order = 0
  order_limit = player_num+1

  for i in range(1, order_limit):
    turn.append('user' + str(i))
    bank.append(0)
    score.append(0)

  return roll_dice(turn, order, order_limit, bank, score)

# 주사위 굴리기 함수
def roll_dice(turn, order, order_limit, bank, score):
    if order == order_limit:
      order = 0
  

    print(f'>> {turn[order]} 차례입니다. [임시점수]: {bank[order]}, [총합점수]: {score[order]}')
    print('주사위를 굴립니다.')
    sleep(1)

    dice = randint(1,6)
    print(f'[{dice}] 나왔습니다.')

    bank[order] += dice


    if dice == 1:
      print("======= 차례가 넘어갑니다. =======")
      bank[order] = 0
      change_turn(turn, order, order_limit)
    else:
      if order == 0:
        com_choose_roll(turn, order, bank, score)
      else:
        user_choose_roll(turn, order, bank, score)

# 턴 체인지 함수
def change_turn(turn, order, order_limit):
  order += 1
  print(" ")
  print("========= 현재 총 스코어 =========")
  for i in range(order_limit):
    print(f'{turn[i]} : {score[i]}점')
    print("=" * 34)
  roll_dice(turn, order, order_limit, bank, score)
  # 멈추고 점수 추가 할지 아님 더 굴릴지


# 컴퓨터 선택 함수
def com_choose_roll(turn, order, bank, score):
  choose = ['roll', 'stop']
  com_choose = choice(choose)

  if com_choose == 'roll':
    print(f"{com_choose}로 이어하겠습니다.")
    roll_dice(turn, order, order_limit, bank, score)
    
  else:
    score[order] += bank[order]
    bank[order] = 0
    print("=" * 34)

    if score[order] >= 50:
      sleep(1)
      print('*' * 34)
      print(f'{turn[order]}가 승리하셨습니다. 축하합니다.')
      print('*' * 34)
      return print('게임이 종료됩니다.')

    print(f"{com_choose}로 턴을 넘기겠습니다.")
    change_turn(turn, order, order_limit)
    
# 유저 선택 함수
def user_choose_roll(turn, order, bank, score):
    user_choose = input('주사위를 굴리겠습니까?(roll or stop) >> ')

    if user_choose == 'roll':
        roll_dice(turn, order, order_limit, bank, score)
    elif user_choose == 'stop':
      score[order] += bank[order]
      bank[order] = 0
      print("=" * 34)

      if score[order] >= 50:
        sleep(1)
        print('*' * 34)
        print(f'{turn[order]}가 승리하셨습니다. 축하합니다.')
        print('*' * 34)
        return print('게임이 종료됩니다.')

      print(f"{user_choose}로 턴을 넘기겠습니다.")
      change_turn(turn, order, order_limit)
    else:
      print('roll or stop 중 입력하십시오.')
      user_choose_roll(turn, order, bank, score)

# Main
if __name__ == "__main__":
    game_start()
