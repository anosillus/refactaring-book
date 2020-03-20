#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: main.py
# First Edit: 2020-03-12
# Last Change: 16-Mar-2020.
"""
This scrip is for test

"""
import json
import locale
from pathlib import Path

from statement import create_statement


def read_json_file(file_name):
    data_path = str(Path("./../data/{}".format(file_name)))
    with open(data_path) as json_file:
        return json.load(json_file)


loc = "en_US.utf-8"
locale.setlocale(locale.LC_ALL, loc)

plays = read_json_file("plays.json")
invoice = read_json_file("invoices.json")


def usd(aNumber):
    return locale.currency(aNumber, grouping=True)


def renderPlainText(data):
    result = "Statement for {}\n".format(data["customer"])

    for perf in data["performances"]:
        result += " {}: {} ( {} seats) \n".format(
            perf["name"], usd(perf["amount"]), perf["audience"],
        )
    result += "Amount owed is {} \n".format(usd(data["totalAmount"]))
    result += "You earned {} credits \n".format(
        usd(data["totalVolumeCredits"])
    )

    return result


def main():
    statementData = create_statement(invoice, plays)
    a = renderPlainText(statementData)
    print(a)


if __name__ == "__main__":
    main()
