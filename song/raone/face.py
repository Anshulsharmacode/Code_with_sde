import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap

def create_raone_face(grid_size=20):
    """
    Create Ra.One's iconic pixelated face with glowing red eyes
    """
    # Create a grid
    face = np.zeros((grid_size, grid_size, 3))
    
    # Define face outline (dark blue/black with hints of color)
    face[:, :] = [0.05, 0.05, 0.15]  # Dark blue-black background
    
    # Head shape (oval-ish)
    for i in range(grid_size):
        for j in range(grid_size):
            # Create head outline
            x = (j - grid_size/2) / (grid_size/2)
            y = (i - grid_size/2) / (grid_size/2)
            
            if x**2 + y**2 * 1.2 < 0.8:  # Oval shape
                face[i, j] = [0.1, 0.1, 0.2]  # Slightly lighter for face
    
    # Add facial features with pixel blocks
    
    # Eyes (glowing red) - positioned higher
    eye_y = int(grid_size * 0.35)
    eye_left_x = int(grid_size * 0.35)
    eye_right_x = int(grid_size * 0.65)
    eye_size = 2
    
    # Left eye with glow
    for dy in range(-1, eye_size+1):
        for dx in range(-1, eye_size+1):
            if 0 <= eye_y+dy < grid_size and 0 <= eye_left_x+dx < grid_size:
                # Bright red center
                if dy >= 0 and dy < eye_size and dx >= 0 and dx < eye_size:
                    face[eye_y+dy, eye_left_x+dx] = [1.0, 0.0, 0.0]  # Bright red
                else:
                    # Red glow around
                    face[eye_y+dy, eye_left_x+dx] = [0.6, 0.0, 0.0]
    
    # Right eye with glow
    for dy in range(-1, eye_size+1):
        for dx in range(-1, eye_size+1):
            if 0 <= eye_y+dy < grid_size and 0 <= eye_right_x+dx < grid_size:
                if dy >= 0 and dy < eye_size and dx >= 0 and dx < eye_size:
                    face[eye_y+dy, eye_right_x+dx] = [1.0, 0.0, 0.0]  # Bright red
                else:
                    face[eye_y+dy, eye_right_x+dx] = [0.6, 0.0, 0.0]
    
    # Nose area (darker pixels)
    nose_y = int(grid_size * 0.5)
    nose_x = int(grid_size * 0.5)
    face[nose_y:nose_y+2, nose_x-1:nose_x+1] = [0.2, 0.2, 0.3]
    
    # Mouth/lower face (subtle darker line)
    mouth_y = int(grid_size * 0.65)
    for x in range(int(grid_size*0.3), int(grid_size*0.7)):
        face[mouth_y:mouth_y+1, x] = [0.15, 0.15, 0.25]
    
    # Add some digital circuitry patterns on face
    circuit_points = [
        (int(grid_size*0.25), int(grid_size*0.5)),
        (int(grid_size*0.75), int(grid_size*0.5)),
        (int(grid_size*0.5), int(grid_size*0.75)),
    ]
    
    for cy, cx in circuit_points:
        if 0 <= cy < grid_size and 0 <= cx < grid_size:
            face[cy, cx] = [0.3, 0.3, 0.5]  # Blue-ish circuit points
    
    return face

def plot_pixelated_face(face, show_grid=True):
    """
    Display the pixelated face with visible grid lines
    """
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='black')
    
    # Display the face
    ax.imshow(face, interpolation='nearest')
    
    # Add grid lines to emphasize the pixelated effect
    if show_grid:
        grid_size = face.shape[0]
        for i in range(grid_size + 1):
            ax.axhline(i - 0.5, color='black', linewidth=0.5, alpha=0.5)
            ax.axvline(i - 0.5, color='black', linewidth=0.5, alpha=0.5)
    
    ax.set_xlim(-0.5, face.shape[1] - 0.5)
    ax.set_ylim(face.shape[0] - 0.5, -0.5)
    ax.axis('off')
    ax.set_title('RA.ONE - Digital Face', color='red', fontsize=20, 
                 fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.show()

# Create and display Ra.One's face
print("Generating Ra.One's pixelated face...")
raone_face = create_raone_face(grid_size=30)
plot_pixelated_face(raone_face, show_grid=True)

print("\nYou can adjust:")
print("- grid_size parameter for more/fewer pixels")
print("- Eye positions and colors")
print("- Add more circuit patterns")
print("- Change the color scheme")