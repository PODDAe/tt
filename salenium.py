from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

class TikTokAutomation:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username: str, password: str):
        """Login to TikTok"""
        self.driver.get("https://www.tiktok.com/login")
        
        # Wait for login page to load
        time.sleep(5)
        
        # You might need to adjust selectors based on TikTok's current layout
        try:
            # Switch to email/username login
            switch_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Use phone / email / username')]"))
            )
            switch_btn.click()
            time.sleep(2)
            
            # Enter credentials
            username_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            username_field.send_keys(username)
            
            password_field = self.driver.find_element(By.NAME, "password")
            password_field.send_keys(password)
            
            # Click login
            login_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
            login_btn.click()
            
            time.sleep(10)  # Wait for login to complete
            
        except Exception as e:
            print(f"Login error: {e}")

    def follow_users_in_hashtag(self, hashtag: str, max_follows: int = 10):
        """Follow users from a specific hashtag"""
        self.driver.get(f"https://www.tiktok.com/tag/{hashtag}")
        time.sleep(5)
        
        follows = 0
        while follows < max_follows:
            try:
                # Find follow buttons
                follow_buttons = self.driver.find_elements(
                    By.XPATH, "//button[contains(text(), 'Follow')]"
                )
                
                for button in follow_buttons[:min(5, len(follow_buttons))]:
                    if follows >= max_follows:
                        break
                    
                    try:
                        button.click()
                        print(f"Followed user {follows + 1}")
                        follows += 1
                        time.sleep(random.uniform(2, 5))
                    except:
                        continue
                
                # Scroll down to load more content
                self.driver.execute_script("window.scrollBy(0, 1000)")
                time.sleep(3)
                
            except Exception as e:
                print(f"Error: {e}")
                break

    def like_and_comment(self, hashtag: str, comments: list, max_actions: int = 5):
        """Like and comment on videos"""
        self.driver.get(f"https://www.tiktok.com/tag/{hashtag}")
        time.sleep(5)
        
        actions = 0
        while actions < max_actions:
            try:
                # Find like buttons
                like_buttons = self.driver.find_elements(
                    By.XPATH, "//span[contains(@class, 'like-icon')]"
                )
                
                for like_button in like_buttons:
                    if actions >= max_actions:
                        break
                    
                    try:
                        like_button.click()
                        print(f"Liked video {actions + 1}")
                        
                        # Add comment (optional)
                        comment_btn = self.driver.find_element(
                            By.XPATH, "//span[contains(@class, 'comment-icon')]"
                        )
                        comment_btn.click()
                        time.sleep(2)
                        
                        comment_field = self.driver.find_element(
                            By.XPATH, "//div[@contenteditable='true']"
                        )
                        comment_field.send_keys(random.choice(comments))
                        time.sleep(1)
                        
                        post_btn = self.driver.find_element(
                            By.XPATH, "//button[contains(text(), 'Post')]"
                        )
                        post_btn.click()
                        
                        actions += 1
                        time.sleep(random.uniform(5, 10))
                        
                    except:
                        continue
                
                self.driver.execute_script("window.scrollBy(0, 800)")
                time.sleep(3)
                
            except Exception as e:
                print(f"Error: {e}")
                break

    def close(self):
        self.driver.quit()

# Usage
bot = TikTokAutomation()
bot.login("your_username", "your_password")
bot.follow_users_in_hashtag("programming", max_follows=5)
bot.close()