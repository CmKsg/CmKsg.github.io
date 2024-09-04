---
title: "Crypto Dashboard Back-end"
collection: projects
permalink: /projects/crypto
excerpt: 'The backend database for a crypto dashboard.'
date: 2024-08-01
venue: ''
---

The client requested a back-end built using API pulls from popular De-Fi databases like defillama and coingecko. This project accesses their API through Python, and cleans the data and calculates different factors using Pandas dataframes.

The client wants a dashboard that is refreshed once every X minutes, and thus this was the time-frame in which the dataframe calculations and API pulls has to be done.

For this specific application, the client wants to calculate factors for fully-diluted valuation for popular crypto protocols, specifically at decentralized exchanges (DEX) within which cryptocurrencies are exchanged. Most exchanges have their own native coins, so their fully diluted valuation can be calculated using their coin's FDV, and then compared against the volume traded as well as the fees gained on the network.

The coin FDVs are retrieved from CoinGecko, which has an extensive API that lists coin information. These FDVs are then compared against the protocol volume and fees, which are retrieved from Defillama. 

An issue regarding data from Defillama compared to CoinGecko is a mismatch in indexes. Defillama does not provide the same indexes for coins as CoinGecko does, so manual selection of specific protocols had to be done, which was determined by selecting top protocols in terms of volume traded and fees.

These top protocols also often consisted of multiple entries under the same main protocol; for example AAVE had both AAVE v2 and AAVE v3 operating with the same native currency. Thus, these had to be combined in Pandas manually as well.

The resulting dataframe, for selected protocols is the following:

<br/><img src="/images/crypto.png">
