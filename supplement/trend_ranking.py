from playwright.sync_api import sync_playwright
import csv


def get_trend_rank():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://m.kinolights.com/ranking")

        ranking_items = page.query_selector_all(".ranking-item")

        rank_data = []
        for ranking_item in ranking_items:

            content = ranking_item.inner_text().split("\n")

            result = {
                "rank": None,
                "media": None,
                "title": None,
                "genre_year": None,
                "rating": None,
            }

            result["rank"] = content[0]

            idx = 2

            if idx < len(content) and content[idx] == "NEW" or content[idx].isdigit():
                idx += 1

            media_types = {
                "TV",
                "영화관",
            }  # 필요에 따라 확장
            if idx < len(content) and content[idx] in media_types:
                result["media"] = content[idx]
                idx += 1

            if idx < len(content):
                result["title"] = content[idx]
                idx += 2

            if idx < len(content):
                result["genre_year"] = content[idx]
                idx += 2

            # 8. 평점: 보통 '%'로 끝나면 평점으로 판단
            if idx < len(content) and content[idx].endswith("%"):
                result["rating"] = content[idx]
                idx += 1

            rank_data.append(result)

        save_csv(rank_data)


def save_csv(rank_data):
    with open("./trend_rank.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "순위",
                "매체",
                "제목",
                "장르 및 출시년도",
                "점수",
            ]
        )

        for data in rank_data:
            writer.writerow(data.values())


if __name__ == "__main__":
    get_trend_rank()
