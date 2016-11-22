import json


def extract_json(title):
    with open('jawiki-country.json') as f:
        json_data = f.readline()
        while json_data:
            article_data = json.loads(json_data)
            if article_data["title"] == title:
                return article_data["text"]
            else:
                json_data = f.readline()
    return ""

if __name__ == '__main__':
    print(extract_json('イギリス'))