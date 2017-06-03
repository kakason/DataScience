# Ads Recommendation System

It can give you some ads that you might like which based on your **Social Network Data**

## Social Network Data

1. Personal information
    * ID, gender, location and age
2. Page preference
    * Created time
3. Page category
    * Foods, travels, movies, musics etc.
4. Data source from engineer **Pin-Liang Chen**
    * [Link](https://goo.gl/pqge2Q)

## Methods

1. Based on user's personal information i.e., gender, location, age and the time when the **like** was clicked to predict the ads that each of them might like the most
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
    * Folder ``tools`` contains 4 python files.
    * ``load_csv.py`` will load the social network data into our program.
    * ``hobby_merge.py`` focuses on reducing the number of user's page categories. Since some hobbies actually are referred to the same meaning, we decided to add this python file to avoid this problem. Also, if there are too many categories, it is really hard for the model to learn the pattern from it which can definitely make our accuracy become smaller.
    * ``translate.py`` will basically encode our features.
    * ``find_best.py`` will decide which combination of features can make our accuracy better than anyone else.

## Usage

1. Make sure that you have downloaded the .csv files from the link we provided above(see the hyper link). Remember to choose the **Social Network Data** ones.
2. Clone our project into your local repository or just download the ZIP file.
3. Create a folder named ``Social_Network_Data`` inside the folder ``ARS`` and put the whole files which is the Socail Network Data that you have downloaded into it.
4. Open Pycharm IDE and run it.
5. The result will have 2 parts.
   * One is the accuracy which will be printed in the console.
   * The other one is that it will generate a file called ``matrix.csv`` which contains the feature matrix and the target matrix of our model before training and testing.

## Problems

1. If you have anything errors when you compile it, please make sure you have downloaded the required modules as the **import** shows.
2. The project isn't very good enough. So if you have any ideas that you want to share with us just feel free to email me.





