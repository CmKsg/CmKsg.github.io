---
title: "Hospital Risk Assessment"
excerpt: "A Bayesian Statistics project, where a hospital's patient arrivals and associated costs were modelled. <br/>"
collection: portfolio
---
## Summary
For this project, the risks to a hospital from heatwaves and sudden events were evaluated through the use of Bayesian Networks and Influence Diagrams. These evaluations were done through the use of Monte Carlo Markov Chain simulations and decision trees to evaluate the utility gained by the decision maker (DM) in these situations.

## Methodology
- With Netica, we drew an Influence Diagram, which took into account multiple decisions the DM had to make, the discrete subjective random events and the discrete objective random events that were evaluated from data analysis.
- With PyMc, we drew a Bayesian Network, which took into account multiple decisions, subjective random events and objective event distributions; which were evaluated from data analysis.

# Details

## Deterministic Influence Diagram

The ED Manager is responsible for overseeing the day-to-day operations of an ED belonging to a hospital in Toronto, Ontario. One of these tasks includes the management of human resources and development of a workforce plan. Workforce planning for an ED is somewhat of a mundane task with established approaches. However, in a week’s time a heat wave is predicted to occur. If Environment Canada is accurate in their weather forecasting, there's a 50% chance the heat wave will start on either July 1st or July 2nd. Should this heat wave occur on July 1st, it will coincide with Canada Day. The ED Manager is particularly concerned about these two events occurring on the same day since they know both Canada Day and heat waves typically bring in more patients to the ED with higher condition severity. The potential of these events happening on the same day could cause strain on the ED staff and increase patient wait times, and present patients with more severe conditions. 

To help him gain insight on the correlation between heat waves, power outages, Canada Day, and patient arrivals, the ED Manager has the option to hire an Overnight Analyst to study how these factors will impact the number of arrivals to the ED. However, since the Analyst is given such short notice she will charge $4,500 to conduct analysis and write a report on her findings. This information would be useful for the ED Manager since the number of patients per day is a key factor in deciding a plan along with estimated patient severity. 

The ED Manager wants to select a workforce plan so the hospital can minimize labour costs while staying within the Ontario government’s guidelines of treating urgent ED patients within 4 hours and non-urgent patients in 8 hours. Failing to meet this regulation will result in cuts to the ED’s funding in the upcoming year. The ED Manager finds that having a patient-to-nurse ratio of 8:1 or lower helps him achieve this regulation (commonly there is a 4:1 ratio of nurses to directly overseeing patients, this 8:1 averages across high severity patients and low severity patients, as a nurse can handle more of them at once; this also includes nurses required for triaging). They must also consider the already high absenteeism rates among nurses which will be increased due to the holiday. However, they have the option to request 4 hours of additional overtime from nurses currently on shift if not enough nurses are present to meet the estimated patient demand. Nurses are known to agree to overtime 30% of the time and are paid time and a half for their efforts. Given all these factors, the ED Manager must decide between High, Normal, or Low levels of staff by framing this problem using Bayesian decision-making methodologies. 

As the DM is worried about being able to service their patients if the combination of these events were to occur, they are very risk averse. The DM would like to meet all of their patient demand for the lowest cost. Going over budget on cost quickly has diminished impact in the DM’s eyes, as overspending would reflect poorly on them at the hospital. With these two goals in mind, the DM believes their utility function follows a sigmoid function;. U(x) = 11+e-μ(profit), where μ is a constant, shown in Figure 1. This function represents their risk aversion because well performing policies will satisfy needs with diminishing returns, and any inability to meet criteria will swiftly remove the policy from the decision pool.

The diagram below showcases the decision nodes, the probability nodes and the utility node of the influence diagram. The probabilities associated are located in the Excel file.

<br/><img src="/images/Portfolio2/Diagram1Portfolio2.png">
