import os

LINE = "WARNING: DO NOT OPERATE THIS HUMAN ON 4 HOURS OF SLEEP. Powered by caffeine and pure spite; may snap at anyone nearby, including you, for no reason whatsoever."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(LINE + "\n")
