import pandas as pd
import os

def analyze_nba_data():
    dataset_file = 'NBA_2018-19_Season - NBA_2018-19_Season.xlsx'
    print(f"Loading data from {dataset_file}...")
    try:
        df = pd.read_excel(dataset_file)
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return

    print("\nFirst 5 rows (Selected Columns):")
    features = ['Conference', 'Division', 'Team', 'Player', 'Age', 'Games', 'Games Started']
    print(df[features].to_string())

    print("\n" + "="*80)
    print("NBA DATA EXPLORATION ANALYSIS")
    print("="*80)

    # 1) Average age of players
    avg_age = df['Age'].mean()
    print(f"\n1) Average Age of Players: {avg_age:.2f} years")

    # 2) Games played by each player (Displaying first 5 for brevity, or full list logic)
    print("\n2) Games played by each player (Top 5 preview):")
    print(df[['Player', 'Games']].head().to_string(index=False))

    # 3) Total teams
    total_teams = df['Team'].nunique()
    print(f"\n3) Total Number of Teams: {total_teams}")

    # 4) Minimum age
    min_age = df['Age'].min()
    print(f"\n4) Minimum Age of Player: {min_age}")

    # 5) Maximum age and details
    max_age_idx = df['Age'].idxmax()
    max_age_player = df.loc[max_age_idx]
    print(f"\n5) Maximum Age of Player and Details:\n{max_age_player[['Player', 'Team', 'Age', 'Games']].to_string()}")

    # 6) Games organized in Eastern region
    eastern_games = df[df['Conference'] == 'Eastern']['Games'].sum()
    print(f"\n6) Total Games Played (recorded stats) in Eastern Region: {eastern_games}")

    # 7) Regions where games organized
    regions = df['Conference'].unique()
    print(f"\n7) Regions where games have been organized: {', '.join(regions)}")

    # 8) Players in "Boston Celtics"
    celtics_players = df[df['Team'] == 'Boston Celtics']['Player']
    print("\n8) List of players in 'Boston Celtics':")
    print(celtics_players.to_string(index=False))

    # 9) Total games organized in each division
    division_games = df.groupby('Division')['Games'].sum()
    print("\n9) Total games organized in each division:")
    print(division_games.to_string())

    # 10) Player with maximum goals (Points)
    max_points_idx = df['Points'].idxmax()
    max_points_player = df.loc[max_points_idx]
    print(f"\n10) Player with maximum goals (Points): {max_points_player['Player']} ({max_points_player['Points']} points)")

    # 11) Player with lowest personal fouls
    min_fouls_idx = df['Personal Fouls'].idxmin()
    min_fouls_player = df.loc[min_fouls_idx]
    print(f"\n11) Player with lowest personal fouls: {min_fouls_player['Player']} ({min_fouls_player['Personal Fouls']} fouls)")

    # 12) Highest 3-point attempts and percentage
    max_3pa_idx = df['3-Point Field Goal Attempts'].idxmax()
    max_3pa_player = df.loc[max_3pa_idx]
    print(f"\n12) Player with highest 3-point attempts: {max_3pa_player['Player']}")
    print(f"    Attempts: {max_3pa_player['3-Point Field Goal Attempts']}")
    print(f"    Percentage: {max_3pa_player['3-Point Field Goal Percentage'] * 100:.2f}%")

    # 13) Average points scored by all players
    avg_points = df['Points'].mean()
    print(f"\n13) Average points scored by all players: {avg_points:.2f}")

    # 14) Average age of players division wise
    avg_age_division = df.groupby('Division')['Age'].mean()
    print("\n14) Average age of players division wise:")
    print(avg_age_division.to_string())

    team_fouls = df.groupby('Team')['Personal Fouls'].sum()
    print("\n15) Total number of fouls in each team:")
    # pd.set_option('display.max_rows', None) # Uncomment to see all if truncated
    print(team_fouls.to_string())
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)

if __name__ == "__main__":
    analyze_nba_data()
