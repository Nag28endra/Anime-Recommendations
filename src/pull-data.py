import requests
from dotenv import load_dotenv
import os
import pandas as pd
import time
import logging
from pathlib import Path

load_dotenv()

# Set up logging
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

log_file = log_dir / "pull-data.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def pull_data():
    BASE_URL = os.getenv('base_url')
    if not BASE_URL:
        logger.error("base_url not found in environment variables")
        exit(1)

    all_anime = []
    page = 1
    max_retries = 3
    retry_delay = 5

    try:
        while True:
            retry_count = 0
            while retry_count < max_retries:
                try:
                    logger.info(f"Fetching page {page}...")

                    response = requests.get(f"{BASE_URL}?page={page}", timeout=10)
                    response.raise_for_status()
                    data = response.json()
                    break  # Success, exit retry loop
                except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
                    retry_count += 1
                    if retry_count < max_retries:
                        logger.warning(f"Connection error on page {page}, retrying in {retry_delay}s... (attempt {retry_count}/{max_retries})")
                        time.sleep(retry_delay)
                    else:
                        logger.error(f"Max retries reached for page {page}: {e}")
                        break
                except requests.exceptions.RequestException as e:
                    logger.error(f"Error fetching page {page}: {e}")
                    break
                except ValueError as e:
                    logger.error(f"Error parsing JSON from page {page}: {e}")
                    break

            if retry_count >= max_retries:
                break

            # Extract anime data
            try:
                for anime in data["data"]:
                    title = anime.get("title")
                    episodes = anime.get("episodes")
                    rating = anime.get("rating")
                    score = anime.get("score")
                    synopsis = anime.get("synopsis")

                    genres = ", ".join(
                        [genre["name"] for genre in anime.get("genres", [])]
                    )

                    all_anime.append({
                        "Title": title,
                        "Episodes": episodes,
                        "Rating": rating,
                        "Score": score,
                        "Synopsis": synopsis,
                        "Genres": genres
                    })
            except (KeyError, TypeError) as e:
                logger.error(f"Error extracting anime data from page {page}: {e}")
                break

            # Stop if no more pages
            if not data["pagination"]["has_next_page"]:
                break

            page += 1
            time.sleep(1)  # respect rate limit

    except Exception as e:
        logger.error(f"Unexpected error during data fetching: {e}")

    if not all_anime:
        logger.warning("No anime data collected")
        return

    try:
        # Convert to DataFrame
        df = pd.DataFrame(all_anime)

        # Create data folder if it doesn't exist
        os.makedirs("data", exist_ok=True)

        # Save to CSV
        df.to_csv("data/anime_data.csv", index=False, encoding='utf-8')

        logger.info(f"Done! CSV file created with {len(all_anime)} records [OK]")
    except Exception as e:
        logger.error(f"Error saving data to CSV: {e}")

if __name__ == "__main__":
    pull_data()