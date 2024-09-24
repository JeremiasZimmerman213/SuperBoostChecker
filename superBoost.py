from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = Options()
options.add_argument('--headless')   
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://www.bet365.com/#/HO/')

# Web scrape
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.pbb-PopularBetBuilder-superboost'))
    )
except:
    print("Super boost element not found!")

super_boosts = driver.find_elements(By.CSS_SELECTOR, '.pbb-PopularBetBuilder-superboost')

# Print super boosts
num_boosts = 1
if super_boosts:
    for boost in super_boosts:
        print(f'Super Boost {num_boosts}:')
        lines = boost.text.strip().split('\n')
        
        lines = lines[1:]

        for line in lines[:-2]:
            print(line)

        print(f"{lines[-2]} --> {lines[-1]}")

        print("=" * 50)
        num_boosts += 1
else:
    print("No super boosts found!")

driver.quit()
