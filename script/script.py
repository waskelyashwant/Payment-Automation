from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import csv
import subprocess
import os
import sys

# total_no_of_apps = sys.argv[1]
total_no_of_apps = 670

# print(total_no_of_apps)

dcs = []
dc = {}
dc['platformName'] = 'android'
dc['deviceName'] = 'Redmi 9 Power'
dc['noReset'] = 'true'
dc['appPackage'] = 'com.android.settings'
dc['appActivity'] = 'com.android.settings.Settings'
dc['realDevice'] = 'true'
dc['automationName'] = 'UiAutomator2'
dcs.append(dc)

passwords = ['5126', '0616', '9828', '9389', '1234']

card_data = pd.read_excel(r'script/data2.xlsx') 
card_df = pd.DataFrame(card_data)
card_length = len(card_df.index)


numbers={"1": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.Button[1]",
         "2": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.Button[2]",
         "3": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.Button[3]",
         "4": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.Button[1]",
         "5": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.Button[2]",
         "6": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.Button[3]",
         "7": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.Button[1]",
         "8": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.Button[2]",
         "9": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.Button[3]",
         "0": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[4]/android.widget.Button[2]"}

dr=None
# total_no_of_apps = sys.argv[1]
data = pd.read_excel(r'script/data.xlsx')
df = pd.DataFrame(data)
length = len(df.index)

location = "Bill File updated.csv"
# location = "Bill File updated.csv"
file = None
thewriter=None
fieldnames = ['Due Date', 'Description', 'Biller Name', 'K Number', 'Amount', 'Status', 'Reason', 'Biller name on bill', 'Amount on bill','Reference no.','App no.']

if os.path.exists(location)==False:
	file = open(location, 'w',newline='')
	thewriter = csv.DictWriter(file, fieldnames=fieldnames)
	thewriter.writeheader()
else:
	file = open(location, 'a',newline='')
	thewriter = csv.DictWriter(file, fieldnames=fieldnames)

file.close()

close=1

bill_pay_value = 0
elec_value = 0

card_used = []


def k_number(k):
	k_num = str(df.iloc[k]['K Number'])
	k_num = k_num.split('.')[0]
	return k_num

def update_app_no(k,n):
	bn = df.iloc[k]['Biller Name']
	if bn==None:
		bn="No biller name"

	f = open("app_no.txt", "w")
	ans = bn +" "+ str(k_number(k))+ " " + str(n)
	f.write(ans)
	f.close()

k_app = 'script/k_and_app.csv'
if os.path.exists(k_app)==False:
	app_no=1
	k=0
	filek = open(k_app, 'w',newline='')
	thewriter = csv.DictWriter(filek, fieldnames=['Last K Number', 'Last i'])
	thewriter.writeheader()
	thewriter.writerow({'Last K Number':k, 'Last i':app_no})
	filek.close()
	update_app_no(k,app_no)
else:
	datak = pd.read_csv(k_app) 
	dfk = pd.DataFrame(datak)
	app_no = int(dfk.iloc[0]['Last i']) + 1
	k = int(dfk.iloc[0]['Last K Number']) + 1
	update_app_no(k,app_no)

def apps(ind):
	x = ind%15
	if x==0:
		x=15
	return '(//android.widget.ImageView[@content-desc="PayZapp+"])[' + str(x) + ']'

def get_card_index():
	flag=0
	x = 0
	for l in range(0,card_length):
		if str(card_df.iloc[l]['Status'])=="Active":
			if l not in card_used:
				flag=1
				card_index=l

	if flag==1:
		return card_index
	else:
		return -1


def change_card_details(card_index):
	change_card_details.c_alias = str(card_df.iloc[card_index]['Card Alias'])
	change_card_details.c_number = str(card_df.iloc[card_index]['Card Number'])
	change_card_details.ex_mm = "0" + str(card_df.iloc[card_index]['Expiry Month'])
	change_card_details.ex_year = str(card_df.iloc[card_index]['Expiry Year'])
	change_card_details.c_hold_name = str(card_df.iloc[card_index]['Card Holder Name'])
	change_card_details.pin_no = str(card_df.iloc[card_index]['Pin'])
	# print("change_card_details")

def swipe(t):
	print("Swipe")
	for n in range(0,t):
		time.sleep(4)
		print("s2")
		subprocess.call("adb shell input swipe 548 1230 537 695")
	time.sleep(4)
  

def login(passw):
	x=app_no%100
	if x==0:
		x = 6
	t=int((x)/15)
	if x%15==0:
		t=t-1
	print("No of times to swipe = ", t)
	# t = input()
	swipe(t)
	print("Swipe complete")
	
	if app_no%100==0:
		el1 = dr.find_element_by_xpath(apps(100))
		el1.click()
	else:
		el1 = dr.find_element_by_xpath(apps(app_no%100))
		el1.click()
	
	for j in passw:
		el = dr.find_element_by_xpath(numbers[j])
		el.click()

	el6 = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/login_button")
	el6.click()

def logout():
	option = dr.find_element_by_xpath('//android.widget.ImageView[@content-desc="More options"]')
	option.click()

	logout = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
	logout.click()

	time.sleep(3)
	dr.back()

def billPay():
	# try:
	# 	if dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.ImageView"):
	# 		pass
	# except:
	# 	print("try")
	# 	ok=dr.find_element_by_id("android:id/button1")
	# 	ok.click()
	# 	ok=dr.find_element_by_id("android:id/button1")
	# 	ok.click()
	# 	print("ok clicked")


	bill_pay_value = 0
	try:
		bill_pay = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.ImageView")
		bill_pay.click()
		elec()
		bill_pay_value = 1
	except:
		logout()
		bill_pay_value=0

	return bill_pay_value


def elec():
	elec_value = 0
	elec = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/image_electricity")
	elec.click()
	time.sleep(2)
	while(1):
		try:
			if dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.widget.EditText"):
				return
		except:
			time.sleep(5)
			elec = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/image_electricity")
			elec.click()
			continue
		time.sleep(2)
	# try:
	# 	elec = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/image_electricity")
	# 	elec.click()
	# 	time.sleep(2)
	# 	while(1):
	# 		try:
	# 			if dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.widget.EditText"):
	# 				return
	# 		except:
	# 			time.sleep(5)
	# 			elec = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/image_electricity")
	# 			elec.click()
	# 			continue
	# 	# else:
	# 	# 	back()
	# 	# 	x = billPay()
	# except:
	# 	dr.back()
	# 	time.sleep(5)
	# 	x = billPay()

def descr(k):
	description = df.iloc[k]['Description']
	string = description.split(" ")
	distributor = ""
	for i in range(0, len(string)-1):
		distributor+=string[i]+" "

	return distributor


def distributor_func(k):
	dist_name = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.widget.EditText")
	dist_name.send_keys(descr(k))
	dist_name.click()
	time.sleep(5)
	operator = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.widget.ListView/android.view.View[1]/android.view.View[2]")
	operator.click()

def k_number_input(k):
	k_num_input = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[2]/android.widget.EditText")
	k_num_input.send_keys(k_number(k))

	confirm = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[3]/android.widget.Button")
	confirm.click()
	time.sleep(8)

def goback():
	dr.back()
	time.sleep(0.5)
	dr.back()
	time.sleep(0.5)
	dr.back()
	

def pay_now_page(k):
	biller_name = df.iloc[k]['Biller Name']
	amount_csv = df.iloc[k]['Amount']
	print("Pay now page")
	time.sleep(3)
	customer_name = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[5]/android.view.View[3]").text
	amount = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[6]/android.widget.EditText").text
	print("touch action")
	amount=str(amount)
	amount = amount.split('.')[0]

	subprocess.call("adb shell input swipe 601 1197 545 548")

	# touch = TouchAction(dr)
	# touch.press(x=601, y=1197)   
	# touch.move_to(x=545, y=548)
	# touch.wait(0.01)
	# touch.release()
	# touch.perform()
	print("done sliding")

	if biller_name!=None:
		biller_name = biller_name.split(' ')[0]

	customer_name = customer_name.split(' ')[0]

	# time.sleep(5)

	x = 0
	# if biller_name == customer_name:
	print(biller_name)
	print(customer_name)
	print(int(amount))
	print(int(amount_csv))
	if str(amount) == str(amount_csv):
		pay_now = dr.find_element_by_xpath ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[7]/android.widget.Button")
		pay_now.click()
		print("passed pay button")
		time.sleep(7)
		x = 1
		return [1, customer_name, amount]

	if x == 0:
		return [0, customer_name, amount]

def directedit():
	card_no = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText")
	card_no.send_keys(change_card_details.c_number)

	ex_month = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText")
	ex_month.send_keys(change_card_details.ex_mm)

	ex_year = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText[2]")
	ex_year.send_keys(change_card_details.ex_year)

	holder_name = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText[2]")
	holder_name.send_keys(change_card_details.c_hold_name)

	try:
		approve = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[7]")
		approve.click()

		time.sleep(5)
		approve = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[7]")
		approve.click()
		print("approve 7")
	except:
		try:
			approve = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[8]")
			approve.click()

			time.sleep(5)
			approve = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[8]")
			approve.click()
			print("approve 8")
		except:
			approve = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[6]")
			approve.click()

			time.sleep(5)

			approve = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[6]")
			approve.click()
			print("approve 6")


def editcardbutton2():
	card_alias = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText")
	card_alias.send_keys(change_card_details.c_alias)
	
	card_no = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText[2]")
	card_no.send_keys(change_card_details.c_number)

	ex_month = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText")
	ex_month.send_keys(change_card_details.ex_mm)

	expiry_year = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText[2]")	
	expiry_year.send_keys(change_card_details.ex_year)

	holder_name = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText[3]")
	holder_name.send_keys(change_card_details.c_hold_name)

	add_card = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button")
	add_card.click()
	# print("editcardbutton2")

def editcardbutton():
	edit_card = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView")
	edit_card.click()

	time.sleep(2)

	try:
		if dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText"):
			print("Edit card button")
			editcardbutton2()
	except:
		delete_card = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView[3]")
		delete_card.click()

		yes = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]")
		yes.click()
		time.sleep(2)
		editcardbutton2()

		# time.sleep(3)

		# approve = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[7]")
		# approve.click()


def close_app():
	# subprocess.call("adb shell input keyevent KEYCODE_APP_SWITCH",shell=True)
	# time.sleep(1)
	# clear = dr.find_element_by_id("com.android.systemui:id/clearAnimView")
	# print(clear)
	# time.sleep(3)
	try:
		# clear.click()
		# time.sleep(5)
		subprocess.call("adb shell input keyevent KEYCODE_APP_SWITCH",shell=True)
		time.sleep(2)
		subprocess.call("adb shell input keyevent DEL")
		time.sleep(3)
	except:
		subprocess.call("adb shell input keyevent DEL")

	# subprocess.call("adb shell input keyevent KEYCODE_APP_SWITCH",shell=True)
	# time.sleep(2)
	subprocess.call("adb shell input keyevent 3")

	print("Clear Action")

	time.sleep(2)
	dr.back()
	print("Back")
	# dr.quit()
	time.sleep(2)

	

shortcut = {"1 - 100":'//android.widget.RelativeLayout[@content-desc="1 - 100"]',
			"101 - 200":'//android.widget.RelativeLayout[@content-desc="101 - 200"]',
			"201 - 300":'//android.widget.RelativeLayout[@content-desc="201 - 300"]',
			"301 - 400":'//android.widget.RelativeLayout[@content-desc="301 - 400"]',
			"401 - 500":'//android.widget.RelativeLayout[@content-desc="401 - 500"]',
			"501 - 600":'//android.widget.RelativeLayout[@content-desc="501 - 600"]',
			"601 - 670":'//android.widget.RelativeLayout[@content-desc="601 - 670"]'}

def ranges(n):
	print(shortcut["1 - 100"])
	if n >= 1 and n <= 100:
		return shortcut["1 - 100"]
	elif n >= 101 and n <= 200:
		return shortcut["101 - 200"]
	elif n >= 201 and n <= 300:
		return shortcut["201 - 300"]
	elif n >= 301 and n <= 400:
		return shortcut["301 - 400"]
	elif n >= 401 and n <= 500:
		return shortcut["401 - 500"]
	elif n >= 501 and n <= 600:
		return shortcut["501 - 600"]
	elif n >= 601 and n <= total_no_of_apps:
		return shortcut["601 - 670"]


exit = 0
card_index = get_card_index()
card_used.append(card_index)
change_card_details(card_index)

dr=None
dr = webdriver.Remote('http://localhost:4723/wd/hub', dcs[0])
time.sleep(2)
start=1
dr.back()

while k<length:
	start=0
	print("start - ", start)
	print(card_index)
	print(change_card_details.c_alias, " " , change_card_details.c_hold_name, " ", change_card_details.c_number)
	# try:
	if app_no%5==0 and start==0:
		print("New driver")
		if dr:
			dr.quit()
		dr=None
		dr = webdriver.Remote('http://localhost:4723/wd/hub', dcs[0])
		time.sleep(3)
		dr.back()

	print("app_no = ", app_no)
	print("k = ", k)
	close=0
	dr.implicitly_wait(20)

	short = dr.find_element_by_xpath(ranges(app_no)).click()
	time.sleep(3)
	print("Start")

	passw = None
	passw = "1234"
	print(passw)
	z=0

	x = 0
	otp=0
	while(1):
		login(passw)
		time.sleep(8)
		print("processing ok")
		
		try:
			print("try")
			ok=dr.find_element_by_id("android:id/button1")
			ok.click()
			ok=dr.find_element_by_id("android:id/button1")
			ok.click()
			print("ok clicked")
		except:
			print("Really")
			pass

		# try:
		# 	if dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.ImageView"):
		# 		pass
		# except:
		# 	if dr.find_element_by_id("com.enstage.wibmo.hdfc:id/main_mbOtp_edit"):
		# 		otp=1
		# 		filek = open(k_app, 'w',newline='')
		# 		thewriter1 = csv.DictWriter(filek, fieldnames=['Last K Number', 'Last i'])
		# 		thewriter1.writeheader()
		# 		thewriter1.writerow({'Last K Number':k-1, 'Last i':app_no})	
		# 		filek.close()
		# 		app_no+=1
		# 		update_app_no(k, app_no)
		# 		break

		try:
			if dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.ImageView"):
				pass
		except:
			# try:
				# el2 = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/buttonNegative")
			filek = open(k_app, 'w',newline='')
			thewriter1 = csv.DictWriter(filek, fieldnames=['Last K Number', 'Last i'])
			thewriter1.writeheader()
			thewriter1.writerow({'Last K Number':k-1, 'Last i':app_no})
			filek.close()
			app_no+=1
			update_app_no(k, app_no)
			close_app()
			z=1
			break
			# except:
			# 	filek = open(k_app, 'w',newline='')
			# 	thewriter1 = csv.DictWriter(filek, fieldnames=['Last K Number', 'Last i'])
			# 	thewriter1.writeheader()
			# 	thewriter1.writerow({'Last K Number':k-1, 'Last i':app_no})	
			# 	filek.close()
			# 	app_no+=1
			# 	update_app_no(k, app_no)
			# 	close_app()
			# 	z=1
			# 	break

		# time.sleep(5)

		x = billPay()
		if x==1:
			break

	# if otp==1:
	# 	close_app()
	# 	continue
	
	if z==1:
		print("App crashed or device verification or no kyc")
		continue

	# close_app()
	# app_no+=1
	# continue

	lis = []
	l=0
	while(1):
		if close==3:
			close_app()
			break
		distributor_loop = 1
		kloop=1
		if x==0:
			elec()
		while(1):
			distributor_func(k)
			while(1):
				k_number_input(k)
				invalid = ""
				try:
					customer_name = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[5]/android.view.View[3]")
				except:
					try:
						invalid = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[1]/android.view.View/android.widget.ListView/android.view.View/android.widget.TextView")
					except:
						break


				if invalid != "":
					print("invalid k number")
					kloop=0
					file = open(location, 'a',newline='')
					thewriter = csv.DictWriter(file, fieldnames=fieldnames)
					thewriter.writerow({'Due Date':df.iloc[k]['Due Date'],	'Description':df.iloc[k]['Description'], 'Biller Name':df.iloc[k]['Biller Name'], 'K Number':df.iloc[k]['K Number'],'Amount':df.iloc[k]['Amount'],	'Status': "Not paid", 'Reason':"Wrong K number", 'Biller name on bill':"", 'Amount on bill':"", 'Reference no.':"",'App no.':""})
					file.close()
					filek = open(k_app, 'w',newline='')
					thewriter1 = csv.DictWriter(filek, fieldnames=['Last K Number', 'Last i'])
					thewriter1.writeheader()
					thewriter1.writerow({'Last K Number':k, 'Last i':app_no})
					filek.close()
					update_app_no(k,app_no)
					k=k+1
				break

			break

		if kloop==0:
			dr.back()
			time.sleep(0.3)
			dr.back()
			x=0
			close+=1
			continue

		try:
			if dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[5]/android.view.View[1]"):
				lis = pay_now_page(k)
				if lis[0] == 0:
					distributor_loop = 0
				elif lis[0] == 1:
					distributor_loop = 1

		except:
			# oops = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[2]")
			# print(dr.page_source)
			reason = ""
			try:
				print("Reason 2")
				reason = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]")
			except:
				try:
					print("Reason 3")
					reason = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]")
				except:
					print("Reason 4")
					reason = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]")

			cont = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.widget.Button")
			cont.click()
			time.sleep(3)
			file = open(location, 'a',newline='')
			thewriter = csv.DictWriter(file, fieldnames=fieldnames)
			thewriter.writerow({'Due Date':df.iloc[k]['Due Date'],	'Description':df.iloc[k]['Description'], 'Biller Name':df.iloc[k]['Biller Name'], 'K Number':df.iloc[k]['K Number'],'Amount':df.iloc[k]['Amount'],	'Status': "Not paid", 'Reason':reason.text, 'Biller name on bill':"", 'Amount on bill':"", 'Reference no.':"",'App no.':""})
			print(df.iloc[k]['Due Date'], "    ", df.iloc[k]['Description'], "    ", df.iloc[k]['Biller Name'], "    ", df.iloc[k]['K Number'],  "    ", df.iloc[k]['Amount'], "    Not paid    ",  reason.text, "    ", "    ", "    ", "    ", "    ", "     ", "    ")
			file.close()

			filek = open(k_app, 'w',newline='')
			thewriter1 = csv.DictWriter(filek, fieldnames=['Last K Number', 'Last i'])
			thewriter1.writeheader()
			thewriter1.writerow({'Last K Number':k, 'Last i':app_no-1})
			filek.close()

			update_app_no(k,app_no)

			k=k+1
			close+=1
			continue


		if distributor_loop == 0:
			file = open(location, 'a',newline='')
			thewriter = csv.DictWriter(file, fieldnames=fieldnames)
			thewriter.writerow({'Due Date':df.iloc[k]['Due Date'],	'Description':df.iloc[k]['Description'], 'Biller Name':df.iloc[k]['Biller Name'], 'K Number':df.iloc[k]['K Number'],'Amount':df.iloc[k]['Amount'],	'Status': "Not paid", 'Reason':"Either biller name or amount does not match", 'Biller name on bill':lis[1], 'Amount on bill':lis[2], 'Reference no.':"",'App no.':""})
			print(df.iloc[k]['Due Date'], "    ", df.iloc[k]['Description'], "    ", df.iloc[k]['Biller Name'], "    ", df.iloc[k]['K Number'],  "    ", df.iloc[k]['Amount'], "    Not paid    ", "Either biller name or amount does not match    ", lis[1], "    ", lis[2], "    ", "     ", "    ")
			file.close()

			filek = open(k_app, 'w',newline='')
			thewriter1 = csv.DictWriter(filek, fieldnames=['Last K Number', 'Last i'])
			thewriter1.writeheader()
			thewriter1.writerow({'Last K Number':k, 'Last i':app_no})
			filek.close()

			update_app_no(k,app_no)

			k=k+1
			x=0
			dr.back()
			time.sleep(0.3)
			dr.back()
			time.sleep(1)
			close+=1
			continue
		else:
			break

	if close==3:
		continue

	# print(k)

	print("Promocode")
	promocode = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[5]")
	promocode.click()
	time.sleep(1)
	enter_pcode = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText")
	enter_pcode.send_keys("billpay")

	apply_butt = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[3]")
	apply_butt.click()
	time.sleep(5)

	try:
		ok = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button")
		ok.click()

		time.sleep(1)

		back = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[2]")
		back.click()
	except:
		pass


	try:
		editcardbutton()
		time.sleep(2.5)
	except:
		directedit()
	
	try:
		ok=dr.find_element_by_id("android:id/button1")
		ok.click()
		# ok=dr.find_element_by_id("android:id/button1")
		# ok.click()
		print("ok clicked")
	except:
		pass
	


	try:
		if dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View[5]/android.view.View/android.view.View[2]/android.widget.EditText"):
			pass
	except:
		# print("Except")
		card_index = get_card_index()
		if card_index == -1:
			print("None of the cards can be used")
			time.sleep(15)
			print("Sorry app had an error")
			exit=1

			ok = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button")
			ok.click()

			dr.back()
			yes = dr.find_element_by_id("android:id/button1")
			yes.click()

			other = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[9]")
			other.click()

			dr.back()
			time.sleep(0.3)
			dr.back()

			time.sleep(1)

			dr.back()

			try:
				ok=dr.find_element_by_id("android:id/button1")
				ok.click()
				# ok=dr.find_element_by_id("android:id/button1")
				# ok.click()
				print("ok clicked")
			except:
				pass

			linked_cards = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[7]/android.widget.RelativeLayout")
			linked_cards.click()

			print("linked cards")
			time.sleep(3)

			delete_card = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView[3]")
			delete_card.click()

			time.sleep(3)

			yes = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]")
			yes.click()

			sys.exit()

		card_used.append(card_index)
		change_card_details(card_index)
		close_app()
		time.sleep(2)
		continue

	time.sleep(2)

	pin = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View[5]/android.view.View/android.view.View[2]/android.widget.EditText")
	print(change_card_details.pin_no)
	pin.send_keys(change_card_details.pin_no)

	try:
		if dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View[7]/android.widget.Button[1]"):
			print("Normal submit")
			submit = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View[7]/android.widget.Button[1]")
			submit.click()
	except:
		if dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View[11]/android.widget.Button[1]"):
			print("LIC submit")
			submit2 = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View[11]/android.widget.Button[1]")
			submit2.click()


	time.sleep(15)


	try:
		transac = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[5]/android.view.View").text
		print(transac)
		file = open(location, 'a', newline='')
		thewriter = csv.DictWriter(file, fieldnames=fieldnames)
		thewriter.writerow({'Due Date':df.iloc[k]['Due Date'],	'Description':df.iloc[k]['Description'], 'Biller Name':df.iloc[k]['Biller Name'], 'K Number':df.iloc[k]['K Number'],'Amount':df.iloc[k]['Amount'],	'Status': "Paid", 'Reason':"", 'Biller name on bill':lis[1], 'Amount on bill':lis[2], 'Reference no.':str(transac),'App no.':app_no})
		file.close()
		print(df.iloc[k]['Due Date'], "    ", df.iloc[k]['Description'], "    ", df.iloc[k]['Biller Name'], "    ", df.iloc[k]['K Number'],  "    ", df.iloc[k]['Amount'], "    paid    ", "                                          ", lis[1], "    ", lis[2], "    ", str(transac), "     ", app_no)
		print("Fetching transaction history")
	except:
		print("Error")
		pass

	# cross = dr.find_element_by_xpath('//android.widget.TextView[@content-desc="Close"]')
	# cross.click()

	# yes = dr.find_element_by_id("android:id/button1")
	# yes.click()

	# other = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[9]")
	# other.click()

	dr.back()
	time.sleep(0.3)
	dr.back()
	time.sleep(3)

	filek = open(k_app, 'w',newline='')
	thewriter1 = csv.DictWriter(filek, fieldnames=['Last K Number', 'Last i'])
	thewriter1.writeheader()
	thewriter1.writerow({'Last K Number':k, 'Last i':app_no})	
	filek.close()

	update_app_no(k,app_no)

	dr.back()
	time.sleep(3)

	try:
		ok=dr.find_element_by_id("android:id/button1")
		ok.click()
		# ok=dr.find_element_by_id("android:id/button1")
		# ok.click()
		print("ok clicked")
	except:
		pass


	# navigate_up = dr.find_element_by_accessibility_id("Navigate up")
	# navigate_up.click()

	# time.sleep(3)

	# print(dr.page_source)

	# linked_cards = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView[2]/android.widget.LinearLayout[3]/android.view.ViewGroup/android.widget.TextView")
	# linked_cards.click()
	linked_cards = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[7]/android.widget.RelativeLayout")
	linked_cards.click()

	print("linked cards")
	time.sleep(3)

	delete_card = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView[3]")
	delete_card.click()

	time.sleep(3)

	yes = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]")
	yes.click()

	time.sleep(3)

	close_app()
	
	k=k+1

	app_no=app_no+1
	if app_no==total_no_of_apps+1:
		app_no=1

	# except:
	# 	if exit==1:
	# 		print("!! No card is proper active !!")
	# 		sys.exit()
	# 	print("error occurred")
	# 	close_app()