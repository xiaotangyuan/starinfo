# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import commands
from pypinyin import pinyin, lazy_pinyin


def get_pinyin(cn_string):
    res_list = lazy_pinyin(cn_string)
    res = ''.join(res_list)
    return res
    

def get_html_filename(star_cn_name):
    pinyinstring = get_pinyin(star_cn_name)
    print 'pinyinstring:', pinyinstring
    return '%s.html' % pinyinstring


def download(uri, save_name, filedir='html_content'):
    if not os.path.exists(filedir):
        os.mkdir(filedir)
    save_name = save_name.replace('/', '_')
    filename =  os.path.join(filedir, save_name)
    filename = filename.replace('(', '{').replace(')','}')
    if os.path.exists(filename):
        print 'already download:', filename
    order_string = u'wget %s -O %s' % (uri, filename)
    print 'order_string:', order_string
    commands.getstatusoutput(order_string)
    

def gen_html(star_cn_name):
    uri = u'baike.baidu.com/item/%s' % star_cn_name
    html_filename = get_html_filename(star_cn_name)
    print html_filename
    download(uri, html_filename)


if __name__ == '__main__':
    import sys
    star_cn_name = sys.argv[1]
    star_cn_name = unicode(star_cn_name, 'utf8')
    gen_html(star_cn_name)
