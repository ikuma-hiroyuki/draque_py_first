import random
import shutil
from pathlib import Path

from config import ACTION_ART_DIR
from characters import Slime, Dragon, Player

command_dict = {"0": "たたかう", "1": "バイキルト", "2": "にげる"}
cmd_string = ""
for k, v in command_dict.items():
    cmd_string += f"{k} : {v}\n"
terminal_size = shutil.get_terminal_size()


def print_hitpoint(func):
    def _print_hitpoint():
        print("-" * terminal_size.columns)
        print(f"残HP\n{player}\t-> {player.hit_point}\n{enemy}\t-> {enemy.hit_point}\n")
        return func()

    return _print_hitpoint


@print_hitpoint
def get_battle_command():
    cmd = ""
    while cmd not in command_dict:
        cmd = input(f"コマンド番号を入力してください\n{cmd_string}\n")
        if cmd not in command_dict:
            print("無効なコマンドです。再度入力してください。\n")
    return command_dict[cmd]


def get_ascii_art(file_name):
    with Path.open(ACTION_ART_DIR / file_name, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    enemy_list = [Slime, Dragon]

    print(f"{get_ascii_art('title.txt')}\n")

    # todo 冒険の書

    player = Player()
    enemy = random.choice(enemy_list)()

    while enemy.hit_point > 0:
        command = get_battle_command()

        # プレイヤーのターン
        if command == "にげる":
            player.runaway()
            exit()
        elif command == "バイキルト":
            player.by_kill_to()
        else:
            player_attack = player.attack()
            enemy.hit_point -= player_attack
            print(f"{enemy} に {player_attack} ポイントのダメージをあたえた\n")

        # todo 一時停止 -> コマンド入力で再開

        # 敵のターン
        if enemy.hit_point > 0:
            enemy_attack = enemy.attack()
            player.hit_point -= enemy_attack
            print(f"{enemy_attack} のポイントのダメージをうけた！\n")

            if player.hit_point <= 0:
                print(get_ascii_art("die.txt"))
                print(f"{player} はしんでしまった……")
                exit()

        # todo 一時停止 -> コマンド入力で再開

    print(get_ascii_art("win.txt"))
    print(f"{enemy} をたおした！")
