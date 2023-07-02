from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import configparser, time

def callback_execute(driver: WebDriver, captcha_token: str):
    recaptcha_query = """
    function findRecaptchaClients() {
  // eslint-disable-next-line camelcase
  if (typeof (___grecaptcha_cfg) !== 'undefined') {
    // eslint-disable-next-line camelcase, no-undef
    return Object.entries(___grecaptcha_cfg.clients).map(([cid, client]) => {
      const data = { id: cid, version: cid >= 10000 ? 'V3' : 'V2' };
      const objects = Object.entries(client).filter(([_, value]) => value && typeof value === 'object');

      objects.forEach(([toplevelKey, toplevel]) => {
        const found = Object.entries(toplevel).find(([_, value]) => (
          value && typeof value === 'object' && 'sitekey' in value && 'size' in value
        ));
     
        if (typeof toplevel === 'object' && toplevel instanceof HTMLElement && toplevel['tagName'] === 'DIV'){
            data.pageurl = toplevel.baseURI;
        }
        
        if (found) {
          const [sublevelKey, sublevel] = found;

          data.sitekey = sublevel.sitekey;
          const callbackKey = data.version === 'V2' ? 'callback' : 'promise-callback';
          const callback = sublevel[callbackKey];
          if (!callback) {
            data.callback = null;
            data.function = null;
          } else {
            data.function = callback;
            const keys = [cid, toplevelKey, sublevelKey, callbackKey].map((key) => `['${key}']`).join('');
            console.log(keys)
            data.callback = `___grecaptcha_cfg.clients${keys}` + "('tkn')";
          }
        }
      });
      return data;
    });
  }
  return [];
}

let res = findRecaptchaClients()[0].callback;
return res

    """
    query = driver.execute_script(recaptcha_query)
    if not query:
        return False
    query = query.replace('tkn', captcha_token)
    driver.execute_script(query)

    return True

def tryEx(type_of_ex):
    def inner(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                pass
        return wrapper
    return inner

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('cfg.ini')
    URL = config.get('LoginData', 'url')
    EMAIL = config.get('LoginData', 'email')
    PASSWORD = config.get('LoginData', 'pwd')

    # chrome_options = Options()
    # chrome_options.add_argument('--headless=new')

    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(options=chrome_options)
    # driver = uc.Chrome()


    driver.get(URL)
    el = WebDriverWait(driver, 10).until(lambda p: p.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]'))
    print('wwqew')
    time.sleep(8)
    print(callback_execute(driver))