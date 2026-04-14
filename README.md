# DSA 210 Project
## Impact of Content Consistency on Social Media Growth

**Student:** Zainab Siddiqui (36082)

## Project Overview
This project investigates whether consistent posting behavior is associated with stronger audience growth and engagement on YouTube.

The analysis uses a video-level dataset structured around multiple creators from a focused segment. The key idea is to test whether creators who post more regularly tend to achieve higher views and engagement.

## Important note
Because live data collection from YouTube was not available in this environment, the current repository contains a **realistic synthetic dataset** designed to match the proposed structure and to demonstrate:
- data collection design,
- preprocessing workflow,
- exploratory data analysis,
- hypothesis testing,
- and a path toward later machine learning work.

A real data collection template is included in `src/youtube_api_collection_template.py` so the dataset can be replaced with actual YouTube data later.

## Repository Structure
```text
DSA210_Project_Zainab_Siddiqui/
├── data/
│   ├── youtube_consistency_dataset.csv
│   └── creator_summary.csv
├── notebooks/
│   └── dsa210_analysis.ipynb
├── src/
│   ├── youtube_api_collection_template.py
│   └── generate_dataset.py
├── README.md
├── requirements.txt
├── report_draft.md
└── AI_USAGE_DISCLOSURE.md
```

## Dataset
The dataset contains approximately 240 observations and includes:
- creator
- upload date
- video duration
- views
- likes
- comments
- upload interval
- engagement rate
- rolling averages
- consistency index

## Research Question
Does content consistency positively affect social media growth and engagement?

## Hypotheses
- **H0:** Content consistency has no statistically significant relationship with growth or engagement.
- **H1:** Greater content consistency is associated with higher growth or engagement.

## Planned Analysis
1. Data cleaning and preprocessing
2. Exploratory data analysis
3. Correlation analysis
4. Independent-samples t-test between high-consistency and low-consistency creators
5. OLS regression predicting views from consistency and control variables

## How to run
```bash
pip install -r requirements.txt
jupyter notebook
```

Then open:
`notebooks/dsa210_analysis.ipynb`

## Next steps
Before the 5 May deadline, this project can be extended with:
- real YouTube API collection,
- additional features such as title length or upload weekday,
- machine learning models for view prediction.
