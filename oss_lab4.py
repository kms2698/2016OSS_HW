"""
========================
  Rock Scissors Paper
========================

1. Created by : Kim minsang
2. Date of Preparation : 2016.10.12
3. Date of Improvement1 : 2016.10.25

========== ========== =======
 computer     user    outcome
========== ========== =======
Rock          Rock		Draw
Rock        Scissors	Lose
Rock		  Paper		Win
Scissors      Rock		Win
Scissors	Scissors	Draw
Scissors	  Paper		Lose
Paper		  Rock		Lose
Paper		Scissors	Win
Paper		  Paper		Draw
========== ========== =======
"""
import random

def main():
	"""This function is intended return the outcome of Rock Scissors Paper between user  and computer
	:param int my_finger:An integer user chose (1: Scissors 2:Rock 3:Paper)
	:param int com_finger:An integer computer chose (1: Scissors 2:Rock 3:Paper)
	:return: The outcome of Rock Scissors Paper between user and computer
	"""
	com_finger = random.randrange(3) + 1

	for i in range(10):
		my_finger = int(input("가위(1), 바위(2), 보(3)를 입력하세요. "))
		while not(my_finger == 1 or my_finger == 2 or my_finger ==3):
			my_finger = int(input("가위(1), 바위(2), 보(3)를 입력하세요. "))

		if(com_finger == 1):
			if(my_finger == 1):
				print("컴퓨터가 낸 것은 가위입니다. ----> 비김")
			elif(my_finger == 2):
				print("컴퓨터가 낸 것은 가위입니다. ----> 사용자 승!")
			elif(my_finger == 3):
				print("컴퓨터가 낸 것은 가위입니다. ----> 컴퓨터 승!")

		elif(com_finger == 2):
			if(my_finger == 1):
				print("컴퓨터가 낸 것은 바위입니다. ----> 컴퓨터가 승리했습니다!")
			elif(my_finger == 2):
				print("컴퓨터가 낸 것은 가위입니다. ----> 비겼습니다!")
			elif(my_finger == 3):
				print("컴퓨터가 낸 것은 가위입니다. ----> 사용자가 승리했습니다!")

		elif(com_finger == 3):
			if(my_finger == 1):
				print("컴퓨터가 낸 것은 바위입니다. ----> 사용자가 승리했습니다!")
			elif(my_finger == 2):
				print("컴퓨터가 낸 것은 가위입니다. ----> 컴퓨터가 승리했습니다!")
			elif(my_finger == 3):
				print("컴퓨터가 낸 것은 가위입니다. ----> 비겼습니다!")

main()
