import random
from pathlib import Path

from config import CHAR_ART_DIR, ACTION_ART_DIR


class Character:
    """登場人物の基底クラス"""
    char_name = ""

    def __init__(self, char_name, hit_point, offensive_power, special_attack_name):
        self.char_name = char_name
        self.hit_point = hit_point
        self.offensive_power = offensive_power
        self.special_attack_name = special_attack_name

    def get_ascii_art(self, file_name, art_dir=CHAR_ART_DIR):
        with Path.open(art_dir / file_name, "r", encoding="utf-8") as f:
            return f.read()

    def normal_attack(self):
        """通常攻撃"""
        print(f"{self.char_name} の攻撃")
        return int(self.offensive_power * (1 + random.random()))

    def special_attack(self):
        """
        特殊攻撃

        通常攻撃より強い
        """
        print(f"{self.char_name} の特殊攻撃\n【{self.special_attack_name}】")
        return int(self.offensive_power * (random.randint(2, 3) + random.random()))

    def attack(self):
        return self.special_attack() if random.random() < 0.3 else self.normal_attack()


class Player(Character):
    """プレイヤークラス"""

    def __init__(self, char_name='ゆうしゃ', hit_point=50, offensive_power=3, ):
        super().__init__(char_name, hit_point, offensive_power, '会心の一撃！')

    def by_kill_to(self):
        """攻撃力が2~10倍になる"""
        by = random.randint(2, 10)
        self.offensive_power *= by
        print(f"【バイキルト】 攻撃力が{by}倍になった！")

    def runaway(self):
        print(self.get_ascii_art("runaway.txt", art_dir=ACTION_ART_DIR))
        print(f"{self.char_name} はにげだした")


class Enemy(Character):
    """ 敵クラス """
    char_art = ''

    def get_char_art(self):
        if self.char_art == '':
            raise NotImplementedError('char_art が未実装です')
        return super().get_ascii_art(self.char_art)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.get_char_art())
        print(f"{self.char_name} があらわれた\n")


class Slime(Enemy):
    char_art = "slime.txt"

    def __init__(self):
        super().__init__('スライム', 10, 1, "溶解液")


class Dragon(Enemy):
    char_art = "dragon.txt"

    def __init__(self):
        super().__init__('ドラゴン', 100, 20, 'ほのお')
