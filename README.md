# DMW Practicals

This repository contains the DMW practical programs split into separate folders with simplified versions of each solution.

## Clone the repository

```bash
git clone https://github.com/rahulprajapati23/DMW_practicals.git
cd DMW_practicals
```

## Install requirements

Use a virtual environment if possible, then install the dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Folder structure

- `Practical_01/` - Web scraping
- `Practical_02/` - NBA data exploration
- `Practical_03/` - Employee data exploration
- `Practical_05/` - Text mining
- `Practical_06/` - Binning and smoothing
- `Practical_07/` - Apriori algorithm
- `Practical_08/` - FP-Tree
- `Practical_09/` - Decision tree
- `Practical_10/` - Clustering

Each practical folder contains:
- the original detailed script
- a simplified script named like `P01_Simple.py`, `P02_Simple.py`, and so on

## Run a practical

From the repository root, run the file for the practical you want.

### Examples

```bash
python Practical_01/P01_Simple.py
python Practical_02/P02_Simple.py
python Practical_03/P03_Simple.py
python Practical_05/P05_Simple.py
python Practical_06/P06_Simple.py
python Practical_07/P07_Simple.py
python Practical_08/P08_Simple.py
python Practical_09/P09_Simple.py
python Practical_10/P10_Simple.py
```

## Data files

Some practicals need local data files inside the same folder:

- `Practical_02/` - `NBA_2018-19_Season - NBA_2018-19_Season.xlsx`
- `Practical_03/` - `employees.xlsx`
- `Practical_05/` - `tweet_data.csv`
- `Practical_07/` - `Online Retail.xlsx`
- `Practical_08/` - `Online Retail.xlsx`
- `Practical_10/` - `Mall_Customers.csv`

Other practicals use embedded data or a remote source and do not need a separate data file.

## Notes

- The scripts use paths relative to each practical folder.
- If your file names differ, update the path inside the script.
- Plot-based practicals may open charts in a window or notebook depending on your environment.
