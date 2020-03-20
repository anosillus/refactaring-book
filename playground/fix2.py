#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: main.py
# First Edit: 2020-03-12
# Last Change: 16-Mar-2020.
"""
This scrip is for test

"""
import itertools
import json
import locale


def read_json_file(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


loc = "en_US.utf-8"
locale.setlocale(locale.LC_ALL, loc)

plays = read_json_file("plays.json")
invoice = read_json_file("invoices.json")


def renderPlainText(data):
    def amountFor(aPerformance):
        result = 0

        if aPerformance["type"] == "tragedy":
            result = 40000

            if aPerformance["audience"] > 30:
                result += 1000 * (aPerformance["audience"] - 30)
        elif aPerformance["type"] == "comedy":
            result = 30000

            if aPerformance["audience"] > 20:
                result += 10000 + 500 * (aPerformance["audience"] - 20)
            result += 300 * aPerformance["audience"]
        else:
            raise Exception("unknown type: {}".format(aPerformance["type"]))

        return result

    def volumeCreditsFor(aPerformance):
        result = 0
        # print(aPerformance)
        result += max(aPerformance["audience"] - 30, 0)

        if "comedy" == aPerformance["type"]:
            result += aPerformance["audience"] // 5

        return result / 5

    def totalVolumeCredits():
        volumeCredits = 0

        for perf in data["performances"]:
            volumeCredits += volumeCreditsFor(perf)

        return volumeCredits

    def totalAmount():
        result = 0

        # for perf in data["performances"]:
        result += amountFor(perf)

        return result / 100

    def usd(aNumber):
        return locale.currency(aNumber, grouping=True)

    result = "Statement for {}\n".format(data["customer"])
    volumeCredits = 0

    for perf in data["performances"]:
        volumeCredits = totalVolumeCredits()

        result += " {}: {} ( {} seats) \n".format(
            perf["name"], usd(amountFor(perf) / 100), perf["audience"],
        )
    result += "Amount owed is {} \n".format(usd(totalAmount()))
    result += "You earned {} credits \n".format(usd(volumeCredits))

    return result


def statement(invoice, plays):
    def enritchPerformance(statementData, plays):
        # 呼び出し元のStatmentDataにplaysの値を追加している。
        # 汚いが元のデータがlistとdictが混在してるようなやつなので仕方がない。
        # 本のjavaのメソッドの内容が良くわからなかったので…。
        # スコープが汚くて見ずらいが、それはpythonが悪い。

        for performance, play in itertools.product(
            statementData["performances"], plays.keys()
        ):
            if performance["playID"] == play:
                performance.update(plays[play])

    statementData = {}
    statementData["customer"] = invoice["customer"]
    statementData["performances"] = invoice["performances"]
    enritchPerformance(statementData, plays)

    return renderPlainText(statementData)


def main():
    print(statement(invoice, plays))


if __name__ == "__main__":
    main()
