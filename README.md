# StockPredictor
Predict the values of stocks by using SEC filing data.
# Data Collection
Downloaded data from EDGAR system from the SEC containing lists of balance sheets from quarters dating back to 2008. Separated out useful data, and selected a few useful training features. Features include: Assets, NetIncome, CashAndCashEquivalents.

Programmed python scripts using yahoo finance api to add to this data the stock price at the time. This step was necessary because the SEC data did not include information about the valuation of the company. Appended the market cap as the target feature to the data.
# Model Training
Python used with numpy to train Linear Regressions, Decision Trees, and Neural Networks with varying hyperparameters, with mixed results.
