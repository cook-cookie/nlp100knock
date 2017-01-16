import xml.etree.ElementTree as ET
import re

target = 'nlp.txt.xml'
pattern = re.compile(r'^\((.*?)\s(.*)\)$')


def search_np(str, list_np):
    match = pattern.match(str)
    tag = match.group(1)
    value = match.group(2)

    depth = 0
    chunk = ''
    words = []

    for char in value:
        if char == '(':
            chunk += char
            depth += 1

        elif char == ')':
            chunk += char
            depth -= 1
            if depth == 0:
                words.append(search_np(chunk, list_np))
                chunk = ''
        else:
            if not (depth == 0 and char == ' '):
                chunk += char

    if chunk != '':
        words.append(chunk)

    result = ' '.join(words)

    if tag == 'NP':
        list_np.append(result)

    return result


if __name__ == '__main__':
    for parse in ET.parse(target).iterfind('./document/sentences/sentence/parse'):
        result = []
        search_np(parse.text.strip(), result)
        result = [s.replace('-LRB- ','(').replace(' -RRB-', ')') for s in result]
        print(*result, sep='\n')
