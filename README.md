Database link in sqlite format can be accessed from here :- https://drive.google.com/drive/folders/1rUTwUeupTpr19kNZkKNGacoefrmbl1wp?usp=sharing

## 1. Click on the "Fork" button in the upper-right corner of the page.

  <img align="center" width = "300" src = "https://docs.github.com/assets/cb-40742/mw-1440/images/help/repository/fork-button.webp" alt="fork image"/>

## 2.Clone the Forked Repository:
  #### Go to your GitHub account, open the forked repository, click on the code button and then click the copy to clipboard icon
![image](https://github.com/Surya-Abhinai/INTEL_QUEST-Plagiarism-Checker-/assets/124990558/7f0cd92a-893d-4860-ae47-364bc7fd3416)
  #### Use the git clone command to clone your forked repository to your local machine. Replace   <repository-url> with the URL of your forked repository.
  ```
  git clone <repository-url>
```

# Getting started with the project
Firstly, initialize a virtual environment in your local system, using the following command (after changing to the cloned repo directory): 
```
python3 -m venv .
```
In order to activate the virtual environment run the following command: 
```
source bin/activate
```
Following this, the dependencies can be installed by running the following command in the command line interface: 
```
pip install -r requirements.txt
```
Following this , Install the database from the link provided above and add that to your virtual environment.

Finally, the flask app can be launched by running the following command in the terminal: 
```
python app.py
```
