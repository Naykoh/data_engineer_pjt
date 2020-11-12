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
Classification of tweets and reddit comments for sentiment analysis : 
* prediction : negative, neutral, positive
Built with: tensorflow

### The Web Interface
Web interface based on the ML model to predict sentiment of sentence.
Built with: Flask

### The Application Package
The final format of the application ready for distribution should be a Docker Image, which administrators can simply run Containers from.
Built with: Docker


<!-- GETTING STARTED -->
## Getting Started

### Requirements 
You will need anaconda, git bash and docker installed on your pc.


### Installation
How to build and run the docker image.


1. Launch an anaconda prompt and put yourself in the directory

2. Build docker image and run it into container on localhost:5000
```sh
docker-compose up
```
3. The webapp is now running on localhost:5000, you can test if the integration is done correctly by doing
```sh
python test_app.py
```
4. Stop the container
```sh
docker-compose down
```


Those steps can be automated using shell script. You can run it on linux or windows. 
run*.sh will buid and run the container.
stop*.sh will stop the container.

### (Optional) 
This project has been done in a specific conda environment, to reproduce this environment:
(reproducing the environment is not mandatory, but if you have problem, it is better to reproduce the same environment)

1. Launch an anaconda prompt

2. Run this from the repo path :
```sh
conda env create -f environment.yml
```
3. Activate this new environment
```sh
conda activate sentiment_analysis
```
