import xml.etree.ElementTree as ET

target = 'nlp.txt.xml'

if __name__ == '__main__':
    for word in ET.parse(target).iter('word'):
        print(word.text)
