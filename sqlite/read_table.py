# -*- coding: utf-8 -*- 
# Created on 2015 10 21 

__author__ = 'SugN'
__copyright__ = "Copyright 2015, SugN All Rights Reserved."
__credits__ = [""]
__license__ = "GPL"
__version__ = "1.0.1"

"""

"""
import xlrd
import data

def read_table(filename):

    book = xlrd.open_workbook(filename)
    for name in book.sheet_names():
        print name


if __name__ == '__main__':

    read_table('2015.xls')