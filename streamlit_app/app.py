import sqlite3
import os
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import plotly.express as px

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Vivino Market Analysis",
    page_icon="🍷",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CUSTOM CSS ───────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Lato:wght@300;400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Lato', sans-serif;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #3D1020 !important;
}
[data-testid="stSidebar"] * {
    color: #ECE2D0 !important;
}
[data-testid="stSidebar"] .stRadio label {
    font-size: 15px !important;
    padding: 4px 0;
}

/* Metric cards */
[data-testid="metric-container"] {
    background: #f9f5f0;
    border: 1px solid #e0d5c8;
    border-radius: 8px;
    padding: 16px;
    border-left: 4px solid #6D2E46;
}

/* Recommendation box */
.rec-box {
    background: linear-gradient(135deg, #6D2E46, #3D1020);
    border-radius: 10px;
    padding: 20px 24px;
    color: #ECE2D0;
    margin: 16px 0;
    border-left: 5px solid #C9A84C;
}
.rec-box h4 {
    color: #C9A84C !important;
    font-family: 'Playfair Display', serif !important;
    margin-bottom: 8px;
    font-size: 18px;
}

/* Insight box */
.insight-box {
    background: #f9f5f0;
    border-radius: 8px;
    padding: 16px 20px;
    border-left: 4px solid #C9A84C;
    margin: 12px 0;
    color: #2C2C2C;
}

/* Award card */
.award-card {
    background: white;
    border-radius: 10px;
    padding: 20px;
    border-top: 5px solid #6D2E46;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    height: 100%;
}

/* Section header */
.section-header {
    color: #6D2E46;
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    font-weight: 700;
    border-bottom: 2px solid #C9A84C;
    padding-bottom: 8px;
    margin-bottom: 20px;
}

/* Title banner */
.title-banner {
    background: linear-gradient(135deg, #3D1020 0%, #6D2E46 100%);
    border-radius: 12px;
    padding: 30px 40px;
    color: white;
    margin-bottom: 30px;
}
.title-banner h1 {
    color: #C9A84C !important;
    font-size: 42px;
    margin: 0;
}
.title-banner p {
    color: #ECE2D0;
    font-size: 16px;
    margin-top: 8px;
}

div[data-testid="stDataFrame"] {
    border-radius: 8px;
    overflow: hidden;
}
</style>
""",
    unsafe_allow_html=True,
)


# ─── DB CONNECTION ─────────────────────────────────────────────────────────────
@st.cache_resource
def get_connection():
    project_root = os.path.dirname(os.path.dirname(__file__))
    db_path = os.path.join(project_root, "data", "vivino.db")
    return sqlite3.connect(db_path, check_same_thread=False)


@st.cache_data
def run_query(sql_file):
    # app.py lives in streamlit_app/ — go one level up to project root
    project_root = os.path.dirname(os.path.dirname(__file__))
    queries_dir = os.path.join(project_root, "queries")
    with open(os.path.join(queries_dir, sql_file), "r") as f:
        query = f.read()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🍷 Vivino")
    st.markdown("### Market Analysis")
    st.markdown("---")
    page = st.radio(
        "Navigate",
        [
            "🏠 Overview",
            "🍷 Top 10 Wines",
            "🌍 Best Country",
            "🏆 Winery Awards",
            "🔑 Taste Keywords",
            "🍇 Grape Analysis",
            "📊 Leaderboards",
            "💰 Price vs Rating",
        ],
    )
    st.markdown("---")
    st.markdown("<small>BeCode Data Science • 2025</small>", unsafe_allow_html=True)

# ─── OVERVIEW PAGE ────────────────────────────────────────────────────────────
if page == "🏠 Overview":
    st.markdown(
        """
    <div class="title-banner">
        <h1>🍷 Vivino Market Analysis</h1>
        <p>A comprehensive wine market analysis for Wiwinio — uncovering actionable insights across wines, countries, wineries and consumer taste profiles.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🍷 Wines in Database", "1,020")
    with col2:
        st.metric("🌍 Countries Analysed", "10+")
    with col3:
        st.metric("🍇 Grape Varieties", "3 Top")
    with col4:
        st.metric("💰 Max Wine Price", "€12,886")

    st.markdown("---")
    st.markdown("### 📋 What This Dashboard Covers")

    col1, col2 = st.columns(2)
    sections = [
        (
            "🍷 Top 10 Wines",
            "Best wines to highlight for increased sales, ranked by rating and popularity.",
        ),
        ("🌍 Best Country", "Which country to prioritise for the marketing budget."),
        (
            "🏆 Winery Awards",
            "Recognising the best wineries across 3 creative categories.",
        ),
        (
            "🔑 Taste Keywords",
            "Wines matching the customer taste cluster: coffee, toast, cream, citrus, green apple.",
        ),
        ("🍇 Grape Analysis", "Top 3 most common grapes and their best rated wines."),
        ("📊 Leaderboards", "Country and vintage rankings by average wine rating."),
        ("💰 Price vs Rating", "Does spending more guarantee a better wine?"),
    ]

    for i, (title, desc) in enumerate(sections):
        col = col1 if i % 2 == 0 else col2
        with col:
            st.markdown(
                f"""
            <div class="insight-box">
                <strong>{title}</strong><br>
                <span style="color:#7A6B6B; font-size:14px;">{desc}</span>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.markdown(
        """
    <div class="rec-box">
        <h4>⚠️ Data Quality Notes</h4>
        <ul>
            <li>The <code>wineries</code> table has broken foreign key relationships — only 4/1020 wines have a valid winery match</li>
            <li>Schema diagram shows a <code>wines_count</code> column in <code>grapes</code> that does not exist</li>
            <li>Some vintages have <code>year = 'N.V.'</code> (Non-Vintage) requiring special handling</li>
            <li>Country names are stored in French</li>
        </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ─── TOP 10 WINES ─────────────────────────────────────────────────────────────
elif page == "🍷 Top 10 Wines":
    st.markdown(
        '<div class="section-header">🍷 Top 10 Wines to Highlight</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        "*Minimum 1,000 ratings — ranked by average rating, then by popularity*"
    )

    results = run_query("top_10_wines.sql")

    col1, col2 = st.columns([2, 1])

    with col1:
        import pandas as pd

        df = pd.DataFrame(
            results, columns=["Wine Name", "Avg Rating", "# Ratings", "Country"]
        )
        df.index = range(1, len(df) + 1)
        st.dataframe(df, use_container_width=True, height=400)

    with col2:
        countries_count = {}
        for row in results:
            c = row[3]
            countries_count[c] = countries_count.get(c, 0) + 1

        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(countries_count.keys(), countries_count.values(), color="#6D2E46")
        ax.set_title("Wines by Country", fontsize=13)
        ax.set_ylabel("Count")
        plt.xticks(rotation=15, ha="right")
        fig.patch.set_facecolor("#f9f5f0")
        ax.set_facecolor("#f9f5f0")
        st.pyplot(fig)

    st.markdown(
        """
    <div class="rec-box">
        <h4>💡 Recommendation</h4>
        We selected wines with a minimum of 1,000 ratings to ensure statistical reliability, ranked by average rating then by popularity.
        <strong>Cabernet Sauvignon</strong> leads with a 4.8 avg rating. The US and Spain dominate the top 10.
    </div>
    """,
        unsafe_allow_html=True,
    )

# ─── BEST COUNTRY ─────────────────────────────────────────────────────────────
elif page == "🌍 Best Country":
    st.markdown(
        '<div class="section-header">🌍 Best Country for Marketing Budget</div>',
        unsafe_allow_html=True,
    )

    results = run_query("best_country.sql")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🏆 Recommended", "United States")
    with col2:
        st.metric("👥 Platform Users", "12.3M")
    with col3:
        st.metric("⭐ Avg Rating", "4.49")

    results_sorted = sorted(results, key=lambda x: x[3])
    countries = [row[0] for row in results_sorted]
    avg_ratings = [row[3] for row in results_sorted]
    colors = ["#C9A84C" if c == "États-Unis" else "#6D2E46" for c in countries]

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.barh(countries, avg_ratings, color=colors)
    ax.set_xlim(4.3, 4.55)
    ax.set_title("Top 10 Countries by Average Wine Rating", fontsize=14, pad=15)
    ax.set_xlabel("Average Rating")
    ax.set_ylabel("Country")
    fig.patch.set_facecolor("#f9f5f0")
    ax.set_facecolor("#f9f5f0")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    st.pyplot(fig)

    st.markdown(
        """
    <div class="rec-box">
        <h4>💡 Recommendation — United States</h4>
        Although Germany leads slightly in avg rating (4.50), the US has <strong>12.3M users</strong> — nearly double France (5.9M).
        Combined with 204K wines and a 4.49 avg rating, the US offers the best combination of reach and quality.
        Germany's user base is 5× smaller, making the US the stronger choice for <strong>maximum marketing impact</strong>.
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📊 Full Data")
    import pandas as pd

    df = pd.DataFrame(
        results, columns=["Country", "Users Count", "Wines Count", "Avg Rating"]
    )
    st.dataframe(df, use_container_width=True)

# ─── WINERY AWARDS ────────────────────────────────────────────────────────────
elif page == "🏆 Winery Awards":
    st.markdown(
        '<div class="section-header">🏆 Winery Awards</div>', unsafe_allow_html=True
    )
    st.markdown(
        "*Due to data quality issues with the wineries table, winery names were identified manually via vintage names.*"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
        <div class="award-card">
            <h4 style="color:#6D2E46; font-family:'Playfair Display',serif;">🥇 Best Overall Winery</h4>
            <h2 style="font-family:'Playfair Display',serif; color:#2C2C2C;">Krug</h2>
            <p style="color:#7A6B6B; font-style:italic;">Avg Rating: 4.64 • 5 wines</p>
            <hr>
            <p style="font-size:14px;">Highest average rating among wineries with 5+ wines. A legendary Champagne house from France 🇫🇷</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="award-card">
            <h4 style="color:#5A7A3A; font-family:'Playfair Display',serif;">🌍 Most International Winery</h4>
            <h2 style="font-family:'Playfair Display',serif; color:#2C2C2C;">Domaine Faiveley</h2>
            <p style="color:#7A6B6B; font-style:italic;">10 regions • Burgundy, France</p>
            <hr>
            <p style="font-size:14px;">Wines present across the most regions worldwide. Iconic Burgundy producer spanning 10 appellations 🇫🇷</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div class="award-card">
            <h4 style="color:#3A5A7A; font-family:'Playfair Display',serif;">🍇 Most Diverse Winery</h4>
            <h2 style="font-family:'Playfair Display',serif; color:#2C2C2C;">Gaja</h2>
            <p style="color:#7A6B6B; font-style:italic;">12 different wines • Italy</p>
            <hr>
            <p style="font-size:14px;">Largest wine portfolio in the database. Legendary Piedmontese producer known for Barbaresco 🇮🇹</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### 📊 Raw Query Results")

    best = run_query("best_winery_award.sql")
    intl = run_query("most_international_winery_award.sql")
    diverse = run_query("most_diverse_winery_award.sql")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Best Overall (Top 3)**")
        import pandas as pd

        st.dataframe(
            pd.DataFrame(best, columns=["Winery ID", "Wine Count", "Avg Rating"]),
            use_container_width=True,
        )
    with c2:
        st.markdown("**Most International (Top 3)**")
        st.dataframe(
            pd.DataFrame(intl, columns=["Winery ID", "Region Count"]),
            use_container_width=True,
        )
    with c3:
        st.markdown("**Most Diverse (Top 3)**")
        st.dataframe(
            pd.DataFrame(diverse, columns=["Winery ID", "Wine Count"]),
            use_container_width=True,
        )

# ─── TASTE KEYWORDS ───────────────────────────────────────────────────────────
elif page == "🔑 Taste Keywords":
    st.markdown(
        '<div class="section-header">🔑 Customer Taste Cluster</div>',
        unsafe_allow_html=True,
    )

    st.markdown("#### Target Keywords *(CASE SENSITIVE, confirmed by >10 users)*")
    kw_cols = st.columns(5)
    for i, kw in enumerate(["coffee", "toast", "green apple", "cream", "citrus"]):
        with kw_cols[i]:
            st.markdown(
                f"""
            <div style="background:#6D2E46; color:#C9A84C; border:1px solid #C9A84C;
                        border-radius:6px; padding:10px; text-align:center;
                        font-weight:bold; font-family:'Playfair Display',serif;">
                {kw}
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("")
    results = run_query("taste_keyword.sql")

    st.markdown(f"**{len(results)} matching wines found**")

    st.markdown(
        """
    <div class="rec-box">
        <h4>💡 Key Insight</h4>
        This taste cluster maps <strong>almost exclusively to premium Champagne wines</strong> (group: non_oak).
        Coffee, toast, green apple, cream and citrus are classic Champagne tasting notes — suggesting a large customer segment
        with a preference for classic Champagne style.
    </div>
    """,
        unsafe_allow_html=True,
    )

    import pandas as pd

    df = pd.DataFrame(results, columns=["Wine Name", "Group Name", "Keyword Count"])
    st.dataframe(df, use_container_width=True, height=400)

# ─── GRAPE ANALYSIS ───────────────────────────────────────────────────────────
elif page == "🍇 Grape Analysis":
    st.markdown(
        '<div class="section-header">🍇 Top 3 Most Common Grapes Worldwide</div>',
        unsafe_allow_html=True,
    )

    grapes = run_query("top_grapes.sql")
    wines_per_grape = run_query("best_wines_per_grape.sql")

    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    colors_grape = ["#6D2E46", "#A26769", "#C9A84C"]

    for i, (grape, total) in enumerate(grapes):
        with cols[i]:
            st.metric(
                f"{'🥇' if i==0 else '🥈' if i==1 else '🥉'} {grape}",
                f"{total:,} wines",
            )

    st.markdown("---")

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    grape_names = ["Cabernet Sauvignon", "Merlot", "Chardonnay"]

    for i, grape_name in enumerate(grape_names):
        data = [
            (row[0], row[1], row[2]) for row in wines_per_grape if row[3] == grape_name
        ]
        if data:
            names = [
                (
                    f"{row[0][:30]}... ({row[2]:,})"
                    if len(row[0]) > 30
                    else f"{row[0]} ({row[2]:,})"
                )
                for row in data
            ]
            ratings = [row[1] for row in data]
            axes[i].barh(names, ratings, color=colors_grape[i])
            axes[i].set_title(grape_name, fontsize=12, fontweight="bold")
            axes[i].set_xlim(4.0, 5.0)
            axes[i].set_xlabel("Avg Rating")
            axes[i].spines["top"].set_visible(False)
            axes[i].spines["right"].set_visible(False)
            fig.patch.set_facecolor("#f9f5f0")
            axes[i].set_facecolor("#f9f5f0")

    plt.tight_layout()
    st.pyplot(fig)

    st.markdown(
        """
    <div class="rec-box">
        <h4>💡 Recommendation</h4>
        Vivino should prioritise <strong>Cabernet Sauvignon</strong> — it leads in both volume (9.6M wines) and quality (avg 4.66).
        Merlot's lower rating (4.37) despite strong volume presents an opportunity to help users <strong>discover better Merlot producers</strong>.
        Chardonnay sits in the middle with a solid 4.45 avg rating.
    </div>
    """,
        unsafe_allow_html=True,
    )

# ─── LEADERBOARDS ─────────────────────────────────────────────────────────────
elif page == "📊 Leaderboards":
    st.markdown(
        '<div class="section-header">📊 Country & Vintage Leaderboards</div>',
        unsafe_allow_html=True,
    )

    tab1, tab2 = st.tabs(["🌍 Country Leaderboard", "📅 Vintage Leaderboard"])

    with tab1:
        country_results = run_query("country_leaderbord.sql")
        sorted_countries = sorted(country_results, key=lambda x: x[1])
        countries = [row[0] for row in sorted_countries]
        ratings = [row[1] for row in sorted_countries]
        colors = ["#C9A84C" if c == "Allemagne" else "#6D2E46" for c in countries]

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.barh(countries, ratings, color=colors)
        ax.set_xlim(4.3, 4.55)
        ax.set_title("Top 10 Countries by Average Wine Rating", fontsize=14)
        ax.set_xlabel("Average Rating")
        fig.patch.set_facecolor("#f9f5f0")
        ax.set_facecolor("#f9f5f0")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        st.pyplot(fig)

        import pandas as pd

        df = pd.DataFrame(country_results, columns=["Country", "Avg Rating"])
        st.dataframe(df, use_container_width=True)

    with tab2:
        vintage_results = run_query("vintage_leaderbord.sql")
        vintage_clean = [
            row
            for row in vintage_results
            if row[0] is not None and row[1] is not None and str(row[0]).isdigit()
        ]
        vintage_sorted = sorted(vintage_clean, key=lambda row: int(row[0]))
        years = [str(row[0]) for row in vintage_sorted]
        avg_ratings = [row[1] for row in vintage_sorted]

        fig = px.line(
            x=years,
            y=avg_ratings,
            labels={"x": "Vintage Year", "y": "Average Rating"},
            title="Average Wine Rating by Vintage Year",
            markers=True,
            color_discrete_sequence=["#6D2E46"],
        )
        fig.update_layout(
            xaxis_title="Vintage Year",
            yaxis_title="Average Rating",
            showlegend=False,
            xaxis=dict(type="category", tickangle=45),
            plot_bgcolor="#f9f5f0",
            paper_bgcolor="#f9f5f0",
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown(
            """
        <div class="insight-box">
            <strong>📌 Key Vintage Insights</strong><br><br>
            • <strong>1929, 1962, 1964</strong> — Highest rated years (4.70)<br>
            • <strong>1910–1980</strong> — Higher avg ratings, older vintages rated more selectively<br>
            • <strong>1980–2010</strong> — Stable plateau around 4.50–4.58<br>
            • <strong>2010–2022</strong> — Slight decline, recent vintages need more time to accumulate ratings<br>
            • <strong>1975</strong> — Notable dip (4.20), known poor harvest year
        </div>
        """,
            unsafe_allow_html=True,
        )

# ─── PRICE VS RATING ──────────────────────────────────────────────────────────
elif page == "💰 Price vs Rating":
    st.markdown(
        '<div class="section-header">💰 Price vs Rating Correlation</div>',
        unsafe_allow_html=True,
    )
    st.markdown("*Does spending more guarantee a better wine?*")

    results = run_query("price_vs_rating.sql")
    prices = [row[1] for row in results if row[1] and row[2] and row[2] > 0]
    ratings = [row[2] for row in results if row[1] and row[2] and row[2] > 0]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Wines Analysed", f"{len(prices):,}")
    with col2:
        st.metric("Price Range", f"€{min(prices):.0f} – €{max(prices):,.0f}")
    with col3:
        st.metric("Correlation", "WEAK")

    max_price = st.slider("Max Price Filter (€)", 100, 5000, 500, step=100)
    filtered = [(p, r) for p, r in zip(prices, ratings) if p <= max_price]
    fp = [x[0] for x in filtered]
    fr = [x[1] for x in filtered]

    fig = px.scatter(
        x=fp,
        y=fr,
        title=f"Price vs Rating (wines ≤ €{max_price})",
        labels={"x": "Price (€)", "y": "Average Rating"},
        opacity=0.4,
        color_discrete_sequence=["#6D2E46"],
    )
    fig.update_layout(
        plot_bgcolor="#f9f5f0",
        paper_bgcolor="#f9f5f0",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
    <div class="rec-box">
        <h4>💡 Business Insight</h4>
        The scatter plot reveals that price and rating have a <strong>weak correlation</strong>.
        Highly rated wines (4.7+) can be found across all price ranges from €23 to €490,
        suggesting that <strong>price is not a reliable indicator of quality</strong> on Vivino.<br><br>
        Vivino can leverage this finding to promote affordable high-quality wines to price-conscious customers,
        potentially increasing platform engagement among budget wine lovers.
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.caption(
        f"⚠️ Prices above €{max_price} excluded from visualization. Max in dataset: €{max(prices):,.0f}"
    )
