import sqlite3
import json

connt = sqlite3.connect('data/enmldata.db')
cur = connt.cursor()
parts_speech = open('data/parts-of-speech.json', 'r')
load_ps = json.loads(parts_speech.read())


def searchWord(word: str):
    search_query = cur.execute(f"SELECT english_word, part_of_speech, malayalam_definition FROM enml WHERE "
                               f"english_word LIKE '{word}'")
    search_result = search_query.fetchall()
    if not search_result:
        raise Exception("Word not fund")
        return
    search_word = search_result[0][0]
    search_definition = [f'{words[2]} - {load_ps[words[1]]["en"]}' for words in search_result if words[1] in load_ps]
    search_entries = [f'{word[2]}' for word in search_result if word[1] not in load_ps]
    return search_word, search_entries, search_definition
