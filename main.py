import random
import shutil

import ascii_art
import characters

command_dict = {"0": "たたかう", "1": "バイキルト", "2": "にげる"}
cmd_string = ""
for k, v in command_dict.items():
    cmd_string += f"{k} : {v}\n"
enemy_list = [characters.Slime, characters.Dragon]
terminal_size = shutil.get_terminal_size()


def print_hitpoint(func):
    def print_hitpoint_():
        print("-" * terminal_size.columns)
        print(f"残HP\n{player}\t-> {player.hit_point}\n{enemy}\t-> {enemy.hit_point}\n")
        return func()

    return print_hitpoint_


@print_hitpoint
def get_battle_command():
    cmd = ""
    while cmd not in command_dict:
        cmd = input(f"コマンド番号を入力してください\n{cmd_string}\n")
        if cmd not in command_dict:
            print("無効なコマンドです。再度入力してください。\n")
    return command_dict[cmd]


if __name__ == "__main__":
    print(ascii_art.title, "\n" * 2)
    player = characters.Player()
    enemy = random.choice(enemy_list)()

    while enemy.hit_point > 0:
        command = get_battle_command()

        # プレイヤーのターン
        if command == "にげる":
            print(ascii_art.runaway)
            print(f"{player} はにげだした")
            exit()
        elif command == "バイキルト":
            player.by_kill_to()
        else:
            player_attack = player.attack()
            enemy.hit_point -= player_attack
            print(f"{enemy} に {player_attack} ポイントのダメージをあたえた\n")

        # 敵のターン
        if enemy.hit_point > 0:
            enemy_attack = enemy.attack()
            player.hit_point -= enemy_attack
            print(f"{enemy_attack} のポイントのダメージをうけた！\n")

            if player.hit_point <= 0:
                print(ascii_art.die)
                print(f"{player} はしんでしまった……")
                exit()

    print(ascii_art.win)
    print(f"{enemy} をたおした！")
