      def calculate_sharpe_ratio(returns, risk_free_rate):
          # Calculation of Sharpe Ratio
          excess_returns = returns - risk_free_rate
          sharpe_ratio = np.mean(excess_returns) / np.std(excess_returns)
          return sharpe_ratio

      def calculate_sortino_ratio(returns, risk_free_rate, target_return):
          # Calculation of Sortino Ratio
          excess_returns = returns - risk_free_rate
          downside_risk = np.std(excess_returns[excess_returns < target_return])
          sortino_ratio = np.mean(excess_returns) / downside_risk
          return sortino_ratio

      def calculate_maximum_drawdown(returns):
          # Calculation of Maximum Drawdown
          cumulative_returns = (1 + returns).cumprod()
          cumulative_roll_max = cumulative_returns.cummax()
          drawdown = cumulative_roll_max - cumulative_returns
          maximum_drawdown = drawdown.max()
          return maximum_drawdown