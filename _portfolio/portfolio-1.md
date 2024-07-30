---
title: "Game Purchase Support System"
excerpt: "A Python based program which uses Steam API data to predict game purchases for users<br/><img src='/images/500x300.png'>"
collection: portfolio
---

## Summary
The goal of this project was to help users choose what games to buy based on releasing games. To tackle this challenge, we aimed to delve into the gaming patterns that influence a user’s purchasing decisions. By examining factors such as game tags, user reviews, and watchtime, we constructed a comprehensive model that can predict critic scores and game engagement based on historical data. Additionally, the similarity between a user’s game library and the video games to buy is calculated using the game tags. Using these, optimization and simulation models are created to optimize game purchases for the given user by maximizing the utility, and to visualize the effect of external factors on game purchases. This visualization allows the user to understand their consumption behavior, and what games they prioritize a majority of the time.

## Methodology
- Exploratory Data Analysis (EDA) conducted to find the correlation of existing parameters within the dataset, and their impact on the three coefficients we were looking for; metacritic score, engagement and similarity.
- Regression models built to predict missing metacritic scores, predicting player engagement and calculating the similarity coefficients between a player's existing game and the new game they are looking at.
- Optimization models built to maximize these three coefficients. The first model was an IP, which was a knapsack model to maximize the three coefficients. 
- The second model was a greedy knapsack, iterating monthly in order to simulate game purchases given that they get released per month rather than at once.
- The third model was a simulation model, where Monte Carlo simulations were used to randomly distribute game release dates and consumer preferences; to better emulate real-world scenarios.

# Details
<details open>
<summary>
## Data Collection, Parsing and Cleaning

The two data sources we used to comprehensively encompass the data from the video games on Steam are Steam’s official Web API and Steam Spy’s API. The official Web API was accessed from their website, while Steam Spy is a third-party statistics website, and their API is based on the original one. From Steam, we extracted the games’ names, days since release, and Metacritic scores. Then, from Steam Spy, we extracted each game’s ratio of positive reviews and price. The Metacritic score of each game represents its critical reception which is directly correlated to overall reviews, with higher scores indicating more favorable reviews. Then, we modified the Metacritic score into a binary indicator, with 0 being lower than average, and 1 being higher than average. This new modified Metacritic score will be predicted for games with missing scores and releasing games. It is one of the key factors in our optimization model later on to quantify each game’s overall consensus on how good the game is. 

In addition, from Steam Spy, we also extracted the user-defined tags for each game which is similar to the genre. This dataset contains 371 different tags and the number of user votes that tag has for each game. For example, the tags include FPS (First-Person Shooter), RPG (Role-Playing Game), and Multiplayer, in which each has a different number of votes between different games such as Counter-Strike 2, a popular FPS game, and Undertale, a role-playing indie game. Then, we utilized one-hot encoding on this data and used it to calculate the similarities between a user’s existing gaming library and other games to purchase. 

Besides Steam, we used data from Sully Gnome, a third-party statistics and analytics website for Twitch, a live-streaming platform where gamers watch gaming influencers and live streamers play. This was to capture more nuances in user preferences when purchasing games. We extracted each game’s average watch time per viewer which we call engagement. We estimated engagement as how much time a player spends watching the game as we found sources that suggested some correlation between engagement in terms of playtime and watchtime. Then, we divided engagement into 3 equal thirds and an indicator of 0, 1, and 2, with 0 being the lowest third, and 2 being the highest third. This will also be predicted and fed into our optimization model to quantify each game’s overall consensus on engagement.



## Prediction Models

Given that some games do not possess a Metacritic score or an engagement score due to missing features in the dataset, prediction models are used to fill in the blanks. These prediction models will also be used to generate the required Metacritic and engagement scores for releasing games so that they can be fed into the optimization model.

In general, we first predict if a game’s critical score is above or below average (0 or 1), then feed all of the remaining features including the predicted Metacritic scores into a second model that predicts player engagement. Predicting Metacritic scores first allows us to fill in any null Metacritic score values in the dataset and maximizes the amount of data used to train the secondary model to improve generalization abilities.

Our initial models using the basic steam features present in the dataset (excluding tag data) yielded significantly poor results when predicting Metacritic score. Both linear and binary classification models failed to achieve any useful predictions or insights into the relationship between the basic steam features and Metacritic scores.

When doing EDA, we found how the number of positive and negative reviews were highly correlated but removing either of them did not improve the accuracy. As such, we turned to feature engineering by dividing the number of positive reviews by the total number of reviews and we found the ratio of positive
reviews, which happened to be highly correlated with Metacritic scores.

Using the newly engineered ratio feature on its own in a decision tree classifier for binary classification yielded a significant improvement in accuracy. Compared to our original attempts yielding an accuracy of 0.3, we managed to achieve a cross-validated (CV) mean accuracy, recall, and precision of 0.706, 0.740, and 0.727, respectively.

In instances where we are unable to calculate the ratio of positive reviews with certainty, such as when there are too few or no reviews for a game due to its pending release, we use its tags to predict the Metacritic score, to infer if the game would have a below or above average critical reception. When feeding a game’s one hot encoded tags into a logistic regression model, we obtain a CV mean accuracy, recall, and precision of 0.662, 0.742, and 0.678, respectively.

In the process of training the predictive models, we used feature engineering and feature selection to try and maximize the obtained accuracy on the validation set. In both cases, we used grid searching to find the best hyper-parameters for the models. Max-depth and minimum sample split for the decision tree classifier, and regularization strength ‘C’ for the logistic regressor.

While both models can perform significantly better than random (accuracy of 0.5), using review ratios in the decision tree classifier yields much higher accuracy than the logistic regression employing tags. As such, whenever possible, when reviews can be found, we use the decision tree classifier to predict Metacritic scores. Namely, when there are more than 5 total reviews, the ratio is calculated and fed into the decision tree classifier, if there are fewer than 5 reviews for a game, then the tags of the game and the logistic regression are used to predict the Metacritic score instead.

When predicting player engagement, we followed a similar process as before. Namely, doing feature selection on the tags to find those most relevant, and how they would affect the accuracy of the model, grid search to find the best set of hyperparameters for the given set of features, and feature engineering.

Overall, we were unable to find a strong and repeatable link between any single tag and its effect on the model’s abilities, as such we opted to include them all and simply feed all of the available features and data into the prediction model. Attempts at feature engineering, a valid and reasonable approximation for player engagement were also done during this stage which was how we obtained the total watchtime/number of viewers as our engagement score.

Similar to predicting Metacritic scores, limited success in linear regression models led us to abstract player engagement further, where a model simply needs to identify if a game has low, middling, or high engagement in general. As before, reformulating this as a classification problem yielded some immediate benefits. Classification models were generally able to perform better than random, whereas linear regression models tended to yield negative scores.

Initially, two stacked decision tree classifiers were used to classify player engagement, where the first model makes an initial prediction and then a second model takes all the features fed into the first model and the initial prediction to make a final prediction yielding a marginal increase in accuracy, recall and precision over a single decision tree. However, comparing the CV mean accuracy score of this method to a simple random forest model showed that the latter is still generally outperforming the stacked decision trees and at worst matching its performance over several different validation splits.

After narrowing down our prediction method to a random forest classifier, we used grid search to search through a large number of potential hyperparameters and narrow down the ones that seem to be local maxima in accuracy.

In the end, while the model was unable to reach particularly high levels of accuracy, it was still able to outperform randomness with an accuracy of 0.33. It achieved a CV mean accuracy, recall, and precision of 0.482, 0.480, and 0.475, respectively. However, the main reason we settled on this model was due to the fact that it was able to avoid the worst form of classification errors, where it would predict high
engagement games as low engagement and vice versa.

Using a score that gives partial credit of 0.5 for predicting a neighboring class instead of the true class improves the model’s mean accuracy to a more reasonable score of 0.68. This weighted scoring method allows us to properly measure the ability of a model to avoid the worst form of classification errors. Our current random forest model was chosen over the decision tree classifier in part due to its improved weighted score. The vast majority of its misclassifications were for neighboring classes which made the low classification accuracy more tolerable in contrast to other models which were more prone to severe misclassifications.</summary>
<br>
</details>



