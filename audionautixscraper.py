from selenium import webdriver
import urllib.request

# To prevent download dialog
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)                                # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)              #no download manager pop-up
profile.set_preference('browser.download.dir', '/tmp')                                  #default directory (you can change this in urllib)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')            #disable ask to save dialog for all files and save profile

#web driver starts here
browser = webdriver.Firefox(profile) 
browser.get("https://audionautix.com/")                                                 #using audionautix for scraping, replace with any website 
radiobutton=browser.find_element_by_id('slow')                                          #a radio button with the label that the software will click on

#print(radiobutton) prints radio button url 
radiobutton.click() #chooses the option
submitbutton=browser.find_element_by_xpath("//input[@value=' Find Music ']").click()    #finds the form submit button to start the search

#this will open a new page for fast audio tracks
mp3anchors=browser.find_elements_by_class_name("sm2_button")                            #each track is inside a list with the download button class as sm2_button
for mp3anchor in mp3anchors:                                                            #for each of such buttons 
    mp3link=mp3anchor.get_attribute('href')                                             #get the download link
    mp3name=str(mp3link)[30:].replace("%20"," ")                                        #trim to get the file name (replace HTML encoded spaces with normal spaces)
    print("Downloading "+mp3name+ " from "+ mp3link)
    urllib.request.urlretrieve(mp3link,"./Music/Slow/"+mp3name)                         #download the file
    print("Done!")
print('All done!')
