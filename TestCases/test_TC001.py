from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_firsttesting():
    driver = Firefox()
    driver.get("https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&prevRID=KQ3CE428QSHKHPZWTE60&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    driver.maximize_window()
    driver.find_element(By.ID,"ap_customer_name").send_keys("Mosunmola")
    driver.find_element(By.ID,"ap_email").send_keys("Ayobamomosunmolaa@gmail.com")
    driver.find_element(By.ID,"ap_password").send_keys("Mosunbaby&9")
    driver.find_element(By.ID,"ap_password_check").send_keys("Mosunbaby&9")
    driver.find_element(By.ID,"continue").click()
    driver.find_element(By.ID,"signInSubmit").click()
    assert driver.current_url == "https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&prevRID=KQ3CE428QSHKHPZWTE60&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
    driver.close()