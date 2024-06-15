import numpy as np

def grados_a_radianes(grados):
    # print(f'rads: {np.radians(grados)}\n')
    return np.radians(grados)

def normalizar_radianes(radianes):
    return (radianes + np.pi) / (2 * np.pi) # Porque tenemos grados de [-360 , 360], por lo que en rads son [-2pi, 2pi] 

def procesar_vector(vector_grados):
    radianes = grados_a_radianes(vector_grados)
    radianes_normalizados = normalizar_radianes(radianes)
    return radianes_normalizados

# ----------------------------------------------------------------------------------
"REY BLANCO"
# .......
## Region 
rey_blanco_r_i = np.array([138.55, -57.06, 51.30, -93.70, -81.20, 319.52])
rey_blanco_r_f = np.array([146.63, -56.59, 46.99, -85.93, -83.68, 327.95])

## Grasp  
rey_blanco_g_i = np.array([138.55, -56.19, 67.36, -110.64, -81.22, 319.58])
rey_blanco_g_f = np.array([146.63, -56.58, 65.98, -104.93, -83.70, 328.01])

# ----------------------------------------------------------------------------------
"REY NEGRO"
# .......
## Region 
rey_negro_r_i = np.array([147.08, -84.58, 87.67, -97.89, -84.51, 327.98])
rey_negro_r_f = np.array([138.57, -80.82, 74.93, -81.57, -89.77, 321.06])

## Grasp  
rey_negro_g_i = np.array([147.08, -81.87, 100.86, -113.80, -84.53, 328.04])
rey_negro_g_f = np.array([138.58, -79.16, 94.80, -103.10, -89.78, 321.14])

# ----------------------------------------------------------------------------------
"CABALLO BLANCO"
# .......
## Region 
caballo_blanco_r_i = np.array([127.51, -53.28, 39.86, -75.53, -86.83, 307.45])
caballo_blanco_r_f = np.array([142.99, -66.96, 59.86, -86.26, -83.95, 325.10])

## Grasp  
caballo_blanco_g_i = np.array([127.51, -54.71, 59.59, -93.83, -86.83, 307.52])
caballo_blanco_g_f = np.array([147.00, -65.88, 79.12, -106.61, -83.97, 325.17])

# ----------------------------------------------------------------------------------
"CABALLO NEGRO"
# .......
## Region 
caballo_negro_r_i = np.array([147.08, -84.58, 87.67, -97.89, -84.51, 327.98]) # Inicial es igual que el del rey negro
caballo_negro_r_f = np.array([132.45, -65.21, 54.79, -74.08, -92.50, 312.87])

## Grasp  
caballo_negro_g_i = np.array([147.08, -81.87, 100.86, -113.80, -84.53, 328.04]) # Inicial es igual que el del rey negro
caballo_negro_g_f = np.array([132.46, -65.59, 73.19, -92.09, -92.51, 312.94])

# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------

# List of all vectors with their names
vectors = [
    ("REY BLANCO Region Inicial", np.array([138.55, -57.06, 51.30, -93.70, -81.20, 319.52-360])), # -360 porque la muñeca del robot tenía 1 vuelta de más
    ("REY BLANCO Grasp Inicial", np.array([138.55, -56.19, 67.36, -110.64, -81.22, 319.58-360])),
    ("REY BLANCO Region Final", np.array([146.63, -56.59, 46.99, -85.93, -83.68, 327.95-360])),
    ("REY BLANCO Grasp Final", np.array([146.63, -56.58, 65.98, -104.93, -83.70, 328.01-360])),

    ("REY NEGRO Region Inicial", np.array([147.08, -84.58, 87.67, -97.89, -84.51, 327.98-360])),
    ("REY NEGRO Grasp Inicial", np.array([147.08, -81.87, 100.86, -113.80, -84.53, 328.04-360])),
    ("REY NEGRO Region Final", np.array([138.57, -80.82, 74.93, -81.57, -89.77, 321.06-360])),
    ("REY NEGRO Grasp Final", np.array([138.58, -79.16, 94.80, -103.10, -89.78, 321.14-360])),

    ("CABALLO BLANCO Region Inicial", np.array([127.51, -53.28, 39.86, -75.53, -86.83, 307.45-360])),
    ("CABALLO BLANCO Grasp Inicial", np.array([127.51, -54.71, 59.59, -93.83, -86.83, 307.52-360])),
    ("CABALLO BLANCO Region Final", np.array([142.99, -66.96, 59.86, -86.26, -83.95, 325.10-360])),
    ("CABALLO BLANCO Grasp Final", np.array([147.00, -65.88, 79.12, -106.61, -83.97, 325.17-360])),

    ("CABALLO NEGRO Region Inicial", np.array([147.08, -84.58, 87.67, -97.89, -84.51, 327.98-360])),  # Igual que el del rey negro
    ("CABALLO NEGRO Grasp Inicial", np.array([147.08, -81.87, 100.86, -113.80, -84.53, 328.04-360])),  # Igual que el del rey negro
    ("CABALLO NEGRO Region Final", np.array([132.45, -65.21, 54.79, -74.08, -92.50, 312.87-360])),
    ("CABALLO NEGRO Grasp Final", np.array([132.46, -65.59, 73.19, -92.09, -92.51, 312.94-360]))
]

# Iterate through each vector, process and print the normalized vector with its name
for name, vector in vectors:
    normalized_vector = procesar_vector(vector)
    normalized_vector_str = ' '.join(format(round(v, 6), ".6f") for v in normalized_vector)
    print(f"{name}: {normalized_vector_str}")