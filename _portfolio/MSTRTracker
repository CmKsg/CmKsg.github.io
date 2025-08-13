---
title: "ASXN MSTR Acquisition Tracker"
excerpt: "A tracker for ASXN, a crypto research firm, for tracking recent acquisitions of Microstrategy using SEC Edgar API Data. <br/>"
collection: portfolio
---
## Summary
For this project, I used the SEC Edgar API to pull 8-K form filings made by MSTR and used a BERT model to parse through and detect possible acquisitions of Bitcoin by the company.

## Methodology
Due to this work being done for my client, I cannot share the exact code for this project. However, the methodology was as follows:

1) Pull most recent SEC filing, check if it is more recent than the last recorded entry (which is in a csv file). If it is more recent, append it and check for the next one until no more recent entries.
2) Conduct data manipulation to only pull in required fields from the lengthy json file that the 8-K form contains.
3) Use BERT to divide up the filing raw text into multiple topic clusters. Analyze each one for keywords.
4) Use traditional regex to scrape the values themselves, append to a dataframe and contrast against market cap and other values.
5) Display this data on a dashboard using React, adding interactibility. A lot of calculations were done using the values I pulled from different APIs such as yfinance, coingecko and the base Edgar API.

Below are a few example images of the dashboard:

### Cost Basis:
<br/><img src="/images/Portfolio6/CostBasisGraph.png">

### Acquisitions vs. Price:
<br/><img src="/images/Portfolio6/AcquisitionsAndPriceGraph.png">

### Total Holdings Over Time:
<br/><img src="/images/Portfolio6/HoldingsGraph.png">

### NAV Premium:
<br/><img src="/images/Portfolio6/NAVPremiumGraph.png">

### NAV Premium Against Market Cap:
<br/><img src="/images/Portfolio6/NAVvsMCapGraph.png">
