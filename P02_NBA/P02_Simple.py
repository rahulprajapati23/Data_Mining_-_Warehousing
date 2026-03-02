import pandas as pd

# 1. Loading the NBA Dataset
dataset_file = 'NBA_2018-19_Season - NBA_2018-19_Season.xlsx'
try:
    df = pd.read_excel(dataset_file)
except Exception as e:
    print(f"Error loading Excel file: {e}")
    exit()

# 2. Basic Exploration
print("\n" + "="*80 + "\nNBA DATA EXPLORATION ANALYSIS\n" + "="*80)
print(f"1) Average Age: {df['Age'].mean():.2f}")
print(f"2) Player Games (Top 5):\n{df[['Player', 'Games']].head().to_string(index=False)}")
print(f"3) Total Number of Teams: {df['Team'].nunique()}")
print(f"4) Minimum Age: {df['Age'].min()}")

# 3. Player Stats and Demographics
max_age = df.loc[df['Age'].idxmax()]
print(f"5) Oldest Player: {max_age['Player']} ({max_age['Age']} yrs, Team: {max_age['Team']})")

east_games = df[df['Conference'] == 'Eastern']['Games'].sum()
print(f"6) Total Eastern Games: {east_games}")
print(f"7) Regions (Conferences): {', '.join(df['Conference'].unique())}")

print(f"8) Celtics Players:\n{df[df['Team'] == 'Boston Celtics']['Player'].to_string(index=False)}")
print(f"9) Division Total Games:\n{df.groupby('Division')['Games'].sum().to_string()}")

# 4. Points and Fouls
max_pts = df.loc[df['Points'].idxmax()]
print(f"10) Top Scorer: {max_pts['Player']} ({max_pts['Points']} points)")

min_fouls = df.loc[df['Personal Fouls'].idxmin()]
print(f"11) Lowest Personal Fouls: {min_fouls['Player']} ({min_fouls['Personal Fouls']} fouls)")

max_3pa = df.loc[df['3-Point Field Goal Attempts'].idxmax()]
print(f"12) 3-Point Leader: {max_3pa['Player']} ({max_3pa['3-Point Field Goal Attempts']} attempts)")

print(f"13) Overall Average Points: {df['Points'].mean():.2f}")
print(f"14) Average Age by Division:\n{df.groupby('Division')['Age'].mean().to_string()}")
print(f"15) Fouls by Team:\n{df.groupby('Team')['Personal Fouls'].sum().to_string()}")

print("\n" + "="*80 + "\nANALYSIS COMPLETE\n" + "="*80)
