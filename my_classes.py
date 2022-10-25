import json
from typing import List

class Mesg:

    definitions = {}

    @staticmethod
    def get(mesg_id: str, replace_list: List[str]):
        if Mesg.definitions and len(Mesg.definitions) > 0:
            if mesg_id in Mesg.definitions:
                try:
                    return Mesg.definitions.get(mesg_id).format(*replace_list)
                except IndexError as e:
                    return "メッセージが要求するindexは引数の要素数を超えました。メッセージID:{} 引数:{}".format(mesg_id, ','.join(replace_list))
            else:
                return "メッセージ存在しません。メッセージID:{} 引数:{}".format(mesg_id, ','.join(replace_list))
        else:
            raise Exception("管理ファイルが定義されていません。")


    @staticmethod
    def read_definition(file_path: str):
        try:
            f = open(file_path)
            Mesg.definitions = json.load(f)
            f.close()
        except IOError:
            raise Exception("管理ファイルが開けません。{}".format(file_path))
