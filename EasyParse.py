# -*- coding: utf-8 -*- 
'''The task is to parse the list of institutes from http://raexpert.ru/rankingtable/?table_folder=/university/2014/main.
    It is given as a list of links. Result is written to .csv file row by row'''

#http://raexpert.ru/rankingtable/?table_folder=/university/2014/main
import re
import csv
import urllib
from bs4 import BeautifulSoup
import os
import sys
import codecs, cStringIO

htmls  = urllib.urlopen('http://raexpert.ru/rankingtable/?table_folder=/university/2014/main').read()


soup = BeautifulSoup(htmls)
         
with open('Insts.csv', 'w',  2) as csvfile:
    testwriter = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator = '\r')
    testwriter.writerow(['Institute'])
    for link in (soup.findAll(href = re.compile('/database/companies/')) ):
        testwriter.writerow([link.get_text().encode("cp1251")])
    
