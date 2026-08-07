# 📈 Crypto Analysis Dashboard

> A fully automated end-to-end cryptocurrency analytics dashboard built using **Python, SQLite, Power BI, and GitHub Actions**.

<img width="1357" height="747" alt="image" src="https://github.com/user-attachments/assets/1c95ddfa-ab80-4692-8349-c922a05cf244" />


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

# 🛠 Tech Stack

## Programming

- Python 

## Database

- SQLite

## Data Processing

- Pandas

## Data Collection

- yFinance
- Requests API
- Coin gecko

## Business Intelligence

- Microsoft Power BI

## Automation

- GitHub Actions

## Version Control

- Git
- GitHub

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

<img width="1331" height="746" alt="image" src="https://github.com/user-attachments/assets/37a71cbd-2696-4af3-9fd7-1cb096051f17" />


---

<img width="1330" height="747" alt="image" src="https://github.com/user-attachments/assets/24fd49fa-65a5-4495-99f6-b336bbfaacc1" />


---

<img width="1331" height="751" alt="image" src="https://github.com/user-attachments/assets/99ec1bbd-7919-436b-b418-5fa09d7f3067" />


---

<img width="1325" height="750" alt="image" src="https://github.com/user-attachments/assets/4d7a4493-964e-498a-84ae-0b87ffa6da94" />


---

<img width="1325" height="750" alt="image" src="https://github.com/user-attachments/assets/f571a89e-1dfc-4746-88ab-5b1f30b462da" />


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
<!--
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
-->
---

# 👨‍💻 Author

**Vaibhav Ahluwalia**

<!-- B.Tech Information Technology -->

<!-- Aspiring Data Analyst | Data Engineer | Software Developer -->

GitHub: https://github.com/ViBH2204

<!-- LinkedIn: https://linkedin.com/in/yourprofile

Portfolio: https://yourportfolio.com -->

---
