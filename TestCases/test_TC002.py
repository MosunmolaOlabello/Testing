from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

def test_secondtesting():
    driver = Firefox()
    driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    driver.find_element(By.NAME,"email").send_keys("ayobamiolabello@gmail.com")
    driver.find_element(By.ID,"continue").click()
    driver.find_element(By.NAME,"password").send_keys("Mosunbaby&9")
    driver.find_element()
    print(driver.page_source)
    driver.close()