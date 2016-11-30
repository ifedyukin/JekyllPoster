#!/usr/bin/env python3
# coding: utf8

from termcolor import colored
import sys
import os
import datetime

#config
dir = ""
username = ""
password = ""
repository = ""

def fileNameGen(title):
    now = datetime.datetime.now()
    date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    fileName = date + "-" + title + ".md"
    return fileName

def headerGen(title):
    headerGen = "---\nlayout: post\ntitle: " + title + "\n---"
    return headerGen

def postTextGet():
    postText = ""
    print(colored("Post text: ","blue"))
    text = input(colored("(input \"%%END%%\" for close input)\n","red"))
    while (text != "%%END%%"):
        postText += "\n" + text
        text = input()
        pass
    return postText

def saveFile(fileName, fileHeader, fileText):
    os.chdir(dir+"/_posts")
    postFile = open(fileName, 'w')
    postFile.write(fileHeader + '\n' + fileText)
    postFile.close()
    pass
    
def gitPush(repository, username, password):
    os.chdir(dir)
    #commit
    commit=os.popen('git add . && git commit -m "New post"')
    print(commit.read())
    commit.close()
    #push
    push=os.popen('git push https://' + username + ':' + password + '@' + repository + ' --all')
    result=push.read()
    push.close()
    return result

def main():
    print(colored("Create new post to your Jekyll-blog!","cyan"))
    postTitle = input(colored("Post [page]-title: ","blue"))
    postLink = input(colored("Post [link]-title: ","blue"))
    fileName = fileNameGen(postLink)
    postText = postTextGet()
    saveFile(fileName, headerGen(postTitle), postText)
    gitPush(repository, username, password)   
    print(colored("Posted!","green"))
    pass

main()
