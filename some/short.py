
import requests
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
import re 
import contextlib
from langdetect import detect
import time
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager



options = wb.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser  = wb.Chrome(options=options)
# url_signin = 'https://www.linkedin.com/'
# search_tag =  'data scientist'

def start_linkedin(username,password):
#    self.browser.get("https://linkedin.com/uas/login")
#def login(driver): #, username, password):
        # browser  = wb.Chrome()
        print("\nLogging in.....\n \nPlease wait :) \n ")
        browser.get("https://www.linkedin.com/")
        try:
            user_field = browser.find_element(By.ID, "session_key")
            pw_field = browser.find_element(By.ID,"session_password")
            login_button = browser.find_element(By.CLASS_NAME,"sign-in-form__submit-button")
            user_field.send_keys(username)
            user_field.send_keys(Keys.TAB)
            time.sleep(1)
            pw_field.send_keys(password)
            time.sleep(3)
            login_button.click()
        except Exception:
            print("TimeoutException! Username/password field or login button not found on linkedin.com")

def search_job(search_tag,location):
        # browser  = wb.Chrome()
        jobsearch = browser.get(f"https://www.linkedin.com/jobs/search/?&keywords={search_tag}&location={location}")
        time.sleep(3)


        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

       
        job_list = browser.find_elements(By.XPATH, '//ul[@class="jobs-search-results__list list-style-none"]//a')
        job_linksz =[job.get_property('href') for job in job_list]
        job_links  = []

        for item in job_linksz:
                m = re.compile(r'jobs/view/*')
                if m.findall(item) != []:
                        job_links.append(item)


        return list(sorted(set(job_links)))


def save_the_jobs(job_link):
	dicts = {
    'position name':[],
    'workplace':[],
    'number of employees':[],
    'location':[],
    'description':[],
    'company name':[],
    'working salary/info':[],
	'number of applicants':[],
	'ad time':[],
	'hiring status':[],
	'corresponds name':[],
	'connection is able':[],
	'ad language':[],
	'job link' : [],
	'easy apply':[],
	# 'easy apply':[],some ads include pre questions before uploading cv and appply buttton, if redirecting to the company website pop up the link
	
    }

	for i in range(len(job_link[:3])):
		# i.click()
		time.sleep(1)
		dicts['job link'].append(job_link[i])
		try:
			k = browser.get(job_link[i])
		# except b:
		# 	browser.find_element(By.XPATH, '//span[@class="t-black--light"]').click()
		except Exception:
			a = 3
		try:
			k = browser.find_element(By.XPATH, '//footer[@class="artdeco-card__actions"]')
			k.click()
		# except Exception:
		# 	browser.find_element(By.XPATH, '//span[@class="artdeco-button__text"]').click()
		except:
			a = 3
		try:
			# postion_name = browser.find_element(By.XPATH, "//h1[@class='t-24 t-bold']").text
			dicts['position name'].append(browser.find_element(By.XPATH, "//h1[@class='t-24 t-bold']").text)
		except:
			dicts['position name'].append('None')
		try:
			dicts['working salary/info'].append(browser.find_elements(By.XPATH, '//li[@class="jobs-unified-top-card__job-insight"]')[0].text)
		except Exception:
			dicts['working salary/info'].append('None')
		try:
			dicts['number of employees'].append(browser.find_elements(By.XPATH, '//li[@class="jobs-unified-top-card__job-insight"]')[1].text.split('.',)[0].split(' ')[0])
		except Exception:
			dicts['number of employees'].append('None')
		try:
			x = browser.find_element(By.XPATH, '//div[@id="job-details"]//span')
			# get ul for requirements abilities tasks etc...

			dicts['description'].append(x.text)
			dicts['ad language'].append(detect(x.text))
		except Exception:
			dicts['description'].append('None')
			
		try:
			locnameidi = browser.find_element(By.XPATH, '//div[@class="mt2"]')
		except Exception:
			locnameidi = 'None'
		try:
			dicts['location'].append(locnameidi.find_element(By.XPATH, '//span[@class="jobs-unified-top-card__bullet"]').text.strip()) 
		except Exception:
			dicts['location'].append('None')
		if locnameidi != 'None':
			try:
				dicts['ad time'].append(locnameidi.find_element(By.XPATH, '//span[@class="jobs-unified-top-card__subtitle-secondary-grouping t-black--light"]//span').text.split(' ago')[0])
			except Exception:
				dicts['ad time'].append('None')
			try:
				dicts['company name'].append(locnameidi.find_element(By.XPATH, '//span[@class="jobs-unified-top-card__company-name"]//a').text.strip())
			except Exception:
				dicts['company name'].append('None')
			try:
				dicts['workplace'].append(locnameidi.find_element(By.XPATH, '//span[@class="jobs-unified-top-card__workplace-type"]').text.strip())
			except:
				dicts['workplace'].append('None')
			try:
				dicts['number of applicants'].append(locnameidi.find_element(By.XPATH, '//span[@class="jobs-unified-top-card__bullet"]//span').text)
			except Exception:
				dicts['number of applicants'].append(0)
		else:
			continue
		try:
			dicts['connection is able'].append(browser.find_element(By.XPATH, '//li[@class="jobs-unified-top-card__job-insight"]//a[@class="app-aware-link"]').text)
		except Exception:
			dicts['connection is able'].append(0)
		try:
			dicts['corresponds name'].append(browser.find_element(By.XPATH,'//a[@data-control-name="jobdetails_profile_poster"]/p').text)
		except:
			dicts['corresponds name'].append('None')

		d= browser.find_element(By.XPATH, '//div[@class="jobs-apply-button--top-card"]//span')
		# easy_apply_button = d.click()
		j = ["True" if d.text == 'Easy Apply' else "False"]
		[dicts['easy apply'].append('True') if j == "True" else dicts['easy apply'].append('False')]
		
		c = browser.find_elements(By.XPATH, '//li[@class="jobs-unified-top-card__job-insight"]//span')
		l = ["True" if m.text == 'Actively recruiting' else "False "for m in c]
		[dicts['hiring status'].append("True") if "True" in l else dicts['hiring status'].append("False")]
			
	return dicts

def dataframe_editor(df):

    df['number of applicants'] = (df['number of applicants'].apply(lambda x: int(x.split()[0]) if x != 0 else x))
    df['connection is able'] = (df['connection is able'].apply(lambda x: int(x.split()[0]) if x != 0 else x))

    return df

def make_clickable(val):
    return f'<a target="blank" href="{val}">click to see link</a>'

def text_evaluater(text):
    pass