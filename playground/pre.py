#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: main.py
# First Edit: 2020-03-12
# Last Change: 14-Mar-2020.
"""
This scrip is for test

"""
import json


def read_json_file(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


plays = read_json_file("plays.json")
invoice = read_json_file("invoices.json")


def statement(invoice, plays):
    totalAmount = 0
    volumeCredits = 0
    result = "Statement for {}\n".format(invoice["customer"])
    format = {
        "lang": "en-US",
        "style": "currency",
        "currency": "USD",
        "minimumFractionDigits": 2,
    }

    for perf in invoice.get("performances"):
        play = plays[perf["playID"]]
        thisAmount = 0

        if play["type"] == "tragedy":
            thisAmount = 40000

            if perf["audience"] > 30:
                thisAmount += 1000 * (perf["audience"] - 30)
        elif play["type"] == "comedy":
            thisAmount = 30000

            if perf["audience"] > 20:
                thisAmount += 10000 + 500 * (perf["audience"] - 20)
            thisAmount += 300 * perf["audience"]
        else:
            raise Exception("unknown type: {}".format(play["type"]))

        volumeCredits += max(perf["audience"] - 30, 0)

        if "comedy" == play["type"]:
            volumeCredits += perf["audience"] // 5

        result += " {}: ${} ( {} seats) \n".format(
            play["name"], thisAmount / 100, perf["audience"]
        )
        totalAmount += thisAmount
    result += "Amount owed is ${} \n".format(totalAmount / 100)
    result += "You earned {} credits \n".format(volumeCredits)

    return result


def main():
    print(statement(invoice, plays))


if __name__ == "__main__":
    main()
