import random


class Character:

    def alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def attack(self, other):
        # 공격력 범위 내에서 랜덤한 데미지를 계산
        damage = random.randint(self.power - 2, self.power + 2)
        # 상대방의 체력을 감소시키고 출력
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        # 상대방의 체력이 0이 되면 쓰러짐을 출력
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        # 캐릭터의 상태를 출력
        print(f"{self.name}의 상태")
        print(f"HP {self.hp}/{self.max_hp}")


class CreateUser(Character):

    def __init__(self, name, power):
        # 이름, 최대 체력, 현재 체력, 공격력, 최대 체력 감소량, 현재 체력 감소량을 초기화
        self.name = name
        self.max_hp = 250
        self.hp = self.max_hp
        self.power = power
        self.max_condition = 50
        self.condition = self.max_condition

    def risk_damage(self):
        # 랜덤한 체력 감소량과 컨디션 감소량을 계산하고 출력
        risk_hp = random.randint(5, 15)
        risk_condition = random.randint(3, 10)
        print(f"{self.name}의 몸에 무리가 옵니다 ")
        print(f"HP : -{risk_hp}")
        print(f"Condition : -{risk_condition}")
        # 현재 체력과 컨디션 감소량을 감소시킴
        self.hp = max(self.hp - risk_hp, 0)
        self.condition = max(self.condition - risk_condition, 0)

    def high_risk_attack(self, other):
        # 공격력 범위 내에서 랜덤한 데미지를 계산
        damage = int(random.randint(self.power, self.power+25))
        # 랜덤한 위험도를 계산하고 출력
        risk = random.randint(0, self.max_condition)
        print(f"{risk} {self.name}는 위험을 무릎쓰고 동작이 큰 공격을 시도했다.")
        if risk <= self.condition:
            other.hp = max(other.hp - damage, 0)
            print(f"{other.name}에게 {damage}의 데미지를 입혔습니다.")
        else:
            print("무리한 공격의 실패로 몸에 큰 무담이 왔습니다.")
            self.risk_damage()
        # 현재 체력 감소량을 감소시킴
        self.condition = max(self.condition - 3, 0)
        # 상대방의 체력이 0이 되면 쓰러짐을 출력
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def recovery(self):
        self.condition = self.max_condition
        self.hp = self.max_hp

    def show_status(self):
        # 캐릭터의 상태를 출력
        print(f"{self.name}의 상태")
        print(f"HP {self.hp}/{self.max_hp}")
        print(f"Condition {self.condition}/{self.max_condition}")
        print(f"Power {self.power}")

    def levelup(self, level):
        self.max_hp += level*3
        self.max_condition += level*2
        self.power += level


class CreateMonster(Character):

    def __init__(self, name, level):
        # 이름, 최대 체력, 현재 체력, 공격력을 초기화
        self.name = name
        self.level = level
        self.hp = random.randint((50*level), 80*level)
        self.max_hp = self.hp
        self.power = (level*3)+3
