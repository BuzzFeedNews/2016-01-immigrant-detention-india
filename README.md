# Data and Analysis: Indian Immigration Detention Rates

This repository contains the data and code supporting several passages in the BuzzFeed News article, "America's Quiet Crackdown On Indian Immigrants," published January 29, 2016.

## Data

The analyses below use data from the Department of Justice's "CASE" database, maintained by the Executive Office of Immigration Review (EOIR). The database, which tracks immigration proceedings, was obtained through a Freedom of Information Request. The data cover all cases whose records were created between Jan. 1, 2000 and Jan. 15, 2015.

You can download the data tables used in this analysis from the [Internet Archive](https://archive.org/details/eoir-detention-data-2015). It contains these files:

- **A_tblCASE.csv**: Metadata about each case.
- **B_tblProceedCharges.csv**: The charges related to each case.
- **first\_scheduled\_proceeding.csv**: The first proceeding for each case, [extracted](https://github.com/BuzzFeedNews/2015-08-immigrant-detention/blob/09475d9a5fdc438a6112e99ba2a763a8cad9fb20/utils/generate-first-scheduled-proceeding.py) from a larger EOIR table of all proceedings.
- **tblLookupNationality.csv**: A table that matches the country codes to country names.

## Analyses


The following passage is supported by the calculations in [this notebook](notebooks/detention-by-nationality-by-year-analysis.ipynb):

- "In 2013, 83% of Indians facing deportation were imprisoned — a far larger percentage than for immigrants from any other country, including Mexico, which had the highest overall rate of detention between 2003 and 2014."

## Technical Notes

To replicate this analysis you'll need Python 2.7 or 3.x as well as the Python libraries listed in [`requirements.txt`](requirements.txt). You'll also need to [download the data from the Internet Archive](https://archive.org/details/eoir-detention-and-bonds), and place it into this repository's `data` subdirectory.

## Questions / Feedback

If you have questions or feedback about the data or analyses, contact John Templon at [john.templon@buzzfeed.com](mailto:john.templon@buzzfeed.com)
