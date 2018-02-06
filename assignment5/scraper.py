#!/usr/bin/env python
#christji

import re
import urllib.request

def find_emails(text):
    """ This function will find all the legal emails from a text, and return a list of them"""

    """ The assignment says "characters which are alphabetical or ., with the...", but my understanding is that only "."
    is legal because a comma is not natural in emails. Also I thought the comma belonged to the assignment text, and
    not the requirement"""

    return re.findall(r'[\w\.#\$%&~’\*\+\-/=\?_‘\|\{}.]+\@[\w\.#\$%&~’\*\+\-/=\?_‘\|\{}.]+\.[a-zA-Z][a-zA-Z.]*[a-zA-Z]', text)

def find_urls(text):
    """ This function will find all the valid urls from the text sent in"""

    # Maybe not the most effective way, because I have to use a for-loop every time to get the second group.
    # I'm open for suggestions to other ways to solve this one :)
    temp = re.findall(r'<a href=([\"\'])((?:http|https)://(?:www.|)[\w\.\-\~]+\.[\w\.\-\~]+\/[\w\/\.\-\~]+)(\1)>.*</a>', text)

    result = []
    for item in temp:
        result.append(item[1])
    return result

def find_urls_v2(text, url):
    """ This function will find all the valid urls, also the relative hyperlinks, from the text sent in"""

    """ I understood the assignment 5.5 that a relative hyperlink consist of the PATH.html only. While the absolute hyperlinks consist of
    'http://HOST.DOMAIN/PATH'. Therefore in this one I've focused on searching for the PATH only when reading hyperlinks """

    # Find all the absolute hyperlinks
    abs_link = re.findall(r'<a href=([\"\'])((?:http|https):\/\/(?:www.|)[\w\.\-\~]+\.[\w\/\@\.\-\~]+)(\1)>?(?:.|\s)*?<\/a>', text)

    result = []
    for item in abs_link:
        result.append(item[1])

    # Find all the relative hyperlinks
    rel_link = re.findall(r'<a href=([\"\'])(\w+)\.html(\1)>', text)

    # Find all the relevant urls from the hyperlinks
    result2 = []
    for hyp_link in rel_link:
        result2.append(hyp_link[1])

    # Not quite sure if I understood the assignment correctly, but here I've tried to concatenate the original url with the relative hyperlink.
    # It will only add the relative hyperlink to the original url, and does for example not add https://lucidtech.io/blabla/relevanthyperlink.html
    # I am open for suggestions on how this could be solved :)
    for word in result2:
        new_string = url + word + ".html"
        result.append(new_string)

    return result

def all_the_emails(url, depth):
    """ Interprets the url I send in as level/depth = 0. Therefore it'll count downwards until we hit zero, so we recursively go through all the urls.
    This method will go through all the urls and call find_emails and find_urls_v2. See above for the method find_urls_v2"""
    url_req = urllib.request.urlopen(url)
    url_read = url_req.read()
    html = url_read.decode("utf8")
    email_list = find_emails(html)
    url_list = find_urls_v2(html, url)
    print(url_list)
    if depth != 0:
        url_list = find_urls(html)
        for url in url_list:
            email_list.append(all_the_emails(url, depth-1))
    url_req.close()
    return email_list

# Just for testing
#all_the_emails("https://lucidtech.io/", 0)
