# The Great Shift of Anime

## Project Overview
This project explores the growth and evolution of anime over time through data collection and exploratory data analysis. By scraping and analyzing data from the MyAnimeList (MAL) API, this project aims to highlight the historical increase in anime releases and popularity, as well as shifts in ratings, common genres, and source materials over the decades.

## Data Collection
The project collects data via the MyAnimeList API. Several scripts handle the extraction of anime records:
- **`InClassPandasAssignment.py`**: A script that gathers anime IDs across various genres (action, romance, fantasy, sports, comedy, drama) and compiles an initial dataset (`mal_anime_raw_messy.csv`).
- **`top_1000_anime.ipynb`**: Iterates through MAL's ranking API to collect detailed information for the top 1,000 anime. Extracted fields include titles, episode counts, user ratings, rank, popularity, broadcast dates, studios, sources, and genres. The data is exported to `top_1000_anime.csv`.

## Data Analysis & Visualizations
The datasets (`mal_anime_clean.csv` and `top_1000_anime.csv`) are analyzed across multiple scripts and Jupyter notebooks to uncover meaningful industry trends:

- **`Summary_statistics.py` & `.ipynb`**: Computes descriptive statistics for the data. This includes feature ranges, the highest-ranked shows, average ratings per year, and the count of anime released annually.
- **`exploratory_analysis.py` & `.ipynb`**: Explores relationships between numerical features by generating a correlation matrix for ratings, popularity, episodes, and release years. It also breaks down frequencies and average ratings by media type, adaptation source, and genre.
- **`visualization.ipynb`**: Uses `matplotlib` to plot bar charts comparing the number of top 1,000 anime released between 1970–1999 vs. 2000–Present, illustrating the explosive growth of the medium in recent years. It also visualizes the top 12 most common genres.
- **`additional_visuals.py` & `.ipynb`**: Generates visual representations of the total number of anime released per year and a breakdown of the top source materials for anime adaptations (e.g., Manga, Light Novels, Original).

## Ethics & Limitations
While MyAnimeList provides a massive repository of data, relying solely on its userbase introduces potential biases. The preferences and habits of the MAL community may not perfectly reflect the broader, global anime audience. 

A key limitation of our analysis is the inability to access historical snapshots of user lists. For example, we cannot see how many users had a specific anime on their list in 2015 compared to today, making it difficult to trace a single show's exact trajectory of popularity over time.

Future improvements could involve expanding the dataset beyond the top 1,000 anime and incorporating cross-referenced data from other anime tracking platforms (like AniList or Kitsu) for a more comprehensive perspective.

## Setup & Usage
1. Ensure you have Python installed along with the required libraries (`pandas`, `matplotlib`, `requests`).
2. If running the API collection scripts, a valid MyAnimeList API Client ID must be provided.
3. You can either generate fresh data by running the collector scripts or analyze the provided `.csv` files.
4. Run the Python scripts (`.py`) or open the Jupyter Notebooks (`.ipynb`) to view the statistics and visualizations.

<img width="4608" height="3456" alt="The Great Shift of Anime Poster (1)" src="https://github.com/user-attachments/assets/27931901-7f08-46a7-bbb0-db5f4bc33c6d" />
