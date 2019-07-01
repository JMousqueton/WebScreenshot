#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 @danlopgom
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# DISCLAMER This tool was developed for educational goals. 
# The author is not responsible for using to others goals.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

import time
import sys, os
from tld import get_tld

screenshot_path = ("results")
if not os.path.exists(screenshot_path):
	os.makedirs(screenshot_path)

#Colors
RED = '\033[91m'
ENDC = '\033[0m'
GREEN = '\033[1;32m'
WHITE = '\033[1m'
BOLD = '\033[01m'

# Browser configuration
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--no-default-browser-check")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path='drivers/chromedriver',chrome_options=chrome_options)

# Get the URLs
with open('urls.dat', 'r') as f:
	urls = f.readlines()

# Remove whitespace characters like `\n` at the end of each line
urls = [x.strip() for x in urls]

# Starts
contador=0

for url in urls:
	aux_tld = get_tld(url, as_object=True)
	print("[%s] URL: %s") % (str(contador),url)

	#timestamp=str(time.strftime("%Y%m%d_%H-%M-%S"))
	new_screenshot =('%s/%s_%s-%s.png') % (screenshot_path,str(contador),str(aux_tld.domain),str(aux_tld.suffix))

	driver.get(url)

	# EXAMPLE
	# Finding a XSS attack
	try:
		driver.switch_to.alert.accept()
		print('\t- ' + RED + '[!] XSS FOUND' + ENDC)
	except:
		print('\t- Clean')

	screenshot = driver.save_screenshot(new_screenshot)
	contador=contador+1
	print(40*"=")
driver.quit()
