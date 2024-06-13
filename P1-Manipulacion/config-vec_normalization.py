import math

def normalize_angle(angle):
    """Normalize an angle in radians to the range [-2π, 2π]."""
    return (angle + 2 * math.pi) % (4 * math.pi) - 2 * math.pi


def convert_and_normalize_angles(degree_angles):
    """Convert a list of angles from degrees to radians and normalize to [-2π, 2π]."""
    radian_angles = [math.radians(angle) for angle in degree_angles]
    # print(radian_angles)
    normalized_angles = [normalize_angle(angle) for angle in radian_angles]
    return normalized_angles

# -------------------------------------------------------------------------------------

"Versión 4x4, 3 piezas"

# Pos Inicial
rey_blanco_i = [141.92, -46.11, 48.33, -97.01, -88.12, 143.22]
rey_negro_i = [153.34, -73.18, 89.35, -106.16, -91.74, 150.11]
caballo_blanco_i = [128.62, -57.58, 67.81, -101.79, -88.67, 124.93]

# Pos Final 
rey_blanco_f = [148.10, -50.03, 55.22, -96.55, -86.49, 146.72]
rey_negro_f = [137.20, -79.10, 98.06, -107.15, -88.33, 135.37]
caballo_blanco_f = [145.33, -59.42, 69.57, -99.96, -87.29, 142.70]

normalized_configuration = convert_and_normalize_angles(caballo_blanco_f)

# Convert the list of normalized angles to a string
# normalized_angles_str = ' '.join(f'{angle:.6f}' for angle in normalized_configuration)
# print(f'\n{normalized_angles_str}')

# column = '\n'.join(f'{angle:.6f}' for angle in normalized_configuration)
# print(f'\n{column}\n')

# -------------------------------------------------------------------------------------

"Versión 4x4, 2 piezas"

# Pos Inicial
rey_blanco_i = rey_blanco_i
caballo_n_i = [153.34, -73.18, 89.35, -106.16, -91.74, 150.11]

# Pos Final
rey_blanco_f = rey_blanco_f
caballo_n_f = [127.12, -72.15, 88.73, -105.54, -86.81, 127.00]

normalized_configuration = convert_and_normalize_angles(caballo_n_f)

# Convert the list of normalized angles to a string
normalized_angles_str = ' '.join(f'{angle:.6f}' for angle in normalized_configuration)
print(f'\n{normalized_angles_str}')

column = '\n'.join(f'{angle:.6f}' for angle in normalized_configuration)
print(f'\n{column}\n')