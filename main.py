import json
import csv
from datetime import datetime


def write_data(data):
    with open('chats.csv', 'a', encoding="utf-8") as file:
        order = ['id', 'dialogId', 'who', 'createTime', 'message']
        writer = csv.DictWriter(file, fieldnames=order, delimiter='|')
        writer.writerow(data)


def get_data(parsed_string):

    for i in parsed_string:
        ids = i['id']
        dialogId = i['dialogId']
        who = i['who']
        createTime = i['createTime']
        message = i['message'].replace("\n", "\t")

        data = {
            'id': ids,
            'dialogId': dialogId,
            'who': who,
            'createTime': createTime,
            'message': message,
        }

        write_data(data)


def main():

    in_file = open("messages.json", "r", encoding='utf-8')
    json_string = in_file.read()
    parsed_string = json.loads(json_string)
    get_data(parsed_string)


if __name__ == '__main__':
    main()
