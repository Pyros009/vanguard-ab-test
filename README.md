# Project Vanguard

Baratheon dept. (Linh Pham and Ricardo Morgado)

## Overview

Vanguard is an investment firm that is currently preparing the launch of a new UI. So, to assess if there's a significant advantage of the newly developed UI versus the old design, asked House Baratheon's department to evaluate both performances and give it's feedback.

Baratheon department was given 4 datasets consisting on:
- **Client profiles:** including Age, Balance, Gender, Tenure and Nr of calls and logons on a 6month period;
- **Experiment Rooster:** client_ids segregated by Test, Control and None;
- **Digital Footprint:** logs of client requests and the dated transaction steps.

All data was then purged from NaNs, formatted and binned together to provide initial EDA's and consequent statistical analysis.

## Defining KPIs

## Major Obstacles

One of the main challenges on this project was the amount of data sourced and it's cleanup. Due to the size of the samples, the process took longer than expected and each new iteration or re-thought on the process led to multiple repetitions.
Defining criterias and KPIs for the evaluation also took some time, as the definitions would impact the new structure and format processes. Specially on the time per step but also on what a complete log would look like made the analysis take longer than it should.
Last but not least, GitHub branch merging and multiple submissions led to some lengthy conflicts hard to solve.

## Conclusions

Regarding test effectiveness, we can say that :
- **Basic EDA** already showed that the **sample size was big** and mostly **well structured**. Samples were **independent** (as each client_id was associated with a single experiment type). **Statistical tests** definitelly **confirmed** that aspect and so the analysis was possible to continue.
- Analysis was made based on clients being separated into age groups, we have some groups that are under-represented. However, due to the lack of information regarding general client's demographics, we can't tell if there's a bias regarding those clients or if it's a reflex on the client's demography. 

For duration assessment and overall results:
- The experiment ran for around 3 months. This timeframe should yield nice and stable results. However, it's possible to see in the analysis that there's an influx of clients at the start of the experiment (during the first half of the experiment time) that made **the first portion of the test concentrate 75% of all client logs**.
- Average KPI's on test vs control point towards a **big improvement in completion(%)** over the 5% increment required by Vanguard as minimum value, together with an **overall trend of less time spent by clients** to completion and even **improved completion rates** if we account full paths (near the 5% required by Vanguard). The **errors on test perform worse** but that might be due to the novelty of the new UI and require further evaluation. **All statistical analysis on these parameteres validate these assumptions**.

- The client distribution over time made some skewness show on test's KPI's regarding first half and second half of the experiment that maybe masked the natural evolution of KPI's as people get used to the new UI.
- There was however a **big change on the behavior of Control parameters during the trial**. Defining a threshold around 30/04 (a date where there's an abrupt rise in completion rate), we see there's a completely change on KPI's behavior. Time spent per step (notoriously in SS1 and S1S2 but also SC) had a different pattern from control on the first part (in favor of test UI) and became very similar to test UI on second part. These patterns repeat all through our KPI's **suggesting maybe an early implementation of fixes or a patch on the Control UI mid-effectiveness test**.

## Recommendations

As **all tests were statistically significant** and point towards a bigger than 5% improvement on new design, **we can recommend Vanguard the implementation of the New design**.
However we would also like to **recommend post-implementation evaluation** to check if the overall KPI's remain consistent with the current analysis.

Analyzing the KPI's we further **recommend future patches to focus on improving errors and backward steps** (maybe by creating more robust steps or simplifying some) to prevent client's moving back and forward on the sequence and a **special attention on each step (particularly step 2)** should be also taken since step 2 performed worst than control in time taken per step.

## Deliverables