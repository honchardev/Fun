# Describing distributions of real data
- Step 1 - understand the nature of each variable in the dataset
    - Read documentation (if present) which might describe what categories and variables actually mean
    - Understand types - texts, continuous, discrete, ... types of valuess
    - Tabulate each variable separately - for cateogrical values
    - Fix missing values. 9, 99, 'unknown', 'other' values
    - Get summary measures: mean, median, range
    - Plot histograms - get an immediate sense about whether variabe or skewed or normally distributed etc
    - In case of skewed data OR non-normal distributions - create aggregations of median, Q1 and Q3 (lower and upper quartiles)
        - median == 50th percentile
        - A percentile is a number where a certain percentage of values for that variable fall below that number
        - lower quartile - 25th, upper quartile - 75th
        - Interquartile range - the difference between several quartiles (Q3 - Q1)
