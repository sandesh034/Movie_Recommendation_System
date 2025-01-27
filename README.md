
# Movie Recommender System

This project is a content-based movie recommender system that uses cosine similarity to recommend movies. The data is sourced from the TMDB dataset.



## Introduction

In this project, we build a content-based movie recommender system using the TMDB dataset. The recommender system suggests movies based on their similarity to a given movie, which is calculated using cosine similarity.

## Dataset

The dataset used in this project is sourced from TMDB. It includes information about movies such as their titles, genres, and descriptions.  [Link](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## Dependencies

The following Python libraries are required to run this project:

- pandas
- numpy
- scikit-learn
- nltk
- pickle

## Installation

To install the dependencies, run the following command:

```bash
pip install pandas numpy scikit-learn nltk pickle
```

## Usage

To use the recommender system, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/sandesh034/Movie_Recommendation_System.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Movie_Recommendation_System
    ```
3. Run the notebook:
    ```bash
    movie_recommendation.ipynb
    ```
## Conclusion

This project demonstrates how to build a simple content-based movie recommender system using cosine similarity and the TMDB dataset. 

## Contributing

We welcome contributions to enhance the movie recommender system! Here are a few ways you can contribute:

### Reporting Bugs

If you encounter any bugs or issues, please report them by creating a new issue in the GitHub repository. Be sure to include detailed information about the issue and how to reproduce it.

### Suggesting Enhancements

If you have ideas for new features or improvements, please open a new issue to discuss your suggestions. We appreciate any feedback that can help make this project better!

### Submitting Pull Requests

To contribute code changes, follow these steps:

1. **Fork the repository**: Click the "Fork" button at the top right of the repository page to create a copy of the repository in your GitHub account.
2. **Clone the forked repository**: Clone your forked repository to your local machine using the following command:
    ```bash
    git clone https://github.com/sandesh034/Movie_Recommendation_System.git
    ```
3. **Create a new branch**: Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-or-bugfix-name
    ```
4. **Make your changes**: Implement your feature or bug fix.
5. **Commit your changes**: Commit your changes with a descriptive commit message:
    ```bash
    git add .
    git commit -m "Description of the changes"
    ```
6. **Push to the branch**: Push your changes to your forked repository:
    ```bash
    git push origin feature-or-bugfix-name
    ```
7. **Create a pull request**: Open a pull request in the original repository, describing your changes and referencing any related issues.

## References

- [TMDB](https://www.themoviedb.org/)
- [scikit-learn documentation](https://scikit-learn.org/stable/)
- [nltk documentation](https://www.nltk.org/)
