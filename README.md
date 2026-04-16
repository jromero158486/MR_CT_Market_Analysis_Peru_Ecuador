Aquí tienes una versión limpia, natural y lista para pegar directamente como `README.md` en GitHub:

---

# MR & CT Market Intelligence — Perú y Ecuador (2020–2025)

## Contexto

Este proyecto simula el trabajo de análisis de mercado que realiza un Product Specialist en empresas de imagen médica (como Siemens Healthineers), enfocado en el soporte a licitaciones y análisis competitivo para equipos de resonancia magnética (MR) y tomografía computarizada (CT) en Perú y Ecuador.

## Objetivo

Analizar datos de contrataciones públicas provenientes de SEACE (Perú) y SERCOP (Ecuador) para entender el comportamiento del mercado de equipos de imagen médica.

El análisis se centra en:

* Participación de mercado por fabricante (Siemens, GE, Philips, Canon)
* Tendencias de compra por año, modalidad (MR/CT) y región
* Principales entidades compradoras y valores promedio de contrato
* Tasas de adjudicación y posicionamiento competitivo

---

## Estructura del repositorio

```
seace-imaging-market-analysis/
├── generate_dataset.py          # Genera dataset simulado basado en patrones reales
├── build_excel_dashboard.py     # Construye dashboard en Excel listo para Power BI
├── fetch_seace.py               # Plantilla para extracción de datos de SEACE
├── fetch_sercop.py              # Plantilla para extracción de datos de SERCOP
├── data/
│   ├── licitaciones_mr_ct.xlsx
│   └── MR_CT_Market_Analysis_Peru_Ecuador.xlsx
└── README.md
```

---

## Resultados principales (2020–2025)

* 180 procesos de contratación analizados
* Aproximadamente 163 millones USD en valor total
* Tasa de adjudicación cercana al 90%
* Cobertura: Perú y Ecuador
* Equipos analizados: MRI (1.5T, 3T) y CT (64, 128, 256 cortes)

### Participación de mercado (procesos adjudicados)

| Fabricante           | Procesos ganados | Participación |
| -------------------- | ---------------- | ------------- |
| Siemens Healthineers | 52               | ~32%          |
| Philips Healthcare   | 50               | ~30%          |
| GE Healthcare        | 40               | ~25%          |
| Canon Medical        | 20               | ~12%          |

---

## Dashboard en Excel

El archivo `MR_CT_Market_Analysis_Peru_Ecuador.xlsx` contiene:

* **Resumen_Ejecutivo**: KPIs principales, participación de mercado y tendencias
* **Analisis_Competitivo**: comparación entre fabricantes y tasas de adjudicación
* **Graficos**: visualizaciones (market share, evolución MR vs CT)
* **Datos_Licitaciones**: base limpia para análisis y conexión con Power BI
* **Guia_PowerBI**: instrucciones para replicar el dashboard

---

## Integración con Power BI

1. Abrir Power BI Desktop
2. Get Data → Excel
3. Seleccionar la hoja `Datos_Licitaciones`
4. Crear visualizaciones:

   * Barras: fabricante vs número de adjudicaciones
   * Pie chart: participación de mercado
   * Línea: tendencia anual MR vs CT
   * Cards: total de procesos, valor total, participación Siemens
5. Agregar filtros: país, año, modalidad, estado
6. Publicar en Power BI Service

---

## Uso con datos reales

Para reemplazar el dataset simulado:

**Perú (SEACE / OSCE):**
[https://contratacionesabiertas.osce.gob.pe/](https://contratacionesabiertas.osce.gob.pe/)
Buscar: “resonancia magnética”, “tomógrafo”, “equipos de imagen”

**Ecuador (SERCOP):**
[https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/datos-abiertos](https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/datos-abiertos)
Filtrar por equipos médicos o imagenología

Mantener la misma estructura de columnas para asegurar compatibilidad con el dashboard.

---

## Requisitos

```bash
pip install pandas numpy openpyxl xlsxwriter
```

---

## Herramientas utilizadas

* Python (pandas, numpy)
* Excel (dashboard)
* Power BI (visualización)

---

## Habilidades demostradas

* Análisis de datos de contrataciones públicas
* Inteligencia de mercado en imagen médica (MR/CT)
* Diseño de dashboards en Excel y Power BI
* Análisis competitivo entre fabricantes
* Construcción de pipelines de datos con Python

---
