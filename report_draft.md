# Draft Report
## Impact of Content Consistency on Social Media Growth

### Motivation
Social media creators often believe that posting regularly helps them grow faster, but this idea is not always tested systematically. This project investigates whether content consistency is associated with higher performance on YouTube. The topic is relevant because creator growth depends not only on content quality, but also on behavioral patterns such as upload timing and posting regularity.

### Data Source
The project is designed around YouTube video-level data collected from a focused segment of creators. The intended real-world variables are upload date, video duration, views, likes, and comments. In the current version, a realistic synthetic dataset is used to demonstrate the analysis pipeline while preserving the same structure proposed at the project stage. The dataset is enriched with derived features such as upload intervals, engagement rate, rolling averages, and a consistency index.

### Data Collection and Preparation
Each observation corresponds to one video. The data is grouped by creator and ordered chronologically, creating a panel-style structure. After collection, the following steps are applied:
- timestamp standardization
- sorting by creator and upload date
- calculation of upload intervals
- calculation of engagement rate
- rolling average features
- creator-level consistency index

Outliers such as unusually viral observations can be reviewed separately because they may distort summary results.

### Exploratory Data Analysis
EDA focuses on:
- distributions of views, likes, comments, and upload intervals
- average engagement by creator
- relationship between consistency index and average views
- relationship between upload intervals and engagement
- growth patterns across creators over time

These visualizations help identify whether more regular posting behavior is associated with stronger outcomes.

### Hypothesis Testing
The following hypotheses are tested:

- **Null hypothesis (H0):** Content consistency has no statistically significant association with social media growth or engagement.
- **Alternative hypothesis (H1):** Content consistency has a statistically significant association with social media growth or engagement.

The analysis includes:
1. Pearson correlation between consistency-related measures and performance
2. Independent-samples t-test comparing high-consistency vs low-consistency creators
3. OLS regression predicting views using consistency and control variables such as duration and subscriber proxy

### Preliminary Findings
The synthetic demonstration dataset suggests that channels with more stable upload intervals tend to show:
- higher average views
- more stable engagement
- stronger rolling performance trends

These findings support the idea that regular posting may contribute positively to audience growth, although causality cannot be fully established.

### Limitations
This version relies on synthetic data for demonstration, so conclusions should not be interpreted as real empirical evidence about YouTube. In addition:
- views may depend on content quality, topic selection, thumbnails, and algorithmic factors
- engagement metrics vary by creator size and audience behavior
- viral outliers can affect averages
- the number of creators is limited

### Future Work
Possible extensions include:
- replacing the synthetic dataset with real YouTube API data
- adding title-level and metadata features
- using machine learning models for prediction
- testing whether consistency affects long-term creator growth differently across content categories
