import requests
#from random import choice
#urlToCheck = input("Enter the url to check:")
try:
    req = requests.get('https://curben.gitlab.io/malware-filter/phishing-filter.txt')
    filterList = req.text.split("\n")
except Exception as err:
    print("Error in loading phishing blocklist:{}\nUsing default...".format(err))
    filterList = []
def checkHost(host):
    match1 = False
    for url in filterList:
        if url.startswith("!"):
            continue
        if url == host:
            #print("Url is malware")
            match1 = True
            break
    if match1 == False:
        if host in filterList:
            return True
        else:
            return False
    else:
        return match1 