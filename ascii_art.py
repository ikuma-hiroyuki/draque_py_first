from pathlib import Path

base_dir = Path(__file__).absolute().parent
ascii_art_dir = base_dir / "resources" / "ascii_art"


def get_art(file_name):
    with open(ascii_art_dir / file_name, "r", encoding="utf-8") as f:
        return f.read()


die = get_art("die.txt")

dragon = get_art("dragon.txt")

runaway = get_art("runaway.txt")

slime = get_art("slime.txt")

title = get_art("title.txt")

win = get_art("win.txt")
