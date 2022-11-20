import shutil
import random

import aa
import character

command_list = ["たたかう", "にげる"]
terminal_size = shutil.get_terminal_size()

enemy_list = [character.Slime, character.Dragon]


def get_battle_command():
    print("-" * terminal_size.columns)
    print(f"残HP\n{player}\t-> {player.hit_point}\n{enemy}\t-> {enemy.hit_point}\n")
    cmd = ""
    while cmd == "":
        cmd = input(f"コマンドを入力してください\n0: {command_list[0]}\n1: {command_list[1]}\n")
    print()
    return int(cmd)


if __name__ == "__main__":
    print(aa.title, "\n"*2)
    player = character.Player()
    enemy = random.choice(enemy_list)()

    while enemy.hit_point > 0:
        command = get_battle_command()

        # プレイヤーのターン
        if command == 1:
            print(aa.runaway)
            print(player, "はにげだした")
            exit()

        player_attack = player.attack()
        enemy - player_attack
        print(enemy, "に", player_attack, "ポイントのダメージをあたえた！\n")

        # 敵のターン
        if enemy.hit_point > 0:
            enemy_attack = enemy.attack()
            player - enemy_attack
            print(enemy_attack, "のポイントのダメージをうけた！\n")

            if player.hit_point <= 0:
                print(aa.die)
                print(player, "はしんでしまった！")
                exit()

    print(aa.win)
    print(enemy, "をたおした")
