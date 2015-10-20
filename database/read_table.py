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

def read_table(filename):

    book = xlrd.open_workbook(filename)
    s1 = book.sheet_by_index(0)
    members = []

    for row in range(1,s1.nrows):

        name = s1.cell(row,0).value
        grade = s1.cell(row,1).value
        member = [name, grade]
        members.append(member)

    return members

if __name__ == '__main__':

    members = read_table('2015.xls')
    print members