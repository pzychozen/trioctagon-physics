def rotate_y(points, angle_deg):
    a = np.radians(angle_deg)
    c, s = (np.cos(a), np.sin(a))
    R = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    return points @ R.T
tri_bottom_base = np.array([[+0.27059805, -0.38268343, 0.0], [0.0, -0.92387953, 0.46868957], [-0.27059805, -0.38268343, 0.0]])
tri_top_base = np.array([[+0.27059805, +0.38268343, 0.0], [0.0, +0.92387953, 0.46868957], [-0.27059805, +0.38268343, 0.0]])
all_tris = []
colors_tri = ['gold', 'orange', 'lightgreen', 'mediumseagreen', 'skyblue', 'cornflowerblue']
for angle in [0, 120, 240]:
    all_tris.append(rotate_y(tri_bottom_base, angle))
    all_tris.append(rotate_y(tri_top_base, angle))
top_bases = []
bot_bases = []
top_apexes = []
bot_apexes = []
for tri in all_tris:
    apex = tri[1]
    b0, b2 = (tri[0], tri[2])
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
    angles = np.arctan2(pts[:, 2], pts[:, 0])
    return pts[np.argsort(angles)]
top_hex = sort_ring(top_bases)
bot_hex = sort_ring(bot_bases)

def build_connecting_faces(hex_ring, apexes):
    faces = []
    for i in range(6):
        p1 = hex_ring[i]
        p2 = hex_ring[(i + 1) % 6]
        edge_mid = 0.5 * (p1 + p2)
        dists = np.linalg.norm(apexes - edge_mid, axis=1)
        nearest_apex = apexes[np.argmin(dists)]
        faces.append(np.array([p1, p2, nearest_apex]))
    return faces
top_faces = build_connecting_faces(top_hex, top_apexes)
bot_faces = build_connecting_faces(bot_hex, bot_apexes)
twist_faces = []
for i in range(6):
    t1 = top_hex[i]
    t2 = top_hex[(i + 1) % 6]
    b1 = bot_hex[(i + 1) % 6]
    b2 = bot_hex[(i + 2) % 6]
    twist_faces.append(np.array([t1, t2, b1]))
    twist_faces.append(np.array([t1, b1, b2]))
