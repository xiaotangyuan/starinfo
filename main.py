import os
import re
import requests
from bs4 import BeautifulSoup
from get_html import download as download_img


key_word_start = 'canyandianshiju2'
key_word_end = 'canyandianying2'
name_head = 'dsj'


def get_content(filename):
    filename = os.path.join('html_content', filename)
    f = open(filename,'r')
    content = f.read()
    return content


def clean_content(content_string):
    content_string = content_string.replace('\n', '')
    pattern = re.compile(r'%s.+%s' % (key_word_start, key_word_end))
    res_list = pattern.findall(content_string)
    return res_list[0]


def get_img_url_list(bs_content):
    li_list = bs_content.find_all('li', attrs={'class':'listItem'})
    img_url_list = [] 
    for li in li_list:
        jpg_name = li.text.replace(' ', '_').replace(';', '_').replace(',', '_')
        jpg_name = '%s.jpg' % jpg_name
        jpg_url = li.img['src']
        img_url_list.append((jpg_name, jpg_url))
    return img_url_list


def write_to_file(the_dict):
    import json
    the_string = json.dumps(the_dict)
    f = open('the_dict.json', 'w')
    f.write(the_string)


        


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    star_name = filename.split('.')[0]
    content = get_content(filename)
    content = clean_content(content)
    #print 'clean: \n', content
    bs = BeautifulSoup(content, 'html.parser')
    img_url_list = get_img_url_list(bs)
    write_to_file(dict(img_url_list))
    print 'get items: %s' % len(img_url_list)
    for img_name, img_url in img_url_list:
        img_name = '%s_%s' % (name_head, img_name)
        download_img(img_url, img_name, filedir=star_name)

