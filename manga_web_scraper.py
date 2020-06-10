from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tkinter import *
from entry_with_placeholder import *


def search_mangakakalot(manga_title):
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
        return_list = []
        try:
            manga_list = WebDriverWait(driver, 10).until(
                #using xpaths to find inner element containingg list of mangas
                EC.presence_of_element_located((By.XPATH, ".//*[@class='panel_story_list']"))
            )
            #initialize list object with list of mangas
            mangas = manga_list.find_elements_by_class_name("story_item_right")
            for manga in mangas:
                #get title element
                title = manga.find_element_by_xpath(".//*[@class='story_name']").find_element_by_tag_name("a")
                if manga_title in title.text.lower():
                    return_list.append(manga)
            return return_list
        finally:
            print("hi")


    def find_chapter_by_chapter(volume, manga_chapter):
        return_list = []
        chapter_list = WebDriverWait(driver, 10).until(
                #using xpaths to find inner element containingg list of mangas
                EC.presence_of_element_located((By.XPATH, ".//*[@class='row-content-chapter']"))
            )
        chapters = chapter_list.find_elements_by_tag_name("li")
        for chapter in chapters:
            name = chapter.find_element_by_tag_name("a")
            string_name = name.text.lower().split(":")[0].strip()
            if volume in string_name and manga_chapter in string_name:
                return_list.append(chapter)
        return return_list
                

    def find_chapter_by_title(title):
        return_list = []
        chapter_list = WebDriverWait(driver, 10).until(
                #using xpaths to find inner element containingg list of mangas
                EC.presence_of_element_located((By.XPATH, ".//*[@class='row-content-chapter']"))
            )
        chapters = chapter_list.find_elements_by_tag_name("li")
        for chapter in chapters:
            name = chapter.find_element_by_tag_name("a")
            string_name = name.text.lower().split(":")[1].strip()
            if title in string_name:
                return_list.append(chapter)
        return return_list
        
    def search_for_manga(volume, chapter, title):
        if title == "":
            find_chapter_by_chapter(volume, chapter)
        else:
            find_chapter_by_title(title)

    search_manga(manga_title)
    return find_manga(manga_title)
    
def initializeListBox(listbox, mangas):
    for manga in mangas:
        listbox.insert(END, manga.find_element_by_tag_name("a").text)
        

def search(user_input):
    mangas = []
    mangas += search_mangakakalot(user_input)
    manga_results_list_box = Listbox(content_frame)
    manga_results_list_box.grid(row=2, columnspan=2)
    initializeListBox(manga_results_list_box, mangas)


def get_search():
    user_input = search_bar_entry.get()
    search(user_input)


#create a blank window
root_window = Tk()

#creating a new frame
title_frame = Frame(root_window)
content_frame = Frame(root_window)
title_frame.grid()
content_frame.grid(row=1)

main_title_label = Label(title_frame, text="Manga Reader")
search_bar_entry = EntryWithPlaceholder(title_frame, placeholder="Search mangas")
search_button = Button(title_frame, text="Search", command=get_search)
main_title_label.grid(row=0, columnspan=2)
search_bar_entry.grid(row=1, )
search_button.grid(row=1, column=1)



#makes window constantly stay on the screen
root_window.mainloop()