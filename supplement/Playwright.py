from playwright.sync_api import sync_playwright
import time


def get_youtube_comments(video_url, scroll_pause_time=2, max_scrolls=100):
    comments = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(video_url, wait_until="networkidle")

        page.evaluate("window.scrollTo(0, 600)")
        page.wait_for_selector("xpath=//*[@id='content-text']")

        last_comments_count = 0
        for i in range(max_scrolls):
            page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(scroll_pause_time)

            comment_elements = page.query_selector_all("xpath=//*[@id='content-text']")

            if len(comment_elements) == last_comments_count:
                print(f"더 이상 스크롤 할 내용이 없습니다. 반복횟수: {i+1}")
                break
            last_comments_count = len(comment_elements)

        comments = [
            elem.inner_text().strip()
            for elem in comment_elements
            if elem.inner_text().strip() != ""
        ]

        browser.close()
    return comments


if __name__ == "__main__":
    video_url = "YouTube_Url"
    comments = get_youtube_comments(video_url)
    print(f"총 {len(comments)}개의 댓글을 수집했습니다.")

    for idx, comment in enumerate(comments, 1):
        print(f"{idx}: {comment}\n")
