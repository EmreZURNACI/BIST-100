import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from termcolor import colored


def addSpace(i):
    if (i + 1) % 6 == 0:
        print()


def getShareandValues(hisseler):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--incognito")
    chromeOptions.add_argument("--headless")
    driver = webdriver.Chrome(chromeOptions)
    driver.delete_all_cookies()
    driver.get("https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/default.aspx")
    driver.implicitly_wait(5)

    hisseAdet = len(driver.find_elements(By.XPATH,
                                         "/html/body/form/div[4]/div/div[2]/div/div/div[1]/div/div[3]/div[1]/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr/td[1]"))

    for i in range(hisseAdet):
        hisse = driver.find_elements(By.XPATH,
                                     "/html/body/form/div[4]/div/div[2]/div/div/div[1]/div/div[3]/div[1]/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr/td[1]")[
            i].text
        price = float(driver.find_elements(By.XPATH,
                                           "/html/body/form/div[4]/div/div[2]/div/div/div[1]/div/div[3]/div[1]/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr/td[2]")[
                          i].text.replace('.', '').replace(',', '.'))
        gunlukDegisim = float(driver.find_elements(By.XPATH,
                                                   "/html/body/form/div[4]/div/div[2]/div/div/div[1]/div/div[3]/div[1]/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr/td[3]")[
                                  i].text.replace(",", "."))
        hisseler.append([hisse, price, gunlukDegisim])


def leastValuableStock(liste):
    enDegersizSayi = sys.maxsize
    enDegersizHisse = None
    for i, item in enumerate(liste):
        if enDegersizSayi > liste[i][1]:
            enDegersizSayi = liste[i][1]
            enDegersizHisse = liste[i][0]
    print(colored(f"En ucuz hisse {enDegersizHisse} ==> {enDegersizSayi} TL", 'black', 'on_light_blue', ['bold'],
                  force_color='True'))


def mostValuableStock(liste):
    enDegerliSayi = -1 * sys.maxsize
    enDegerliHisse = None
    for i, item in enumerate(liste):
        if enDegerliSayi < liste[i][1]:
            enDegerliSayi = liste[i][1]
            enDegerliHisse = liste[i][0]
    print(colored(f"En pahalı hisse {enDegerliHisse} ==> {enDegerliSayi} TL", 'black', 'on_light_blue', ['bold'],
                  force_color='True'))


def sortForPercent30Share(liste):
    sirali_liste = sorted(liste, key=lambda x: x[2])[::-1]
    for i in range(30):
        if (sirali_liste)[i][2] > 0:
            print(colored(str((sirali_liste)[i][0]) + "  % " + str((sirali_liste)[i][2]), 'green',
                          'on_black', ['blink'],
                          force_color='True'), end=" ")
        elif (sirali_liste)[i][2] == 0:
            print(colored(str((sirali_liste)[i][0]) + "  % " + str((sirali_liste)[i][2]), 'white',
                          'on_black', ['blink'],
                          force_color='True'), end=" ")
        else:
            print(colored(str((sirali_liste)[i][0]) + "  % " + str((sirali_liste)[i][2]), 'red',
                          'on_black', ['blink'],
                          force_color='True'), end=" ")
        addSpace(i)


hisseler = list()
getShareandValues(hisseler)
print("Python Borsa İstanbul Uygulamasına Hoşgeldiniz")
kontrol=True
print(
        " \n 1. En Pahalı Hisse \n 2. En Ucuz Hisse \n 3. En Çok Hacim Yapan 30 Hisse \n 4. Hisseler \n 5. Çıkmak için 'q'")
while kontrol :
    secim = input("Hangi İşlemi Yapmak İstersiniz : ")
    if secim == '1':
        mostValuableStock(hisseler)
    elif secim == '2':
        leastValuableStock(hisseler)
    elif secim == '3':
        sortForPercent30Share(hisseler)
    elif secim == '4':
        for i, item in enumerate(hisseler):
            print(item[0], item[1],end="     ")
            if (i+1)%7==0:print()
            print()
    elif secim == 'q' or secim=="Q":
        print("Çıkış Yapıldı")
        kontrol=False
