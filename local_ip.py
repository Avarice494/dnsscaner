# coding=utf-8
#
# for Python 3.0+
# 来自 https://pypi.python.org/pypi/qqwry-py3
# 版本：2020-06-25
#
# 用法
# ============
# from qqwry import QQwry
# q = QQwry()
# q.load_file('qqwry.dat')
# result = q.lookup('8.8.8.8')
#
#
# 解释q.load_file(filename, loadindex=False)函数
# --------------
# 加载qqwry.dat文件。成功返回True，失败返回False。
#
# 参数filename可以是qqwry.dat的文件名（str类型），也可以是bytes类型的文件内容。
#
# 当参数loadindex=False时（默认参数）：
# ﻿程序行为：把整个文件读入内存，从中搜索
# ﻿加载速度：很快，0.004 秒
# ﻿进程内存：较少，16.9 MB
# ﻿查询速度：较慢，5.3 万次/秒
# ﻿使用建议：适合桌面程序、大中小型网站
#
# ﻿﻿当参数loadindex=True时：
# ﻿程序行为：把整个文件读入内存。额外加载索引，把索引读入更快的数据结构
# ﻿加载速度：★★★非常慢，因为要额外加载索引，0.78 秒★★★
# ﻿进程内存：较多，22.0 MB
# ﻿查询速度：较快，18.0 万次/秒
# ﻿使用建议：仅适合高负载服务器
#
# ﻿﻿（以上是在i3 3.6GHz, Win10, Python 3.6.2 64bit，qqwry.dat 8.86MB时的数据）
#
#
# 解释q.lookup('8.8.8.8')函数
# --------------
# ﻿找到则返回一个含有两个字符串的元组，如：('国家', '省份')
# ﻿没有找到结果，则返回一个None
#
#
# 解释q.clear()函数
# --------------
# ﻿清空已加载的qqwry.dat
# ﻿再次调用load_file时不必执行q.clear()
#
#
# 解释q.is_loaded()函数
# --------------
# q对象是否已加载数据，返回True或False
#
#
# 解释q.get_lastone()函数
# --------------
# ﻿返回最后一条数据，最后一条通常为数据的版本号
# ﻿没有数据则返回一个None

import array
import bisect
import struct
import socket
import logging
from typing import Tuple, Union

__all__ = ('QQwry',)

logger = logging.getLogger(__name__)

def int3(data, offset):
    return data[offset] + (data[offset+1] << 8) + \
           (data[offset+2] << 16)

def int4(data, offset):
    return data[offset] + (data[offset+1] << 8) + \
           (data[offset+2] << 16) + (data[offset+3] << 24)

class QQwry:
    def __init__(self) -> None:
        self.clear()

    def clear(self) -> None:
        '''清空加载的数据，再次调用.load_file()时不必执行.clear()。'''
        self.idx1 = None
        self.idx2 = None
        self.idxo = None

        self.data = None
        self.index_begin = -1
        self.index_end = -1
        self.index_count = -1

        self.__fun = None

    def load_file(self, filename: Union[str, bytes], loadindex: bool=False) -> bool:
        '''加载qqwry.dat文件。成功返回True，失败返回False。
        参数filename可以是qqwry.dat的文件名（str类型），也可以是bytes类型的文件内容。'''
        self.clear()

        if type(filename) == bytes:
            self.data = buffer = filename
            filename = 'memory data'
        elif type(filename) == str:
            # read file
            try:
                with open(filename, 'br') as f:
                    self.data = buffer = f.read()
            except Exception as e:
                logger.error('%s open failed：%s' % (filename, str(e)))
                self.clear()
                return False

            if self.data == None:
                logger.error('%s load failed' % filename)
                self.clear()
                return False
        else:
            self.clear()
            return False

        if len(buffer) < 8:
            logger.error('%s load failed, file only %d bytes' %
                  (filename, len(buffer))
                  )
            self.clear()
            return False

        # index range
        index_begin = int4(buffer, 0)
        index_end = int4(buffer, 4)
        if index_begin > index_end or \
           (index_end - index_begin) % 7 != 0 or \
           index_end + 7 > len(buffer):
            logger.error('%s index error' % filename)
            self.clear()
            return False

        self.index_begin = index_begin
        self.index_end = index_end
        self.index_count = (index_end - index_begin) // 7 + 1

        if not loadindex:
            logger.info('%s %s bytes, %d segments. without index.' %
                  (filename, format(len(buffer),','), self.index_count)
                 )
            self.__fun = self.__raw_search
            return True

        # load index
        self.idx1 = array.array('L')
        self.idx2 = array.array('L')
        self.idxo = array.array('L')

        try:
            for i in range(self.index_count):
                ip_begin = int4(buffer, index_begin + i*7)
                offset = int3(buffer, index_begin + i*7 + 4)

                # load ip_end
                ip_end = int4(buffer, offset)

                self.idx1.append(ip_begin)
                self.idx2.append(ip_end)
                self.idxo.append(offset+4)
        except:
            logger.error('%s load index error' % filename)
            self.clear()
            return False

        logger.info('%s %s bytes, %d segments. with index.' %
              (filename, format(len(buffer),','), len(self.idx1))
               )
        self.__fun = self.__index_search
        return True

    def lookup(self, ip_str: str) -> Union[Tuple[str, str], None]:
        '''查找IP地址的归属地。
           找到则返回一个含有两个字符串的元组，如：('国家', '省份')
           没有找到结果，则返回一个None。'''
        ip = struct.unpack(">I", socket.inet_aton(ip_str.strip()))[0]
        print(ip)
        print(type(ip))
        try:
            return self.__fun(ip)
        except:
            if not self.is_loaded():
                logger.error('Error: qqwry.dat not loaded yet.')
            else:
                raise






if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        fn = 'qqwry.dat'
        q = QQwry()
        q.load_file(fn)

        for ipstr in sys.argv[1:]:
            s = q.lookup(ipstr)
            print('%s\n%s' % (ipstr, s))
    else:
        print('请以查询ip作为参数运行')
