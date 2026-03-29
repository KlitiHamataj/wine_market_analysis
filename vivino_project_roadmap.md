# 🍷 Vivino Market Analysis — Project Roadmap

> **Mentor note:** This guide walks you through the project step by step.
> It will NOT give you the answers — it will help you *think* and *discover* them yourself.
> At each step, ask yourself: *"Do I understand WHY I'm doing this?"*

---

## 📁 Step 1 — Set Up Your Repository

**What to do:**
- Create a GitHub repository named `wine_market_analysis`
- Set up a clean folder structure from the start

**Example folder structure:**
```
wine_market_analysis/
│
├── data/                  # Store the .sqlite database here
├── queries/               # One .sql file per question
│   ├── top_10_wines.sql
│   ├── best_country.sql
│   └── ...
├── notebooks/             # Your Jupyter Notebook(s)
├── streamlit_app/         # Your Streamlit app
├── presentation/          # Your PowerPoint
└── README.md
```

**Think about:**
- Why is it important to separate `.sql` files from your Python code?
- What should go in your `README.md`? (Hint: look at the deliverables section)

---

## 🗺️ Step 2 — Understand the Database Diagram

**What to do:**
- Open the database diagram carefully
- Identify every table and what it represents
- Understand the relationships between tables (PRIMARY KEYS vs FOREIGN KEYS)

**Example questions to ask yourself:**
- What does the `wines` table contain?
- How is the `wines` table linked to the `countries` table?
- What is the difference between a PRIMARY KEY and a FOREIGN KEY?

**Mini-exercise:**
> Draw (on paper or digitally) a simplified version of the diagram with only the tables and the links between them. This will be your mental map for writing queries later.

**Think about:**
- Which tables will you need to JOIN to answer: *"Top 10 wines to increase sales"*?
- Which tables are needed to find keyword-related wines?

---

## 🔌 Step 3 — Connect to the Database

**What to do:**
- Load the `.sqlite` file in Python using the `sqlite3` library
- Run a first simple query to make sure everything works

**Example (to get you started — not the full solution):**
```python
import sqlite3

conn = sqlite3.connect("data/your_database.sqlite")
cursor = conn.cursor()

# Try a simple query
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
```

**Think about:**
- What tables does this return?
- Does it match the database diagram?

---

## 🧭 Step 4 — Explore the Data

**What to do:**
- Before answering any business question, explore each table
- Check: How many rows? What columns? Any NULLs? What are the value ranges?

**Example exploration query:**
```sql
-- How many wines are in the database?
SELECT COUNT(*) FROM wines;

-- What does the ratings data look like?
SELECT MIN(ratings_average), MAX(ratings_average), AVG(ratings_average)
FROM wines;
```

**Think about:**
- Are there wines with very few ratings? Could that affect your top 10 recommendation?
- Are there NULL values that could distort your averages?

---

## ❓ Step 5 — Answer the Business Questions (One by One)

> Write **one `.sql` file per question**. Keep them clean and commented.

### 5.1 — Top 10 Wines to Highlight
**Hints (not answers):**
- What makes a wine "highlight-worthy"? Think: rating, number of ratings, price...
- Should you recommend a wine with a 5-star average but only 2 reviews?
- Which columns and tables are relevant here?

**SQL concepts you'll need:** `SELECT`, `ORDER BY`, `LIMIT`, maybe `WHERE`

---

### 5.2 — Best Country for Marketing Budget
**Hints:**
- What metrics make a country a good target? Volume of wines? Average rating? Popularity?
- Which table links wines to countries?

**SQL concepts you'll need:** `JOIN`, `GROUP BY`, `AVG`, `COUNT`, `ORDER BY`

---

### 5.3 — Awards for Best Wineries
**Hints:**
- Think creatively! You could award: *Best Average Rating*, *Most Consistent*, *Best Value*
- What data do you have about wineries?

**SQL concepts you'll need:** `JOIN`, `GROUP BY`, `AVG`, `HAVING`, `ORDER BY`, `LIMIT`

---

### 5.4 — Wines Matching the Taste Keywords
**Keywords:** `coffee`, `toast`, `green apple`, `cream`, `citrus` *(CASE SENSITIVE!)*

**Hints:**
- Which table stores keywords/tastes?
- How do keywords link to wines?
- You need wines where **all 5 keywords** are confirmed by **more than 10 users**
- What does `group_name` refer to in the keywords context?

**SQL concepts you'll need:** `JOIN`, `WHERE`, `GROUP BY`, `HAVING`, `COUNT`

> ⚠️ Think carefully: do you need wines that match **at least one** keyword, or **all five**?

---

### 5.5 — Top 3 Most Common Grapes + Best Rated Wines per Grape
**Hints:**
- "Most common" — common how? By number of wines? By number of countries?
- Once you have the top 3 grapes, how do you get the 5 best wines for each?

**SQL concepts you'll need:** `JOIN`, `GROUP BY`, `COUNT`, `ORDER BY`, `LIMIT`

---

### 5.6 — Country Leaderboard (Average Wine Rating)
**Hints:**
- This is a GROUP BY + AVG query
- The result should be visualized — think about what chart type makes sense

**SQL concepts you'll need:** `JOIN`, `GROUP BY`, `AVG`, `ORDER BY`

---

### 5.7 — Same Leaderboard for Vintages
**Hints:**
- What is a "vintage"? How is it stored in the database?
- Is the structure similar to the country leaderboard query?

---

## 📊 Step 6 — Build Your Visualizations

**What to do:**
- Use your query results to create charts in Python (matplotlib, seaborn, or plotly)
- Each chart should answer a specific business question

**Think about:**
- What is the best chart type for a **ranking**? (bar chart? horizontal bar?)
- What is the best chart type for a **leaderboard**?
- How do you make a chart readable for a **non-technical business client**?

**Example checklist for each visual:**
- [ ] Does it have a title?
- [ ] Are the axes labeled?
- [ ] Is it easy to read at a glance?
- [ ] Does it directly answer the business question?

---

## 🖥️ Step 7 — Build the Streamlit App

**What to do:**
- Create an interactive app that lets users explore your findings
- Each business question can be a section or a page

**Example structure:**
```
📌 Home — Project intro
🍷 Top 10 Wines
🌍 Country Analysis
🏆 Winery Awards
🔑 Taste Keywords
🍇 Grape Analysis
📊 Leaderboards
💡 Extra Insights
```

**Think about:**
- Who is your audience? (Business client, not a developer)
- What filters or interactions would be useful?

---

## 📽️ Step 8 — Build the PowerPoint Presentation

**What to do:**
- Tell a **story** with your data
- Each slide = one key finding or business recommendation

**Suggested slide structure:**
1. Title slide
2. Context & objectives
3. Top 10 wines recommendation + reasoning
4. Country to prioritise + reasoning
5. Winery awards
6. Taste cluster findings
7. Grape & wine recommendations
8. Country & vintage leaderboard
9. Extra insights
10. Conclusion & recommendations

**Think about:**
- Would a business client understand this without reading your code?
- Are your recommendations backed by data?

---

## 🧹 Step 9 — Clean Up & Document

**What to do:**
- Add comments to your `.sql` files explaining what each query does
- Add comments to your Python/notebook code
- Write a proper `README.md`

**README should include:**
- What is this project?
- How to install dependencies
- How to run the notebook / Streamlit app
- Screenshots of key visuals

---

## ✅ Final Checklist

| Task | Done? |
|------|-------|
| GitHub repo created | ☐ |
| Database explored | ☐ |
| All `.sql` files written | ☐ |
| All business questions answered | ☐ |
| Visualizations created | ☐ |
| Streamlit app working | ☐ |
| PowerPoint presentation ready | ☐ |
| README written | ☐ |
| Code cleaned & commented | ☐ |

---

## 💡 General Mentor Tips

- **Start simple.** Get a basic query working before making it complex.
- **Test your JOINs.** Always check if your JOIN returns the number of rows you expect.
- **Beware of NULLs.** They can silently break your averages and counts.
- **Think like a business client.** Your findings need to be actionable, not just technical.
- **Version control early.** Commit to GitHub regularly, not just at the end.
