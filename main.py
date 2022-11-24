import random
import shutil
from pathlib import Path

from characters import Dragon, Player, Slime
from config import ACTION_ART_DIR

command_dict = {"0": "たたかう", "1": "バイキルト", "2": "にげる"}
cmd_string = ""
for k, v in command_dict.items():
    cmd_string += f"{k} : {v}\n"
terminal_size = shutil.get_terminal_size()
pause_message = '【何かキーを押してください】\n'


def print_hitpoint(func):
    def _print_hitpoint():
        print("-" * terminal_size.columns)
        print(f"残HP\n{player.char_name} -> {player.hit_point}\n{enemy.char_name} -> {enemy.hit_point}\n")
        print(enemy.get_char_art())
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

    is_play = input("ぼうけんをはじめる [y/n]\n")
    if is_play == 'n':
        exit()

    player_name = ""
    while player_name == "":
        player_name = input("なまえをにゅうりょくしてください\n")

    player = Player(player_name)
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
            print(f"{enemy.char_name} に {player_attack} ポイントのダメージをあたえた\n")

        # 敵のターン
        if enemy.hit_point > 0:
            input(pause_message)
            enemy_attack = enemy.attack()
            player.hit_point -= enemy_attack
            print(f"{enemy_attack} のポイントのダメージをうけた！\n")

            if player.hit_point <= 0:
                print(get_ascii_art("die.txt"))
                print(f"{player.char_name} はしんでしまった……")
                exit()

            input(pause_message)

    print(get_ascii_art("win.txt"))
    print(f"{enemy.char_name} をたおした！")
