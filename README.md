# PYTHON API DATA EXTRACTOR | DYNAMIC JSON TO EXCEL TOOL

### 🎯 Project Overview

A professional, high-value Python tool designed to securely connect to external REST APIs (e.g., NewsAPI, Weather API), retrieve data in **JSON** format, and export a clean, structured report to Excel.

### ✨ Key Features & Technical Robustness

* **Secure Credential Handling (NEW!):** API keys and tokens are loaded securely from a **.env file** using `python-dotenv` and `os.getenv`. This ensures **your credentials are never exposed** in the source code.
* **Dynamic Querying:** Uses the **`argparse`** module to allow the user to define search parameters (e.g., topic, page size) directly from the command line, making the script highly flexible.
* **Data Transformation:** Efficiently parses complex JSON structures and converts the key data points (Title, URL, Date) into a readable, tabular format using **Pandas**.
* **Core Technology:** `requests`, `pandas`, `argparse`, `python-dotenv`.

### 🚀 Execution and Usage

**1. Setup:** Install dependencies: `pip install requests pandas openpyxl python-dotenv`
**2. Security:** Create a file named **`.env`** in the project root containing your API key: `NEWS_API_KEY="YOUR_KEY_HERE"`
**3. Execution (Dynamic):** Run the script from your terminal using the `--query` argument:

    ```bash
    python news_api_extractor.py --query "artificial intelligence"
    ```

**4. Output:** A new Excel file (e.g., `artificial_intelligence_news_report.xlsx`) will be generated.
