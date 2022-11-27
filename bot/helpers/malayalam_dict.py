import sqlite3
import json

connt = sqlite3.connect('data/enmldata.db')
cur = connt.cursor()
parts_speech = open('data/parts-of-speech.json', 'r')
load_ps = json.loads(parts_speech.read())


def do_search(user_text):
    word: str
    word_id: str
    result = []
    ps_result = []
    sql_serch_id = cur.execute(
        f"SELECT word, _id FROM words_en WHERE stems LIKE '%{user_text}%' OR stems LIKE '{user_text}' ORDER BY "
        f"LENGTH(word) LIMIT 1")
    for row in sql_serch_id:
        word, word_id = row
    sql_search_dict = cur.execute(
        f'SELECT word, id_en,type FROM relations_en_ml LEFT JOIN words_ml ON (words_ml._id = relations_en_ml.id_ml) '
        f'WHERE id_en IN ({word_id}) ORDER BY LENGTH(word)')
    for row in sql_search_dict:
        word_dict, _, p_speech = row
        if p_speech in load_ps:
            ps_result.append(f"◦ {word_dict} - {load_ps[p_speech]['en']}")
        else:
            result.append(f"-{word_dict}")
    return word, ps_result, result
