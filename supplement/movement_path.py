from playwright.sync_api import sync_playwright
import time


def get_movement_path(departure, arrival):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        page.goto("https://www.google.co.kr/maps/")

        page.locator("[aria-label=경로]").click()

        page.get_by_placeholder("출발지를 선택하거나 지도를 클릭하세요.").fill(
            departure
        )

        arrival_input = page.get_by_placeholder(
            "목적지를 선택하거나 지도를 클릭하세요."
        )

        arrival_input.fill(arrival)
        arrival_input.press("Enter")

        time.sleep(5)

        page.screenshot(path=f"movement_path.png", full_page=True)


if __name__ == "__main__":

    departure = "출발지"
    arrival = "종로 솔데스크"

    get_movement_path(departure, arrival)
