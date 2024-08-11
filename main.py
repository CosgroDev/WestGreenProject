import streamlit as st
import pandas as pd
import matplotlib as plt
import numpy as np

df = pd.read_excel("dartsData.xlsx")
st.title("West Green WMC Darts")

st.image('image.png', caption="West Green WMC Darts")

# Create last 6 games results show
dfMatch = df[["Title","OPPONENT","LEGS_WON","LEGS_AGAINST","RESULT","AVERAGE_WG","FIRST_9","GAME_DATE","SEASON"]]
st.subheader("Latest match result")
st.write(dfMatch.head(6))
# West Green Stats
st.subheader("Team Stats")

season = dfMatch['SEASON'].unique()
selectedSeason = st.selectbox("Select a season to filter by", season)
dfMatch = dfMatch[dfMatch['SEASON'] == selectedSeason]

colGamesPlayed, colGamesWon, colGamesDraw, colGamesLoss = st.columns(4)
# Number of games played West Green
gamesPlayed = dfMatch.shape[0]
colGamesPlayed.metric("Games Played", gamesPlayed)
# Number of games won West Green
gamesWon = dfMatch[dfMatch['RESULT'] == 'WIN']
gamesWon = gamesWon.shape[0]
colGamesWon.metric("Games Won", gamesWon)
# Number of games drawn West Green
gamesDraw = dfMatch[dfMatch['RESULT'] == 'DRAW']
gamesDraw = gamesDraw.shape[0]
colGamesDraw.metric("Games Draw", gamesDraw)
# Number of games lost West Green
gamesLoss = dfMatch[dfMatch['RESULT'] == 'LOSS']
gamesLoss = gamesLoss.shape[0]
colGamesLoss.metric("Games Lost", gamesLoss)


# Show match data by person
st.subheader("Player Results")
player = dfMatch['Title'].unique()
selectedPlayer = st.selectbox("Select a player to filter by", player)
filteredMatch = dfMatch[dfMatch['Title'] == selectedPlayer]
st.write(filteredMatch)

st.header("Player Stats")

st.subheader("Game Stats")
colGamesPlayed, colGamesWon, colGamesDraw, colGamesLoss = st.columns(4)
# Number of Games Played
gamesPlayed = filteredMatch.shape[0]
colGamesPlayed.metric("Games Played",gamesPlayed)
# Number of Wins
gamesWon = filteredMatch[filteredMatch['RESULT'] == 'WIN']
gamesWon = gamesWon.shape[0]
colGamesWon.metric("Games Won", gamesWon)
# Number of Draws
gamesDraw = filteredMatch[filteredMatch['RESULT'] == 'DRAW']
gamesDraw = gamesDraw.shape[0]
colGamesDraw.metric("Games Drawn", gamesDraw)
# Number of Loss
gamesLoss = filteredMatch[filteredMatch['RESULT'] == 'LOSS']
gamesLoss = gamesLoss.shape[0]
colGamesLoss.metric("Games Lost", gamesLoss)

st.subheader("Leg Stats")
colLegsPlayed, colLegsWon, colLegsLoss = st.columns(3)
# Legs Played
legsPlayed = filteredMatch['LEGS_WON'].sum() + filteredMatch['LEGS_AGAINST'].sum()
colLegsPlayed.metric("Legs Played", int(legsPlayed))
# Count of Legs Won
legsWon = filteredMatch['LEGS_WON'].sum()
colLegsWon.metric("Legs Won", legsWon)
legsLost = filteredMatch['LEGS_AGAINST'].sum()
colLegsLoss.metric("Legs Lost", int(legsLost))


# Generate Graph for Average or First 9
st.subheader("Generate Graphs")
st.text("This area is where you can create graphs of your stats")
yColumnAverages = st.selectbox("Select Average or First 9", ['AVERAGE_WG','FIRST_9'])
st.scatter_chart(filteredMatch.set_index(['GAME_DATE'])[yColumnAverages])

# Generate Bar Chart for Wins & Losses
st.text("Legs Won")
st.bar_chart(filteredMatch.set_index(['GAME_DATE'])['LEGS_WON'])