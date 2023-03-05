import requests
from bs4 import BeautifulSoup
import re
import webbrowser
import searcher

import webview

anime_code, anime_name = searcher.formator()

url = "https://gogoanime.wiki/"+anime_code

def get_gogo(url):
	# creating request object
	req = requests.get(url)
	  
	# creating soup object
	data = BeautifulSoup(req.text, 'html.parser')
	  
	# finding all li tags in ul and printing the text wimport reithin it
	data1 = data.find_all('iframe')

	link=re.findall('"([^"]*)"', str(data1))
	linkgogo  = link[5]
	return (f"https:{linkgogo}")

#Open in webview window
def toggle_fullscreen(window):
    window.toggle_fullscreen()

window = webview.create_window(anime_name, get_gogo(url))
webview.start(toggle_fullscreen, window)
