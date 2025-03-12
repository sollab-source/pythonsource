from playwright.sync_api import sync_playwright
import csv


def get_trend_rank():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://m.kinolights.com/rank_data/kino")

        rank_data_items = page.query_selector_all(".rank_data-item")

        rank_data = []
        for rank_data_item in rank_data_items:

            content = rank_data_item.inner_text().split("\n")

            rank = content[0]
            etc = content[3] if content[5] == "" else "해당 정보 없음"
            title = content[4] if content[5] == "" else content[3]
            genre_birth = (content[6] if content[5] == "" else content[5]).split("·")
            genre = genre_birth[0].strip()
            birth = (
                genre_birth[1].strip() if len(genre_birth) == 2 else "해당 정보 없음"
            )
            if len(content) != 7:
                score = content[8] if content[7] == "" else content[7]
            else:
                score = "해당 정보 없음"

            rank_data.append(
                {
                    "순위": rank,
                    "매체": etc,
                    "제목": title,
                    "장르": genre,
                    "출시년도": birth,
                    "점수": score,
                }
            )

        save_csv(rank_data)


def save_csv(rank_data):
    with open("./trend_rank.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "순위",
                "매체",
                "제목",
                "장르",
                "출시년도",
                "점수",
            ]
        )

        for data in rank_data:
            writer.writerow(data.values())


if __name__ == "__main__":
    get_trend_rank()
