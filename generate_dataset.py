"""
generate_dataset.py
-------------------
Genera un dataset realista de licitaciones de equipos de imagen médica
(Resonancia Magnética y Tomografía Computada) en Perú y Ecuador (2020–2025).

Los datos están basados en patrones reales del SEACE (Perú) y SERCOP (Ecuador):
- Tipos de procedimiento, rangos de precio, entidades compradoras reales
- Para usar con datos reales: ver fetch_seace.py y fetch_sercop.py

Output: data/licitaciones_mr_ct.xlsx  (listo para Power BI)
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

random.seed(42)
np.random.seed(42)

# ── Entidades reales compradoras de MR/CT en Perú ──────────────────────────
entidades_peru = [
    "Hospital Nacional Edgardo Rebagliati Martins (EsSalud)",
    "Hospital Nacional Guillermo Almenara Irigoyen (EsSalud)",
    "Hospital Nacional Alberto Sabogal Sologuren (EsSalud)",
    "Hospital Nacional Arzobispo Loayza (MINSA)",
    "Hospital Nacional Dos de Mayo (MINSA)",
    "Instituto Nacional de Enfermedades Neoplásicas (INEN)",
    "Hospital Nacional Cayetano Heredia (MINSA)",
    "Hospital de la Solidaridad (SISOL)",
    "Clínica Internacional S.A.",
    "Clínica Ricardo Palma S.A.",
    "Hospital Regional de Lambayeque",
    "Hospital Regional Honorio Delgado (Arequipa)",
    "Hospital Nacional Carlos Alberto Seguín Escobedo (EsSalud Arequipa)",
    "Hospital de Alta Complejidad Virgen de la Puerta (EsSalud La Libertad)",
    "Gobierno Regional de Piura - Gerencia Regional de Salud",
]

entidades_ecuador = [
    "Hospital de Especialidades Fuerzas Armadas N°1",
    "Hospital Carlos Andrade Marín (IESS)",
    "Hospital del IESS Ceibos",
    "Hospital Metropolitano (privado)",
    "Hospital de los Valles (privado)",
    "Ministerio de Salud Pública - Hospital Eugenio Espejo",
    "Hospital Teodoro Maldonado Carbo (IESS Guayaquil)",
    "Hospital General IESS Riobamba",
    "SOLCA Núcleo de Quito",
    "Hospital de Especialidades Baca Ortiz",
]

# ── Equipos y marcas ────────────────────────────────────────────────────────
equipos = {
    "Resonancia Magnética 1.5T": {
        "marcas": {
            "Siemens Healthineers": ("MAGNETOM Sola", 850_000, 1_200_000),
            "GE Healthcare":        ("SIGNA Artist",  800_000, 1_100_000),
            "Philips Healthcare":   ("Ingenia 1.5T",  820_000, 1_150_000),
            "Canon Medical":        ("Vantage Orian", 750_000, 1_050_000),
        },
        "tipo": "MR",
        "campo_T": 1.5,
    },
    "Resonancia Magnética 3T": {
        "marcas": {
            "Siemens Healthineers": ("MAGNETOM Vida",   1_400_000, 2_200_000),
            "GE Healthcare":        ("SIGNA Premier",   1_350_000, 2_100_000),
            "Philips Healthcare":   ("Ingenia Elition", 1_380_000, 2_150_000),
        },
        "tipo": "MR",
        "campo_T": 3.0,
    },
    "Tomógrafo CT 64 cortes": {
        "marcas": {
            "Siemens Healthineers": ("SOMATOM go.Up",   280_000,  420_000),
            "GE Healthcare":        ("Revolution EVO",  270_000,  410_000),
            "Philips Healthcare":   ("Incisive CT",     275_000,  415_000),
            "Canon Medical":        ("Aquilion Lightning", 265_000, 400_000),
        },
        "tipo": "CT",
        "cortes": 64,
    },
    "Tomógrafo CT 128 cortes": {
        "marcas": {
            "Siemens Healthineers": ("SOMATOM go.Top",    450_000,  680_000),
            "GE Healthcare":        ("Revolution Ascend", 440_000,  660_000),
            "Philips Healthcare":   ("Incisive CT 128",   445_000,  670_000),
        },
        "tipo": "CT",
        "cortes": 128,
    },
    "Tomógrafo CT 256 cortes": {
        "marcas": {
            "Siemens Healthineers": ("SOMATOM go.Now",    700_000,  950_000),
            "GE Healthcare":        ("Revolution HD",     680_000,  930_000),
            "Philips Healthcare":   ("IQon Spectral CT",  720_000,  970_000),
        },
        "tipo": "CT",
        "cortes": 256,
    },
}

procedimientos_peru = [
    "Licitación Pública",
    "Adjudicación Simplificada",
    "Concurso Público",
    "Subasta Inversa Electrónica",
]

procedimientos_ecuador = [
    "Licitación",
    "Cotización",
    "Menor Cuantía",
    "Subasta Inversa Electrónica",
]

regiones_peru = [
    "Lima", "Lima", "Lima",  # peso mayor
    "Arequipa", "La Libertad", "Piura",
    "Cusco", "Lambayeque", "Junín", "Ica",
]

regiones_ecuador = [
    "Pichincha", "Pichincha",  # Quito
    "Guayas", "Guayas",        # Guayaquil
    "Azuay", "Manabí", "Tungurahua",
]

estados = ["Adjudicado", "Adjudicado", "Adjudicado", "Desierto", "Nulo"]  # pesos

# ── Generar registros ───────────────────────────────────────────────────────
records = []
start_date = datetime(2020, 1, 1)
end_date   = datetime(2025, 12, 31)

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def gen_codigo_peru(year, idx):
    return f"LP-{idx:04d}-{year}-SEACE"

def gen_codigo_ecuador(year, idx):
    return f"SIE-{idx:04d}-{year}-SERCOP"

idx_peru = 1
idx_ecuador = 1

# Perú: ~120 registros
for _ in range(120):
    equipo_nombre = random.choice(list(equipos.keys()))
    eq = equipos[equipo_nombre]
    marca = random.choice(list(eq["marcas"].keys()))
    modelo, precio_min, precio_max = eq["marcas"][marca]
    precio = round(random.uniform(precio_min, precio_max), -3)

    fecha = random_date(start_date, end_date)
    estado = random.choices(estados, weights=[40, 30, 20, 7, 3])[0]
    ganador = marca if estado == "Adjudicado" else ""
    region = random.choice(regiones_peru)
    entidad = random.choice(entidades_peru)

    records.append({
        "codigo":           gen_codigo_peru(fecha.year, idx_peru),
        "pais":             "Perú",
        "fuente":           "SEACE",
        "region":           region,
        "entidad":          random.choice(entidades_peru),
        "tipo_equipo":      equipo_nombre,
        "modalidad":        eq["tipo"],
        "fecha_convocatoria": fecha.strftime("%Y-%m-%d"),
        "año":              fecha.year,
        "trimestre":        f"Q{(fecha.month-1)//3+1}",
        "procedimiento":    random.choice(procedimientos_peru),
        "valor_referencial_USD": precio,
        "moneda":           "USD",
        "estado":           estado,
        "marca_ganadora":   ganador,
        "modelo_ganador":   modelo if estado == "Adjudicado" else "",
        "num_postores":     random.randint(1, 5) if estado != "Desierto" else 0,
        "incluye_instalacion": random.choice(["Sí", "Sí", "No"]),
        "incluye_capacitacion": random.choice(["Sí", "No"]),
        "campo_T":          eq.get("campo_T", ""),
        "cortes_CT":        eq.get("cortes", ""),
    })
    idx_peru += 1

# Ecuador: ~60 registros
for _ in range(60):
    equipo_nombre = random.choice(list(equipos.keys()))
    eq = equipos[equipo_nombre]
    marca = random.choice(list(eq["marcas"].keys()))
    modelo, precio_min, precio_max = eq["marcas"][marca]
    precio = round(random.uniform(precio_min, precio_max), -3)

    fecha = random_date(start_date, end_date)
    estado = random.choices(estados, weights=[40, 30, 20, 7, 3])[0]
    ganador = marca if estado == "Adjudicado" else ""

    records.append({
        "codigo":           gen_codigo_ecuador(fecha.year, idx_ecuador),
        "pais":             "Ecuador",
        "fuente":           "SERCOP",
        "region":           random.choice(regiones_ecuador),
        "entidad":          random.choice(entidades_ecuador),
        "tipo_equipo":      equipo_nombre,
        "modalidad":        eq["tipo"],
        "fecha_convocatoria": fecha.strftime("%Y-%m-%d"),
        "año":              fecha.year,
        "trimestre":        f"Q{(fecha.month-1)//3+1}",
        "procedimiento":    random.choice(procedimientos_ecuador),
        "valor_referencial_USD": precio,
        "moneda":           "USD",
        "estado":           estado,
        "marca_ganadora":   ganador,
        "modelo_ganador":   modelo if estado == "Adjudicado" else "",
        "num_postores":     random.randint(1, 4) if estado != "Desierto" else 0,
        "incluye_instalacion": random.choice(["Sí", "Sí", "No"]),
        "incluye_capacitacion": random.choice(["Sí", "No"]),
        "campo_T":          eq.get("campo_T", ""),
        "cortes_CT":        eq.get("cortes", ""),
    })
    idx_ecuador += 1

df = pd.DataFrame(records)
df = df.sort_values("fecha_convocatoria").reset_index(drop=True)

# ── Tablas de análisis ──────────────────────────────────────────────────────
# 1. Market share por marca (solo adjudicados)
adj = df[df["estado"] == "Adjudicado"]
market_share = (
    adj.groupby(["pais", "marca_ganadora"])
    .agg(licitaciones_ganadas=("codigo", "count"),
         monto_total_USD=("valor_referencial_USD", "sum"))
    .reset_index()
)
market_share["market_share_%"] = (
    market_share.groupby("pais")["licitaciones_ganadas"]
    .transform(lambda x: round(x / x.sum() * 100, 1))
)

# 2. Tendencia anual
tendencia = (
    df.groupby(["año", "pais", "modalidad"])
    .agg(num_licitaciones=("codigo", "count"),
         monto_promedio_USD=("valor_referencial_USD", "mean"),
         monto_total_USD=("valor_referencial_USD", "sum"))
    .reset_index()
)

# 3. Top entidades compradoras
top_entidades = (
    df.groupby(["pais", "entidad"])
    .agg(num_licitaciones=("codigo", "count"),
         monto_total_USD=("valor_referencial_USD", "sum"))
    .sort_values("monto_total_USD", ascending=False)
    .reset_index()
    .head(20)
)

# ── Exportar a Excel  ─────────────────────────────────
os.makedirs("data", exist_ok=True)
output_path = "data/licitaciones_mr_ct.xlsx"

with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Datos_Licitaciones", index=False)
    market_share.to_excel(writer, sheet_name="Market_Share", index=False)
    tendencia.to_excel(writer, sheet_name="Tendencia_Anual", index=False)
    top_entidades.to_excel(writer, sheet_name="Top_Entidades", index=False)

print(f" Dataset generado: {output_path}")
print(f"   Total registros: {len(df)}")
print(f"   Perú: {len(df[df['pais']=='Perú'])} | Ecuador: {len(df[df['pais']=='Ecuador'])}")
print(f"   Rango años: {df['año'].min()} – {df['año'].max()}")
print(f"\n📊 Market share MR+CT (adjudicados):")
print(market_share.groupby("marca_ganadora")["licitaciones_ganadas"].sum().sort_values(ascending=False))
