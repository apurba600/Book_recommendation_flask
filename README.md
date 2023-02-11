http://book-recommendation-wiki.herokuapp.com/

## The GitHub repository for the book recommendation system consists of the following files:

- Book recommendation system final.ipynb: This is the Jupyter Notebook containing the code for the Machine Learning model to recommend books. It includes pre-processing of the data, tokenization, creation of integer index and vector representation of the words, and training of the Recurrent Neural Network model.

- app.py: This is the Flask code for the backend of the web application. It handles the API requests and responses, and integrates the Machine Learning model into the web application.

- templates and static: These directories contain the HTML, CSS, and JavaScript code for the frontend of the web application. The templates directory contains the HTML templates and the static directory contains the CSS and JavaScript files.

- book_recommendation.h5: This is the trained Machine Learning model in the Keras H5 format.

- predict.py: This is the code for the backend of the web application. It contains the implementation of the prediction logic and the API endpoints.

- wikipedia.json: This is the data file containing the book titles scraped from Wikipedia that was used to train the model.

- requirements.txt: This is the environment and version file that lists all the dependencies required to run the code. To clone the repository to your local machine, you need to install these dependencies by running the command "pip install -r requirements.txt".

## Project Overview:

The book recommendation model aims to tackle the challenge of finding the right book that matches an individual's reading preferences and interests. By leveraging the latest advances in natural language processing (NLP) and embedding techniques, the model analyzes the data obtained from scraping the Wikipedia pages of books. The data includes the book's title, author, genre, and themes, as well as the titles of similar books at the bottom of each Wikipedia page.

The model then uses this information to determine the books that are most likely to be of interest to the reader. It does so by creating embeddings for each book and using NLP techniques to compare the relationships between the books and the reader's reading history and preferences. The result is a personalized list of book recommendations that the reader is most likely to enjoy.

The project's objective is to provide an efficient and effective way for book lovers to discover new books, using the vast information available on Wikipedia. By utilizing NLP and embedding techniques, the model promises to make the process of finding the right book a much more straightforward and enjoyable experience.


## Problem Statement:

With the increasing availability of books and the abundance of information available online, it has become challenging for book lovers to find books that match their reading interests and preferences. The conventional methods of searching for books, such as browsing through bookstores or searching online, often result in an overwhelming amount of options, making the decision process time-consuming and complicated. As a result, there is a need for a more effective and efficient way of recommending books that align with an individual's reading preferences.

To address this challenge, the goal of this project is to develop a book recommendation natural language model that utilizes wikipedia similarity to make personalized book recommendations. The model will analyze an individual's reading preferences and history, as well as their Wikipedia page, to determine the books that are most likely to be of interest to them. By leveraging the vast information available on Wikipedia, the model will be able to recommend books based on a variety of factors. Ultimately, the goal is to provide a simple and effective way for book lovers to discover new books that match their reading interests and preferences.



## Book Recommendation System

The book recommendation project is a comprehensive solution for providing personalized book recommendations to users. The project consists of three main components: a machine learning (ML) model, a web application, and deployment on Heroku.

- ML Model: The ML model is designed to make personalized book recommendations based on the similarities of each book's Wikipedia page to the query book. To achieve this, the following steps were taken:

Pre-processing and vectorization of book titles using the Natural Language Toolkit (NLTK) library. This involved cleaning and standardizing the text data, converting the book titles into numerical representations, and preparing the data for analysis.
Use of word embedding techniques to group similar vectors in the vector space. The model creates dense vector representations of the book titles, allowing for the representation of the relationships between different books.
Training of the ML model using a recurrent neural network (RNN). The RNN was trained on a large dataset of book information and reader preferences to ensure the recommendations generated were accurate and relevant.
- Web Application: The web application was implemented to provide an intuitive and user-friendly interface for accessing the book recommendations. The following tools and technologies were used:

Flask for the backend of the web application, allowing for the integration of the ML model and the processing of user requests.
HTML, CSS, and Javascript for the frontend, providing a visually appealing and interactive user interface.
- Heroku Deployment: The final step was to deploy the web application on Heroku, a cloud platform that provides a quick and easy way to deploy and scale web applications. By deploying the web application on Heroku, the book recommendation solution is accessible to a wider audience, and is able to handle an increased volume of user requests.

In conclusion, the book recommendation project is a comprehensive solution that leverages the latest advances in NLP, embedding techniques, and ML to provide personalized book recommendations to users. By utilizing the NLTK library, word embedding techniques, RNNs, Flask, HTML, CSS, Javascript, and Heroku deployment, the project provides a scalable and accessible solution for helping book lovers discover new books.


 ## The following Python libraries were used in the book recommendation project:

- Pandas: Pandas is a powerful data analysis library used to pre-process and manipulate the data required for the project.

- Numpy: Numpy is a numerical computing library that provides support for arrays, matrices, and mathematical operations required for training the ML model.

- Scikit-learn (Sklearn): Sklearn is a machine learning library used to vectorize the book titles and train the ML model.

- Flask: Flask is a microweb framework used for the backend of the web application, providing the necessary functionality for processing user requests and generating book recommendations.

- Math: The Math library provides support for mathematical operations and calculations required for the ML model.

- Matplotlib: Matplotlib is a data visualization library used to create visual representations of the data and training results.

- Natural Language Toolkit (NLTK): NLTK is a library used for pre-processing and manipulating text data, including the vectorization of book titles.

## FUTURE IMPROVEMENTS:

- Complete Book Title Input: Currently, the book title needs to be typed out in full in order to generate a recommendation. To improve this in the future, the solution could be enhanced to allow for keyword-based searches, where users could type out a keyword related to the book title, and receive relevant recommendations.

- Data Cleaning: Another area for improvement is the data used for generating the book recommendations. The data quality can significantly impact the accuracy of the recommendations, and further data cleaning and pre-processing techniques could be applied to ensure that the data is consistent and of high quality.

- Improved Pearson Correlation: The Pearson correlation is a measure of the similarity between two datasets. By improving the quality of the data, and potentially incorporating additional techniques such as singular value decomposition (SVD) or matrix factorization, it may be possible to increase the accuracy of the Pearson correlation between books and provide more relevant recommendations to users.

- These future improvements have the potential to enhance the accuracy and relevancy of the book recommendations, providing users with a more personalized and enjoyable experience.

## Conclusions:

The book recommendation system is a solution that aims to provide personalized book recommendations to users based on their interests. The project uses NLP techniques and machine learning algorithms to recommend books based on the similarity of their Wikipedia pages. The solution is built using a combination of Flask for the backend, HTML, CSS, and JavaScript for the frontend, and deployed on the Heroku platform for easy access.

## Summary:

The book recommendation system is a solution that provides personalized book recommendations to users based on their interests. The solution uses NLP techniques, machine learning algorithms, and deployment on the Heroku platform to achieve its goals. The project has the potential to provide users with a personalized and enjoyable experience, making it easier for them to discover new books and expand their reading horizons.

## How you can use the WebAPP and How to make improvements

### Using the Web App:

- Visit the Heroku deployment link for the Web App.
- Type in the name of the book you are looking for recommendations for.
- The Web App will display a list of book recommendations based on its similarity to the query book.

### Improving the code:

- Visit the GitHub repository of the project.
- Fork the repository to your own GitHub account.
- Clone the repository to your local machine.
- Install the necessary dependencies mentioned in the "Requirements.txt" file.
- Make the desired changes and improvements to the code.
- Commit and push the changes to your forked repository.
- Submit a pull request to the original repository for review and merging.
- Note: It's recommended to have a basic understanding of NLP, web development and Git before attempting to improve the code.


![image1](https://user-images.githubusercontent.com/90535174/218240959-37a2ac75-71a8-4555-a430-f3d0162373d3.jpg)

![image2_1](https://user-images.githubusercontent.com/90535174/218241045-83a25fd0-6654-43ad-b03a-f15121b371a9.jpg)
