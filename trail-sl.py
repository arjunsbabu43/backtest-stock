# nifty bees 1.4
# federal bank 4.1

import yfinance as yf


def check_stop_loss(stock, buy_price, percentage_change, purchase_date):
    ticker = yf.Ticker(stock)
    historical_data = ticker.history(start=purchase_date)
    sl_set = 0
    factor = 2
    for i in range(0, len(historical_data)):
        print(f"Date is {historical_data.index[i]} ")
        close_price = historical_data['Close'][i]
        print(f"close price is {close_price}")
        low_price = historical_data['Low'][i]
        print(f"low price is {low_price}")
        percent_change = (close_price - buy_price) / buy_price * 100
        print(f"percent_change is {percent_change}")

        if sl_set == 0 and percent_change >= factor * percentage_change:
          times = int(percent_change / percentage_change)
          stop_loss_price = buy_price + (buy_price * (times - 1)*percentage_change / 100)
          print(f" initial Stoploss set at {stop_loss_price} on {historical_data.index[i]}")
          sl_set = 1
          factor = factor + 1
                   
        if sl_set == 1 and stop_loss_price >= low_price:
            print(f"Stop triggered at {stop_loss_price} on {historical_data.index[i]}")
            gain = (stop_loss_price - buy_price)*100/buy_price
            print(f"You got a gain of {gain}")
            break
        elif sl_set == 1 and stop_loss_price < low_price and percent_change >= factor * percentage_change :
          times = int(percent_change / percentage_change)
          stop_loss_price = buy_price + (buy_price * (times - 1)*percentage_change  / 100)
          print(f"Stoploss at {stop_loss_price} on {historical_data.index[i]}")
          factor = factor + 1

          


# Example usage
stock_name = "FEDERALBNK.NS"  # Replace with the stock ticker for IDFC First Bank
buy_price = 124  # Replace with your buy price (x)
percentage_change = 5   # Replace with your desired percentage change (y)
purchase_date = "2023-03-28"  # Replace with your purchase date (z)

check_stop_loss(stock_name, buy_price, percentage_change, purchase_date)
