import time													#import time for delay
import datetime												#import datetime to check for Mondays
import random												#import random for randomizing search terms
import sys
from splinter.browser import Browser 						#import Splinter package

print 'Bing! Script v. 1.2 \nAuthor: Long Tran\nLast Updated: Jul 8, 2014 9:09:52\n\n---------------------------------------------------------------'
maxCount = 30												#max number of searches
count = 0													#number of searches
i = 0														#index variable for array of logins
pwd = '#PUT PASSWORD HERE'									#password
sentence1 = "Mark Cuban (born July 31, 1958)[3] is an American businessman, investor, and owner of the NBA's Dallas Mavericks,[4] Landmark Theatres, and Magnolia Pictures, and the chairman of the HDTV cable network AXS TV.[5] He is also a \"shark\" investor on the television series Shark Tank. In 2011 Cuban wrote an e-book, How to Win at the Sport of Business, in which he chronicles his life experiences in business and sports."
sentence2 = "Donald John Trump, Sr. (born June 14, 1946) is an American business magnate, investor, television personality and author. He is the chairman and president of The Trump Organization and the founder of Trump Entertainment Resorts.[1] Trump's extravagant lifestyle, outspoken manner, and role on the NBC reality show The Apprentice have made him a well-known celebrity who was No. 17 on the 2011 Forbes Celebrity 100 list."
searchFrom1 = sentence1.split(' ')
searchFrom2 = sentence2.split(' ')

if len(sys.argv) == 2:
	loginList = open(sys.argv[1])
else:
	loginList = open('login.txt')							#open the the text file
credentials = loginList.readlines()							#read all the credentials in the text file


if datetime.datetime.today().weekday() == 0:				#if today is Monday
	maxCount = 60

while i < len(credentials):									#for each login credential
	b = Browser('chrome')									#create a browser instance
	loginURL = 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=12&ct=1400194110&rver=6.0.5286.0&wp=MBI&wreply=http:%2F%2Fwww.bing.com%2FPassport.aspx%3Frequrl%3Dhttp%253a%252f%252fwww.bing.com%252f&lc=1033&id=264960'
	b.visit(loginURL)										#login URL


	b.find_by_name('login').fill(credentials[i])			#find form using name ID (username)
	b.find_by_name('passwd').fill(pwd)						#find form using name ID (password)
	b.find_by_name('SI').click()							#find button using name ID (sign in button)

	time.sleep(5)											#delay 5s before starting to search

	while count < maxCount:									#perform the searches
		stub1 = searchFrom1[random.randrange(0, len(searchFrom1))]
		stub2 = searchFrom2[random.randrange(0, len(searchFrom2))]
		url = "http://www.bing.com/search?=setmkt=en-US&q="
		url += '%s+%s' % (stub1, stub2)
		b.visit(url)
		time.sleep(1)
		count += 1


	pwd = 'Bingbing'										#quick hack for pwd change
	count = 0

	time.sleep(5)											#delay 5s before reporting

	b.visit('https://www.bing.com/rewards/dashboard')
	currentPointString = b.find_by_css("div.credits").first.value
	print 'Total credits for %s: %s' % (credentials[i], currentPointString)
	print 'With mobile: %d days.' % ((200 - int(currentPointString))/25 + 1)
	print 'Without mobile: %d days.' % ((200 - int(currentPointString))/15 + 1)


	b.quit()

	print '---------------------------------------------------------------'
	i += 1

print 'Script completed.'
