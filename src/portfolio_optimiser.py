import yfinance as yf
import pandas as pd
from datetime import datetime

class PortfolioOptimiser:
    def __init__(self, etfs, start_date='1980-01-01', end_date=datetime.today().strftime('%Y-%m-%d')):
        self.etfs = etfs
        self.start_date = start_date
        self.end_date = end_date
        self.benchmark = 'SPY'
        self.data = {}

    def fetch_data(self):
        for etf in self.etfs:
            try:
                self.data[etf] = yf.download(etf, start=self.start_date, end=self.end_date)
            except Exception as e:
                print(f"Could not fetch data for {etf}. Error: {str(e)}")

    def backtest(self):
        # TODO for Duckie: Implement backtesting logic here
        # This should include the following techniques:
        # - Multi time frame Momentum
        # - Minimum Variance
        # - Mean-variance optimization
        # - Markowitz optimization
        # - Modern portfolio theory
        # - Genetic algorithms
        # - Particle swarm optimization

    def save_results(self, filename):
        # TODO for Duckie: Implement logic to save backtesting results to a file

    def load_results(self, filename):
        # TODO for Duckie: Implement logic to load backtesting results from a file