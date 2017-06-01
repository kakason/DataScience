# Ads Recommendation System

It can give you some ads that you might like which based on your **Social Network Data**

## Social Network Data

1. Personal information
    * ID, gender, location and age
2. Page preference
    * Created time
3. Page category
    * Foods, travels, movies, musics etc.
4. Data source from **Pin-Liang Chen**
    * [Link](https://goo.gl/pqge2Q)

## Methods

1. Based on user's personal information i.e., gender, location, age and the time when this **like** was made to predict that each of them might like which types of ads most
2. Decision tree
    * Features: **Gender**, **Location**, **Age**, **Morning**, **Afternoon**, **Night**, **Midnight**
    * Target: **Category**
3. Our current accuracy is about **30%**

## Details

1. ``main.py`` will call the function ``classify()`` of ``decision_tree.py`` to build the decision tree

2. There are 3 parts in the ``decision_tree.py``
    * split(): Call ``data.py`` to load the data and do the preprocessing
    * output_matrix(): Show the feature matrix and the target matrix(It will produce a file called ``matrix.csv``)
    * classify(): Train and test the model which is returned from ``split()`` and print the accuracy
    
3. ``tools`` and ``tests``
    * We use relative path to include python files which can make it more clear and readable
    * There is a file called ``find_best.py``. We will explain it in **Usage** part

## Usage

1. //Todo 







