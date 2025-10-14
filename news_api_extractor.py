import requests
import pandas as pd
import os
import argparse
from dotenv import load_dotenv

# ==========================================================
# 1. CONFIGURATION AND ARGUMENT PARSING
# ==========================================================

# Load environment variables from .env file
load_dotenv()

# Define output file
OUTPUT_FILE = "news_report_results.xlsx"
BASE_URL = "https://newsapi.org/v2/everything" # Using /everything for flexible search queries

def parse_arguments():
    """Reads the search query from the command line."""
    parser = argparse.ArgumentParser(
        description="A Python tool to extract news articles from NewsAPI based on a user-defined query and export them to Excel.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    # The --query argument is now mandatory
    parser.add_argument(
        '--query', 
        '-q',
        type=str,
        required=True,
        help="The search term (topic) for which to find news articles (e.g., 'artificial intelligence' or 'stocks')."
    )
    parser.add_argument(
        '--pagesize',
        '-p',
        type=int,
        default=25,
        help="Number of articles to retrieve (max 100 per request)."
    )
    return parser.parse_args()

# ==========================================================
# 2. DATA EXTRACTION AND EXPORT
# ==========================================================

def extract_and_export(articles, search_query):
    """Extracts specific fields from the JSON articles list and exports them to Excel."""
    news_list = []
    
    for article in articles:
        news_list.append({
            'Title': article.get('title'),
            'Source': article.get('source', {}).get('name'), 
            'PublishedAt': article.get('publishedAt'),
            'Article_URL': article.get('url')
        })
    
    if not news_list:
        print("⚠️ WARNING: No data extracted. List of articles is empty.")
        return

    df = pd.DataFrame(news_list)
    
    # Update output file name to include the search query
    safe_query = search_query.replace(' ', '_').lower()
    final_output_file = f"{safe_query}_news_report.xlsx"
    
    try:
        df.to_excel(final_output_file, index=False)
        print("\n==============================================")
        print(f"✅ SUCCESS! Data extracted and saved to: {final_output_file}")
        print(f"Total articles processed: {len(df)}")
        print("==============================================")
    except Exception as e:
        print(f"❌ EXPORT ERROR: Could not write to Excel file: {e}")


# ==========================================================
# 3. API CONNECTION AND PARSING
# ==========================================================

def get_news_data(search_query, page_size):
    """Handles the API connection, authentication, and error checking."""
    print(f"Starting API connection for query: '{search_query}'...")
    
    # Securely retrieve the key from the .env file
    API_KEY = os.getenv('NEWS_API_KEY')
    
    if not API_KEY:
        print("❌ CRITICAL ERROR: NEWS_API_KEY not found. Check your .env file setup.")
        return

    # Dynamic parameters based on user input
    API_PARAMS = {
        'q': search_query,  # The dynamic search term
        'apiKey': API_KEY,  # The securely loaded key
        'pageSize': page_size,
        'language': 'en'
    }

    try:
        response = requests.get(BASE_URL, params=API_PARAMS)
        
        if response.status_code == 200:
            print("Connection successful. Parsing JSON response...")
            data = response.json()
            
            if data['status'] == 'ok' and data['totalResults'] > 0:
                extract_and_export(data.get('articles', []), search_query)
            else:
                print("❌ API ERROR: The API returned an error or 0 results.")
                print(f"Response message: {data.get('message', 'No message provided')}")
        
        else:
            print(f"❌ FAILED TO CONNECT. HTTP Status Code: {response.status_code}")
            print("Verify the API endpoint or your network connection.")

    except requests.exceptions.RequestException as e:
        print(f"❌ CRITICAL NETWORK ERROR: Could not connect to the API server: {e}")


# ==========================================================
# 4. MAIN EXECUTION
# ==========================================================

if __name__ == "__main__":
    args = parse_arguments()
    get_news_data(args.query, args.pagesize)