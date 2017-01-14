import xml.etree.ElementTree as ET

target = 'nlp.txt.xml'

if __name__ == '__main__':
    for token in ET.parse(target).iterfind('./document/sentences/sentence/tokens/token[NER="PERSON"]'):
        print(token.findtext('word'))
