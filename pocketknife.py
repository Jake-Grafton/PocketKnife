import requests # Import requests for fetching static web content.
import argparse # Import argparse for command line argument parsing.
import threading # Import threading for faster scraping.
parser = argparse.ArgumentParser(description='A simple admin login page scraper.')
parser.add_argument("-t", help="Target to scrape for login page.", dest='target')
target = parser.parse_args().target # Define target from parsed input.
target = target.strip().strip("https://").strip("http://").strip("/")
target = "http://" + target + "/"
# The variable target now looks like 'http://example.com/' instead of 'example.com'.

wordfile1 = open("admin-wordlist-part-1.txt", "r")
wordlist1 = wordfile1.readlines()
wordfile1.close()
wordfile2 = open("admin-wordlist-part-2.txt", "r")
wordlist2 = wordfile2.readlines()
wordfile2.close()
wordfile3 = open("admin-wordlist-part-3.txt", "r")
wordlist3 = wordfile3.readlines()
wordfile3.close()
wordfile4 = open("admin-wordlist-part-4.txt", "r")
wordlist4 = wordfile4.readlines()
wordfile4.close()
# All wordlists have been inputed into variables.

def scan1():
    for extension in wordlist1:
        scan = target + extension
        req = requests.get(scan)
        code = req.status_code
        if code == 200:
            print("\033[1;32;40m[+] " + scan, end='')
        elif code == 404:
            print("\033[1;31;40m[-] " + scan, end='')
        else:
            print("\033[1;33;40m[?] " + scan, end='')

def scan2():
    for extension in wordlist2:
        scan = target + extension
        req = requests.get(scan)
        code = req.status_code
        if code == 200:
            print("\033[1;32;40m[+] " + scan, end='')
        elif code == 404:
            print("\033[1;31;40m[-] " + scan, end='')
        else:
            print("\033[1;33;40m[?] " + scan, end='')

def scan3():
    for extension in wordlist3:
        scan = target + extension
        req = requests.get(scan)
        code = req.status_code
        if code == 200:
            print("\033[1;32;40m[+] " + scan, end='')
        elif code == 404:
            print("\033[1;31;40m[-] " + scan, end='')
        else:
            print("\033[1;33;40m[?] " + scan, end='')

def scan4():
    for extension in wordlist4:
        scan = target + extension
        req = requests.get(scan)
        code = req.status_code
        if code == 200:
            print("\033[1;32;40m[+] " + scan, end='')
        elif code == 404:
            print("\033[1;31;40m[-] " + scan, end='')
        else:
            print("\033[1;33;40m[?] " + scan, end='')

# Scans set up for multithreading.

t1 = threading.Thread(target=scan1, name='t1')
t2 = threading.Thread(target=scan2, name='t2')
t3 = threading.Thread(target=scan3, name='t3')
t4 = threading.Thread(target=scan4, name='t4')
# Threads created.

t1.start()
t2.start()
t3.start()
t4.start()
# Threads started.

t1.join()
t2.join()
t3.join()
t4.join()
# Wait until all threads finish.
print("\033[0;37;40m", end='')
