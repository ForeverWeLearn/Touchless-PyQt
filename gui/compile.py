from pathlib import Path
import os


for file in os.listdir("./gui/design"):
    out = Path(os.path.join("./gui/compiled", file.removesuffix("ui") + "py"))

    cmd = rf'pyside6-uic {file} -o "{out.absolute()}"'

    print(cmd)

    os.system(f"cd ./gui/design && {cmd}")
