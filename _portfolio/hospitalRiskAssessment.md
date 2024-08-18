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

## Netica Diagram

<br/><img src="/images/Portfolio2/Diagram2Portfolio2.png">

In the above Netica Influence Diagram (ID), all of the decisions the DM must make and the uncertainties that influence said decisions are represented. Importantly, there are 5 major influences on the DM’s utility function for cost minimization: HireOvernightAnalyst, PatientSeverity, NumberOfPatients, RequestOvertime, and ActualNurseArrival.

The other aspects affecting the model include whether the heat wave occurs tomorrow on Canada Day, or the day after represented by the Heatwave Node, whether or not there is a power outage represented by the PowerOutage Node, whether or not these events occur on Canada Day or the following day represented by the CanadaDay Node, and the workforce plan decision by the DM is represented by the WorkforcePlan Node.

## Result

**Scenario 1:** Netica Global Solution
Without considering any of the chance nodes, the decisions the that will lead the DM to optimizing his utility are the following: 

---
Don't Hire Analyst
Create A Highly Staffed Workforce Plan
Request Overtime
---

Opting to not hire the Analyst, choosing the high staff plan, and requesting overtime will maximize the DM’s utility.

---
Don't Hire Analyst
Create A Highly Staffed Workforce Plan
Request Overtime
---

## Bayesian Approach

The previous model, which was done through the use of Netica, used deterministic probabilities. These deterministic probabilities presented binary solutions that worked in a decision tree like pattern. This does not fully represent the way real scenarios work, where aspects such as patients have continuous arrivals, following distributions rather than binary numbers with set probabilities.

## Updates

For this model, certain aspects are changed to account for a continuous scenario. There are still deterministic events, but a lot of continuous probabilities are added. 

Patients arrive by walk-in or by ambulance. Both methods of arrival can be described by the Gamma distribution. By knowing the arrival rates of patients, the DM estimates that the number of patients to be serviced is represented by the Poisson distribution, where the mean number of arrivals depends on the arrival rates of walk-in and ambulance patients. 

In addition to reducing the cost of the workforce and not serving patients, the DM is also looking to make decisions that will also lower the number of hours they have to work during their shift since their daughter’s birthday party is taking place the same day and they would like to be able to attend. A typical shift is 8 hours, but they may be able to leave a maximum of two hours early. Their worst-case scenario is working 4 hours of overtime which corresponds to a 12-hour shift. The DM is motivated to make decisions that will lower their multiattribute utility of time at work and the cost incurred by the hospital. 

The DM’s Multiattribute Utility Function is composed of two independent utility functions pertaining to time spent and cost. Both of the functions are independent of one another, as the cost function only pertains to the hospital's expenses, (not including the DM’s wage), and the DM’s time is completely unaffected by the expenses for the Workforce Plan. The DM’s time spent utility function follows the exponential function (Ut(x)=ex, where x is the time spent in hours for the coming DM’s shift on this task, it could be dealt with within the work day, or require up to four hours of overtime i.e. the same amount of overtime a nurse might have [6,12]). The DM requires a resolution to the issue as soon as possible, this is normalised between [0,1] where 0 is the worst possible amount of time spent of 12, and 1 is the best possible amount of time spent of 6. Altering the schedule and finding people to come in for an extra shift, and deciding on whether overtime will be required will be difficult: so starting as early as possible is paramount. The DM’s cost utility function follows the square root function  (Uc(y) = y , where y is equal to the sum of costs i.e. nurse staffing, missed patients, hiring overnight analyst: [9573.5, 207,611.5]). Going over budget on cost has a diminishing impact in the DM’s eyes, as any unrequired overspending would already reflect poorly on them at the hospital. Both utilities are normalised between [0,1]:

Ũt(x) = e^x - 162,754.9/-162,351,   Ũc(y) = sqrt(y) - 455.64/-357.8

To translate the above utilities into a multiattribute utility function, the DM was presented with the following best-case/worst-case gambles to elicit weights (kx,ky): (best time, worst cost) and (worst time, best cost). The DM was indifferent between (worst time, best cost) and a gamble of 0.8⋅(worst time, worst cost) + 0.2⋅(best time, best cost) & (best cost, worst time) and a gamble of 0.6⋅(worst time, worst cost) + 0.4⋅(best time, best cost). These translate to:

U(x,y) = 0.4 ⋅ Ũt(x) + 0.2 ⋅ Ũc(y) + 0.4 ⋅ Ũt(x) * Ũc(y)

In PyMC, the model used is a Bayesian network that is run multiple times for all possible decision combinations. The following influence diagram below showcases the relations between each node, including decision nodes and uncertainty nodes, and their distributions used to formulate the Bayesian networks within PyMC.

<br/><img src="/images/Portfolio2/Diagram3Portfolio2.png">

The probability distributions, along with the code for them, can be found in the Python files provided.

The resulting decision was to not hire an analyst, have an average number of staff and not request overtime.

[Click Here to Open the Folder Containing the Python Code](https://github.com/CemKesisoglu/CemKesisoglu.github.io/tree/master/code)
