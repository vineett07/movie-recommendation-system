import pandas as pd
import streamlit as st

# 1. Setup the Webpage Title
st.title("🎬 Movie Recommendation System")
st.write("An AIML hackathon project that suggests movies based on matching genres!")


# 2. Load the Dataset
@st.cache_data  # This makes the app load faster
def load_data():
    return pd.read_csv("movies.csv")


df = load_data()

# 3. Create a dropdown menu on the webpage for the user to pick a movie
movie_list = df["Title"].values
selected_movie = st.selectbox(
    "Select a movie you like:", movie_list, index=None, placeholder="Choose..."
)


# 4. Recommendation Logic (The AI/ML part)
def get_recommendations(movie_title):
    # Find the row of the movie the user selected
    selected_row = df[df["Title"] == movie_title].iloc[0]
    selected_genre = selected_row["Genre"]

    # Filter out the selected movie, and find others with the EXACT same genre
    recommendations = df[
        (df["Genre"] == selected_genre) & (df["Title"] != movie_title)
    ]

    return recommendations


# 5. Display results when a user selects a movie
if selected_movie:
    st.subheader(f"Because you liked '{selected_movie}':")

    results = get_recommendations(selected_movie)

    if not results.empty:
        # Loop through the matches and show them on the webpage
        for index, row in results.iterrows():
            st.markdown(f"### 🎥 **{row['Title']}**")
            st.caption(f"**Genre:** {row['Genre']}")
            st.write(row["Description"])
            st.write("---")
    else:
        st.write("No similar movies found in our small database yet!")