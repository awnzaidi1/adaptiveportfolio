import yfinance as yf
from tkinter import *

def fetch_historical_data(tickers, start_date, end_date):
    # Fetch historical price data for selected tickers using Yahoo Finance API
    data = yf.download(tickers, start=start_date, end=end_date)
    assert not data.empty, "Data should not be empty"
    return data

def get_user_input():
    # Create a GUI to get user input
    root = Tk()
    Label(root, text="Enter at least one ETF (For multiple ETFs, separate them by comma):").pack()
    etf = StringVar()
    Entry(root, textvariable=etf).pack()
    Label(root, text="Enter start date (YYYY-MM-DD):").pack()
    start_date = StringVar()
    Entry(root, textvariable=start_date).pack()
    Label(root, text="Enter end date (YYYY-MM-DD):").pack()
    end_date = StringVar()
    Entry(root, textvariable=end_date).pack()
    Button(root, text="Submit", command=root.quit).pack()
    root.mainloop()
    return etf.get().split(','), start_date.get(), end_date.get()

tickers, start_date, end_date = get_user_input()
fetch_historical_data(tickers, start_date, end_date)