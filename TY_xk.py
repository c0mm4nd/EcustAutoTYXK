#!/usr/bin/python
# coding:utf8

import requests
import mechanize
import cookielib

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()  
br.set_cookiejar(cj)  

br.set_handle_equiv(True)  
br.set_handle_gzip(True)  
br.set_handle_redirect(True)  
br.set_handle_referer(True)  
br.set_handle_robots(False)  
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)  



login = br.open('http://59.78.109.103/tyx/StdIndex.aspx')

# reqs = requests.Session()
# r = reqs.get('http://59.78.109.103/tyx/StdIndex.aspx')
# txt = r.text

txt = login.read()

num1 = txt.find("digit")
verify_code_1 = txt[num1 + 5: num1 + 6]
num2 = txt.find("digit", num1+6,len(txt))
verify_code_2 = txt[num2 + 5: num2 + 6]
num3 = txt.find("digit", num2+6,len(txt))
verify_code_3 = txt[num3 + 5: num3 + 6]
num4 = txt.find("digit", num3+6,len(txt))
verify_code_4 = txt[num4 + 5: num4 + 6]

verify_code = verify_code_1 + verify_code_2 + verify_code_3 + verify_code_4

# login
br.select_form(name="form1")
br.form["txt_studentid"] = "10142045"
br.form["txt_pwd"] = "10142045"
br.form["YZM"] = str(verify_code)
br.submit()

# print br.response().read()

br.open("http://59.78.109.103/tyx/Std/Stdxkindex1.aspx")

