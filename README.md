# Readability
An application to calculate the Average Reading Rate 
using the by using the formula of Coleman Liau.

The application was implemented as a xCS50 assignment.<br>
Please respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.

A demo of the application can be watched at [xCS50 Problem set 6: Readability](https://cs50.harvard.edu/x/2024/psets/6/readability/)

## Installation
1. Clone the repository:
```sh
# Using SSh 
ssh git@github.com:krigjo25/Console-Readability-py.git

# Using git bash
git clone https://github.com/krigjo25/Console-Readability-py.git

# Using Github Cli
gh repo clone Console-Readability-py
```

2. Navigate to the project directory
```sh
cd Console-Readability-py
```

3. Run the file
```sh
python app.py
```

##  Usage
To use the application, run the following command in your terminal

### Example
```sh
python app.py

Calculate Sentence:  <Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec lobortis nulla nec elit sagittis, at sollicitudin mi egestas. Nam egestas finibus nibh, vitae cursus orci condimentum sed. Nulla diam augue, aliquam in magna sit amet, euismod ornare ligula. Aliquam pharetra, velit finibus mattis euismod, leo augue molestie ex, at tempor leo ex ut neque. Nam ultrices porta metus. Curabitur facilisis risus dolor, nec auctor lectus laoreet at. Nam nec tellus ante.>
Grade : 12
```
Replace `<Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec lobortis nulla nec elit sagittis, at sollicitudin mi egestas. Nam egestas finibus nibh, vitae cursus orci condimentum sed. Nulla diam augue, aliquam in magna sit amet, euismod ornare ligula. Aliquam pharetra, velit finibus mattis euismod, leo augue molestie ex, at tempor leo ex ut neque. Nam ultrices porta metus. Curabitur facilisis risus dolor, nec auctor lectus laoreet at. Nam nec tellus ante.>` with the desired ammount

##  Math formula

### Coleman-Liau formula
-   Average number of letters per 100 words
-   Average numbers of sentence per 100 words
-   L = letters / x words * 100
-   S = sentence / x words * 100
-   CLI = (L - S - 15.8)

### Date created / finished
Tuesday, January 10, 2023
Wednesday, January 11, 2023 11:56 AM CET

##  Testing framework  / Datasets
No tests for this project

## LICENCE
The application is under [The Unlicensed](./LICENCE).

## Notes from the developer
Created with love, for python programming,

Thanks for reading, and have a blessed day,<br>
@krigjo25