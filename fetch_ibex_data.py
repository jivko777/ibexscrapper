import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

URL = "https://ibex.bg/данни-за-пазара/пазарен-сегмент-ден-напред/day-ahead-prices-and-volumes-v2-0/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_data():
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")

    if not table:
        raise Exception("Таблицата не е намерена.")

    rows = table.find_all("tr")[1:]  # Пропускаме заглавния ред
    last_column_data = []

    for row in rows:
        cols = row.find_all("td")
        if cols:
            last_value = cols[-1].text.strip()
            last_column_data.append(last_value)

    return last_column_data

if __name__ == "__main__":
    try:
        data = fetch_data()
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        result = {
            "fetched_at": now,
            "values": data
        }
        with open("ibex_data.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print("Успешно записани данни в ibex_data.json")
    except Exception as e:
        print("Грешка при изтегляне:", e)
