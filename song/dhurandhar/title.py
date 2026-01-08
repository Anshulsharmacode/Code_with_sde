import json
import time
import sys
import os

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, typing_speed):
    """Type out text character by character"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(typing_speed)
    print()  # New line after text

def run_song_script(json_file):
    """Load JSON and animate the song script"""
    try:
        # Load JSON file
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"\n🎵 {data.get('title', 'Song Script')} 🎵\n")
        time.sleep(2)
        
        clear_screen()
        
        # Track the actual start time
        script_start_time = time.time()
        
        # Process each sequence item
        for item in data['sequence']:
            text = item['text']
            start_time = item['start']
            typing_speed = item['typing_speed']
            
            # Calculate how long to wait before starting this text
            elapsed_time = time.time() - script_start_time
            wait_time = start_time - elapsed_time
            
            if wait_time > 0:
                time.sleep(wait_time)
            
            # Type out the text
            type_text(text, typing_speed)
        
        print("\n✨ Script Complete ✨\n")
        
    except FileNotFoundError:
        print(f"❌ Error: Could not find file '{json_file}'")
    except json.JSONDecodeError:
        print(f"❌ Error: Invalid JSON format in '{json_file}'")
    except KeyError as e:
        print(f"❌ Error: Missing required field {e} in JSON")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    # Check if filename was provided
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
    else:
        json_file = input("Enter JSON filename: ")
    
    run_song_script(json_file)