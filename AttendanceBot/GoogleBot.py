from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import TimeTable
import discordbot as DB


class GB(TimeTable.TT):
    def __init__(self,binary_location,driver_path):
        TimeTable.TT.__init__(self)
        self.options = Options()
        self.options.add_argument('--ignore-ssl-errors=yes')
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--start-maximized")
        self.options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1
        })
        self.options.binary_location = binary_location
        self.driver = webdriver.Chrome(executable_path=driver_path,
                                       options=self.options)
        self.driver.maximize_window()
        self.email = ''
        self.password = ''

    def gmail_Login(self,
                    URL='https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false'
                        '&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Ftab%3Drm%26ogbl&scc=1&ltmpl=default'
                        '&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'):
        self.driver.get(URL)

        self.email = input('Enter a correct valid email:')
        self.password = input('Enter a valid password for the email:')
        time.sleep(3)
        gmail_email_Xpath = '//input[@type="email"]'
        try:
            gmail_email = WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element_by_xpath(gmail_email_Xpath))
            gmail_email.send_keys(self.email)
            gmail_email.send_keys(Keys.RETURN)
            time.sleep(2)
        except:
            print('Error Encountered : Recheck your email')
            print('Email:', self.email)
        try:
            gmail_pass_Xpath = '//input[@type="password"]'
            gmail_pass = WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element_by_xpath(gmail_pass_Xpath))
            gmail_pass.send_keys(self.password)
            gmail_pass.send_keys(Keys.RETURN)
            time.sleep(2)
        except:
            print('Error Encountered:Recheck your Password')
            print('Password:', self.password)

    def gm_Toggle_and_JoinMeeting(self, URL, SUBJECT, NAME):

        # AUDIO
        try:
            self.driver.get(URL)
            Xpath = '//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div'
            toggleButton = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(
                Xpath))
            toggleButton.click()
            # VIDEO
            Xpath = '//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[2]/div/div'
            toggleButton = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(
                Xpath))
            toggleButton.click()

            # JOIN/ASK TO JOIN
            time.sleep(5)
            Xpath = '//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]'
            toggleButton = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(Xpath))
            toggleButton.click()
            DB.send_start_details(SUBJECT, NAME)

        except:

            DB.send_start_error_details(SUBJECT, NAME)
            print('Error encountered: while joining the  meeting')

    def gm_LeaveMeeting(self, SUBJECT, NAME):
         try:
                time.sleep(5)
                Xpath = '//div[@class = "U26fgb JRY2Pb mUbCce kpROve GaONte Qwoy0d ZPasfd vzpHY"]'
                Button = WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element_by_xpath(Xpath))
                time.sleep(10)
                Button.click()
                DB.send_end_details(SUBJECT, NAME)
         except:
               DB.send_end_error_details(SUBJECT, NAME)
               print('Error encountered: while exiting the  meeting')

    def __del__(self):
        self.driver.quit()
