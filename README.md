# Import to Anki from Youdao XML output

A simple tool to convert youdao xml file into tab separated txt file for importing to Anki. 

Note that by default, youdao exports one word three times into its xml file. So no worries 
if anki throws warnings that words are imported twice. 

## Usage
Please make sure python is installed in your system. After downloading the file, Execute 
the following command in command line:  
    `python youdaoxml2anki.py your_youdao_wordbook.xml your_anki_wordbook.txt`  
Use the import function in anki to import the words. That's it, done!

Anki是一个基于间格重复（Spaced Repetition）的字卡软件，anki 开源稳定，简洁高效，可作为
有道单词本的替代
