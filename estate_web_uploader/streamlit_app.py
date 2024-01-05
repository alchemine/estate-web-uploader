from estate_web_uploader._utils import *

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


# 사이트 접속
driver = get_driver()
driver.get("https://www.tojidanawa.com/")


# 사이트 로그인
submit_text_retry(driver, "ans5454", css_selector="#member_id")
submit_text_retry(driver, "tkajszld@94", css_selector="#pass", send_return=True)
send_active_return(driver)

# 매물 등록
## 매물 등록하기 클릭
click_button_retry(driver, "#main1 > table > tbody > tr > td:nth-child(1) > a:nth-child(3) > img")

## 카테고리 및 매물옵션 선택
wait = WebDriverWait(driver, 10)
cat_elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#category1")))
select_object = Select(cat_elem)
select_object.select_by_visible_text("상가 | 사무실")

sleep(10)
