from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def get_youtube_comments(video_url, scroll_pause_time=2, max_scrolls=100):
    chrome_options = Options()

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(video_url)
    time.sleep(5)

    driver.execute_script("window.scrollTo(0, 600);")
    time.sleep(2)

    last_comments_count = 0
    for i in range(max_scrolls):
        driver.execute_script(
            "window.scrollTo(0, document.documentElement.scrollHeight);"
        )
        time.sleep(scroll_pause_time)

        comment_elements = driver.find_elements(By.XPATH, '//*[@id="content-text"]')

        if len(comment_elements) == last_comments_count:
            print(f"더 이상 스크롤 할 내용이 없습니다. 반복횟수: {i+1}")
            break
        last_comments_count = len(comment_elements)

    comment_elements = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
    comments = [elem.text for elem in comment_elements if elem.text.strip() != ""]

    driver.quit()
    return comments


if __name__ == "__main__":
    video_url = "YouTube_Url"
    comments = get_youtube_comments(video_url)
    print(f"총 {len(comments)}개의 댓글을 수집했습니다.")

    for idx, comment in enumerate(comments, 1):
        print(f"{idx}: {comment}\n")
