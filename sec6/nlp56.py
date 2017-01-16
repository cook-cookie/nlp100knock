import xml.etree.ElementTree as ET

target = 'nlp.txt.xml'

if __name__ == '__main__':
    rep_dict = {}

    for coreference in ET.parse(target).iterfind('./document/coreference/coreference'):

        # 代表参照表現のテキストを取得
        rep_text = coreference.findtext('./mention[@representative="true"]/text')

        for mention in coreference.iterfind('./mention'):

            # 'representative'という単語を探し、無ければfalseを返す
            if mention.get('representative', 'false') == 'false':
                sentence_id = int(mention.findtext('sentence'))
                start_id = int(mention.findtext('start'))
                end_id = int(mention.findtext('end'))
                rep_dict[(sentence_id, start_id)] = (end_id, rep_text)

    for sentence in ET.parse(target).iterfind('./document/sentences/sentence'):
        sentence_id = int(sentence.get('id'))
        org_rest = 0 # 置換中のtoken数の残り

        for token in sentence.iterfind('./tokens/token'):
            token_id = int(token.get('id'))

            if org_rest == 0 and (sentence_id, token_id) in rep_dict:
                (end_id, rep_text) = rep_dict[(sentence_id, token_id)]
                print('[' + rep_text + '] (', end='')
                org_rest = end_id - token_id

            print(token.findtext('word'), end='')

            # 置換の終わりにカッコ閉じ
            if org_rest > 0:
                org_rest -= 1
                if org_rest == 0:
                    print(') ', end='')
            print(' ', end='')

        print()
