
import os
import sys
import gspread
import oauth2client; print(oauth2client.__version__)
from oauth2client.service_account import ServiceAccountCredentials
from numpy.random import *


# 最終行を取得
def create_random_num(worksheet):
    str_list = list(filter(None, sheet.col_values(1)))  # fastest
    return random_integers(len(str_list))


scope = ['https://spreadsheets.google.com/feeds']

# 3でダウンロードしたjsonファイルを指定する
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)
sheet = client.open("English-line-bot").sheet1


class Reply:
    # def __init__(self, reply_msg , answer):
    #     self.reply_msg = reply_msg
    #     self.answer = answer
    def __init__(self):
        pass
        print("Reply init")

    def reply(self, request_text):
        random = create_random_num(sheet)
        # pick out question and answer
        question = sheet.cell(int(random), 3).value
        answer = sheet.cell(int(random), 2).value

        # record a frequency of questions
        rate = sheet.cell(int(random), 4).value
        if rate is None:
            sheet.update_cell(int(random), 4, 1)
            frequency = 1
        else:
            sheet.update_cell(int(random), 4, int(rate) + 1)
            frequency = int(rate) + 1

        return question, answer, random, frequency

