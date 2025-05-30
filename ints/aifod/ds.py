# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
#     "beautifulsoup4",
#     "selenium",
#     "ipdb",
# ]
# ///


import concurrent.futures
import json
import time
import traceback
from dataclasses import dataclass
from typing import Any

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

SITE_URL = "https://www.dentons.com/en/our-professionals"


@dataclass
class Professional:
    # Base class implemetation for Professionals
    url: str
    data: str
    content: Any | None = None

    def extract_name(self) -> str:
        return ""

    def extract_email(self) -> str:
        return ""

    def extract_phone(self) -> str:
        return ""

    def get_record(self) -> dict:
        name, email = self.extract_name(), self.extract_email()
        if name or email:
            return {
                "name": name,
                "email": email,
                "phone": self.extract_phone(),
                "url": self.url,
            }
        return {}


class DentonProfession(Professional):
    # Specific Professional with implementation of extraction
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = BeautifulSoup(self.data, "html.parser")

    def extract_phone(self):
        try:
            for p in self.content.find_all("div"):
                if phone := p.find("a", href=lambda x: x and "callto:" in x):
                    return phone.attrs["href"].split(":", 1)[-1].strip()
        except:
            return ""

    def extract_name(self):
        try:
            return self.content.find("title").text.split("-", 1)[-1]
        except:
            return ""

    def extract_email(self):
        try:
            for p in self.content.find_all("div"):
                if email := p.find("a", href=lambda x: x and "mailto:" in x):
                    return email.attrs["href"].split(":", 1)[-1].strip()
        except:
            return ""


def get_default_chrome_options():
    # Setup Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return chrome_options


def get_loaded_page_src(url):
    # download dynamic pages (with JavaScript)
    try:
        driver = webdriver.Chrome(options=get_default_chrome_options())
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        return driver.page_source
    except Exception as e:
        print(f"Error getting page {url} error:{e}")
    finally:
        driver.quit()


def get_pages(site_url, max_pages=None):
    driver = webdriver.Chrome(options=get_default_chrome_options())
    try:
        print(f"Loading {site_url}")
        driver.get(site_url)

        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Try to find and click "Load more" buttons to get all professionals
        count = 0
        while True:
            try:
                load_more_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[contains(text(), 'Load more')]")
                    )
                )
                driver.execute_script("arguments[0].click();", load_more_button)
                count += 1
                time.sleep(2)  # Wait for content to load
                if max_pages and count >= max_pages:
                    print(f"Loaded requested #pages {max_pages}.")
                    break
                print("Clicked 'Load more' button")
            except:
                print("No more 'Load more' buttons found or clickable")
                break

        return driver.page_source
    except Exception as e:
        print(f"Error getting pages {e}")
    finally:
        driver.quit()


def get_professionals(pages, tasks=5):
    # Get the page source after all content is loaded
    soup = BeautifulSoup(pages, "html.parser")
    professionals = []
    # filter out non professional pages and duplicates
    prof_links = list(
        set(
            lnk.attrs["href"]
            for lnk in soup.find_all("a")
            if lnk.attrs.get("href", "").startswith("https://www.dentons.com/")
        )
    )

    print(f"Processing {len(prof_links)} professionals with {tasks} threads")
    with concurrent.futures.ThreadPoolExecutor(max_workers=tasks) as executor:
        futures = {
            executor.submit(get_loaded_page_src, lnk): lnk for lnk in prof_links[:2]
        }
        for future in concurrent.futures.as_completed(futures):
            try:
                professionals.append(
                    DentonProfession(futures[future], future.result()).get_record()
                )
            except Exception as e:
                print(f"Error processing element {e}")
                continue
    return professionals


def save_data(professionals, filename="dentons_professionals.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(professionals, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(professionals)} professionals to {filename}")


if __name__ == "__main__":
    # get pages of profession links [max 2 pages for demo]
    pages = get_pages(SITE_URL, max_pages=2)
    # process links 10  at a time
    professionals = get_professionals(pages, tasks=10)
    # save data to file
    save_data(professionals)

    print(f"\nScraping completed!")
    print(f"Total professionals found: {len(professionals)}")

    if professionals:
        print("\nFirst few professionals:")
        for i, prof in enumerate(professionals[:3]):
            print(f"{i + 1}. {prof}")
    else:
        print(
            "No professionals found. The page structure might need different parsing approach."
        )
