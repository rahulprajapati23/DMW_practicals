# Practical 2: NBA Data Exploration - Simple Version

import pandas as pd
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_excel(os.path.join(SCRIPT_DIR, "NBA_2018-19_Season - NBA_2018-19_Season.xlsx"))

print("1. Average age of NBA players:", df['Age'].mean())
print("2. Games played by each player:\n", df[['Player', 'Games']].head())
print("3. Total teams in NBA:", df['Team'].nunique())
print("4. Minimum age:", df['Age'].min())
print("5. Maximum age details:\n", df[df['Age'] == df['Age'].max()])
print("6. Total Eastern region games:", df[df['Conference'] == 'Eastern']['Games'].sum())
print("7. Total regions:", df['Conference'].nunique())
print("8. Boston Celtics Players:\n", df[df['Team'] == 'Boston Celtics']['Player'].values)
print("9. Games per Division:\n", df.groupby('Division')['Games'].sum())
print("10. Player with maximum points:\n", df.loc[df['Points'].idxmax()])
print("11. Player with minimum fouls:\n", df.loc[df['Personal Fouls'].idxmin()])
print("12. Highest 3-point attempts:\n", df.loc[df['3-Point Field Goal Attempts'].idxmax()][['Player', '3-Point Field Goal Attempts', '3-Point Field Goal Percentage']])
print("13. Average points scored:", df['Points'].mean())
print("14. Average age by division:\n", df.groupby('Division')['Age'].mean())
print("15. Total fouls per team:\n", df.groupby('Team')['Personal Fouls'].sum())
