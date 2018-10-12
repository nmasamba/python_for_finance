

import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as dataRetrieve
import datetime


beg_date = datetime.datetime(2012, 1, 5)
end_date = datetime.datetime(2012, 12, 1)

df = dataRetrieve.get_data_google('AAPL', beg_date, end_date) # always worth trying both yahoo and google in case one fails

print(df.head())