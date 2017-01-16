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

                # 述語の辞書に追加
                governor = dep.find('./governor')
                idx = governor.get('idx')
                dict_pred[idx] = governor.text

                # 主語、目的語の辞書に追加
                if dep_type == 'nsubj':
                    dict_nsubj[idx] = dep.find('./dependent').text
                else:
                    dict_dobj[idx] = dep.find('./dependent').text

        for idx, pred in sorted(dict_pred.items(), key=lambda x: int(x[0])):
            nsubj = dict_nsubj.get(idx)
            dobj = dict_dobj.get(idx)
            if nsubj and dobj:
                print('{}\t{}\t{}'.format(nsubj, pred, dobj))