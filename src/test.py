import itertools
import random
import threading
import time

import urllib3
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import requests
import requests_random_user_agent
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'},headers=headers
req=requests.get("https://shikimori.one/api/animes/52168/screenshots").json()[0]['original']

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
# user_agents = user_agent_rotator.get_user_agents()
API_URL="https://shikimori.one/api/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
screenshot = requests.get(f"{API_URL}animes/{32542}/screenshots",headers=headers).json()[0]['original']
print(screenshot)




print()

file=open("proxy.txt","r")
proxy=[]
for line in file.readlines():
    proxy.append(line.strip())
print(proxy)

print(req)

ids=[18393, 32281, 245, 30300, 34134, 36098, 30778, 44942, 35076, 22043, 32485, 31240, 3352, 49618, 35790, 32937, 9982, 34577, 26055, 934, 37675, 32686, 1535, 11061, 42249, 34964, 34572, 32189, 26055, 23755, 36456, 6702, 34599, 39456, 26055, 431, 38408, 48661, 15109, 31964, 9982, 30016, 36456, 11061, 28297, 20899, 4224, 20899, 34599, 12049, 30654, 34964, 40313, 33486, 32648, 32182, 38691, 29575, 43608, 37999, 40591, 32189, 35076, 6702, 4107, 1535, 33, 37510, 34240, 29803, 35848, 34964, 2001, 36862, 11111, 35073, 32930, 28171, 4565, 18393, 31772, 2904, 47778, 42310, 19815, 43608, 32542, 2001, 2001, 2001, 13535, 38594, 40591, 12729, 9919, 39195, 15451, 33524, 245, 6702, 28851, 34881, 44942, 24833, 245, 38691, 49926, 31845, 15109, 1575, 40748, 11617, 578, 4705, 268, 32648, 14719, 15109, 30831, 35972, 18679, 29803, 34612, 11843, 30654, 37991, 2001, 9253, 39026, 33255, 37521, 11266, 31933, 37105, 268, 28405, 5114, 22199, 31845, 13357, 49926, 35972, 32542, 32615, 30243, 26055, 9253, 39991, 37779, 10863]
print(len(ids))
scrs=[]

NUM_OF_THREADS=150
def getFromApi(ids,proxy):
    thread_list = []
    for id in ids:
        proxy = next(proxylist)
        # print(anime.name)
        # print("Proccesing " + anime.name)
        t = threading.Thread(target=getApi, args=[id,proxy])
        thread_list.append(t)
        t.start()
        while threading.active_count() > NUM_OF_THREADS:  # max thread count (includes parent thread)
            # print('\n == Current active threads ==: ' + str(threading.active_count() - 1))

            time.sleep(1)  # block until active threads are less than 4
    for ex in thread_list:  # wait for all threads to finish
        ex.join()

from fake_useragent import UserAgent
ua = UserAgent()

lives=[]


proxylist=itertools.cycle(proxy)

def getApi(id,proxies):
    proxy=proxies
    print("Current proxy: ", proxy)
    print(f"{len(scrs)}/{len(ids)}")
    # print("Beba:",proxy)
    proxy={'https':f'{proxy}'}
    #print(proxy)
    user_agent = {'User-Agent':f'{ua.random}'}
    # print(user_agent)
    #req=requests.get(f"https://shikimori.one/api/animes/{str(id)}/screenshots",headers=user_agent,proxies=proxy)
    try:
        #req = requests.get(f"https://api.ipify.org?format=json", headers=user_agent, proxies=proxy,timeout=3)
        req = requests.get(f"https://shikimori.one/api/animes/{str(id)}/screenshots", headers=user_agent, proxies=proxy,timeout=2)
        if not "Retry" or "403" in req.text:
            #print("ABOBA")
            #print(req.text)
            scrs.append(req.text+str(id))
            lives.append(proxy['https'])
        else:
            proxylist = itertools.cycle(proxy)
            getApi(id, proxies)
    except (urllib3.exceptions.ConnectTimeoutError,requests.exceptions.ConnectTimeout,requests.exceptions.ProxyError,requests.exceptions.SSLError,requests.exceptions.ReadTimeout,requests.exceptions.ConnectionError):
        print("dead")
        time.sleep(10)
        getApi(id,proxies)



    # print(f"Getting {id}")

getFromApi(ids,proxy=proxy)

print(lives)
for i in lives:
    print(f"{i}")


print(len(ids))
print(len(scrs))

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
for i in scrs:
    print(i)

# norm=[]
# for i in scrs:
#     try:
#         print(i.json()[0])
#         norm.append(i.json()[0])
#     except requests.exceptions.JSONDecodeError:
#         ...

#print(len(norm))