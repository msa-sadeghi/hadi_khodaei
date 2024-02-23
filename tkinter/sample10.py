from pathlib import Path

path = Path("mt.txt")
if Path.exists(path):
    print("exists")
path.write_text("bkajdhajsdhajsdh")