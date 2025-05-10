import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np 
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch 

# Constants
OPEN_SPACE = 996
DOOR = 997 
INTER_WALL = 998
EXT_WALL = 999
OUTSIDE = 1000
END = 1001
STAIRS = 1002

floorplan_matrix =    [
            [EXT_WALL,  EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,  EXT_WALL, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, END],
            [EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, INTER_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, INTER_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, EXT_WALL, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, END],
            [EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, INTER_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, INTER_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, EXT_WALL, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, END],
            [EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, INTER_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, INTER_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, EXT_WALL, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, END],
            [EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, INTER_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, INTER_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, EXT_WALL, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, END],
            [EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, INTER_WALL, DOOR, INTER_WALL, INTER_WALL, INTER_WALL, INTER_WALL, INTER_WALL, INTER_WALL, INTER_WALL, INTER_WALL, INTER_WALL, DOOR, INTER_WALL, EXT_WALL, EXT_WALL, EXT_WALL, EXT_WALL, EXT_WALL, EXT_WALL, END],
            [EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE,    DOOR, OPEN_SPACE, OPEN_SPACE, STAIRS, STAIRS, STAIRS, STAIRS, STAIRS, STAIRS, STAIRS, INTER_WALL, OPEN_SPACE, INTER_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, EXT_WALL, END],
            [EXT_WALL, INTER_WALL, INTER_WALL, INTER_WALL, INTER_WALL, INTER_WALL,INTER_WALL, OPEN_SPACE, OPEN_SPACE, STAIRS, STAIRS, STAIRS, STAIRS, STAIRS, STAIRS, STAIRS, INTER_WALL, OPEN_SPACE, INTER_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, EXT_WALL, END],
            [OUTSIDE, EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE,    DOOR,    DOOR, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, DOOR, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE,OPEN_SPACE, EXT_WALL, END],
            [OUTSIDE, EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, EXT_WALL, EXT_WALL, EXT_WALL, EXT_WALL, EXT_WALL, INTER_WALL, DOOR, INTER_WALL, INTER_WALL, INTER_WALL, INTER_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE,OPEN_SPACE, EXT_WALL, END],
            [OUTSIDE, EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, EXT_WALL, OUTSIDE, OUTSIDE, OUTSIDE, EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, EXT_WALL, EXT_WALL, EXT_WALL, EXT_WALL, EXT_WALL, EXT_WALL, EXT_WALL, END],
            [OUTSIDE, EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, EXT_WALL, OUTSIDE, OUTSIDE, OUTSIDE, EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, EXT_WALL, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, END],
            [OUTSIDE, EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, EXT_WALL, OUTSIDE, OUTSIDE, OUTSIDE, EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, EXT_WALL, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, END],
            [OUTSIDE, EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, EXT_WALL, OUTSIDE, OUTSIDE, OUTSIDE, EXT_WALL, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, OPEN_SPACE, EXT_WALL, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, END],
            [OUTSIDE, EXT_WALL,  EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,  EXT_WALL, OUTSIDE, OUTSIDE, OUTSIDE, EXT_WALL,  EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,   EXT_WALL,  EXT_WALL, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, OUTSIDE, END],
            ]

# from manual data collection ;(
a = [54,52,47,48,41,59,65,58,60,62,65,61,61,71,72,75]
b = [45,71,41,40,54,49,47,55,57,54,57,56,77,60,72,70]
c = [65,64,56,57,60,49,51,52,52,48,56,54,76,66,71,69]
d = [57,56,52,51,61,51,64,53,53,57,56,52,74,66,70,74]

e = [52,58,55,55,56]
f = [49,60,59,56,59] 

g = [43,51,60,65,68,76,79,78]

h = [41,48,62,66,60,68,69,67]
i = [43,43,42,45,47,43,47,46,51,50,55,56,53,57,62,61,67,70,69]


j = [39,34,36,28,42,40,71,72,70,74,73]
k = [41,31,36,27,40,34,50,54,61,66,65]
l = [37,36,34,41,36,36,50,57,70,64,66]
m = [35,36,34,34,29,41,61,57,69,60,61]
n = [37,39,40,23,34,35,64,66,66,54,60]

dbms_master = [*a, *b, *c, *d, *e, *f, *g, *h, *i, *j, *k, *l, *m, *n]

print(f"Total data points: {len(dbms_master)}")

# Convert floorplan_matrix to NumPy array and pad if necessary
max_cols = max(len(row) for row in floorplan_matrix)
padded_matrix = []
for row in floorplan_matrix:
    padded_row = row.copy()
    while len(padded_row) < max_cols:
        padded_row.append(END)
    padded_matrix.append(padded_row)
    
floorplan = np.array(padded_matrix)

# Create signal strength matrix initialized with NaN values
signal_matrix = np.full_like(floorplan, np.nan, dtype=float)

def is_open_space(value):
    return value == OPEN_SPACE

# Populate signal strength values in the interior spaces
data_index = 0
for i in range(floorplan.shape[0]):
    for j in range(floorplan.shape[1]):
        if is_open_space(floorplan[i, j]) and data_index < len(dbms_master):
            signal_matrix[i, j] = dbms_master[data_index]
            data_index += 1

print(f"Data points used: {data_index}")

plt.figure(figsize=(12, 10))
sns.set_style("whitegrid")

floorplan_colors = {
    OPEN_SPACE: "#FFFFFF",  # White
    DOOR: "#8BC34A",        # Green
    INTER_WALL: "#9E9E9E",  # Gray
    EXT_WALL: "#795548",    # Brown
    OUTSIDE: "#E3F2FD",     # Light blue
    END: "#000000",         # Black
    STAIRS: "#FF9800"       # Orange
}

structure_mask = ~np.isin(floorplan, [OPEN_SPACE])
wifi_colors = sns.color_palette("RdYlGn_r", as_cmap=True)

signal_mask = np.isnan(signal_matrix)

# Create the WiFi strength heatmap with Seaborn
ax = sns.heatmap(signal_matrix, 
                mask=signal_mask,
                cmap=wifi_colors, 
                cbar_kws={'label': 'WiFi Signal Strength (dBm)', 'shrink': 0.8},
                square=True,
                annot=True,  # Show actual values
                fmt=".1f",   # Format with 1 decimal place
                annot_kws={"size": 9, "color": "black", "weight": "bold"},
                linewidths=0.5)

# Define color map for structural elements
structure_cmap = mcolors.ListedColormap([
    floorplan_colors[INTER_WALL],  # Interior walls
    floorplan_colors[EXT_WALL],    # Exterior walls
    floorplan_colors[OUTSIDE],    # Outside areas
    floorplan_colors[END],        # End markers
    floorplan_colors[DOOR],       # Doors
    floorplan_colors[STAIRS]       # Stairs
])

# Create a mask for different structural elements
walls_mask = ~np.isin(floorplan, [INTER_WALL, EXT_WALL, OUTSIDE, END])
doors_mask = ~np.isin(floorplan, [DOOR])
stairs_mask = ~np.isin(floorplan, [STAIRS])

# Overlay walls
walls_data = np.ma.array(floorplan, mask=walls_mask)
plt.imshow(walls_data, 
          cmap=mcolors.ListedColormap([floorplan_colors[INTER_WALL], 
                                      floorplan_colors[EXT_WALL],
                                      floorplan_colors[OUTSIDE], 
                                      floorplan_colors[END]]), 
          alpha=0.7, interpolation='none')

# overlay doors
doors_data = np.ma.array(floorplan, mask=doors_mask) 
plt.imshow(doors_data,
          cmap=mcolors.ListedColormap([floorplan_colors[DOOR]]),
          alpha=0.7, interpolation='none')

# overlay stairs
stairs_data = np.ma.array(floorplan, mask=stairs_mask)
plt.imshow(stairs_data,
          cmap=mcolors.ListedColormap([floorplan_colors[STAIRS]]),
          alpha=0.7, interpolation='none')

legend_elements = [
    Patch(facecolor=floorplan_colors[EXT_WALL], edgecolor='black', label='Exterior Wall'),
    Patch(facecolor=floorplan_colors[INTER_WALL], edgecolor='black', label='Interior Wall'),
    Patch(facecolor=floorplan_colors[DOOR], edgecolor='black', label='Door'),
    Patch(facecolor=floorplan_colors[STAIRS], edgecolor='black', label='Stairs'),
    Patch(facecolor=floorplan_colors[OUTSIDE], edgecolor='black', label='Outside')
]
plt.legend(handles=legend_elements, loc='upper right', fontsize=10, 
           title="Building Elements", title_fontsize=12)

plt.title("WiFi Signal Strength Heatmap", fontsize=18, pad=20)

plt.suptitle("Building WiFi Signal Strength Analysis", fontsize=22, y=0.98)

cbar_ax = plt.gcf().axes[-1]
cbar_ax.set_title("Signal Strength", fontsize=12)
cbar_ax.text(1.5, 0.1, "Stronger", fontsize=10, color='green', weight='bold')
cbar_ax.text(1.5, 0.9, "Weaker", fontsize=10, color='red', weight='bold')

plt.figtext(0.5, 0.01, 
            "Note: Lower dBm values (green) indicate stronger WiFi signal, higher values (red) indicate weaker signal.",
            ha='center', fontsize=12, 
            bbox={'facecolor':'white', 'alpha':0.8, 'pad':5, 'boxstyle':'round,pad=0.5'})

plt.axis('off')
plt.tight_layout()
plt.subplots_adjust(top=0.92, bottom=0.08)
plt.show()