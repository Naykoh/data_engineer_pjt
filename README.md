# data_engineer_pjt
The purpose of this project is to combine all the skills collected throughout the course thus far, and to provide a solid example of real-life application development in a DevOps environment.

## User Stories
* The application is a sentiment analysis application, which, given a piece of text, should be able to reply with its sentiment as being positive, negative, or neutral.
* The text language used must be English
* The application should have a web interface with an input form and a submit button, where users can input their sentences, and hit submit, and the sentiment of their sentence will be presented.
* The accuracy of the sentiment analyzer should be above 80%
* The application must be easily deployable


## Technical Description
### The ML model
Classification of amazon reviews for sentiment analysis : 
* prediction : "__label1__" means that it is a bad review
* prediction : "__label2__" means that it is a good review
Built with: ntlk, pickle, sklearn( TfidfVectorizer and Naive Bayes)

### The Web Interface
Web interface based on the ML model to predict sentiment of sentence.
Built with: Flask

### The Application Package
The final format of the application ready for distribution should be a Docker Image, which administrators can simply run Containers from.
Built with: Docker


<!-- GETTING STARTED -->
## Getting Started

How to build and run the docker image

### Prerequisites
This project has been done in specific conda environment

```sh
conda create --name <env_name> --file requirementsconda.txt
```
### Installation

1. Build docker image
```sh
docker build -t sentiment_analysis .
```
2. Run the docker image on localhost:5000
```sh
docker run -p 5000:5000 sentiment_analysis
```
4. The image is now running on localhost:5000, you can test if the integration is done correctly by doing
```sh
python test_app.py
```