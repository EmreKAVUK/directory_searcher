import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = input("Enter website's url")
w_directory = input("Enter the wordlist index. If you leave the  blank, you will use the manual wordlist")
if w_directory == "":
    w_directory = "directory.txt"
wordlist = open(w_directory, "r")

for x in wordlist:
    ul = url + x.strip("\n")

    y = requests.get(ul,verify=False)
    if y.status_code < 400:
        print("URL --> "+ul+" ("+str(y.status_code)+")")
    