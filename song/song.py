import json
import sys
import time
import pygame

TYPE_SPEED = 0.08
TITLE_SPEED = 0.06
TITLE_PAUSE = 1.5

AUDIO_FILE = "Dooron Dooron Unplugged Paresh Pahuja 320 Kbps.mp3"

def type_text(text, speed):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")
    sys.stdout.flush()

def play_lyrics(lyrics, start_time):
    for line in lyrics:
        now = time.time() - start_time
        wait_time = max(0, line["time"] - now)
        time.sleep(wait_time)
        type_text(line["text"], TYPE_SPEED)

if __name__ == "__main__":
    # Load lyrics
    with open("song.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Clear terminal
    print("\033c", end="")

    # 🎵 Print song title
    print("\033[1m", end="")
    type_text(data["title"], TITLE_SPEED)
    print("\033[0m", end="")

    time.sleep(TITLE_PAUSE)
    print()

    # 🔊 Init audio
    pygame.mixer.init()
    pygame.mixer.music.load(AUDIO_FILE)

    # ▶ START AUDIO
    pygame.mixer.music.play()

    # ⏱ START TIMER EXACTLY HERE
    start_time = time.time()

    # ▶ START LYRICS
    play_lyrics(data["lyrics"], start_time)

    # Keep script alive until audio ends
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
