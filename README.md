# Machine-Learning-Clustering

###### The project

This project is an example of using a popular machine learning algorithm: The “k-means” clustering [algorithm](https://en.wikipedia.org/wiki/K-means_clustering). The algorithm is used to cluster different countries according to the relationship between their birth rate and life expectancy. The python algorithm was implemenetd from scratch and is my original attempt at the task (a lot simpler than a lot of the other readily available k-means python projects). The program allows the user to choose the number of clusters to create and the number of iterations to run (both being positive integers). It also allows the user to select which dataset to use. A user is able to run this algorithm on a completely different dataset but the code would need to be adjusted according to how the data has been layed out in the file.

###### Usefulness

This project is useful in the sense that it provides a base understanding of how the k-means clustering algorithm can be applied to datasets with the aim of grouping (clustering) elements that share similar patterns and/or behaviours. The algorithm in the program can be applied to any dataset that includes elements that hold a relationship between two variables (in the program countries are the elements and they hold a relationship between birth rate and life expectancy). By understanding this real life scenarios can be simulated to show clusters of elements according to the variables attached to them and how these variables relate to one another.

###### Maintainers and contributers 

Egor Zakharov

###### Running the program

Getting the program to work is fairly simple and works as follows:

* You will need to install Numpy and Matplotlib. For more information on installing python packages see https://packaging.python.org/tutorials/installing-packages/
* Download kmeans.py & all the csv files to the same directory
* In line 20 of kmeans.py specify which csv file you would like to use in the program
* Run the code in an IDE that supports python and provide valid input for the number of clusters and the number of iterations (any positive integer)
* A new window will open up with a graph plotted with all the elements (countries) with BirthRate on the x-axis and LifeExpectancy on the y-axis. These elements will also be assigned to a random cluser (initially) and be color coded according to their cluster. Close this window for the new window to pop up to see how each iteration of the algorithm updates the clusters making them more accurate each time. In the end some analysis about the clusters will be outputted by the program.
