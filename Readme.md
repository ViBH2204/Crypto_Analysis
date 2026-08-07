# 📈 Crypto Analysis Dashboard

> A fully automated end-to-end cryptocurrency analytics dashboard built using **Python, SQLite, Power BI, and GitHub Actions**.

![Dashboard Banner](images/dashboard_banner.png)

---

## 🚀 Overview

Crypto Analysis Dashboard is an end-to-end Business Intelligence project that combines **data engineering, data modeling, automation, and interactive visualization** into a single analytics solution.

The project automatically collects cryptocurrency market data, stores it in a structured SQLite database, and visualizes key market insights through a modern Power BI dashboard featuring dynamic filtering, historical trend analysis, and interactive KPIs.

The entire ETL pipeline is automated using **GitHub Actions**, ensuring that fresh market data is available every day without manual intervention.

---

# ✨ Features

### 📊 Interactive Dashboard

- Coin selector (Bitcoin, Ethereum, Tether, Solana, Cardano)
- Dynamic KPI cards
- Historical price analysis
- Market dominance visualization
- ATH & ATL metrics
- 52 Week High / Low
- Live Market Cap
- 24 Hour Volume
- 24 Hour Price Change
- Dynamic accent colors based on selected coin
- Professional Glassmorphism UI

---

### 📈 Analytical Insights

- Current Price
- All Time High
- All Time Low
- ATH Distance %
- 52 Week High
- 52 Week Low
- Coin Dominance
- Market Capitalization
- Historical Closing Price Trend
- Interactive Hover Tooltips

---

### ⚙ Automation

- Daily data refresh using GitHub Actions
- Automated ETL pipeline
- Automatic SQLite database update
- Automatic Git commit & push
- Scheduled execution every day at **9:00 AM IST**

---

# 🏗 Project Architecture

```
             GitHub Actions
                    │
                    ▼
        Daily Scheduled Workflow
                    │
                    ▼
          Python ETL Pipeline
          ├── Fetch Live Data
          ├── Fetch Historical Data
          ├── Update SQLite
          ├── Create Views
          └── Create Indexes
                    │
                    ▼
          SQLite Database
                    │
                    ▼
          Power BI Dashboard
                    │
                    ▼
        Interactive Analytics
```

---

# 🛠 Tech Stack

## Programming

- Python 3.11

## Database

- SQLite

## Data Processing

- Pandas

## Data Collection

- yFinance
- Requests API

## Business Intelligence

- Microsoft Power BI

## Automation

- GitHub Actions

## Version Control

- Git
- GitHub

---

# 📂 Project Structure

```
Crypto_Analysis/

│
├── .github/
│   └── workflows/
│       └── daily_etl.yml
│
├── dashboard/
│
├── database/
│   └── crypto_analytics.db
│
├── scripts/
│   ├── config.py
│   ├── fetch_live.py
│   ├── fetch_historical.py
│   ├── create_database.py
│   ├── create_indexes.py
│   ├── create_views.py
│
├── power_bi/
│   └── crypto_analysis.pbix
│
├── etl_pipeline.py
│
├── requirements.txt
│
└── README.md
```

---

# 🔄 ETL Pipeline

The ETL pipeline consists of four major stages.

## 1. Extract

Historical cryptocurrency prices are collected.

Live market metrics are fetched.

Collected metrics include

- Current Price
- Market Cap
- Volume
- Supply
- Daily Change

---

## 2. Transform

The data is cleaned and standardized.

Transformations include

- Removing duplicates
- Data type conversion
- Currency formatting
- Date formatting
- Table normalization

---

## 3. Load

The transformed data is loaded into a SQLite database.

Database contains

### Fact Tables

- Historical Price Data

### Dimension Tables

- Coin Information

---

## 4. Reporting

Power BI connects directly to SQLite and provides interactive reporting.

---

# ⚡ Automation

The project is fully automated using **GitHub Actions**.

Every day at **9:00 AM IST**

GitHub automatically

- Starts a virtual machine
- Installs Python
- Installs dependencies
- Executes the ETL pipeline
- Updates the SQLite database
- Commits the new database
- Pushes changes back to GitHub

This eliminates any manual data update process.

Workflow:

```
Schedule (9 AM IST)
        │
        ▼
GitHub Actions
        │
        ▼
Run ETL Pipeline
        │
        ▼
Update SQLite Database
        │
        ▼
Commit Changes
        │
        ▼
Push to GitHub
```

---

# 📊 Dashboard Preview

## Main Dashboard

![Dashboard](images/dashboard.png)

---

## Historical Trend

![Trend](images/trend.png)

---

## Coin Analysis

![Coin](images/coin.png)

---

# 📌 KPIs Included

| KPI | Description |
|------|-------------|
| Current Price | Latest market price |
| ATH | All Time High |
| ATL | All Time Low |
| ATH Distance % | Distance from ATH |
| Market Cap | Total Market Capitalization |
| Coin Dominance | Share of Total Market Cap |
| 24H Change | Daily Percentage Change |
| 24H Volume | Trading Volume |
| 52 Week High | Highest price in last year |
| 52 Week Low | Lowest price in last year |

---

# 🎨 Dashboard Design

The dashboard follows a modern Glassmorphism-inspired UI.

Design Features

- Dark theme
- Purple gradient background
- Dynamic accent colors
- Rounded cards
- Interactive visuals
- Clean typography
- Responsive layout
- Minimalistic design

---

# 📈 DAX Measures

The dashboard includes several custom DAX measures including

- Current Price
- Market Cap
- 24H Change %
- 24H Volume
- Coin Dominance
- Selected Coin
- ATH
- ATL
- ATH Distance %
- 52 Week High
- 52 Week Low

---

# 💡 Key Learnings

This project demonstrates practical experience in

- Data Engineering
- ETL Pipelines
- SQL Database Design
- Data Modeling
- Power BI Dashboard Development
- DAX
- GitHub Actions Automation
- Data Visualization
- Business Intelligence
- Version Control

---

# 🚀 Future Improvements

- Live streaming data
- Power BI Service deployment
- Multi-page dashboard
- Portfolio performance tracker
- Technical indicators (RSI, EMA, MACD)
- Candlestick charts
- Price prediction using Machine Learning
- Alerts & notifications
- Portfolio optimization
- Mobile responsive dashboard

---

# 👨‍💻 Author

**Vaibhav Ahluwalia**

<!-- B.Tech Information Technology -->

<!-- Aspiring Data Analyst | Data Engineer | Software Developer -->

GitHub: https://github.com/ViBH2204

<!-- LinkedIn: https://linkedin.com/in/yourprofile

Portfolio: https://yourportfolio.com -->

---

# ⭐ If you found this project useful, consider giving it a star!