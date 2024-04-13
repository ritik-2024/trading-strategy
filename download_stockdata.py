import yfinance as yf
import pandas as pd

## ---for particular stock download

# stack_name='RELIANCE'
# data = yf.download(f'{stack_name}.NS')
# # print(data)
# data.to_csv(f'Data/{stack_name}.CSV')


##-- download multiple stocks--

equity_details = pd.read_csv('EQUITY_L.csv')
# print(equity_details.SYMBOL)

for name_of_stock in equity_details.SYMBOL[:5]:
    print(name_of_stock)
    try:
        data = yf.download(f'{name_of_stock}.NS')
        data.to_csv(F'Data/{name_of_stock}.CSV')
    except Exception as e:
        print(f'{name_of_stock} ===> e')
    
    
print("All data Download complete")
    