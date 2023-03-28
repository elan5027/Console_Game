import time
import os
import chaticter
import gameset
import random
# @ 현재 위치
# # 갈수있는곳
# ! 몬스터 위치
# * 탈출 지점
# $ 무기 획득 지점


def ending(num):
    print("게임 Over")
    if num == 0:
        print("몬스터에 의하여 사망하였습니다.")
        exit(0)
    if num == 1:
        print("다양한 이유")
        exit(0)
    time.sleep(2)
    os.system('cls||clear')


def start():
    os.system('cls||clear')
    print("가끔씩 튀어오는 따가운 불똥에 피부가 따갑고, 숲속에서 불어오는 바람에 피부에 소름이 돋으려는 것을 보니 꿈은 아닌것 같다.")
    time.sleep(2)
    print("지금 당장 할 수 있는 선택지는 이대로 아침이 오길 기다리거나 무슨 일이 벌어지기 전에 이 숲에서 나가는 길 밖에 없는 것 같다.")
    time.sleep(2)
    print("일단 정신을 차리고 떠올려 보자 내 이름은 뭐지?")
    name = input("내 이름은 >>")
    user = chaticter.CreateUser(name, 17)
    time.sleep(1.5)
    print(f'내 이름은 {user.name}이다 ')
    time.sleep(1.5)
    print("이제 현실을 마주할 시간이다 어떻게하지?")
    print("1. 이곳에서 아침을 기다린다.")
    print("2. 사람이 지나다니는 걸로 보이는 길을 따라 나선다")
    i = choice("start")
    time.sleep(1.5)
    if i == '1':
        print("주변에서 많은 기척이 느껴진다.")
        for i in range(3):
            start_battle(user)
            print("지금이라도 자리를 벗어날까?")
            if check_yesno():
                break

    print("어딜 봐도 모두 다 비슷해 보인다.")
    print("이동하기 전에 길을 해매지 않으려면 표시를 남겨야 할것 같다.")
    gameset.mapset()
    gameset.showmap()
    os.system("pause")
    os.system('cls||clear')

    while (True):
        os.system('cls||clear')
        i = choice("select")
        if i == '1':
            usermove(user)
            if user.hp <= 0:
                return ending(0)

        elif i == '2':
            user.show_status()
            os.system("pause")
            os.system('cls||clear')
        elif i == '3':
            print("미구현")
            os.system("pause")
            os.system('cls||clear')

        elif i == '4':
            gameset.showmap()
            os.system("pause")
            os.system('cls||clear')
        else:
            print("잘못된 입력입니다.")


def usermove(user):

    print("""
            1. 앞으로 간다 
            2. 왼쪽으로 간다.
            3. 오른쪽으로 간다.
            4. 뒤로 간다
    *움직일 때 마다 컨티션이 1씩 감소합니다.
            """)
    cmd = input("어디로 갈까 ? >> ")
    if cmd == '1' or cmd == '2' or cmd == '3' or cmd == '4':
        event = gameset.move(cmd)
        if user.condition > 0:
            user.condition = max(user.condition-1, 0)
        else:
            user.hp = max(user.hp-1, 0)
        if event == "battle":
            start_battle(user)

        elif event == "camp":
            camp(user)
            os.system("pause")
            os.system('cls||clear')

        elif event == "escape":
            # 탈출 루트 [ 게임 엔딩 ]
            escape()
            return exit()

    else:
        print("잘못된 입력입니다.")
        os.system("pause")


def choice(scene):
    while (True):
        if scene == "start":
            cmd = input("어떻게 할까? >> ")
            if cmd == '1' or cmd == '2':
                return cmd
            else:
                print("잘못된 입력입니다.")
                os.system("pause")

        elif scene == "explore":
            cmd = input("어떻게 할까? >>")

        elif scene == "select":
            print("1. 이동하기")
            print("2. 몸상태 확인")
            print("3. 소지품 확인")
            print("4. 지나온길 떠올리기")
            cmd = input("어떻게 할까? >> ")
            if cmd == '1' or cmd == '2' or cmd == '3' or cmd == '4':
                return cmd
            else:
                print("잘못된 입력입니다.")
                os.system("pause")


def escape():
    print("숲에서 나가는 길을 발견했다.")
    # 아이템으로 분기 또는 각종 설정 추가.


def camp(user):
    print("잠시 쉬어 갈 만한 공간을 발견했다.")
    print("휴식을 취하시겠습니까?")
    if check_yesno():
        user.recovery()
    for i in range(3):
        print(" . . . ")
        time.sleep(1)
    print("휴식을 취하니 몸상태가 많이 좋아진 것 같다.")
    user.show_status()
    # 체력 및 컨디션 회복 또는 아이템 관련 추가.


def check_yesno():
    while (True):
        cmd = input("계속 진행 하시겟습니까? [ y / n ]")
        if cmd == 'y' or cmd == 'Y':
            return True
        elif cmd == 'n' or cmd == 'N':
            return False
        else:
            print("잘못된 입력입니다.")
            continue


def create_monster():
    doc = {2: "Wolf", 3: "bear", 4: "tiger"}
    level = random.randint(2, 4)
    return chaticter.CreateMonster(doc[level], level)


def start_battle(user):
    monster = create_monster()
    print(f"{monster.name}와 전투를 시작한다.")
    os.system("pause")
    while (True):
        if user.alive():
            os.system('cls||clear')
            print(f"{user.name} HP : {user.hp}")
            print(f"{monster.name} HP : {monster.hp}\n")

            print("1. 일반 공격")
            print("2. 동작이 큰 공격")
            cmd = input("어떻게 할까? >> ")
            if cmd == '1':
                user.attack(monster)
            elif cmd == '2':
                print("현재 공격의 성공 확률은 ", (user.condition /
                                         user.max_condition)*100, "% 입니다.")
                if check_yesno():
                    user.high_risk_attack(monster)
            else:
                print("잘못된 입력입니다.")
                os.system("pause")
                continue

            if user.alive() and monster.alive():
                monster.attack(user)
            elif monster.alive() == False:
                print("전투의 경험으로 능력치가 상승합니다.")
                user.levelup(monster.level)
                # 경험치 or 아이템 드랍 코드 가능
                os.system("pause")
                return 0
        else:
            return ending(0)
        os.system("pause")
