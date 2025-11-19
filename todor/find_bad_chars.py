import os

for root, dirs, files in os.walk("."):
    for f in files:
        if f.endswith(".py"):
            path = os.path.join(root, f)
            try:
                open(path, "r", encoding="utf-8").read()
            except Exception as e:
                print("\n[ERROR] Archivo con problemas:", path)
                print(e)
