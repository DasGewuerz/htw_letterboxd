# Letterboxd Film Dataset Analysis

## Project Overview
This project analyzes a comprehensive dataset of movies from Letterboxd, available on Kaggle. The dataset includes various components such as actors, countries of production, crew members, genres, languages, releases, studios, and themes. In addition to this, the project enhances actor data by scraping additional information from IMDb, including gender, age, birthplace, and cause of death.

## Dataset
The Letterboxd dataset consists of the following files:
- `actors.csv`: Information about actors in various movies.
- `countries.csv`: Countries where the movies were produced.
- `crew.csv`: Information on crew members.
- `genres.csv`: Different genres assigned to the movies.
- `movies.csv`: Core dataset with movies and their attributes.
- `languages.csv`: Languages in which the movies were released.
- `releases.csv`: Release dates of the movies across different regions.
- `studios.csv`: Studios involved in the production of the movies.
- `themes.csv`: Themes associated with the movies.
- `actors_imdb_enriched.csv`: Enhanced actor information scraped from IMDb.

## Features
- Analysis of movie production trends over years and across countries.
- Examination of the most frequent actors and their roles in various films.
- Visualization of the distribution of movies by country and language.
- Analysis of gender and demographics of actors through enriched IMDb data.

## Requirements
This project uses Python and requires the following libraries:
- `pandas` for data manipulation,
- `numpy` for numerical operations,
- `matplotlib` and `seabase` for data visualization.

To install these dependencies, run:
`pip install pandas numpy matplotlib seaborn`
or use your prefered method of installation.

## Additional Helper Scripts
This project includes several helper scripts located in the `/helpers` subfolder, which are essential for data processing and enhancement:

- `html_parser.py`: Parses HTML content for data extraction. This is a key component for scraping web data effectively.
- `html_parser_loop.py`: Extends `html_parser.py` to handle multiple files or URLs in a loop, optimizing the scraping process.
- `scrape_imdb.py`: Dedicated to scraping additional information from IMDb. It utilizes `html_parser.py` for HTML content parsing.
- `tsv_to_csv.py`: Converts TSV (Tab Separated Values) files to CSV format, facilitating easier data manipulation and integration in Python.
- `actor_ai.ipynb`: Creates a deliberately sexist Regression ML Model to showcase the inequality in the movie industry.

## Usage
1. Clone this repository to your local machine.
2. Ensure you have the required datasets in a directory named `letterboxd/` and your IMDb enriched data in `imdb/`.
3. Place the helper scripts in the `/helper` subfolder.
4. Execute the Jupyter notebook `letterboxd.ipynb` to view the analyses and visualizations.
5. Execute the Jupyter notebook `actor_ai.ipynb` to train the sexist ML Model.


## Visualization Samples
- Pie charts showing the percentage distribution of movies by country.
- Bar graphs of the top 10 actors by the number of movies appeared in.
- Detailed actor profiles enriched with IMDb data.
- Gender distribution count, also by Pie chart.

## Contributing
Contributions to this project are welcome. Please fork this repository and submit your pull requests for review.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
