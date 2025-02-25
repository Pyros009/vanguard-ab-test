# Project Vanguard

Baratheon dept. (Linh Pham and Ricardo Morgado)

## Overview

Vanguard is an investment firm that is currently preparing the launch of a new UI. So, to assess if there's a significant advantage of the newly developed UI versus the old design, asked House Baratheon's department to evaluate both performances and give it's feedback.

Baratheon department was given 4 datasets consisting on:
- **[Client profiles](https://github.com/data-bootcamp-v4/lessons/blob/main/5_6_eda_inf_stats_tableau/project/files_for_project/df_final_demo.txt):** including Age, Balance, Gender, Tenure and Nr of calls and logons on a 6month period;
- **[Experiment Rooster](https://github.com/data-bootcamp-v4/lessons/blob/main/5_6_eda_inf_stats_tableau/project/files_for_project/df_final_experiment_clients.txt):** client_ids segregated by Test, Control and None;
- **[Digital Footprint part 1](https://github.com/data-bootcamp-v4/lessons/blob/main/5_6_eda_inf_stats_tableau/project/files_for_project/df_final_web_data_pt_1.txt) , [Digital Footprint part 2](https://github.com/data-bootcamp-v4/lessons/blob/main/5_6_eda_inf_stats_tableau/project/files_for_project/df_final_web_data_pt_2.txt):** logs of client requests and the dated transaction steps.

All data was then purged from NaNs, formatted and binned together to provide initial EDA's and consequent statistical analysis.

## Defining KPIs
To assess the advantage of the newly designed UI we defined 3 Key Performance Indicators (KPI):
- **Completion rate** subdivided into 2 parameters: **complete** (those that reached "complete step") and **completion rate** (those who had start and complete steps); 
- **Error rate** assessed into 3 parameters: **error quantity** (errors are all repetions of step already completed), **error amount** (number of transactions with atleast 1 error) and **step reversion** (number of times a transaction reverts steps);
- **Time between steps** measured as per step (for example: "SS1" as start to step_1) and total path ("SC" as start to complete).

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
Kanban - [Vanguard Trello](https://trello.com/invite/b/6703dad556cc9c320af6e09e/ATTIe2bafeeb203644040a1a9358844ff61b42B0C5BB/project5) <br>
Presentation - [Vanguard A/B test](https://docs.google.com/presentation/d/1Pihzjf8NO48L5Ajib52p6fFpWuUHfBb-6goOAe80EhA/present?pli=1&slide=id.gd4588e802c_1_186) <br>
Tableau Public - [Vanguard - Baratheon Tableau](https://public.tableau.com/views/demographic_distribution/Demographics?:language=pt-BR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) <br>
