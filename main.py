import requests
from bs4 import BeautifulSoup
baidu_baike = 'baike.baidu.com/item/{star_name}'


def get_content():
    f = open('wenzl.html','r')
    content = f.read()
    return content


def get_img_url_list(bs_content):
    ul_list = bs_content.find_all('ul', attrs={'class':'starWorksList'})
    img_url_list = [] 
    for ul in ul_list:
        the_li = ul.find('li')
        jpg_name = the_li.text.replace('\n', '').replace(' ', '_').replace(';', '_').replace(',', '_')
        jpg_url = the_li.img['src']
        img_url_list.append((jpg_name, jpg_url))
    return img_url_list


def write_to_file(the_dict):
    import json
    the_string = json.dumps(the_dict)
    f = open('the_dict.json', 'w')
    f.write(the_string)


if __name__ == '__main__':
    content = get_content()
    bs = BeautifulSoup(content)
    img_url_list = get_img_url_list(bs)
    write_to_file(dict(img_url_list))

    

