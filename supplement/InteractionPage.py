from playwright.sync_api import sync_playwright


def get_wishket_project(login_url):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(login_url)

        page.locator("[name=emailOrId]").fill("id")
        page.locator("[name=password]").fill("password")

        page.locator("[type=submit]").click()

        page.wait_for_selector("img")

        applied_projects_count = (
            page.get_by_text("지원한 프로젝트").locator("p").inner_text()
        )
        contracted_projects_count = (
            page.get_by_text("계약한 프로젝트").locator("p").inner_text()
        )
        total_completed_amount = (
            page.get_by_text("누적 완료 금액").locator("p").inner_text()
        )

        print(f"지원한 프로젝트: {applied_projects_count}")
        print(f"계약한 프로젝트: {contracted_projects_count}")
        print(f"누적 완료 금액: {total_completed_amount}")


if __name__ == "__main__":
    wishket_url = "https://auth.wishket.com/login?next=/mywishket/"
    projects = get_wishket_project(wishket_url)
