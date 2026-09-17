import math

# ============================================================
# INGRESO DE DATOS EXPERIMENTALES
# ============================================================
print("INGRESE LOS DATOS EXPERIMENTALES")
print("=========================================")
da = float(input("Densidad del agua ρ_agua (g/cm³): "))
h1 = float(input("Altura de la columna de agua h1 (cm): "))
h2 = float(input("Altura de la columna del líquido h2 (cm): "))
print("\nINGRESE LAS RESOLUCIONES DE LOS INSTRUMENTOS")
print("=========================================")
Deltah1 = float(input("Resolución para h1 Δh1 (cm): "))
Deltah2 = float(input("Resolución para h2 Δh2 (cm): "))


# ============================================================
# CÁLCULO DE LA DENSIDAD
# ============================================================
# Densidad del líquido
Den = da * h1 / h2
# Derivadas parciales de la densidad
fh1 = da / h2
fh2 = -da * h1 / h2**2
# Error de la densidad (propagación de errores)
Deltaden = math.sqrt((fh1 * Deltah1)**2 + (fh2 * Deltah2)**2)

# ============================================================
# RESULTADOS
# ============================================================
print("\nRESULTADOS EXPERIMENTALES")
print("=========================================")
print(f"Densidad = ({Den:.3f} ± {Deltaden:.3f}) g/cm³")
print("=========================================")
print(f"Densidad por exceso = {Den + Deltaden:.3f} g/cm³")
print(f"Densidad por defecto = {Den - Deltaden:.3f} g/cm³")
print("=========================================")
print(f"Error relativo de la densidad = " f"{100 * Deltaden / Den:.2f} %")
print("=========================================")