import optparse
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-u","--url",dest="url",help="Enter your url without / at the end of the site ")
    parse_object.add_option("-w","--wordlist",dest="wordlist",help="Enter your wordlist's directory (NOT REQUIRED)")
    return parse_object.parse_args()

def find_directory(url,wordlist):
    if user_inputs.wordlist == None:
        w_directory = "directory.txt"
    else:
        w_directory = user_inputs.wordlist
    wordlist = open(w_directory, "r")

    for x in wordlist:
        ul = str(user_inputs.url) + x.strip("\n")

        y = requests.get(ul,verify=False)
        if y.status_code < 400:
            print("URL --> "+ul+" ("+str(y.status_code)+")")

(user_inputs,arguments)=get_user_input()
find_directory(user_inputs.url,user_inputs.wordlist)