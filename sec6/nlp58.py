import xml.etree.ElementTree as ET

if __name__ == '__main__':
    target = 'nlp.txt.xml'
    
    for sentence in ET.parse(target).iterfind('./document/sentences/sentence'):
        sentence_id = int(sentence.get('id'))

        dict_pred = {}
        dict_nsubj = {}
        dict_dobj = {}

        for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
            dep_type = dep.get('type')
            if dep_type == 'nsubj' or dep_type == 'dobj':
                governor = dep.find('./governor')
                idx = governor.get('idx')
                dict_pred[idx] = governor.text

                if dep_type == 'nsubj':
                    dict_nsubj[idx] = dep.find('./dependent').text
                else:
                    dict_dobj[idx] = dep.find('./dependent').text

        for idx, pred in sorted(dict_pred.items(), key=lambda x: x[1]):
            nsubj = dict_nsubj.get(idx)
            dobj = dict_dobj.get(idx)
            if nsubj is not None and dobj is not None:
                print('{}\t{}\t{}'.format(nsubj, pred, dobj))