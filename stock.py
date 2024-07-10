import yfinance as yf
import streamlit as st
msft= yf.Ticker("MSFT")

import datetime
start_date= st.date_input("Please enter Starting Date",
            datetime.date(2019, 1, 1))
end_date= st.date_input("Please enter Ending Date",
            datetime.date(2022, 12,31))

hist= msft.history(period= "1d", start=f"{start_date}", end=f"{end_date}")

st.dataframe(hist)

st.line_chart(hist.Close)
