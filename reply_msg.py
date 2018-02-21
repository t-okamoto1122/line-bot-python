import os
import sys
import gspread
import oauth2client;

print(oauth2client.__version__)
from oauth2client.service_account import ServiceAccountCredentials
from numpy.random import *


scope = ['https://spreadsheets.google.com/feeds']
spreadsheetId = '1zErUZR08O1AmemZWedtR3MqYvr35PvWr1FMYXlyJMAY'

# 3でダウンロードしたjsonファイルを指定する
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)
sheet = client.open("English-line-bot").sheet1


# 最終行を取得
def create_random_num():
    str_list = list(filter(None, sheet.col_values(1)))  # fastest
    return random_integers(len(str_list))


def select_random(all_records):
    target_list = []
    for i, record in enumerate(all_records):

        if record[-1] != 'done':
            target_list.append(record[0])

    # all done
    if len(target_list) == 0:
        # 1/ Max_count
        return 0, 1

    random_num = random_integers(len(target_list))
    return target_list[random_num - 1], len(target_list)


# remove 'done' from sheet and return random number
def all_done(all_records):
    cell_list = sheet.range('E1:E' + str(len(all_records)))
    for cell in cell_list:
        cell.value = ''
    sheet.update_cells(cell_list)
    return create_random_num()


class Reply:
    def __init__(self):
        pass

    def reply(self, request_text):
        all_records = sheet.get_all_values()
        max_count = len(all_records)
        random, remain_count = select_random(all_records)

        # when all questions have set
        if random == 0:
            random = all_done(all_records)

        # pick out question and answer
        question = sheet.cell(int(random), 3).value
        answer = sheet.cell(int(random), 2).value

        # record a frequency of questions
        rate = sheet.cell(int(random), 4).value
        if rate is '':
            sheet.update_cell(int(random), 4, '1')
            frequency = 1
        else:
            frequency = int(rate) + 1
            sheet.update_cell(int(random), 4, frequency)

        # doneのものを取得する
        sheet.update_cell(int(random), 5, 'done')

        return question, answer, random, frequency, max_count - remain_count, max_count
