import time
import sys

script_lines = [
    "Kyun dikhe mujhe tu sirhaane mere",
    "Soch ke teri baatein hum muskurane lage Haaye haaye haaye!",
    "Kyun dikhe mujhe tu sirhaane mere",
    "Soch ke teri baatein hum muskurane lage",
    "Dil se nikal ke aahein lafzon pe aane lagi",
    "Kaisi teri khumari hai Hum gungunane lage 💕",
    "Channa ve..... Channa ve.....",
    "Kuch toh hai tere mere darmiyan kyun lage",
    "Channa ve..... Channa ve.....",
    "Kuch toh hai tere mere darmiyan kyun lage",
]
LINE_DURATION = 3.2  

for line in script_lines:
    char_delay = LINE_DURATION / len(line)  

    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    print()
    time.sleep(1.7)   
