#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: test.py
# First Edit: 2020-03-13
# Last Change: 16-Mar-2020.
"""
This scrip is for test

"""
import json  # 必ず必要
import locale
import math


# a = {}
# a["aaa"] = 50
# print(a)

# print(max(50, 20))
# print(50 / 3)
# print(math.floor(50 / 3))
# print(50 // 3)
#
# print(locale.setlocale(locale.LC_ALL, ""))
# value = 123456789
#
# l = locale.setlocale(
#     locale.LC_ALL, ""
# )  # LC_CTYPE=en_US.UTF-8;LC_NUMERIC=fr_FR.UTF-8;LC_TIME=fr_FR.UTF-8;LC_COLLATE=en_US.UTF-8;LC_MONETARY=fr_FR.UTF-8;LC_MESSAGES=en_US.UTF-8;LC_PAPER=fr_FR.UTF-8;LC_NAME=fr_FR.UTF-8;LC_ADDRESS=fr_FR.UTF-8;LC_TELEPHONE=fr_FR.UTF-8;LC_MEASUREMENT=fr_FR.UTF-8;LC_IDENTIFICATION=fr_FR.UTF-8
# s = locale.currency(value, grouping=True)  # 123 456 789,00 €
# print(s)
# locale.setlocale(locale.LC_ALL, "en_US.utf-8")
# s = locale.currency(value, grouping=True)
# print(s)
# # print(locale.setlocale(locale.LC_ALL, "en_US"))
# "English_United States.1252"


def read_json_file(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


plays = read_json_file("plays.json")
invoice = read_json_file("invoices.json")


print(plays)

# print()
#
# a = {}
# a["plays"] = plays
# print(a)
#
# print(a)
# a.update(invoice)
# print(a)
# print()
# print(a.keys())
# print(a["plays"].keys())
# print(a["customer"])
# print(a["performances"])
#
# print(content2)
# print(type(content2))
# print(content2.keys())
# # print(content2.get("hamlet"))
# print(list(content2.keys())[0])
# print()
#
# print(content2.get("performances"))
# a = content2.get("performances")
#
# print(a[0])
# print(type(a[0]))
# print(a[0].get("playID"))
# pid = a[0].get("playID")
#
# print("test")
# print(a[0]["playID"])
# print(content)
#
# print(content[pid])
# print(content[pid]["type"])
