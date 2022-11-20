import random
import shutil

import ascii_art
import character

terminal_size = shutil.get_terminal_size()
command_dict = {"0": "たたかう", "1": "バイキルト", "2": "にげる"}
enemy_list = [character.Slime, character.Dragon]

cmd_string = ""
for k, v in command_dict.items():
    cmd_string += f"{k} : {v}\n"


def get_battle_command():
    print("-" * terminal_size.columns)
    print(f"残HP\n{player}\t-> {player.hit_point}\n{enemy}\t-> {enemy.hit_point}\n")
    cmd = ""
    while cmd not in command_dict:
        cmd = input(f"コマンド番号を入力してください\n{cmd_string}\n")
    print()
    return command_dict[cmd]


if __name__ == "__main__":
    print(ascii_art.title, "\n" * 2)
    player = character.Player()
    enemy = random.choice(enemy_list)()

    while enemy.hit_point > 0:
        command = get_battle_command()

        # プレイヤーのターン
        if command == "にげる":
            print(ascii_art.runaway)
            print(player, "は逃げ出した")
            exit()
        elif command == "バイキルト":
            player.by_kill_to()
        else:
            player_attack = player.attack()
            enemy.hit_point -= player_attack
            print(enemy, "に", player_attack, "ポイントのダメージを与えた！\n")

        # 敵のターン
        if enemy.hit_point > 0:
            enemy_attack = enemy.attack()
            player.hit_point -= enemy_attack
            print(enemy_attack, "のポイントのダメージをうけた！\n")

            if player.hit_point <= 0:
                print(ascii_art.die)
                print(player, "は死んでしまった！")
                exit()

    print(ascii_art.win)
    print(enemy, "を倒した！")
