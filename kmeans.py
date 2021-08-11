# import relevant libraries
import math
import csv
import random
import matplotlib.pyplot as plt
import numpy


# Function that computes the distance between two data points
# that takes 2 lists of length 2 as parameters where
# first element is x value and 2nd element is y value
def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# Function that reads data in from csv files
# and stores the data in a list
def reader():
    # Open csv file to read
    with open('dataBoth.csv', 'r') as data_file:
        # store file in variable
        data = csv.reader(data_file)
        # loop and add every row of data in file to list
        for row in data:
            countries.append(row)

    # remove unnecessary first element in list
    countries.remove(countries[0])

    # loop through each country moving the country name to the end of the list
    # and converting remaining string values to floats
    for country in countries:
        country.append(country[0])
        country.remove(country[0])
        country[0] = float(country[0])
        country[1] = float(country[1])


# Define a function that finds the closest centroid to each point out of all the centroids
def closest_centroid():
    # global variable for total distance
    global total_distance
    # set distance to 0 each time function is called
    total_distance = 0
    # clear all clusters
    clusters.clear()
    # add k amount of empty lists to clusters
    for num_of_clusters in range(k):
        clusters.append([])
    # loop through each point in the list of countries
    for point in countries:
        # create an array for distances
        distances = []
        # loop over each centroid
        for centroid in centroids:
            # add the distance between the point and the centroid to distances list
            # by calling the distance function and passing the point and the centroid
            distances.append(distance(point, centroid))
        # get the index of the cluster with the shortest distance using numpy
        result = numpy.amin(distances)
        # increment the total distance by the square of the distance
        # between the point and the centroid to which it belongs
        total_distance += result ** 2
        # loop over every centroid
        for centroid in centroids:
            # if the centroid is equal to the centroid with the closest distance to the point
            if centroid == centroids[distances.index(result)]:
                # add the point to the cluster that includes the closest centroid to the point
                clusters[centroids.index(centroid)].append(point)


# Function to visualise the clusters
def visualise():
    # create a list called datasets storing all x and y values to be plotted per cluster
    datasets = []
    # add k amount of 2d arrays with 2 elements to datasets
    for y in range(k):
        datasets.append([[], []])
    # loop through every cluster
    for every_cluster in clusters:
        # store index of each cluster
        dataset_index = clusters.index(every_cluster)
        # loop through every element in each cluster
        for cluster_element in range(len(every_cluster)):
            # add x and y values to their specified positions in the dataset from every cluster
            datasets[dataset_index][0].append(every_cluster[cluster_element][0])
            datasets[dataset_index][1].append(every_cluster[cluster_element][1])
    # loop through every element in each cluster
    for cluster_element in range(len(datasets)):
        # plot the x and y values from the lists inside the dataset for every cluster
        plt.scatter(datasets[cluster_element][0], datasets[cluster_element][1])
        # plot every centroid
        plt.plot(centroids[cluster_element][0], centroids[cluster_element][1], marker='x', markersize=20)
    # show the plot
    plt.show()


# list for countries
countries = []
# call function to read in csv file
reader()
# get number of clusters as input from user
k = int(input("Enter the number of clusters (k): "))
# get the number of iterations as input from user
i = int(input("Enter the number of iterations: "))
# randomly choose centroids
centroids = random.sample(countries, k)
# list for clusters
clusters = []
# list for cluster countries
cluster_countries = []
# create variable for total distance and set to zero
total_distance = 0

# add k amount of empty lists to clusters and cluster countries
for cluster in range(k):
    clusters.append([])
    cluster_countries.append([])


# Function to calculate the new mean of all the points in each cluster
def mean():
    # loop through every cluster
    for every_cluster in clusters:
        # set total for x and y to 0
        x_total = 0
        y_total = 0
        # loop though each point in every cluster
        for point in every_cluster:
            # increment total for x and y
            x_total += point[0]
            y_total += point[1]
        # set the new value for each centroid to the mean of each cluster
        centroids[clusters.index(every_cluster)] = [x_total / len(every_cluster), y_total / len(every_cluster)]


# Function to iterate
def iterate(iterations):
    # for every iteration
    for iteration in range(iterations):
        # call the closest centroid function
        closest_centroid()
        # call the mean function
        mean()
        # visualise the changes
        visualise()
        # output the total distance
        print("Total sum of squared distances :", total_distance)


# call iteration function i times
iterate(i)
# loop through each cluster
for cluster in clusters:
    # loop through every element in each cluster
    for element in cluster:
        # add the country name to the cluster country of the same index of the cluster where the country belongs
        cluster_countries[clusters.index(cluster)].append(element[2])

# Print out the results for questions

# 1.) The number of countries belonging to each cluster
for cluster in clusters:
    number = clusters.index(cluster) + 1
    print("Number of countries in cluster", number, ":", len(cluster))

# 2.) The list of countries belonging to each cluster
for cluster in clusters:
    number = clusters.index(cluster) + 1
    print("Countries belonging to cluster", number, ":", cluster_countries[number-1])

# 3.) The mean Life Expectancy and Birth Rate for each cluster
for cluster in clusters:
    number = clusters.index(cluster) + 1
    total_birth_rate = 0
    total_life_expectancy = 0
    for element in cluster:
        total_birth_rate += element[0]
        total_life_expectancy += element[1]
    mean_birth_rate = total_birth_rate/len(cluster)
    mean_life_expectancy = total_life_expectancy/len(cluster)
    print("The mean birth rate for cluster", number, ":", mean_birth_rate)
    print("The mean life expectancy for cluster", number, ":", mean_life_expectancy)
