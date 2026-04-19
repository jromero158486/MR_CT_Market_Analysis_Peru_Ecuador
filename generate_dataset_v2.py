"""
generate_dataset.py — v2
Marcas genéricas: Marca A / B / C / D
Sin columna modelo_ganador (evita identificación por modelo)
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random, os

random.seed(42)
np.random.seed(42)

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

equipos = {
    "Resonancia Magnética 1.5T": {
        "marcas": {"Marca A": (850000,1200000), "Marca B": (800000,1100000), "Marca C": (820000,1150000), "Marca D": (750000,1050000)},
        "tipo": "MR", "campo_T": 1.5,
    },
    "Resonancia Magnética 3T": {
        "marcas": {"Marca A": (1400000,2200000), "Marca B": (1350000,2100000), "Marca C": (1380000,2150000)},
        "tipo": "MR", "campo_T": 3.0,
    },
    "Tomógrafo CT 64 cortes": {
        "marcas": {"Marca A": (280000,420000), "Marca B": (270000,410000), "Marca C": (275000,415000), "Marca D": (265000,400000)},
        "tipo": "CT", "cortes": 64,
    },
    "Tomógrafo CT 128 cortes": {
        "marcas": {"Marca A": (450000,680000), "Marca B": (440000,660000), "Marca C": (445000,670000)},
        "tipo": "CT", "cortes": 128,
    },
    "Tomógrafo CT 256 cortes": {
        "marcas": {"Marca A": (700000,950000), "Marca B": (680000,930000), "Marca C": (720000,970000)},
        "tipo": "CT", "cortes": 256,
    },
}

proc_peru    = ["Licitación Pública","Adjudicación Simplificada","Concurso Público","Subasta Inversa Electrónica"]
proc_ecuador = ["Licitación","Cotización","Menor Cuantía","Subasta Inversa Electrónica"]
regiones_peru    = ["Lima","Lima","Lima","Arequipa","La Libertad","Piura","Cusco","Lambayeque","Junín","Ica"]
regiones_ecuador = ["Pichincha","Pichincha","Guayas","Guayas","Azuay","Manabí","Tungurahua"]
estados = ["Adjudicado","Adjudicado","Adjudicado","Desierto","Nulo"]

start_date, end_date = datetime(2020,1,1), datetime(2025,12,31)
def rdate(s,e): return s + timedelta(days=random.randint(0,(e-s).days))

records = []
for i in range(120):
    eq_name = random.choice(list(equipos.keys()))
    eq = equipos[eq_name]
    marca = random.choice(list(eq["marcas"].keys()))
    pmin, pmax = eq["marcas"][marca]
    precio = round(random.uniform(pmin, pmax), -3)
    fecha  = rdate(start_date, end_date)
    estado = random.choices(estados, weights=[40,30,20,7,3])[0]
    records.append({
        "codigo": f"LP-{i+1:04d}-{fecha.year}-SEACE",
        "pais": "Perú", "fuente": "SEACE",
        "region": random.choice(regiones_peru),
        "entidad": random.choice(entidades_peru),
        "tipo_equipo": eq_name, "modalidad": eq["tipo"],
        "fecha_convocatoria": fecha.strftime("%Y-%m-%d"),
        "año": fecha.year, "trimestre": f"Q{(fecha.month-1)//3+1}",
        "procedimiento": random.choice(proc_peru),
        "valor_referencial_USD": precio, "moneda": "USD",
        "estado": estado,
        "marca_ganadora": marca if estado == "Adjudicado" else "",
        "num_postores": random.randint(1,5) if estado != "Desierto" else 0,
        "incluye_instalacion": random.choice(["Sí","Sí","No"]),
        "incluye_capacitacion": random.choice(["Sí","No"]),
        "campo_T": eq.get("campo_T",""), "cortes_CT": eq.get("cortes",""),
    })

for i in range(60):
    eq_name = random.choice(list(equipos.keys()))
    eq = equipos[eq_name]
    marca = random.choice(list(eq["marcas"].keys()))
    pmin, pmax = eq["marcas"][marca]
    precio = round(random.uniform(pmin, pmax), -3)
    fecha  = rdate(start_date, end_date)
    estado = random.choices(estados, weights=[40,30,20,7,3])[0]
    records.append({
        "codigo": f"SIE-{i+1:04d}-{fecha.year}-SERCOP",
        "pais": "Ecuador", "fuente": "SERCOP",
        "region": random.choice(regiones_ecuador),
        "entidad": random.choice(entidades_ecuador),
        "tipo_equipo": eq_name, "modalidad": eq["tipo"],
        "fecha_convocatoria": fecha.strftime("%Y-%m-%d"),
        "año": fecha.year, "trimestre": f"Q{(fecha.month-1)//3+1}",
        "procedimiento": random.choice(proc_ecuador),
        "valor_referencial_USD": precio, "moneda": "USD",
        "estado": estado,
        "marca_ganadora": marca if estado == "Adjudicado" else "",
        "num_postores": random.randint(1,4) if estado != "Desierto" else 0,
        "incluye_instalacion": random.choice(["Sí","Sí","No"]),
        "incluye_capacitacion": random.choice(["Sí","No"]),
        "campo_T": eq.get("campo_T",""), "cortes_CT": eq.get("cortes",""),
    })

df = pd.DataFrame(records).sort_values("fecha_convocatoria").reset_index(drop=True)
adj = df[df["estado"] == "Adjudicado"]

market_share = (
    adj.groupby(["pais","marca_ganadora"])
    .agg(licitaciones_ganadas=("codigo","count"), monto_total_USD=("valor_referencial_USD","sum"))
    .reset_index()
)
market_share["market_share_%"] = (
    market_share.groupby("pais")["licitaciones_ganadas"]
    .transform(lambda x: round(x/x.sum()*100, 1))
)

tendencia = (
    df.groupby(["año","pais","modalidad"])
    .agg(num_licitaciones=("codigo","count"),
         monto_promedio_USD=("valor_referencial_USD","mean"),
         monto_total_USD=("valor_referencial_USD","sum"))
    .reset_index()
)

top_entidades = (
    df.groupby(["pais","entidad"])
    .agg(num_licitaciones=("codigo","count"), monto_total_USD=("valor_referencial_USD","sum"))
    .sort_values("monto_total_USD", ascending=False)
    .reset_index().head(20)
)

os.makedirs("data", exist_ok=True)
with pd.ExcelWriter("data/licitaciones_mr_ct.xlsx", engine="openpyxl") as w:
    df.to_excel(w, sheet_name="Datos_Licitaciones", index=False)
    market_share.to_excel(w, sheet_name="Market_Share", index=False)
    tendencia.to_excel(w, sheet_name="Tendencia_Anual", index=False)
    top_entidades.to_excel(w, sheet_name="Top_Entidades", index=False)

print(f"✅ Dataset generado: data/licitaciones_mr_ct.xlsx ({len(df)} registros)")
print(market_share.groupby("marca_ganadora")["licitaciones_ganadas"].sum().sort_values(ascending=False))
