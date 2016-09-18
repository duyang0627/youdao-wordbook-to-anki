#!/bin/python
# -*- coding:utf-8 -*-
# a script convert xml wordbook from youdao dict to anki

import sys
from xml.dom.minidom import parse, parseString
'''
XML format as of September 2016:
<wordbook><item>
        <word>hysteria</word>
        <trans><![CDATA[n. 歇斯底里]]></trans>
        <phonetic><![CDATA[[hɪ'stɪərɪə]]]></phonetic>
        <tags></tags>
        <progress>10</progress>
    </item><item>
        ...
    </item>
</wordbook>
'''

def convertDict(xmlFilename, ankiFilename):
    ''' Read the xml file as a string '''
    xmlFile = open(xmlFilename, 'r');
    dictXml = xmlFile.read();
    xmlFile.close();
    
    ''' Begin parsing the xml '''
    dom =  parseString(dictXml);
    
    ankiFile = open(ankiFilename, 'w')
    
    wordbook = dom.getElementsByTagName('wordbook')[0]
    for item in wordbook.getElementsByTagName('item'):
        word = item.getElementsByTagName('word')[0].firstChild.wholeText

        try:
            phonetic = item.getElementsByTagName('phonetic')[0].firstChild.wholeText
        except:
            phonetic = ''

        try:
            trans = item.getElementsByTagName('trans')[0].firstChild.wholeText
        except:
            trans = ''

        word = word.strip().encode('utf-8')
        trans = trans.strip().encode('utf-8')
        trans = trans.replace('\n', '<br>')
        phonetic = phonetic.strip().encode('utf-8')
        
        ankiFile.write(word + ' ' + phonetic + '\t' + trans)
        ankiFile.write('\r\n')
    ankiFile.close()
    print 'Conversion Success!'

def main(args):
    if len(args) < 3 or (args[1] in ['-u', '--usage', '-h', '--help', '/h', '/help']):
        print 'Usage:\n\t python', args[0], '<youdao_xml_file_name> <anki_file_name>\n'
        sys.exit(0)

    convertDict(args[1], args[2])
    
if __name__ == '__main__':
    main(sys.argv)
