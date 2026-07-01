import requests
import json
import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

load_dotenv()

def fetch_job_data():
    app_id = os.getenv('ADZUNA_APP_ID')
    app_key = os.getenv('ADZUNA_APP_KEY')
    
    if not app_id or not app_key:
        print("Error: API credentials not found in .env file.")
        return

    country = 'gb'
    all_jobs = []  
    page = 1  
    
    print("Starting data ingestion from Adzuna API...")

    while True:
        url = f'https://api.adzuna.com/v1/api/jobs/{country}/search/{page}'
        
        params = {
            'app_id': app_id,
            'app_key': app_key,
            'results_per_page': 50,
            'max_days_old': 1,
            'content-type': 'application/json'
        }

        try:
            print(f"Fetching page {page}...")
            response = requests.get(url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                results = data.get('results', [])
                
                if not results:
                    break
                    
                all_jobs.extend(results)
                
                if len(results) < 50:
                    break
                    
                page += 1
            else:
                print(f"Failed on page {page}. Status code: {response.status_code}")
                break
                
        except Exception as e:
            print(f"An error occurred on page {page}: {e}")
            break

    print(f"Ingestion complete. Total new jobs fetched: {len(all_jobs)}")
    
    with open('raw_jobs_data.json', 'w') as f:
        json.dump(all_jobs, f, indent=4)
        
    print("All data successfully saved to raw_jobs_data.json")

if __name__ == "__main__":
    fetch_job_data()