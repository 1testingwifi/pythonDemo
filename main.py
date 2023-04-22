# !/usr/bin python3
# encoding: utf-8 -*-
# @file   : main.py
# @author : WangJian
# @Time   : 2023/4/22 10:29
# @Project: pythonProject

import pickle

import json
import base64

if __name__ == '__main__':
    #第一种实现方式：使用的是pickle.dumps模块将一个Python字典对象序列化为二进制数据。接着，它将二进制数据写入文件并从文件中读取数据。最后使用pickle.loads将二进制数据反序列化为Python对象并打印反序列化后的结果
    # # 创建一个新的Person实例
    person = {
        "name": "John",
        "id": 1234,
        "email": "jdoe@example.com",
        "phones": [
            {"number": "555-4321", "type": "HOME"},
            {"number": "555-1234", "type": "WORK"},
        ]
    }

    # 将Person实例序列化为二进制数据
    person_data = pickle.dumps(person)

    # 将二进制数据写入文件
    with open("person.bin", "wb") as f:
        f.write(person_data)

    # 从文件中读取二进制数据
    with open("person.bin", "rb") as f:
        person_data_read = f.read()

    # 反序列化二进制数据为Person实例
    person_read = pickle.loads(person_data_read)

    # 打印反序列化后的数据
    print(person_read)




    # #第二种方法实现：使用 JSON 序列化字典的方式，将序列化后的字符串使用 base64 编码后，
    # # 然后将编码后的数据写入二进制文件。从二进制文件中读取数据时，先读取全部数据并使用 base64 解码，
    # # 再将解码后的数据转换为字典。最后打印字典中的信息。
    # # 先创建一个字典表示一笔数据
    # person = {
    #     "name": "Alice",
    #     "id": 123,
    #     "email": "alice@example.com",
    #     "phones": [
    #         {"number": "555-1234", "type": "HOME"},
    #         {"number": "555-5678", "type": "WORK"}
    #     ]
    # }
    #
    # # 将字典转换为 JSON 格式的字符串，并使用 base64 编码
    # data = base64.b64encode(json.dumps(person).encode())
    #
    # # 将编码后的数据写入二进制文件
    # with open("insertBook.bin", "wb") as f:
    #     f.write(data)
    #
    # # 从二进制文件中读取数据并解析
    # with open("insertBook.bin", "rb") as f:
    #     # 读取全部数据并使用 base64 解码
    #     data = base64.b64decode(f.read())
    #     # 将解码后的数据转换为字典
    #     person = json.loads(data.decode())
    #
    # # 打印 person 的信息
    # print("Name:", person["name"])
    # print("ID:", person["id"])
    # print("Email:", person["email"])
    # for phone in person["phones"]:
    #     print("Phone:", phone["number"], "Type:", phone["type"])