import random

import ascii_art


class Character:
    """登場人物の基底クラス"""

    def __init__(self):
        self.hit_point = None
        self.offensive_power = None
        self.special_attack_name = None

    def __str__(self):
        """登場人物の名前を返す"""
        return self.__class__.__name__

    def _normal_attack(self):
        """通常攻撃"""
        print(f"{self.__class__.__name__} の攻撃")
        return int(self.offensive_power * (1 + random.random()))

    def _special_attack(self):
        """
        特殊攻撃

        通常攻撃より強い
        """
        print(f"{self.__class__.__name__} の特殊攻撃\n【{self.special_attack_name}】")
        return int(self.offensive_power * (random.randint(2, 3) + random.random()))

    def attack(self):
        if random.random() < 0.3:
            return self._special_attack()
        else:
            return self._normal_attack()


class Player(Character):
    """プレイヤークラス"""

    def __init__(self):
        super().__init__()
        self.hit_point = 50
        self.offensive_power = 3
        self.special_attack_name = "会心の一撃！"

    def by_kill_to(self):
        """攻撃力が2~10倍になる"""
        by = random.randint(2, 10)
        self.offensive_power *= by
        print(f"【バイキルト】 攻撃力が{by}倍になった！")


class Enemy(Character):
    """
    敵クラス

    コンストラクタでaaを表示する
    """

    def __init__(self, aa):
        super().__init__()
        print(aa)
        print(f"{self.__class__.__name__} があらわれた\n")


class Slime(Enemy):
    def __init__(self):
        super().__init__(ascii_art.slime)
        self.hit_point = 10
        self.offensive_power = 1
        self.special_attack_name = "溶解液"


class Dragon(Enemy):
    def __init__(self):
        super().__init__(ascii_art.dragon)
        self.hit_point = 100
        self.offensive_power = 20
        self.special_attack_name = "ほのお"
