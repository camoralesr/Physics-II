import math

# ============================================================
# INGRESO DE DATOS EXPERIMENTALES
# ============================================================
print("INGRESE LOS DATOS EXPERIMENTALES")
print("=========================================")
d = float(input("Diámetro d (mm): "))
z = float(input("Espesor z (mm): "))
m = float(input("Masa m (g): "))
print("\nINGRESE LAS RESOLUCIONES DE LOS INSTRUMENTOS")
print("=========================================")
Deltad = float(input("Resolución para el diámetro Δd (mm): "))
Deltaz = float(input("Resolución para el espesor Δz (mm): "))
Deltam = float(input("Resolución de la báscula Δm (g): "))

# ============================================================
# CÁLCULO DEL VOLUMEN
# ============================================================
# Volumen del cilindro (convertido de mm³ a cm³)
Vol = math.pi * d**2 * z / 4 / 1000
# Derivadas parciales del volumen
fd = (math.pi * d * z) / 2
fz = (math.pi * d**2) / 4
# Error del volumen (propagación de errores)
Deltav = math.sqrt((fd * Deltad)**2 + (fz * Deltaz)**2) / 1000

# ============================================================
# CÁLCULO DE LA DENSIDAD
# ============================================================
# Derivadas parciales de la densidad
fm = 1 / Vol
fv = -m / Vol**2
# Densidad
Den = m / Vol
# Error de la densidad
Deltaden = math.sqrt((fm * Deltam)**2 + (fv * Deltav)**2)

# ============================================================
# RESULTADOS
# ============================================================
print("\nRESULTADOS EXPERIMENTALES")
print("=========================================")
print(f"Volumen = ({Vol:.2f} ± {Deltav:.2f}) cm³")
print(f"Densidad = ({Den:.2f} ± {Deltaden:.2f}) g/cm³")
print("=========================================")
print(f"Error relativo del volumen = {100 * Deltav / Vol:.2f} %")
print(f"Error relativo de la densidad = {100 * Deltaden / Den:.2f} %")
print("=========================================")
