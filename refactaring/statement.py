#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: stament.py
# First Edit: 2020-03-16
# Last Change: 17-Mar-2020.
"""
This scrip is for test

"""
import itertools


def create_statement(invoice, plays):
    class performanceCalucurator:
        def __init__(self):
            self.play = ""
            self.amount = 0
            self.volumeCredits = 0

        def __call__(self, statementData, plays):
            for performance, play in itertools.product(
                statementData["performances"], plays.keys()
            ):
                if performance["playID"] == play:
                    performance.update(plays[play])
            self.play = play
            self.amount = 

    def enritchPerformance(statementData, plays):
        def merge_play_and_performance(statementData, plays):
            # 呼び出し元のStatmentDataにplaysの値を追加している。
            # 汚いが元のデータがlistとdictが混在してるようなやつなので仕方がない。
            # 本のjavaのメソッドの内容が良くわからなかったので…。
            # スコープが汚くて見ずらいが、それはpythonが悪い。

            for performance, play in itertools.product(
                statementData["performances"], plays.keys()
            ):
                if performance["playID"] == play:
                    performance.update(plays[play])

                # return statementData

        def calc_amount(data):
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
                    raise Exception(
                        "unknown type: {}".format(aPerformance["type"])
                    )

                return result / 100

            for perf in data["performances"]:
                perf.update({"amount": amountFor(perf)})

        merge_play_and_performance(statementData, plays)
        calc_amount(statementData)

    def volumeCreditsFor(aPerformance):
        result = 0
        result += max(aPerformance["audience"] - 30, 0)

        if "comedy" == aPerformance["type"]:
            result += aPerformance["audience"] // 5

        return result / 5

    def totalVolumeCredits(data):
        volumeCredits = 0

        for perf in data["performances"]:
            volumeCredits += volumeCreditsFor(perf)

        return volumeCredits

    def totalAmount(data):
        result = 0

        for perf in data["performances"]:
            result += perf["amount"] / 100

        return result

    statementData = {}
    statementData["customer"] = invoice["customer"]
    statementData["performances"] = invoice["performances"]
    calculator = performanceCalucurator()
    enritchPerformance(statementData, plays)
    statementData["totalAmount"] = totalAmount(statementData)
    statementData["totalVolumeCredits"] = totalVolumeCredits(statementData)

    return statementData
