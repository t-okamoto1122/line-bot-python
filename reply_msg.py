
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
        question = sheet.cell(int(random), 3).value
        answer = sheet.cell(int(random), 2).value
        return question, answer

