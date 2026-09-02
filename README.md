# Data and Statistical Reasoning Project

Project 2 submission for the AI Master's capstone sequence. This repository contains a complete statistical analysis of a real-world public dataset using Python, Pandas, NumPy, Matplotlib/Seaborn, SciPy, and Jupyter.

## Project Focus

The project analyzes **San Francisco 311 Cases** from the City and County of San Francisco open-data portal. The analysis will use descriptive statistics, three visual models, and hypothesis testing to study patterns in 311 service requests and communicate findings for both technical and non-technical audiences.

**Dataset source:** San Francisco Open Data (DataSF)  
**Dataset view/API:** `syr9-3867`  
**Public API endpoint:** `https://data.sfgov.org/api/v3/views/syr9-3867/query.json`

The final submitted CSV will be stored in the same folder as `analysis.ipynb`, as required by the project instructions.

## Required Submission Files

- `analysis.ipynb`
- `Statistical_Analysis_Report.pdf`
- `requirements.txt`
- San Francisco 311 dataset CSV used by the notebook

## Planned Statistical Workflow

1. Validate the Python/Jupyter environment.
2. Load the public San Francisco 311 CSV with Pandas.
3. Inspect data types, missing values, and the first rows.
4. Compute descriptive statistics with `df.describe()` and categorical value counts.
5. Explore distributions of key numeric variables.
6. Create at least three visual models with descriptive titles and labeled axes.
7. Compare what each visual model reveals and identify which best supports the analytical question.
8. State null and alternative hypotheses clearly.
9. Perform an appropriate hypothesis test with SciPy and report the test statistic and p-value.
10. Summarize findings, challenges, limitations, bias, and ethical considerations.
11. Produce a professional statistical report with academic citations.
12. Generate `requirements.txt` using `pip freeze > requirements.txt`.

## Reproducibility

Create and activate a Python 3.9+ environment, then install the project dependencies:

```bash
pip install -r requirements.txt
```

Open the notebook with Jupyter Notebook, JupyterLab, or VS Code and run `analysis.ipynb` from top to bottom.

The final `requirements.txt` will be generated from the environment used for final QA:

```bash
pip freeze > requirements.txt
```

## Environment Validation

The final notebook will verify the required libraries:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
```

## Report Requirements

`Statistical_Analysis_Report.pdf` will contain:

- Overview
- Dataset Description
- Methods
- Results
- Interpretation for a Non-Technical Audience
- Limitations and Potential Bias
- References

The report will cite the required peer-reviewed article, **Initial Data Analysis for Longitudinal Studies to Build a Solid Foundation for Reproducible Analysis**, and at least one additional peer-reviewed scholarly source supporting a relevant statistical or methodological choice.

## Responsible Data Use

This project uses public, non-synthetic open-government data. No private client data, credentials, or confidential records should be committed to this repository. Any analysis of geographic or service-request patterns will be interpreted cautiously because reporting frequency, access to 311 services, neighborhood behavior, and administrative processes can introduce selection and measurement bias.

## Status

Repository initialized for Project 2. Dataset acquisition, notebook implementation, statistical analysis, final report generation, dependency freezing, and clean execution QA are the remaining implementation steps.
