---
title: "Forecasting Stock Prices"
excerpt: "An forecasting project in which Tencent Music Entertainment stock prices were predicted using two methods, which were then compared against one another. <br/>"
collection: portfolio
---
## Summary
The closing prices for the month of January 2022 for the company Tencent Music Entertainment Group (TME) was forecasted through the use of traditional forecasting methods. First, Exploratory Data Analysis (EDA) was conducting to understand the trends within the 2021 data. Then, through these observations, two methods; the double moving average method and the mean reversion method were chosen to forecast the prices. These methods were then used to predict the closing prices for the month of January 2022. The better forecast, through the use of MSE and visual comparison, was chosen to be the double moving average method.

## Methodology
- Using EDA, 4 different trends were identified within the TME Closing Prices dataset
- Forecasting was conducted through the use of the double moving average and mean reversion methods. The double moving average focused on the downwards trend in the closing prices while the mean reversion method focused on the variation within the change in the closing prices.
- Window sizes, and other parameters were determined through the use of sensitivity analysis and data engineering on the 2021 data.
- The forecasts were evaluated against the actual data.The double moving average method had a lower MSE, MAE and MAPE, and included a downward trend.

# Details

## Exploratory Data Analysis

The primary objective is to use the training data for the closing prices of TME from January 1st to December 31st of 2021 in order to forecast the closing prices of January 2022. Throughout the report, the NYSE TME closing prices data from Yahoo Finance will be analyzed and evaluated. As of the 31st December 2021, the stock has a volume of over 12 million shares and a closing price of 6.85$. 

Furthermore, the TME closing prices for January 2022 will be forecast using two different methods; double moving average and forecasting using mean reversion. Then, these two methods will be compared using error indicators such as MAPE, MSE and MAD, as well as visual analysis.

<br/><img src="/images/Portfolio4/Portfolio4Diagram1.png">

Throughout 2021, there were 4 different “states” of trend within the TME stock closing prices.

**Trend 1:** There was a sudden increase in the closing prices of Tencent Music during the month of January, which remained stable for a few weeks. This sudden trend was due to the acquisition of Lazy Audio, a music streaming platform, for 415$ million. This purchase was rallied by Wall Street, which caused a jump in the closing price of 38%.
**Trend 2 and Trend 3:** Following this 38% increase, there was a period of stationarity in the closing prices, until there was a jump on March 15th and a larger fall on March 22nd. This rise and the subsequent fall were both the result of the firm’s announcement that they would create a joint venture record label with Warner Music in China.
**Trend 4:** Following the sudden crash, there was a period of decline in the stock prices for Tencent as the Chinese government continued to crack down on the tech sector, including the multiple music apps that Tencent owned. There was also increased competition from other brands in the same sector. These factors resulted in a net decrease in the profits of Tencent by 763$ million, followed by a continuous decline in the closing prices.

Two different methods were used to forecast the closing prices for January 2022. The first method was the double moving average method, which predicts closing prices based on previous closing prices for window size k. The second method was based on the mean reversion method which attempted to predict closing prices using the changes that followed a certain value of the closing price for each day.

Given the highly random nature, and large fluctuations of the stock price, instead of trying to create a model using the closing prices, the two methods instead forecast based on the change in the closing prices. 

<br/><img src="/images/Portfolio4/Portfolio4Diagram2.png">

From the two graphs, it can be seen that there is no clear average and trend from the closing prices due to the large jumps and fluctuations within the data. This means that a forecast based on this data could be inaccurate, especially with high window size, as there is a large difference between the closing prices of the first three months and the rest of the data.

There is also a visible difference in the variance within the graph of the change in the closing prices, as in the first three months, the data is highly varied, and then, the variance starts decreasing over time. The change in the closing prices data seems to be centered around a mean of ~0.

## Double Moving Average [Window Size = 55]

Testing all possible window sizes within the range of  2k55 and graphing all the resulting errors generated graphs with 53 different lines within them. This made it impossible to gather any useful information out of the graphs generated. Instead, the MAD and MSE were graphed, and the window size with the lowest errors was chosen.

From observation, there is a clear trend that indicates that window size is inversely proportional to the error, meaning as window size increases, MSE and MAD both decrease. This visual observation was supported by the statistic that the lowest error was when k was equal to 55, where the MAD was 0.296 and MSE was 0.144. Therefore, a window size of 55 was deemed appropriate for the forecast.

<br/><img src="/images/Portfolio4/Portfolio4Diagram3.png">

When visually analyzing the forecast compared to the future data itself, it can be seen that the trend is the same, as both the forecast and the data trends downwards. There also does not appear to be too much variation between the data and the forecast. These visual observations are supported by the calculation of the MSE, MAD and MAPE, which were 0.359, 0.178 and 5.5% respectively. Therefore, this model is accurate in the sense that it predicts the trend correctly, and has a low amount of error.

## Mean Reversion

This method attempts to take a closer look at the variation and volatility within the training data of the closing prices and attempts to incorporate some of that variation into the forecast itself. The method was derived using the idea of the mean reversion method, a popular idea that is used by stock market investors. The mean reversion method predicts a trend in the change of the closing price by following the idea that a high closing price discourages investors from investing, while a low closing price encourages them to invest, which means that as closing prices get lower, the likelihood of an increase in the closing price in the next day gets higher, and as the closing prices get higher, the likelihood of a decrease in the closing price in the next day gets higher. 

The model itself applies this method by changing the closing prices based on the price difference training data. First, the price difference between day [i-1] and day [i] is predicted by finding the closest value to the initial price difference, then the price difference between day [i] and day [i+1] is predicted by finding out how the price changes following the change in the previous day. This is repeated until the 20th day. For this method, the appropriate window size was deemed to be 200, as at that point the closing price change’s variance had stabilized, and there was a clear downwards trend in the closing price following the trend that occurred after the 24th of March.

<br/><img src="/images/Portfolio4/Portfolio4Diagram4.png">

It can be seen above, that the forecast (blue) was off-target, as it didn’t have a downwards trend like the actual closing prices (orange), and predicted values that were far from the actual data, and often predicted the opposite of what actually occurred.

The MAD and MSE for this forecast against the actual prices were 1.191 and 2.768, while the MAPE was 19.219%. The MAPE alone showcases how far off the predictions were from the actual data, and since there is also no downwards trend like the actual data, this forecast was not viable.

[Click Here to Open the Folder Containing the Python Code](https://cemkesisoglu.github.io/code)
