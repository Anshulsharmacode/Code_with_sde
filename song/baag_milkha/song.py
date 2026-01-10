import sys
import time

CURSOR = "▌"

def blink_cursor(times=3, speed=0.4):
    for _ in range(times):
        # sys.stdout.write(CURSOR)
        sys.stdout.flush()
        time.sleep(speed)
        sys.stdout.write("\b \b")
        sys.stdout.flush()
        time.sleep(speed)

def slow_type(text, char_delay=0.06, line_pause=0.3):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char == "\n":
            time.sleep(line_pause)
        elif char in [","]:
            time.sleep(0.5)
        else:
            time.sleep(char_delay)

    # blink_cursor(2)


lyrics = [
    # "Woh noor ka jharna hai\n",
    # "Main pyaas puraani\n",
    # "Maine aankh gatak liya\n",
    # "Us husn ka paani\n\n",

    "Woh noor ka jharna hai\n",
    "Main pyaas puraani\n",
    "Maine aankh gatak liya\n",
    "Us husn ka paani \n\n",
    "Hmmmmmmmm \n",
    "Use takte takte umr guzaarun\n",
    "Koi aur khayaal jo aaye,\n",
    "jhat se utaarun\n\n",

    "Ishq karun ya karun ibaadat\n",
    "Ishq karun ya karun ibaadat\n",
    "Ikko hi gal aayi\n\n",

    "\nAlif Allah...\n",
    "Alif Allah...\n",
    "Alif Allah-hu\n"
]

# Opening silence
# time.sleep(2)
# blink_cursor(4)

# Start slow animation
for line in lyrics:
    slow_type(line)
    time.sleep(1.2)
