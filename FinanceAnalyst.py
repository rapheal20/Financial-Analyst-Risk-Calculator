import yfinance as yf
import numpy as np
import pandas
from datetime import date


#data = yf.Ticker("AAPL")
data1 = yf.download(["AAPL","MSFT"], start="2026-09-14", end="2026-09-25")
#print(type(data1))
#print(data1.loc[:,('Open', 'AAPL')].iloc[0])


print(data1)

openPrice = data1.loc["2026-09-14",('Open', 'AAPL')]
closePrice = data1.loc["2026-09-18",('Close', 'AAPL')]
print(openPrice, closePrice)

#.loc is used to index in the dataframe
# yfiance returns a multi index column dataframe
# so the date is used to index the rows and the tuple is used to index the columns



# dataset = {
#     'col1' : ["test1", "test2", "test3"],
#     'col2'  : ["test4", "test5", "test6"]
# }

# data = pd.DataFrame(dataset)
# # pd.DataFrame.head()
# print(data["col1"])