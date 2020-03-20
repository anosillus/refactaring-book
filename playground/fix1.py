#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: main.py
# First Edit: 2020-03-12
# Last Change: 15-Mar-2020.
"""
This scrip is for test

"""
import json
import locale


def read_json_file(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


loc = "en_US.utf-8"
locale.setlocale(locale.LC_ALL, loc)

plays = read_json_file("plays.json")
invoice = read_json_file("invoices.json")


def statement(invoice, plays):
    def amountFor(aPerformance):
        result = 0

        if playFor(aPerformance)["type"] == "tragedy":
            result = 40000

            if aPerformance["audience"] > 30:
                result += 1000 * (aPerformance["audience"] - 30)
        elif playFor(aPerformance)["type"] == "comedy":
            result = 30000

            if aPerformance["audience"] > 20:
                result += 10000 + 500 * (aPerformance["audience"] - 20)
            result += 300 * aPerformance["audience"]
        else:
            raise Exception(
                "unknown type: {}".format(playFor(aPerformance)["type"])
            )

        return result

    def playFor(aPerformance):
        return plays[aPerformance["playID"]]

    def volumeCreditsFor(aPreformance):
        # ループの分離
        result = 0
        result += max(aPreformance["audience"] - 30, 0)

        if "comedy" == playFor(aPreformance)["type"]:
            result += aPreformance["audience"] // 5

        return result / 5

    def totalVolumeCredits():
        volumeCredits = 0

        for perf in invoice["performances"]:
            volumeCredits += volumeCreditsFor(perf)

        return volumeCredits

    def totalAmount():
        result = 0

        for perf in invoice.get("performances"):
            result += amountFor(perf)

        return result / 100

    def usd(aNumber):
        return locale.currency(aNumber, grouping=True)

    result = "Statement for {}\n".format(invoice["customer"])
    volumeCredits = 0

    for perf in invoice.get("performances"):
        volumeCredits = totalVolumeCredits()

        result += " {}: {} ( {} seats) \n".format(
            playFor(perf)["name"], usd(amountFor(perf) / 100), perf["audience"]
        )
    # 関数のインライン化
    result += "Amount owed is {} \n".format(usd(totalAmount()))
    result += "You earned {} credits \n".format(usd(volumeCredits))

    return result


def main():
    print(statement(invoice, plays))


if __name__ == "__main__":
    main()
