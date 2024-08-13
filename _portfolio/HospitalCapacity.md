---
title: "RWA Analysis of Fiber Network"
excerpt: "An algorithm design and numerical methods project, where several algorithms were developed and tested on various fiber networks to optimize fiber traffic. <br/>"
collection: portfolio
---
## Summary
The performance of different operational strategies to reduce waiting times at Canadian hospitals were assessed to determine the optimal solution for the given scenario. Input modelling was conducted to get the distribution of parameters using Excel and R. These were each normalized, and outliers were removed through the use of QQ-Plots. A base Simio model was created to set a baseline for capacity, against which different alternatives of the hospital processes were assessed. The conclusion was that the use of a "pooling" model, where patients are pooled into different segments to be processed in a FIFO fashion, was the optimal solution.
## Methodology
- Input Modelling through the use of the data. The distributions of the parameters, including their mean and variation, were determined to be used in the Simio model.
- A baseline model was created, where patients would arrive through two separate departments to be sent to one of four servers. Initial tests were run to confirm the assumptions and validity of our data.
- Two alternative models were created, which were compared against each other. The pooling model was determined as the most effective in addressing capacity concerns.

# Details

## Exploratory Data Analysis

### Patient Processing Times

~~

The distribution for acute medicine processing times can be seen on the left. There are a few outliers within the data-set as seen between when t: [20-30]. Within this distribution, the data is not distributed around the mean like a normal distribution. It also does not have it’s peak density when t = 0, and is therefore not exponentially distributed. Therefore, visually, it is seen that the processing times follow log-normal or gamma distribution.

The distribution for acute neuro processing times can be seen on the right. There are a few outliers within the data-set as seen between when t: [15-30]. Much like in medicine, within this distribution, the data is not distributed around the mean like a normal distribution. It also does not have it’s peak density when t = 0, and is therefore not exponentially distributed. Therefore, visually, it is seen that the processing times follow log-normal or gamma distribution.

~~

The distribution for rehab medically complex processing times can be seen on the left. There are a few outliers within the data-set as seen between when t: [50-100]. The data does not have it’s peak density when t = 0, and is therefore not exponentially distributed. The data is around the mean like a normal distribution, however it is still biased towards the left of the mean, implying that it is a log-normal or gamma distribution. 

The distribution for rehab stroke processing times can be seen on the right. There are a few outliers within the data-set as seen between when t: [20-30]. The data peaks density when t = 0, and is therefore assumed to be exponentially distributed. There is the potentiality of log-normal distribution, as at very low processing times, the distribution decreases, but this is attributed to randomness within the data rather than a different distribution.

### Parameter Analysis

As seen in the figures above, the curve of rehabilitation stroke follows an approximately exponential distribution, as even though at the “tails” there is a huge variance between the theoretical and actual data-points, this is explained by the fact that there are only 1000 data points for the distribution and that an exponential distribution is highly variable compared to other distributions. The rest follow approximately log-normal distributions, and are less varied than the exponential distribution, which can be seen visually above. The slight amount of variance at the “tails” can once again be explained by the fact that there are a limited number of data points, and log-normal distribution still has a certain level of variability associated with it.

### Arrival Data with Mean Arrivals

~~

## Simio Base Model

~~

The base model, as seen above, has a single source that generates all model entities, 2 acute wards, 4 rehabilitation wards as specified, and a single sink/discharge. For the base model 16 different model entities, representing all the possible routes a patient could take, were utilized. For example, a patient that moves to discharge after Medicine Acute Care is a MedDis entity, while a patient that requires Medically Complex Rehab after MSK acute care is MSKMC.

## Pooling Model

~~ 

As seen above, the structure of the pooling model only has 1 change associated with it. Instead of having multiple servers for rehabilitation, there is only one “pool” of servers, where there is a combined total of 87 capacity in terms of beds available to patients. Besides this, there is no structural or model-related change, besides the fact that the processing times are also increased by 5%. The resulting performance measures can be seen in the following table.

The waiting time, queueing length, blocking proportion and utilization for all of the acute ward servers have all decreased, meaning that patients are spending less time waiting and that the servers are spending a lower proportion of their time processing patients. The waiting times for every group of patients has also decreased to approximately a fifth of the previous waiting times. 

There is also a generally lowered trend in variance within all of the means, which implies that the model’s queue times, scheduled utilization and beds blocked will all have lower uncertainty, and thus, the issues with high variance within queueing models has been lowered. The only increase in utilization is within the rehabilitation server, as it increased from its average of 82.2% across all rehab servers to 87.17%. This increase could be explained by the 5% increase in rehabilitation times, which would directly affect the server utilization. This implies that the system does not have as much “buffer” for uncertainty and random events that may suddenly increase arrivals. 

However, despite this one issue, the alternative design of the system is an improvement, as it lowers the waiting times for the patients, the queue in front of the servers and the blocked beds as well as the server utilization for the acute ward, despite a 5% increase in rehabilitation times. Therefore, this alternative design is recommended.
