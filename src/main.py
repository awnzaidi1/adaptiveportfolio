from src.fetch_data import fetch_historical_data
from src.portfolio_optimization import portfolio_optimization
from src.backtest_techniques import backtest_techniques
from src.display_results import display_results

def main(tickers, start_date, end_date, optimization_method):
    data = fetch_historical_data(tickers, start_date, end_date)
    portfolio = portfolio_optimization(data, optimization_method)
    returns = backtest_techniques(portfolio, data)
    display_results(portfolio, returns)

if __name__ == "__main__":
    # TODO for Duckie: Replace with actual values
    tickers = ['AAPL', 'GOOG', 'MSFT']
    start_date = '2020-01-01'
    end_date = '2020-12-31'
    optimization_method = 'mean-variance'
    main(tickers, start_date, end_date, optimization_method)