---
title: "Game Purchase Support System"
excerpt: "A Python based program which uses Steam API data to predict game purchases for users<br/><img src='/images/500x300.png'>"
collection: portfolio
---

# Summary

## Abstract
The goal of this project was to help users choose what games to buy based on releasing games. To tackle this challenge, we aimed to delve into the gaming patterns that influence a user’s purchasing decisions. By examining factors such as game tags, user reviews, and watchtime, we constructed a comprehensive model that can predict critic scores and game engagement based on historical data. Additionally, the similarity between a user’s game library and the video games to buy is calculated using the game tags. Using these, optimization and simulation models are created to optimize game purchases for the given user by maximizing the utility, and to visualize the effect of external factors on game purchases. This visualization allows the user to understand their consumption behavior, and what games they prioritize a majority of the time.

## Methodology
- Exploratory Data Analysis (EDA) conducted to find the correlation of existing parameters within the dataset, and their impact on the three coefficients we were looking for; metacritic score, engagement and similarity.
- Regression models built to predict missing metacritic scores, predicting player engagement and calculating the similarity coefficients between a player's existing game and the new game they are looking at.
- Optimization models built to maximize these three coefficients. The first model was an IP, which was a knapsack model to maximize the three coefficients. 
- The second model was a greedy knapsack, iterating monthly in order to simulate game purchases given that they get released per month rather than at once.
- The third model was a simulation model, where Monte Carlo simulations were used to randomly distribute game release dates and consumer preferences; to better emulate real-world scenarios.

# Details

## Data Collection, Parsing and Cleaning

The two data sources we used to comprehensively encompass the data from the video games on Steam are Steam’s official Web API and Steam Spy’s API. The official Web API was accessed from their website, while Steam Spy is a third-party statistics website, and their API is based on the original one. From Steam, we extracted the games’ names, days since release, and Metacritic scores. Then, from Steam Spy, we extracted each game’s ratio of positive reviews and price. The Metacritic score of each game represents its critical reception which is directly correlated to overall reviews, with higher scores indicating more favorable reviews. Then, we modified the Metacritic score into a binary indicator, with 0 being lower than average, and 1 being higher than average. This new modified Metacritic score will be predicted for games with missing scores and releasing games. It is one of the key factors in our optimization model later on to quantify each game’s overall consensus on how good the game is. 

In addition, from Steam Spy, we also extracted the user-defined tags for each game which is similar to the genre. This dataset contains 371 different tags and the number of user votes that tag has for each game. For example, the tags include FPS (First-Person Shooter), RPG (Role-Playing Game), and Multiplayer, in which each has a different number of votes between different games such as Counter-Strike 2, a popular FPS game, and Undertale, a role-playing indie game. Then, we utilized one-hot encoding on this data and used it to calculate the similarities between a user’s existing gaming library and other games to purchase. 

Besides Steam, we used data from Sully Gnome, a third-party statistics and analytics website for Twitch, a live-streaming platform where gamers watch gaming influencers and live streamers play. This was to capture more nuances in user preferences when purchasing games. We extracted each game’s average watch time per viewer which we call engagement. We estimated engagement as how much time a player spends watching the game as we found sources that suggested some correlation between engagement in terms of playtime and watchtime [7]. Then, we divided engagement into 3 equal thirds and an indicator of 0, 1, and 2, with 0 being the lowest third, and 2 being the highest third. This will also be predicted and fed into our optimization model to quantify each game’s overall consensus on engagement.

