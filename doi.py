# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 06:39:13 2018

@author: mjdog1
"""

import requests
import re
import traceback

"""
get author surname and paper article
"""
def analysis_bib(bib_path):
    bibfile = open(bib_path)
    bibfilestr = bibfile.read()
    bibstr = r'(s|e)\s*?{(.*?)\d+(.*?),.*?itle\s*?={(.*?)}'
    com_bibstr = re.compile(bibstr, re.S) 
    items = re.findall(com_bibstr,bibfilestr)
    return items
def gethtml(url,data,filepath):
    r = requests.post(url,data)
    doifile=open(filepath,'w+')
    return r.text

def analysis_data(htmltext):
    zzstr = r'href=http://dx.doi.org/(.*?)>http' #只要抓去doi就可以
    doifile = open(filepath)
    #doifilestr = doifile.read()
    com_zzstr=re.compile(zzstr,re.S)
    items=re.findall(com_zzstr,htmltext)
    return items

#def outputdoi(all_doi_items):

def Spiderman(url,bib_path,filepath):
    bib_items=analysis_bib(bib_path)
    title =''
    auth_surname = ''
    all_doi_items = []
    namedoi= '{:100}\t{:16}'
    outputfile = open(filepath,'w')
    gouge=''
    try:

        for i in bib_items:
            print('surname1 is'+ i[1]+'surname2 is \t'+i[2]+' paper title is \t'+i[3])
            if(i[1]==''):
                auth_surname = i[2]
            else:
                auth_surname = i[1]
            title = i[3]
            condata = {'queryType':'author-title','auth2':auth_surname,'atitle2':title,'multi_hit':'true','article_title_search':'Search'}
            htmltext = gethtml(url,condata,filepath)
            doi_items = analysis_data(htmltext)
            print(doi_items)
            outputfile.write(namedoi.format('\npaper is '+title, 'doi is '+str(doi_items)))
            all_doi_items.append(doi_items)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    url = 'https://www.crossref.org/guestquery/'
    bib_path = '.../your.bib'
    file_path = '.../your.txt'
    Spiderman(url,bib_path,file_path)

