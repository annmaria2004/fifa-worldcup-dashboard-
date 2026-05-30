
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="FIFA World Cup Intelligence Dashboard",
    page_icon="⚽",
    layout="wide"
)

# =====================
# LOAD DATA
# =====================

base_path = "/content/drive/MyDrive/FIFA_WorldCup_Project/dashboard_data"

# Historical Data
champions = pd.read_csv(f"{base_path}/champions.csv")
team_wins = pd.read_csv(f"{base_path}/team_wins.csv")
argentina_2022 = pd.read_csv(f"{base_path}/argentina_2022.csv")
france_2018 = pd.read_csv(f"{base_path}/france_2018.csv")
morocco_2022 = pd.read_csv(f"{base_path}/morocco_2022.csv")
goals_per_year = pd.read_csv(f"{base_path}/goals_per_year.csv")
matches_per_year = pd.read_csv(f"{base_path}/matches_per_year.csv")
world_cup_titles = pd.read_csv(f"{base_path}/world_cup_titles.csv")

# 2026 Data
worldcup_2026_info = pd.read_csv(
    f"{base_path}/worldcup_2026_info.csv"
)

worldcup_2026_stadiums = pd.read_csv(
    f"{base_path}/worldcup_2026_stadiums.csv"
)

worldcup_2026_teams = pd.read_csv(
    f"{base_path}/worldcup_2026_teams.csv"
)

worldcup_2026_schedule = pd.read_csv(
    f"{base_path}/worldcup_2026_schedule.csv"
)

team_intelligence = pd.read_csv(
    f"{base_path}/team_intelligence_v2.csv"
)

# =====================
# TITLE
# =====================

st.title("⚽ FIFA World Cup Intelligence Dashboard")

# =====================
# SIDEBAR
# =====================

page = st.sidebar.selectbox(
    "Choose Analysis",
    [
        "Overview",

        "Champions",
        "Top Teams",
        "Goals Trend",
        "World Cup Titles",

        "Argentina 2022",
        "France 2018",
        "Morocco 2022",

        "2026 Tournament Info",
        "2026 Stadiums",
        "2026 Qualified Teams",
        "2026 Schedule",
        "2026 Team Intelligence"
    ]
)

# =====================
# OVERVIEW
# =====================

if page == "Overview":

    st.markdown("""
    ### Explore FIFA World Cup History (1930–2022) and World Cup 2026
    """)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "World Cups",
        len(champions)
    )

    col2.metric(
        "Countries Won",
        champions["Winner"].nunique()
    )

    col3.metric(
        "2026 Teams",
        len(worldcup_2026_teams)
    )

    col4.metric(
        "2026 Stadiums",
        len(worldcup_2026_stadiums)
    )

    st.markdown("---")

    st.subheader("⚽ Goals Scored Across World Cups")

    fig = px.line(
        goals_per_year,
        x="Year",
        y="Total Goals",
        markers=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("🏆 Countries with Most World Cup Titles")

    fig = px.bar(
        world_cup_titles.head(10),
        x="Country",
        y="Titles"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("🌍 FIFA World Cup Champions Timeline")

    fig = px.scatter(
        champions,
        x="Year",
        y="Winner",
        hover_data=["Score", "Match Name"]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================
# CHAMPIONS
# =====================

elif page == "Champions":

    st.header("🏆 World Cup Champions")

    st.dataframe(champions)

# =====================
# TOP TEAMS
# =====================

elif page == "Top Teams":

    st.header("⚽ Most Successful Nations")

    fig = px.bar(
        team_wins.head(10),
        x="Country",
        y="Wins"
    )

    st.plotly_chart(fig)

    st.dataframe(team_wins)

# =====================
# GOALS TREND
# =====================

elif page == "Goals Trend":

    st.header("⚽ Goals Per Tournament")

    fig = px.line(
        goals_per_year,
        x="Year",
        y="Total Goals",
        markers=True
    )

    st.plotly_chart(fig)

# =====================
# WORLD CUP TITLES
# =====================

elif page == "World Cup Titles":

    st.header("🏆 Countries with Most Titles")

    fig = px.bar(
        world_cup_titles,
        x="Country",
        y="Titles"
    )

    st.plotly_chart(fig)

    st.dataframe(world_cup_titles)

# =====================
# ARGENTINA 2022
# =====================

elif page == "Argentina 2022":

    st.header("🇦🇷 Argentina 2022 Journey")

    st.dataframe(
        argentina_2022[
            [
                "Match Name",
                "Score",
                "Stage Name",
                "Winner"
            ]
        ]
    )

# =====================
# FRANCE 2018
# =====================

elif page == "France 2018":

    st.header("🇫🇷 France 2018 Journey")

    st.dataframe(
        france_2018[
            [
                "Match Name",
                "Score",
                "Stage Name",
                "Winner"
            ]
        ]
    )

# =====================
# MOROCCO 2022
# =====================

elif page == "Morocco 2022":

    st.header("🇲🇦 Morocco 2022 Journey")

    st.dataframe(
        morocco_2022[
            [
                "Match Name",
                "Score",
                "Stage Name",
                "Winner"
            ]
        ]
    )

# =====================
# 2026 INFO
# =====================

elif page == "2026 Tournament Info":

    st.header("🌎 FIFA World Cup 2026")

    st.dataframe(worldcup_2026_info)

# =====================
# 2026 STADIUMS
# =====================

elif page == "2026 Stadiums":

    st.header("🏟️ 2026 Stadiums")

    st.dataframe(worldcup_2026_stadiums)

    fig = px.bar(
        worldcup_2026_stadiums.sort_values(
            "Capacity",
            ascending=False
        ),
        x="Stadium",
        y="Capacity",
        color="Country"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================
# 2026 QUALIFIED TEAMS
# =====================

elif page == "2026 Qualified Teams":

    st.header("⚽ Qualified Teams")

    st.dataframe(worldcup_2026_teams)

    fig = px.pie(
        worldcup_2026_teams,
        names="Confederation",
        title="Teams by Confederation"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================
# 2026 SCHEDULE
# =====================

elif page == "2026 Schedule":

    st.header("📅 Tournament Schedule")

    st.dataframe(worldcup_2026_schedule)

# =====================
# 2026 TEAM INTELLIGENCE
# =====================

elif page == "2026 Team Intelligence":

    st.header("📊 Team Intelligence")

    st.dataframe(team_intelligence)

    fig = px.bar(
        team_intelligence.sort_values(
            "World Cup Titles",
            ascending=False
        ).head(15),
        x="Team",
        y="World Cup Titles",
        title="World Cup Titles Among Qualified Teams"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    fig = px.scatter(
        team_intelligence,
        x="FIFA Ranking",
        y="World Cup Titles",
        hover_name="Team"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
