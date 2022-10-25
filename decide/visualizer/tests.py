from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from base.tests import BaseTestCase
from voting.models import Voting, Question

class AdminTestCase(StaticLiveServerTestCase):


    def setUp(self):
        #Load base test functionality for decide
        self.base = BaseTestCase()
        self.base.setUp()

        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

        super().setUp()            
            
    def tearDown(self):           
        super().tearDown()
        self.driver.quit()

        self.base.tearDown()

 #   def test_simplevisualizer():
  #      q= Question(desc='test question')
  #      q.save()

  #      v=Voting(name='test voting', question=q)
   #     v.save()
   #     response=self.driver.get(f'{self.live_srver_urll}/visualizer/{}')
