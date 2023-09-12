from src.evaluate_performance import calculate_sharpe_ratio, calculate_sortino_ratio, calculate_maximum_drawdown

def display_results(portfolio, returns):
    # Display the results of the optimization and backtesting
    sharpe_ratio = calculate_sharpe_ratio(returns, 0.01)  # assuming 1% risk-free rate
    sortino_ratio = calculate_sortino_ratio(returns, 0.01, 0.02)  # assuming 1% risk-free rate and 2% target return
    maximum_drawdown = calculate_maximum_drawdown(returns)
    assert sharpe_ratio is not None, "Sharpe Ratio should not be None"
    assert sortino_ratio is not be None, "Sortino Ratio should not be None"
    assert maximum_drawdown is not be None, "Maximum Drawdown should not be None"
    print(f'Sharpe Ratio: {sharpe_ratio}')
    print(f'Sortino Ratio: {sortino_ratio}')
    print(f'Maximum Drawdown: {maximum_drawdown}')