from graphviz import Digraph
import xml.etree.ElementTree as ET

'''
--memo--
G.node(id, label)
G.edge(from, to)
'''

if __name__ == '__main__':
    target = 'nlp.txt.xml'

    G = Digraph(format='png')
    G.attr('node', shape='circle')

    for sentence in ET.parse(target).iterfind('./document/sentences/sentence'):
        sentence_id = int(sentence.get('id'))
        edges = []

        for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
            if dep.get('type') != 'punct':
                governor = dep.find('./governor')
                dependent = dep.find('./dependent')
                edges.append(
                    ((governor.get('idx'), governor.text), (dependent.get('idx'), dependent.text))
                )

        if len(edges) > 0:
            for edge in edges:
                id1 = str(edge[0][0])
                label1 = str(edge[0][1])
                id2 = str(edge[1][0])
                label2 = str(edge[1][1])

                G.node(id1, label1)
                G.node(id2, label2)
                G.edge(id1, id2)
            G.render('{}'.format(sentence_id))
