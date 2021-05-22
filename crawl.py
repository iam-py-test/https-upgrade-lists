import requests
import random
def mk_url(length,ext):
    url = ''
    while len(url) <= length:
        url += random.choice(["a","b","c",'d','e','f','g','h','i','j','k','K','l','m','n','o','p','q','r','s','t','u','v','w','W','x','y','z','X','Y',"Z","0",'1','2','3','4','5','6','7','8','9','.','Q',"books","ama","ky","wiki","whole","food","health","net","ad","se","in","ee","oo","ho","A","B","C","D","E"])
    return url + '.' + ext
def choseExt():
    return random.choice(["com","com","com","net","net","org","org","gov","edu","int","ac","xyz","us","info","co","jobs","biz","appspot.com","app","in","co.uk","github.io","blogspot.com"])
def choseLength():
    return random.choice([1,1,2,3,4,5,6,7,8,9,10,10,11,12,13,14,15,90])
def mk_url_words(length,ext):
    url = ''
    while len(url) <= length:
        url += random.choice(["book","books","ads","research","software","wiki","blog","code","malware","test","sandbox","joe","bob","tree","trees","save","eco","gas","shell","google","yahoo","duck","search","block","ad","net","safe","food","whole","health","windows","window","computer","free","linux","mac","iOS","pi","about","fix","win","fire","fox","firefox","chrome","solve","security","light","lite","privacy","spread","cream","chose","daily","mail","us","uk","ever"])
    return url + "." + ext
hosts = []
noprompt = False
times = 0
validhosts = 0
hostshttps = 0
while True:
    for t in range(1,12):
        try:
            url = mk_url(choseLength(),choseExt())
            if url.startswith("."):
                url = mk_url(choseLength(),choseExt())
            if ".." in url and len(url) > 3:
                url = mk_url_words(choseLength(),choseExt())
            if len(url) >= 90:
                url = mk_url_words(choseLength(),choseExt())
            if url in hosts:
                print("Already done.")
                continue
            print("Testing \"{}\"...".format(url))
            requests.head('http://{}'.format(url))
        except:
            #print("Retrying...")
            try:
                requests.get("http://{}".format(url))
            except:
                print("\"{}\" is not a host".format(url))
            else:
                validhosts += 1
                try:
                    requests.get("https://{}".format(url))
                except:
                    print("\"{}\" does not support https".format(url))
                else:
                    hostshttps += 1
                    if noprompt == True:
                        try:
                            with open("crawled.txt","a") as f3:
                                f3.write(url)
                                f3.write("\n")
                                f3.close()
                        except Exception as err:
                            print("Error in saving:{}".format(err))
                    else:
                        hosts.append(url)
                
        else:
            validhosts += 1
            try:
                requests.get("https://{}".format(url))
            except:
                print("\"{}\" does not support https".format(url))
            else:
                hostshttps += 1
                if noprompt == True:
                    try:
                        with open("crawled.txt","a") as f3:
                            f3.write(url)
                            f3.write("\n")
                            f3.close()
                    except Exception as err:
                        print("Error in saving:{}".format(err))
                else:
                    hosts.append(url)
                
                    
    if noprompt == True and times < 15:
        print("\tPrompting is disabled. Program has run {} times".format(times))
        times = times + 1 
        continue
    c = input("Continue? (y/n)").lower()
    if c == 'n':
        break
    elif c == "noprompt":
        noprompt = True
        times = 0
        with open("crawled.txt","a") as f:
            for host in hosts:
                f.write(host)
                f.write("\n")
            f.close()
with open("crawled.txt","a") as f:
    for host in hosts:
        f.write(host)
        f.write("\n")
    f.close()
    print("{} valid hosts found. {} new hosts support https.".format(validhosts,hostshttps))