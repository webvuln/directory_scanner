import os

T = input("update or scanning?: ")

if T == "update":
    os.system('sudo apt-get update')
    os.system('sudo apt install dirb')
    os.system('git clone https://github.com/anonymouse327311/directory_scanner')

if T == "scanning":
    Web = input("URL of website with http: ")
    os.system('dirb ' + Web + ' -w >> results.txt')
