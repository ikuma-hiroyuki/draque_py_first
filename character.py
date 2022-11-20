import random

import aa


class Character:
    """
    """

    def __init__(self, is_enemy, aa=""):
        """
        登場人物のHPと攻撃力を設定する

        敵キャラクターだった場合は敵の名前を表示する
        """
        self.hit_point = None
        self.offensive_power = None
        self.special_attack_name = None
        if is_enemy:
            print(aa)
            print(self.__class__.__name__, "があらわれた\n")

    def __str__(self):
        """ 登場人物の名前を返す """
        return self.__class__.__name__

    def __sub__(self, other):
        """
        登場人物のhit_pointを削る
        :param other: ダメージ
        """
        self.hit_point -= other

    def _normal_attack(self):
        """
        通常攻撃

        :return: offensive_power * 1~3
        """
        print(self.__class__.__name__, "のこうげき")
        return int(self.offensive_power * (1 + random.random()))

    def _special_attack(self):
        """
        特殊攻撃

        :return:offensive_power * 3~6
        """
        print(self.__class__.__name__, "のとくしゅこうげき！\n", f"【{self.special_attack_name}】")
        return int(self.offensive_power * (random.randint(2, 3) + random.random()))

    def attack(self):
        if random.random() < 0.3:
            return self._special_attack()
        else:
            return self._normal_attack()


class Player(Character):
    def __init__(self):
        super(Player, self).__init__(False)
        self.hit_point = 50
        self.offensive_power = 3
        self.special_attack_name = "かいしんのいちげき"


class Slime(Character):
    def __init__(self):
        self.aa = aa.slime
        super(Slime, self).__init__(True, self.aa)
        self.hit_point = 10
        self.offensive_power = 1
        self.special_attack_name = "ようかいえき"


class Dragon(Character):
    def __init__(self):
        self.aa = aa.dragon
        super(Dragon, self).__init__(True, self.aa)
        self.hit_point = 100
        self.offensive_power = 30
        self.special_attack_name = "ほのお"
