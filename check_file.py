import requests
import malware_test
import phish_test
filename = input("Enter the filename of the file to verify: ")
try:
    with open("sites.txt") as f:
        existingsites = f.read().split("\n")
except:
    print("Can not load existing sites")
    existingsites = []
def testHTTPS(host):
    try:
        requests.get("https://{}".format(host))
    except:
        return False
    else:
        return host != ''
try:
    with open(filename) as f:
        newsites = f.read().split('\n')
        verifyedsites = []
        for site in newsites:
            if site == '' or site == ' ':
                continue
            if malware_test.checkHost(site):
                print("{} is malware. Not adding.".format(site))
            try:
                requests.get("http://{}".format(site))
            except:
                print("Retrying...")
                try:
                    requests.get('http://{}'.format(site))
                    continue
                except:
                    print("{} can not be reached. ".format(site))
                    continue
                else:
                    if testHTTPS(site) == True:
                        print("{} supports https.".format(site))
                        if malware_test.checkHost(site) == False and phish_test.checkHost(site) == False:
                            if site in verifyedsites:
                                print("Site is already verifyed. Not adding")
                                continue
                            verifyedsites.append(site)
                            continue
                        else:
                            print("{} is a malware or phishing site. Not adding.".format(site))
                            continue
            else:
                if testHTTPS(site) == True:
                    print("{} supports https.".format(site))
                    if malware_test.checkHost(site) == False and phish_test.checkHost(site) == False:
                        if site in verifyedsites:
                            print("Site is already verifyed. Not adding")
                            continue
                        verifyedsites.append(site)
                        continue
                    else:
                        print("{} is a malware or phishing site. Not adding.".format(site))
                        continue
    try:
        print("{} hosts will be removed. {} hosts remaining.".format(len(newsites) - len(verifyedsites),len(verifyedsites)))
        if input("Save to {}? (y/n) ".format(filename)) == "y":
            with open(filename,"w") as f2:
                for site in verifyedsites:
                    f2.write(site)
                    f2.write("\n")
                f2.close()
    except Exception as err:
        print("Error in saving:{}".format(err))
except Exception as err:
    print("Error:{}".format(err))