from cmath import log
from distutils.log import Log
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from os import system
import time
from colorama import Fore, Back, Style
import logging
logging.basicConfig(level=logging.INFO)

system("title " + "Mèo Siêu Nhân")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options) # chạy thằng chrome driver
driver.set_window_size(1260, 720) # size của thằng chrome vừa mở lên

z = 0
mode = 1

def botViewByMeo():
    global z
    time.sleep(10)
    try:
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click() # views button

    except:
        print(Fore.RED + 'Lỗi rồi bạn ơi!!!')
        driver.refresh() # refresh
        botViewByMeo()
    try:
        time.sleep(3)

        print("[N] Getting link: ", vidUrl)

        driver.find_element(By.XPATH, "//*[@id=\"sid4\"]/div/form/div/input").clear() # remove input
        driver.find_element(By.XPATH, "//*[@id=\"sid4\"]/div/form/div/input").send_keys(vidUrl) # paste url  
        driver.find_element(By.XPATH, "//*[@id=\"sid4\"]/div/form/div/div/button").click() # search 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click() # submit
        time.sleep(2)

        driver.refresh() # refresh
        z += 1
        total = z * 1000 # "z" số lần xài tool, 1000 views cho 1 "z"

        print(Fore.GREEN + 'Xong rồi bạn ơi! Tổng lượt xem:', total,'views')

        time.sleep(330) # 5min30sec thời gian chờ
        botViewByMeo() # starting loop
        
    except:
        print(Fore.RED + 'Bị ngáo rồi, 3p sau thử lại đi') # khi web thay đổi thời gian chờ thì sẽ bị, nâng thời gian sleep lên là được
        time.sleep(2)
        driver.refresh() # refresh
        botViewByMeo() # starting loop

print('''\r\n
 ██╗      ██████╗ ███╗   ██╗ ██████╗          /\_/\                               oo__     
 ██║     ██╔═══██╗████╗  ██║██╔════╝        =( °w° )=            oo__            <;___)------
 ██║     ██║   ██║██╔██╗ ██║██║  ███╗         )   (  //         <;___)------       " "
 ██║     ██║   ██║██║╚██╗██║██║   ██║        (__ __)//            " "   
 ███████╗╚██████╔╝██║ ╚████║╚██████╔╝                    oo__
 ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝                    <;___)------
                                                          " "
         _          __________                              _, 
     _.-(_)._     ."          ".      .--""--.          _.-{__}-._   
   .'________'.   | .--------. |    .'        '.      .:-'`____`'-:.
  [____________] /` |________| `\  /   .'``'.   \    /_.-"`_  _`"-._\  
  /  / .\/. \  \|  / / .\/. \ \  ||  .'/.\/.\'.  |  /`   / .\/. \   `\  
  |  \__/\__/  |\_/  \__/\__/  \_/|  : |_/\_| ;  |  |    \__/\__/    |
  \            /  \            /   \ '.\    /.' / .-\                /-.
  /'._  --  _.'\  /'._  --  _.'\   /'. `'--'` .'\/   '._-.__--__.-_.'   \ 
 /_   `""""`   _\/_   `""""`   _\ /_  `-./\.-'  _\'.    `""""""""`    .'`\ 
(__/    '|    \ _)_|           |_)_/            \__)|        '       |   |
  |_____'|_____|   \__________/   |              | `_________'________`;-'
   '----------'    '----------'   '--------------'`--------------------`
┌─────────────────────────────────────────────────────┐
│                      ฅ^•ﻌ•^ฅ                        │
│                                                     │ 
│                   Tiktok Bot v1                     │
│                                                     │
│                                                     │
├─────────────────────────────────────────────────────┤
│               Code: Mèo Siêu Nhân                   │
│                      /\_/\                          │
│                    =( °w° )=                        │
│                      )   (  //                      │
│                     (__ __)//                       │
│                                                     │
└─────────────────────────────────────────────────────┘\r\n''')

vidUrl = input("Nhập URL zô đây: ") # video link input
print("[N] Link nãy nhập nè: ", vidUrl)
print("Nhập captcha đi bà nội!")

time.sleep(6)

if mode == 1:
    driver.get("https://zefoy.com/") # driver getting the 
    botViewByMeo() # starting the loop
