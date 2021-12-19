
import time

import pytest

from Pages.LoginPage import LoginPage


class Test_01_Main:

    baseUrl = "https://www.facebook.com"
    uname="liji.prathapan@gmail.com"
    pwd="Samy@rak09!"

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        print(self.baseUrl.title())
        self.lp = LoginPage(self.driver)
        time.sleep(2)
        self.lp.EnterUsername(self.uname)
        self.lp.EnterPassword(self.pwd)
        self.lp.clickLogin()




