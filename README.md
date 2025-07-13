# Crypto ETL Pipeline using CoinGecko API

## 📌 Project Overview

This project demonstrates a complete **ETL (Extract, Transform, Load)** pipeline using real-time cryptocurrency data. It fetches data from the **CoinGecko API**, processes and stores it in a **PostgreSQL** database, and serves it through a **FastAPI** backend. A dedicated table tracks **Bitcoin** data specifically, enabling further analysis and insights.

## 🚀 Features

- Extracts live crypto data from the CoinGecko API
- Transforms JSON responses into structured Pandas DataFrames
- Loads transformed data into a PostgreSQL database
- Tracks Bitcoin prices at two-minute intervals in a dedicated table
- FastAPI endpoints to interact with and display collected data
- Foundation for building alert systems and visual insights on crypto movements

## 🎯 Motivation

I built this project to:
- Learn and apply the principles of ETL pipelines
- Develop a hands-on project involving real-world crypto data
- Extract actionable insights from Bitcoin and eventually other cryptocurrencies

## 👤 Who Is This For?

This project is useful for:
- Beginners learning about data engineering and API integration
- Crypto analysts who want a foundation to build custom alerts or visualizations
- Developers seeking to extend or repurpose the pipeline for broader crypto studies

## 🧠 Problems It Aims to Solve (Future Goals)

While the current version focuses on displaying Bitcoin price data every two minutes, the roadmap includes:

- 🔔 Tracking and alerting users about sudden price drops or spikes
- 📊 Comparing a coin's current market cap to its all-time high
- 📈 Visualizing a coin’s recovery since its all-time low

## 🛠️ Tech Stack

- **Language:** Python
- **API Source:** CoinGecko API
- **Backend:** FastAPI
- **Database:** PostgreSQL
- **Libraries:** Pandas, SQLAlchemy, Requests

---

