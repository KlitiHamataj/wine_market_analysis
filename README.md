# 🍷 Vivino Market Analysis

> A comprehensive wine market analysis built for Wiwinio, leveraging the Vivino database to uncover actionable business insights across wines, countries, wineries, and consumer taste profiles.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange)

---

## 📌 Description

This project analyses the Vivino wine database to answer key business questions:

- 🍷 Which 10 wines should we highlight to increase sales?
- 🌍 Which country should we prioritise for our marketing budget?
- 🏆 Which wineries deserve awards, and for what?
- 🔑 Which wines match a specific customer taste cluster?
- 🍇 What are the top grapes worldwide and their best wines?
- 📊 How do countries and vintages rank by average wine rating?
- 💰 Is there a correlation between wine price and rating?

---

## 📁 Project Structure

```
├── 📁 notebooks
│   └── 📄 analysis.ipynb
├── 📁 presentation
│   └── 📄 vivino_market_analysis.pptx
├── 📁 queries
│   ├── 📄 best_country.sql
│   ├── 📄 best_winery_award.sql
│   ├── 📄 best_wines_per_grape.sql
│   ├── 📄 country_leaderbord.sql
│   ├── 📄 most_diverse_winery_award.sql
│   ├── 📄 most_international_winery_award.sql
│   ├── 📄 price_vs_rating.sql
│   ├── 📄 taste_keyword.sql
│   ├── 📄 test_queries.sql
│   ├── 📄 top_10_wines.sql
│   ├── 📄 top_grapes.sql
│   └── 📄 vintage_leaderbord.sql
├── ⚙️ .gitignore
├── 📄 LICENSE
├── 📝 README.md
└── 📄 requirements.txt
```

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/KlitiHamataj/wine_market_analysis.git
cd wine_market_analysis
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv

# Mac/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add the database
Download the `vivino.db` SQLite file and place it in the `data/` folder.

---

## 🚀 Usage

### Run the Jupyter Notebooks
```bash
jupyter notebook
```
Open `notebooks/exploration.ipynb` to explore the database, then `notebooks/analysis.ipynb` for the full market analysis.

---

## 📊 Key Findings

| Question | Finding |
|----------|---------|
| 🍷 Top wine | Cabernet Sauvignon (4.8 avg, 2941 ratings) |
| 🌍 Best market | United States (12.3M users) |
| 🏆 Best winery | Krug (4.64 avg rating) |
| 🔑 Taste cluster | Coffee + toast + cream + citrus + green apple → Champagne |
| 🍇 Top grape | Cabernet Sauvignon (9.6M wines worldwide) |
| 💰 Price vs rating | Weak correlation — great wines exist at all price points |

---

## ⚠️ Data Quality Notes

During the analysis, several data quality issues were identified:

- The `wineries` table has broken foreign key relationships with the `wines` table — only 4 out of 1020 wines have a valid winery match
- The database schema diagram shows a `wines_count` column in `grapes` that does not exist
- Some vintages have `year = 'N.V.'` (Non-Vintage) which requires special handling
- Country names are stored in French

---

## 🧰 Tech Stack

- **Python** — data processing and visualization
- **SQLite / sqlite3** — database queries
- **Jupyter Notebook** — analysis and storytelling
- **Matplotlib / Plotly** — data visualization

---

## 👤 Contributors

- [Kliti Hamataj](https://github.com/KlitiHamataj)

---

## 📜 License

This project was completed as part of the BeCode Data Science curriculum.
