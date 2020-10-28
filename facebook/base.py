from bot_service.resrc_service import get_facebook_user
from http.cookies import SimpleCookie
from selenium import webdriver
from .like import like_post_by_id
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random


class Facebook:
    def __init__(self, driver_type=1, driver_path="", facebook_id="", cookie=""):
        self.driver_type = driver_type
        self.driver_path = driver_path
        self.cookie = cookie
        self.facebook_id = facebook_id
        self.username = None
        self.action_script = None
        self.facebook_action_list = []
        self.driver = None
        self.get_driver()
        self.flag = False

    def get_driver(self):
        if self.driver_type == 1:
            self.driver = webdriver.Firefox(executable_path=r'C:\Users\admin\PycharmProjects\day1__py\geckodriver.exe')

    def set_action_list(self, action_script_list):
        # get action list
        self.facebook_action_list = action_script_list

    def exe_action_script(self):
        for action in self.facebook_action_list:
            # exc
            pass
        pass

    def update_status_to_server(self):
        pass

    def logging_account(self):
        pass

    def login(self):
        self.driver.get("https://www.facebook.com/")
        rawdata = self.cookie
        cookie = SimpleCookie()
        cookie.load(rawdata)

        for key, morsel in cookie.items():
            self.driver.add_cookie({'name': key, 'value': morsel.value})

        self.driver.get("https://www.facebook.com/")

    def logout(self):
        self.driver.close()

    def export_cookie_to_file(self, save_path):
        pass

    def update_cookie_to_server(self):
        pass

    def get_facebook_user_account(self):
        data_user = get_facebook_user()
        if data_user['is_email']:
            self.username = data_user['email']
        else:
            self.username = data_user['phone']

        self.cookie = data_user['cookie']

    def like_facebook_post_by_id(self, id_baiviet):
        return like_post_by_id(self.driver, id_baiviet)

    def new_feed_scoll(self, h=0, m=0, s=0):


        # ve trang chu

        self.driver.get("https://www.facebook.com/")
        s0 = 0

        s0 += h*60*60
        s0 += m*60
        s0 += s

        actions = ActionChains(self.driver)
        while s0 >= 0 and self.flag is False:
            actions.send_keys(Keys.SPACE).perform()
            time_sleep_random = random.randint(1, 10)
            time.sleep(time_sleep_random)
            s0 -= time_sleep_random
            print("chay done")









