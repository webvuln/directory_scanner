import os

T = input("update or scanning?: ")

if T == "update":
    os.system('sudo apt-get update')
    os.system('sudo apt install dirb')
    os.system('github link here ')

if T == "scanning":
    Web = input("URL of website with http: ")
    os.system('dirb ' + Web + ' -w >> results.txt')
