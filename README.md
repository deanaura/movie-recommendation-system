# 🎬 Movie Recommendation System

This is a content-based Movie Recommendation System built using **Python**, **Machine Learning**, and and **Streamlit** with movie posters fetched via the **TMDb API**.

![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-red?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
[![Deployed on Streamlit](https://img.shields.io/badge/Deployed%20on-Streamlit-blue?logo=streamlit)](https://share.streamlit.io/)

## 🚀 Features

- Recommend similar movies based on user selection
- View posters and scroll long titles horizontally
- Built with content-based filtering (cosine similarity)
- Fast and clean UI with Streamlit

## 🧠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Pickle
- Streamlit
- TMDB API

## 📦 Installation

1. **Clone this repository:**

```bash
git clone https://github.com/deanaura/movie-recommender.git
cd movie-recommender
```

2. **Create a virtual environment and activate it:**

```bash
python -m venv env
env\Scripts\activate  # On Windows
```

3. **Install the required libraries:**

```bash
pip install -r requirements.txt
```

4. **Add your TMDb API key:**

Create a file named .env in the project root:

```bash
TMDB_API_KEY=your_tmdb_api_key_here
```

## ▶️ Run the App

```bash
streamlit run app.py
```

## 🙌 Acknowledgments
- TMDB API
- Streamlit
- Scikit-learn


Made with ❤️ by deanaura