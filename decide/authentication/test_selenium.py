from pyexpat import model
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from base.tests import BaseTestCase
from voting.models import Question, Voting
from time import sleep
from django.contrib.auth.models import User


class AdminTestCase(StaticLiveServerTestCase):


    def setUp(self):
        #Load base test functionality for decide
        self.base = BaseTestCase()
        self.base.setUp()

        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

        superuser_admin = User(username='superadmin', is_staff=True, is_superuser=True)
        superuser_admin.set_password('qwerty')
        superuser_admin.save()

        super().setUp()            
            
    def tearDown(self):           
        super().tearDown()
        self.driver.quit()

        self.base.tearDown()
        
    def test_simpleVisualizer(self):        
        q = Question(desc='test question')
        q.save()
        v = Voting(name='test voting', question=q)
        v.save()
        response =self.driver.get(f'{self.live_server_url}/visualizer/{v.pk}/')
        vState= self.driver.find_element(By.TAG_NAME,"h2").text
        self.assertTrue(vState, "Votación no comenzada")
    
    def test_simpleCorrectLogin(self):                    
        self.driver.get(f'{self.live_server_url}/admin/')
        self.driver.find_element(By.ID,'id_username').send_keys("admin")
        self.driver.find_element(By.ID,'id_password').send_keys("qwerty",Keys.ENTER)
        
        print(self.driver.current_url)
        #In case of a correct loging, a element with id 'user-tools' is shown in the upper right part
        self.assertTrue(len(self.driver.find_elements(By.ID,'user-tools'))==1)

    def test_test_login_incorrect(self):
        self.driver.get(f'{self.live_server_url}/admin/')
        self.driver.find_element(By.ID,'id_username').send_keys("test_fallo")
        self.driver.find_element(By.ID,'id_password').send_keys("qwerty",Keys.ENTER)
        self.assertTrue(len(self.driver.find_elements(By.CLASS_NAME,'errornote'))==1)
    
    def test_new_question(self):
        self.driver.get(f'{self.live_server_url}/admin/')
        self.driver.find_element(By.ID,'id_username').send_keys("superadmin")
        self.driver.find_element(By.ID,'id_password').send_keys("qwerty",Keys.ENTER)
        self.driver.get(f'{self.live_server_url}/admin/voting/question/add/')
        self.driver.find_element(By.ID, "id_desc").send_keys("test")
        self.driver.find_element(By.ID, "id_options-0-number").send_keys("1")
        self.driver.find_element(By.ID, "id_options-0-option").send_keys("question1")
        self.driver.find_element(By.ID, "id_options-1-number").send_keys("2")
        self.driver.find_element(By.ID, "id_options-1-option").send_keys("question2")
        self.driver.find_element(By.NAME, "_save").click()
        self.assertTrue(len(self.driver.find_elements(By.CLASS_NAME,'success'))==1)
  


    

  
