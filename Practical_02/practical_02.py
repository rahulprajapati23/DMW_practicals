# Practical 2: NBA Data Exploration
# Extracted from DMW_Practical_source_code.py

import pandas as pd
import os

# Get the directory of this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "NBA_2018-19_Season - NBA_2018-19_Season.xlsx")

def main():
    df = pd.read_excel(DATA_PATH)

    # 1) Average age of players
    avg_age = df['Age'].mean()
    print("Average age of NBA players:", avg_age)

    # 2) Games played by each player
    games_per_player = df[['Player', 'Games']]
    print("Games played by each player:\n", games_per_player.head())

    # 3) Total number of teams
    total_teams = df['Team'].nunique()
    print("Total teams in NBA:", total_teams)

    # 4) Minimum age
    min_age = df['Age'].min()
    print("Minimum age:", min_age)

    # 5) Maximum age and details
    max_age = df['Age'].max()
    max_age_details = df[df['Age'] == max_age]
    print("Maximum age details:\n", max_age_details)

    # 6) Games organized in Eastern region
    eastern_games = df[df['Conference'] == 'Eastern']['Games'].sum()
    print("Total Eastern region games:", eastern_games)

    # 7) Total regions
    total_regions = df['Conference'].nunique()
    print("Total regions:", total_regions)

    # 8) Players from Boston Celtics
    boston_players = df[df['Team'] == 'Boston Celtics']['Player']
    print("Boston Celtics Players:\n", boston_players)

    # 9) Total games in each division
    games_per_division = df.groupby('Division')['Games'].sum()
    print("Games per Division:\n", games_per_division)

    # 10) Player with maximum points
    max_points_player = df.loc[df['Points'].idxmax()]
    print("Player with maximum points:\n", max_points_player)

    # 11) Player with minimum personal fouls
    min_fouls_player = df.loc[df['Personal Fouls'].idxmin()]
    print("Player with minimum fouls:\n", min_fouls_player)

    # 12) Highest 3-point attempts and percentage
    max_3pt_attempts = df.loc[df['3-Point Field Goal Attempts'].idxmax()][['Player', '3-Point Field Goal Attempts', '3-Point Field Goal Percentage']]
    print("Highest 3-point attempts:\n", max_3pt_attempts)

    # 13) Average points scored
    avg_points = df['Points'].mean()
    print("Average points scored:", avg_points)

    # 14) Average age division-wise
    avg_age_division = df.groupby('Division')['Age'].mean()
    print("Average age by division:\n", avg_age_division)

    # 15) Total fouls in each team
    fouls_per_team = df.groupby('Team')['Personal Fouls'].sum()
    print("Total fouls per team:\n", fouls_per_team)

if __name__ == '__main__':
    main()
