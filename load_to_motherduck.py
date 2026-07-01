import duckdb
import os
from dotenv import load_dotenv

load_dotenv()
motherduck_token = os.getenv('MOTHERDUCK_TOKEN')

if not motherduck_token:
    print("Error: MOTHERDUCK_TOKEN not found in .env file.")
    exit()

def load_data():
    try:
        print("Connecting to MotherDuck...")
        con = duckdb.connect(f'md:?motherduck_token={motherduck_token}')
        
        con.execute("CREATE DATABASE IF NOT EXISTS job_market_db")
        con.execute("USE job_market_db")
        
        print("Loading JSON data into Bronze layer...")
        
        # JSON ফাইলটি সরাসরি ক্লাউড টেবিলে লোড করা হচ্ছে
        con.execute("""
            CREATE OR REPLACE TABLE bronze_jobs AS 
            SELECT * FROM read_json_auto('raw_jobs_data.json')
        """)
        
        result = con.execute("SELECT COUNT(*) FROM bronze_jobs").fetchone()
        print(f"Success! {result[0]} rows loaded into the 'bronze_jobs' table.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        con.close()

if __name__ == "__main__":
    load_data()