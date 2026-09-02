# Statistical Analysis Report

## San Francisco 311 Service-Request Resolution Times

**Student:** Peyman Mohammad Hassan  
**Project:** Project 2 — Data and Statistical Reasoning  
**Dataset:** San Francisco 311 Cases  
**Source:** DataSF / San Francisco 311

## Overview

This project analyzes real public San Francisco 311 service-request data to understand patterns in case resolution time and whether resolution-time behavior differs across common service categories. The analysis uses descriptive statistics, three visual models, and a nonparametric hypothesis test so that the statistical conclusions are grounded in the observed structure of the data rather than in synthetic or simulated records.

## Dataset Description

The submitted dataset is a public San Francisco 311 extract obtained from DataSF. Each row represents a 311 service request and includes fields such as case identifier, opened and closed timestamps, status, responsible agency, service category, request subtype, neighborhood, supervisor district, source, and location information. The exact row and column counts used in the final report should be taken from the executed notebook so that this document remains synchronized with the frozen CSV submitted for grading. The main variables examined are service category and a derived numeric measure, `resolution_hours`, calculated from the difference between the closed and opened timestamps.

## Methods

Initial data analysis is used to inspect missingness, duplicates, data types, category frequencies, and the distribution of resolution time before formal inference. This follows the reproducibility-oriented principle that important data properties and analytical assumptions should be identified and documented before confirmatory analysis rather than hidden inside later statistical steps (Lusa et al., 2024).

Descriptive statistics include `df.describe()`, categorical value counts, and summaries of the derived resolution-time variable. These measures describe the scale, central tendency, dispersion, and composition of the data. Three visual models are used because each emphasizes a different aspect of the same real-world pattern: a histogram shows the overall shape and skew of resolution time, a boxplot compares medians and spread across common service categories, and a bar chart communicates category-level median resolution times in a concise form.

The primary analytical question asks whether the two most common closed service categories have different resolution-time distributions. Because administrative resolution times are typically right-skewed and may contain long tails, the final notebook uses a two-sided Mann–Whitney U test rather than assuming normally distributed response times. The Mann–Whitney procedure is a rank-based method designed for comparing two independent groups without requiring normality of the measured variable (Mann & Whitney, 1947). The analysis uses alpha = 0.05, and the test statistic and p-value are reported directly from SciPy.

The test hypotheses are:

- **H0:** The resolution-time distributions for the two most common closed service categories are the same.
- **H1:** The resolution-time distributions for the two most common closed service categories differ.

The analysis is observational. Statistical association or distributional difference is not interpreted as evidence that service category itself causes faster or slower resolution.

## Results

The final values in this section must be taken directly from the executed `analysis.ipynb` after the frozen `sf311_cases.csv` file is created. The report should state the total number of records, the number of closed cases with valid non-negative resolution times, the two service categories compared, their sample sizes and median resolution times, the Mann–Whitney U statistic, and the p-value.

Figure 1 in the notebook shows the overall resolution-time distribution and is expected to reveal substantial right-skew, which motivates using robust descriptive summaries and a rank-based inferential procedure. Figure 2 compares the distributions of the most common service categories and is the strongest visual model for the analytical question because it retains information about median, spread, and relative distribution shape. Figure 3 summarizes median resolution time by category and is the easiest figure for a non-technical reader, but it compresses each group to a single number and therefore hides within-category variability.

The final statistical conclusion should follow the executed p-value. If `p < 0.05`, the null hypothesis is rejected and the report should state that the dataset provides evidence that the two selected service categories have different resolution-time distributions. If `p >= 0.05`, the null hypothesis should not be rejected. In either case, the conclusion should be framed as evidence about this public 311 dataset rather than as a causal claim about city operations.

## Interpretation for a Non-Technical Audience

San Francisco 311 requests do not all move through the city at the same speed. Different kinds of requests may require different agencies, inspections, equipment, staffing, or follow-up, so comparing their completion times can reveal operational differences. The charts in this project show the overall range of resolution times and make it possible to compare common request categories. The statistical test then asks whether the observed difference between the two largest groups is large enough to be unlikely under a model where the groups have the same resolution-time distribution. Even when a statistically significant difference is found, it does not automatically mean that one department is performing better or worse, because case complexity and reporting practices may differ substantially between categories.

## Limitations and Potential Bias

The dataset contains only cases recorded through the San Francisco 311 system, so it does not represent every service need experienced by residents. Reporting access and behavior may vary by neighborhood, language, digital access, socioeconomic conditions, awareness of 311, and preferred communication channel. This creates potential representation bias: areas with more recorded complaints may have more active reporting rather than objectively worse conditions.

Resolution time also has important limitations. It can depend on case complexity, agency workload, administrative closure practices, duplicate reports, follow-up requirements, and resource availability. Closed-date completeness may differ by request type, and open cases are necessarily excluded from analyses that require a completed resolution time, which can introduce selection bias.

A potential ethical misuse would be ranking neighborhoods, communities, or agencies solely by complaint volume or resolution time without considering reporting differences and case mix. Such rankings could reinforce misleading narratives about particular communities or public services. Initial data analysis, transparent assumptions, and careful interpretation help reduce the risk of overstating what administrative data can support (Lusa et al., 2024).

## References

Lusa, L., Proust-Lima, C., Schmidt, C. O., Lee, K. J., le Cessie, S., Baillie, M., et al. (2024). Initial data analysis for longitudinal studies to build a solid foundation for reproducible analysis. *PLOS ONE, 19*(5), e0295726. https://doi.org/10.1371/journal.pone.0295726

Mann, H. B., & Whitney, D. R. (1947). On a test of whether one of two random variables is stochastically larger than the other. *The Annals of Mathematical Statistics, 18*(1), 50–60. https://doi.org/10.1214/aoms/1177730491
