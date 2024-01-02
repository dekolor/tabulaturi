from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os.path

#modifica linia de mai jos pentru folderul in care se vor salva cantecele
save_path = "D:/cod/github/tabulaturi/versuri/"

browser = webdriver.Chrome(executable_path=r"chromedriver.exe")

#url = "https://www.tabulaturi.ro/litere/0"
url = "https://www.tabulaturi.ro"

browser.get(url) #a se inlocui link-ul

browser.find_element_by_id("btnAcceptCookies").click()

lista_litere = [
 "https://www.tabulaturi.ro/litere/0",
 "https://www.tabulaturi.ro/litere/1",
 "https://www.tabulaturi.ro/litere/2", 
 "https://www.tabulaturi.ro/litere/4", 
 "https://www.tabulaturi.ro/litere/5", 
 "https://www.tabulaturi.ro/litere/6", 
 "https://www.tabulaturi.ro/litere/7", 
 "https://www.tabulaturi.ro/litere/8", 
 "https://www.tabulaturi.ro/litere/9", 
 "https://www.tabulaturi.ro/litere/10", 
 "https://www.tabulaturi.ro/litere/11", 
 "https://www.tabulaturi.ro/litere/13", 
 "https://www.tabulaturi.ro/litere/14", 
 "https://www.tabulaturi.ro/litere/15", 
 "https://www.tabulaturi.ro/litere/16", 
 "https://www.tabulaturi.ro/litere/17", 
 "https://www.tabulaturi.ro/litere/18", 
 "https://www.tabulaturi.ro/litere/19", 
 "https://www.tabulaturi.ro/litere/20",
 "https://www.tabulaturi.ro/litere/21", 
 "https://www.tabulaturi.ro/litere/22", 
 "https://www.tabulaturi.ro/litere/23", 
 "https://www.tabulaturi.ro/litere/24", 
 "https://www.tabulaturi.ro/litere/25", 
 "https://www.tabulaturi.ro/litere/26", 
 "https://www.tabulaturi.ro/litere/27", 
 "https://www.tabulaturi.ro/litere/28", 
 "https://www.tabulaturi.ro/litere/30", 
 "https://www.tabulaturi.ro/litere/31"]

for d in lista_litere:
	browser.get(d)
	artisti = browser.find_elements_by_css_selector(".table-responsive > table > tbody > tr > td > a")
	linkuri_artisti = []
	for z in artisti:
		linkuri_artisti.append(z.get_attribute("href"))
		#print(z.get_attribute("href"))
	for e in linkuri_artisti:
		browser.get(e)
		randuri = browser.find_elements_by_css_selector("#recordsetTabs > table > tbody > tr > td > a")
		linkuri = []
		piese = []
		for x in randuri:
		    #print(x.get_attribute("href"))
		    linkuri.append(x.get_attribute("href"))
		    artist = browser.find_element_by_css_selector(".card-header > h1")
		    artistul = artist.text
		for y in linkuri:
		    browser.get(y)
		    try:
		    	titlu = browser.find_element_by_css_selector(".card-header > h1")
		    except:
		    	continue
		    #print(titlu.text)
		    versuri = browser.find_element_by_css_selector(".tab-text")
		    tabid = browser.find_element_by_css_selector("#tabID")
		    tabid = tabid.get_attribute("value")
		    if(titlu.text[-1]=='?'):
		    	titlusalvat = titlu.text[:-1]
		    	#print("am eliminat ultimul caracter")
		    else:
		    	titlusalvat = titlu.text
		    # titlusalvat = titlu.text
		    fullpath = os.path.join(save_path, titlusalvat.replace('"',"'").replace("/", " - ").replace("*", "-") + " (" + tabid + ").txt")
		    #print("path:" + fullpath)
		    f = open(fullpath, "wb")
		    f.write(versuri.text.encode('utf8'))
		    f.close()
		    #print("---------------------------")

browser.close()