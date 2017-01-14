import xml.etree.ElementTree as ET

target = 'nlp.txt.xml'

if __name__ == '__main__':
    for token in ET.parse(target).iter('token'):
        word = token.findtext('word')
        lemma = token.findtext('lemma')
        pos = token.findtext('POS')
        print('{}\t{}\t{}'.format(word, lemma, pos))
