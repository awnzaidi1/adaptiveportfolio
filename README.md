# adaptiveportfolio

## Portfolio Optimiser

The Portfolio Optimiser is a feature that allows you to backtest a portfolio of ETFs against the SPY ETF. You can configure the ETFs and the date range for the backtest. The results can be saved and loaded for future reference.

The backtesting includes the following techniques:
- Multi time frame Momentum
- Minimum Variance
- Mean-variance optimization
- Markowitz optimization
- Modern portfolio theory
- Genetic algorithms
- Particle swarm optimization

To use the Portfolio Optimiser, navigate to the root directory of the project and run the following command:

```
python src/ui_handler.py
```

Then, open a web browser and navigate to `http://localhost:5000`. Enter the ETFs and date range, then click "Submit" to run the backtest. The results will be displayed on the page.