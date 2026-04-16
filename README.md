# 📊 MR & CT Market Intelligence — Perú & Ecuador (2020–2025)

> **Context:** This project simulates the market analysis work done by a Product Specialist at a medical imaging company (e.g., Siemens Healthineers) to support tender responses and competitive intelligence for MRI and CT equipment procurement in Peru and Ecuador.

## 🎯 Objective

Analyze public procurement data from Peru's SEACE and Ecuador's SERCOP to identify:
- Market share by manufacturer (Siemens, GE, Philips, Canon)
- Procurement trends by year, modality (MR/CT), and region
- Top buying entities and average contract values
- Win rates and competitive positioning

## 📁 Repository Structure

```
seace-imaging-market-analysis/
├── generate_dataset.py          # Generates realistic dataset based on SEACE/SERCOP patterns
├── build_excel_dashboard.py     # Builds formatted Excel + Power BI-ready workbook
├── fetch_seace.py               # (Template) Real data fetcher from OSCE API
├── fetch_sercop.py              # (Template) Real data fetcher from SERCOP API
├── data/
│   ├── licitaciones_mr_ct.xlsx                      # Raw dataset (180 records)
│   └── MR_CT_Market_Analysis_Peru_Ecuador.xlsx       # Final dashboard workbook
└── README.md
```

## 📊 Key Findings (2020–2025 Sample)

| Metric | Value |
|--------|-------|
| Total tenders analyzed | 180 |
| Total procurement value | ~$163M USD |
| Award rate | ~90% |
| Countries | Perú, Ecuador |
| Equipment types | MRI 1.5T, MRI 3T, CT 64-slice, CT 128-slice, CT 256-slice |

### Market Share (Awarded Tenders)
| Manufacturer | Tenders Won | Share |
|---|---|---|
| Siemens Healthineers | 52 | ~32% |
| Philips Healthcare | 50 | ~30% |
| GE Healthcare | 40 | ~25% |
| Canon Medical | 20 | ~12% |

## 🗂️ Excel Workbook Structure

The output Excel file contains 5 sheets:

1. **Resumen_Ejecutivo** — KPI summary + market share table + yearly trend
2. **Analisis_Competitivo** — Siemens vs competitors, win rates, country breakdown
3. **Graficos** — Embedded charts (pie market share, bar chart MR vs CT by year)
4. **Datos_Licitaciones** — Clean dataset with auto-filter and freeze panes (Power BI source)
5. **Guia_PowerBI** — Step-by-step instructions to connect to Power BI Desktop

## 🔌 Connecting to Power BI

1. Open Power BI Desktop → Get Data → Excel
2. Select this file → check `Datos_Licitaciones` sheet
3. Load data and create visuals:
   - Bar chart: Winning brand vs. # tenders (filter by country)
   - Pie chart: Market share %
   - Line chart: Yearly trend MR vs CT
   - Cards: Total tenders, total value, Siemens share %
   - Slicer filters: Country, Year, Modality, Status
4. Publish to Power BI Service → embed link in portfolio

## 🌐 Using Real Data

To replace the simulated dataset with real procurement data:

**Peru (SEACE/OSCE):**
```
https://contratacionesabiertas.osce.gob.pe/
Search keywords: "resonancia magnética", "tomógrafo", "equipo de imagen"
Download: CSV or XLSX format
```

**Ecuador (SERCOP):**
```
https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/datos-abiertos
Filter by: "equipos médicos", "imagenología"
Download: CSV or JSON format
```

Replace `data/licitaciones_mr_ct.xlsx` (sheet `Datos_Licitaciones`) keeping the same column names.

## 🛠️ Requirements

```bash
pip install pandas openpyxl xlsxwriter numpy
```

## 📌 Skills Demonstrated

- Public procurement data analysis (OCDS standard — Perú & Ecuador)
- Market intelligence for medical imaging equipment
- Excel dashboard design with professional formatting
- Power BI data modeling
- Python data pipeline (pandas)
- Competitive analysis: Siemens vs GE vs Philips vs Canon
- Technical knowledge: MRI field strength (1.5T/3T), CT slice count

---
*Data in this repository is simulated based on real procurement patterns from SEACE and SERCOP public records. For real data, see the data sources above.*
