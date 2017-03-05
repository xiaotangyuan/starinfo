# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
from pypinyin import pinyin, lazy_pinyin


def get_pinyin(cn_string):
    res_list = lazy_pinyin(cn_string)
    res = ''.join(res_list)
    return res
    

def get_html_filename(star_cn_name):
    pinyinstring = get_pinyin(star_cn_name)
    print 'pinyinstring:', pinyinstring
    return '%s.html' % pinyinstring
    

def gen_html(star_cn_name):
    order_string = u'wget baike.baidu.com/item/%s -O %s'
    html_filename = get_html_filename(star_cn_name)
    print html_filename
    order_string = order_string % (star_cn_name, html_filename)
    print 'order:', order_string
    #os.system(order_string)
    import commands
    commands.getstatusoutput(order_string)


if __name__ == '__main__':
    import sys
    star_cn_name = sys.argv[1]
    gen_html(star_cn_name)
