import pandas_datareader as web
import datetime
from datetime import timedelta

def get_most_recent_business_day():
   """
      This function uses the datetime module to get the most recent business day.

      Return Value:
         The most recent business day as a datetime object: YYYY-MM-DD

      Citation:
      https://stackoverflow.com/questions/2224742/most-recent-previous-business-day-in-python
   """

   # Get the most recent business day
   lastBusDay = datetime.datetime.today()
   if datetime.date.weekday(lastBusDay) == 5:      #if it's Saturday
      lastBusDay = lastBusDay - datetime.timedelta(days = 1) #then make it Friday
   elif datetime.date.weekday(lastBusDay) == 6:      #if it's Sunday
      lastBusDay = lastBusDay - datetime.timedelta(days = 2); #then make it Friday
      # If current date is not a business day (weekend), most recent business day is Friday
   
   lastBusDay = lastBusDay.date() # strip the time from the datetime string

   return lastBusDay


def get_stock_data(tickers, start_date, end_date):
   """
      This function uses pandas_datareader module to grab historical stock data.

      Params: 
         1) tickers
               type: list
               desc: stock tickers where each ticker is represented by a string
         2) start_date 
               type: datetime
               desc: start date of stock data
         3) end_date
               type: datetime
               desc: end date of stock data

      Return Value:
         A dictionary where each key is the stock ticker and the value is that respective
         ticker's data
   """
   
   res = {}
   for ticker in tickers:
      success = False
      counter = 0

      while not success and counter < 50:
         try:
            res[ticker] = web.DataReader(ticker,'yahoo', start_date - timedelta(days=counter), end_date - timedelta(days=counter)).head(1).to_dict('list')
            success = True
         except:
            counter = counter + 1

   return res