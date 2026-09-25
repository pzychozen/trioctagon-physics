import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def rotate_y(points, angle_deg):
    a = np.radians(angle_deg)
    c, s = np.cos(a), np.sin(a)
    R = np.array([[ c, 0, s], [ 0, 1, 0], [-s, 0, c]])
    return points @ R.T

tri_bottom_base = np.array([
    [+0.27059805, -0.38268343,  0.0],
    [ 0.0,        -0.92387953,  0.46868957],
    [-0.27059805, -0.38268343,  0.0],
])
tri_top_base = np.array([
    [+0.27059805, +0.38268343,  0.0],
    [ 0.0,        +0.92387953,  0.46868957],
    [-0.27059805, +0.38268343,  0.0],
])

all_tris = []
colors_tri = ['gold', 'orange', 'lightgreen', 'mediumseagreen', 'skyblue', 'cornflowerblue']
for angle in [0, 120, 240]:
    all_tris.append(rotate_y(tri_bottom_base, angle))
    all_tris.append(rotate_y(tri_top_base, angle))

# Build hexagons
top_bases = []
bot_bases = []
top_apexes = []
bot_apexes = []

for tri in all_tris:
    apex = tri[1]
    b0, b2 = tri[0], tri[2]
    if b0[1] > 0:
        top_bases.append(b0)
        top_bases.append(b2)
        top_apexes.append(apex)
    else:
        bot_bases.append(b0)
        bot_bases.append(b2)
        bot_apexes.append(apex)

top_bases = np.array(top_bases)
bot_bases = np.array(bot_bases)
top_apexes = np.array(top_apexes)
bot_apexes = np.array(bot_apexes)

def sort_ring(pts):
    angles = np.arctan2(pts[:,2], pts[:,0])
    return pts[np.argsort(angles)]

top_hex = sort_ring(top_bases)
bot_hex = sort_ring(bot_bases)

# Connecting faces from hex edges to apexes
def build_connecting_faces(hex_ring, apexes):
    faces = []
    for i in range(6):
        p1 = hex_ring[i]
        p2 = hex_ring[(i+1) % 6]
        edge_mid = 0.5 * (p1 + p2)
        dists = np.linalg.norm(apexes - edge_mid, axis=1)
        nearest_apex = apexes[np.argmin(dists)]
        faces.append(np.array([p1, p2, nearest_apex]))
    return faces

top_faces = build_connecting_faces(top_hex, top_apexes)
bot_faces = build_connecting_faces(bot_hex, bot_apexes)

# Twisted connection between top and bottom hexagons:
# Instead of connecting top[i] to bot[i] (mirrored/straight),
# connect top[i] to bot[(i+1)%6] (shifted one to the left).
# Each quad face: top[i], top[i+1], bot[(i+2)%6], bot[(i+1)%6]
# Split into two triangles for rendering.

twist_faces = []
for i in range(6):
    t1 = top_hex[i]
    t2 = top_hex[(i+1) % 6]
    b1 = bot_hex[(i+1) % 6]  # shifted one left
    b2 = bot_hex[(i+2) % 6]  # shifted one left
    # Quad as two triangles
    twist_faces.append(np.array([t1, t2, b1]))
    twist_faces.append(np.array([t1, b1, b2]))

print(f"Twist faces: {len(twist_faces)}")

# =============================================
# PLOT
# =============================================
fig = plt.figure(figsize=(16, 12))

views = [
    (30, 30, "3D View"),
    (90, -90, "Top-down (along Y)"),
    (0, 0, "Front (YZ)"),
    (0, 90, "Side (XZ)"),
]

for si, (elev, azim, title) in enumerate(views):
    ax = fig.add_subplot(2, 2, si+1, projection='3d')
    
    # Original small triangles
    for tri, color in zip(all_tris, colors_tri):
        ax.add_collection3d(Poly3DCollection([tri], facecolor=color, edgecolor='darkred', alpha=0.5, linewidth=0.8))
        for i in range(3):
            p, q = tri[i], tri[(i+1)%3]
            ax.plot([p[0],q[0]], [p[1],q[1]], [p[2],q[2]], 'darkred', linewidth=0.8)
        ax.scatter(*tri[1], color='red', s=25, zorder=5)
    
    # Hexagons
    for hex_ring in [top_hex, bot_hex]:
        for i in range(6):
            p, q = hex_ring[i], hex_ring[(i+1)%6]
            ax.plot([p[0],q[0]], [p[1],q[1]], [p[2],q[2]], 'k-', linewidth=2)
    
    # Hex-to-apex faces
    for face in top_faces + bot_faces:
        ax.add_collection3d(Poly3DCollection([face], facecolor='mediumpurple', edgecolor='k', alpha=0.3, linewidth=0.8))
    
    # Twisted connecting faces
    for face in twist_faces:
        ax.add_collection3d(Poly3DCollection([face], facecolor='cyan', edgecolor='k', alpha=0.3, linewidth=1))
        for i in range(3):
            p, q = face[i], face[(i+1)%3]
            ax.plot([p[0],q[0]], [p[1],q[1]], [p[2],q[2]], 'k-', linewidth=1)
    
    lim = 1.5
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
    ax.set_box_aspect([1,1,1])
    ax.view_init(elev=elev, azim=azim)
    ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
    ax.set_title(title)

plt.suptitle("Twisted connection: top hex[i] → bot hex[i+1] (shifted left)", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/tri_octagon.png', dpi=150, bbox_inches='tight')

import os; os.system("cp /home/claude/hex_twist.py /mnt/user-data/outputs/tri_oct.py")
print("\nDone")
