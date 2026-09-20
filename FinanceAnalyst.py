import yfinance as yf
import numpy as np
import pandas
from datetime import date

startDate = str("2026-07-14")
endDate = str("2026-09-19")
stockName = yf.Ticker("AAPL")
dividents = stockName.dividends
inRangeDividents = dividents.loc[startDate:endDate]


#print(inRangeDividents.loc[])
#print(dividents[1])

data1 = yf.download("AAPL", start=startDate, end=endDate)
# # #print(type(data1))
# # #print(data1.loc[:,('Open', 'AAPL')].iloc[0])

# print(data1)

openPrice = round(float(data1.loc[startDate,('Close', 'AAPL')]), 3)
closePrice = round(float(data1.loc["2026-09-18",('Close', 'AAPL')]), 3)
print(openPrice, closePrice)

# def calculateReturns(openPrice, closePrice, inRangeDividents):
#     if not inRangeDividents.empty:
#         totalDividents = 0
#         for divident in inRangeDividents:
#             print(divident)
#             totalDividents += divident
    #     totalReturn = round(((closePrice - openPrice + totalDividents)/openPrice) * 100,2)
    # else:
totalReturn = round(((closePrice - openPrice)/openPrice) * 100,2)
    #return totalReturn


print()
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