#!/usr/bin/env python
#christji

import re

def parse_nwodkram(text):
    """The functions task is to change Nwodkram-language to HTML. """
    # Converts a picture from Nwodkram to HTML
    html = re.sub(r'\<(.*?)\>\(w=(\d+)\,h=(\d+)\)', r'<img src=\"\\1\" style=\"width:\\2px;height:\\3px\";>', text)

    # Converts the wikipedia query to a hyperlink
    html = re.sub(r'\[wp:(.*?)\]', '<a href=\"www.wikipedia.org/wiki/\\1\">Search Wikipedia for \\1</a>', html)

    # Sets URL with extra http:// if missing already and converts to html-URL
    html = re.sub(r'\[([^\]]*)\]\((http://|https://)(.*?)\)', '<a href=\'\\2\\3\'>\\1</a>', html)
    html = re.sub(r'\[(.*?)\]\((.*?)\)', '<a href=\'http://\\2\'>\\1</a>', html)

    # Convertes to bold and removes the /%
    html = re.sub(r'(?<!\\)%(.*?(?<!\\))%', '<b>\\1</b>', html)
    html = re.sub(r'\\%', '%', html)

    # Converts to italic and removes the /*
    html = re.sub(r'(?<!\\)\*(.*?(?<!\\))\*', '<i>\\1</i>', html)
    html = re.sub(r'\\\*', '*', html)

    # Converts the quoteline to html
    html = re.sub(r'>>(.*)', '<blockquote>\\1</blockquote>', html)
    return html
