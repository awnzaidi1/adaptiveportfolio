from flask import Flask, request, render_template
from portfolio_optimiser import PortfolioOptimiser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        etfs = request.form.get('etfs').split(',')
        start_date = request.form.get('start-date')
        end_date = request.form.get('end-date')
        optimiser = PortfolioOptimiser(etfs, start_date, end_date)
        optimiser.fetch_data()
        optimiser.backtest()
        # TODO for Duckie: Implement logic to display backtesting results
    return render_template('ui.html')

if __name__ == '__main__':
    app.run(debug=True)