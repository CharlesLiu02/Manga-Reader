from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#chromedriver needed to interact with webpage
driver = webdriver.Chrome()

#opening new webpage with link
driver.get("https://mangakakalot.com/")

def search_manga(manga_title):
    search_bar = driver.find_element_by_id("search_story")
    #setting text in search bar
    search_bar.send_keys(manga_title)
    #hitting enter button to search
    search_bar.send_keys(Keys.RETURN)


def find_manga(manga_title):
    try:
        manga_list = WebDriverWait(driver, 10).until(
            #using xpaths to find inner element containingg list of mangas
            EC.presence_of_element_located((By.XPATH, ".//*[@class='panel_story_list']"))
        )
        #initialize list object with list of mangas
        mangas = manga_list.find_elements_by_class_name("story_item")
        for manga in mangas:
            #get title element
            title = manga.find_element_by_xpath(".//*[@class='story_name']").find_element_by_tag_name("a")
            if manga_title in title.text.lower():
                title.click()
                break
    finally:
        print("hi")


def find_chapter_by_chapter(volume, manga_chapter):
    chapter_list = WebDriverWait(driver, 10).until(
            #using xpaths to find inner element containingg list of mangas
            EC.presence_of_element_located((By.XPATH, ".//*[@class='row-content-chapter']"))
        )
    chapters = chapter_list.find_elements_by_tag_name("li")
    for chapter in chapters:
        name = chapter.find_element_by_tag_name("a")
        string_name = name.text.lower().split(":")[0].strip()
        print(string_name)
        if volume in string_name and manga_chapter in string_name:
            name.click()
            break
            

def find_chapter_by_title(title):
    chapter_list = WebDriverWait(driver, 10).until(
            #using xpaths to find inner element containingg list of mangas
            EC.presence_of_element_located((By.XPATH, ".//*[@class='row-content-chapter']"))
        )
    chapters = chapter_list.find_elements_by_tag_name("li")
    for chapter in chapters:
        name = chapter.find_element_by_tag_name("a")
        string_name = name.text.lower().split(":")[1].strip()
        if title in string_name:
            name.click()
            break

def search(manga_title, volume, chapter, title):
    search_manga(manga_title)
    find_manga(manga_title)
    if title == "":
        find_chapter_by_chapter(volume, chapter)
    else:
        find_chapter_by_title(title)
    

search("naruto", "72", "698.1", "")