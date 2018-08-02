#!/usr/bin/env python3.6
"""
Stock
=====

Playing with stock APIs.
"""
from iexfinance import Stock


class StockTest(object):

    def __init__(self):
        pass

    @staticmethod
    def run():
        tsla = Stock('VOO')
        price_open = tsla.get_open()
        price_now = tsla.get_price()
        print(price_open)
        print(price_now)

    @staticmethod
    def plot():
        from iexfinance import get_historical_data

        from datetime import datetime

        import matplotlib.pyplot as plt

        start = datetime(2017, 2, 9)

        end = datetime(2017, 5, 24)
        f = get_historical_data("VOO", start, end, output_format='pandas')

        plt.plot(f["close"]-f["open"])

        plt.title('Time series chart for VOO')

        plt.show()


def _main(args):
    pass
    StockTest.run()
    StockTest.plot()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Stock playground.")
    args = parser.parse_args()
    _main(args)
