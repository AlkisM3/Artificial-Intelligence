# -*- coding: utf-8 -*-
"""Artificial Intelligence,lab3 el18162 and el18868.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-mcff7VH326g5wBwdN40go93Jj9HGeyX
"""

### Μέλη Ομάδας:

#Ον/μο1: ΣΤΕΦΑΝΟΣ ΒΟΪΚΟΣ  
#Αρ. Μητρώου 1: 03118162

#Ον/μο2: ΑΛΚΙΒΙΑΔΗΣ ΜΙΧΑΛΙΤΣΗΣ
#Αρ. Μητρώου 2: 03118868

from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score
from matplotlib import pyplot as plt
import numpy as np
import random

class Evaluate:
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred

    def my_accuracy(self):
        y_true = self.y_true
        y_pred = self.y_pred
        
        ##################
        ## Your code below
        wrong = 0
        for index in range(len(y_true)):
          if y_true[index] != y_pred[index]:
            wrong = wrong + 1
        right = len(y_true)-wrong
        acc = 1
        acc = right/len(y_true)
        ## Your code above
        ##################
        return acc

    def get_metrics(self):
        precision = precision_score(self.y_true, self.y_pred, average = "macro")
        recall = recall_score(self.y_true, self.y_pred, average = "macro")
        f1 = f1_score(self.y_true, self.y_pred, average = "macro")
        results = {"precision": precision, "recall": recall, "f1": f1, "accuracy": self.my_accuracy()}
        return results   
    
    def confusion_matrix(self):
        cm = confusion_matrix(self.y_true, self.y_pred)
        return cm 

    def get_evaluation_report(self):
        metrics = self.get_metrics()
        for m in metrics:
            print(m + ': ' + str(metrics[m]))
        cm = self.confusion_matrix()
        print("Confusion matrix: ")
        print(cm)

y_true = [1, 0, 1, 0, 0, 1, 1, 0]
y_pred = [1, 0, 1, 0, 1, 1, 0, 0]

eval = Evaluate(y_true, y_pred)
eval.get_evaluation_report()

from google.colab import drive
import os
drive.mount('/gdrive')
os.listdir('/gdrive/My Drive') 
path='/gdrive/My Drive/'

import pandas as pd
from tqdm.notebook import tqdm 
# read data in the form of pandas DataFrame
data = pd.read_csv(path + "music_df_processed.csv")

# print the first 5 values of the DataFrame using .head() command
print(data.head())
# What can we see here?
data.describe()

print("Lenght of data is : " + str(len(data)) + " and are :")
#print((data.to_numpy)[0])

import pandas as pd

df = pd.DataFrame(data)

#numpy_array = df.to_numpy()

#print((numpy_array))

#print(data.shape)

#ΠΗΡΑ ΜΟΝΟ ΤΑ ΝΟΥΜΕΡΑ ΕΕ
#ΝΑΙ 4,5,7,8,10,13
# χαρακτηριστικά
inputs = ["acousticness", "danceability", "energy", "instrumentalness", "liveness", "speechiness"]

# κατηγορίες-στόχοι
output = "music_genre"
genres = ["Electronic", "Rock", "Rap"]

# φιλτράρουμε το DataFrame ώστε να διατηρήσουμε μόνο τις 3 κατηγορίες που μας ενδιαφέρουν.
data = data[data[output].isin(genres)]
print(data.shape)
# dictionary to map genre to label id 
genres_to_id = {genre: i for i, genre in enumerate(genres)}

# εδώ πρέπει να διαχωρίσετε τα δεδομένα σε train (70% των δεδομένων)/test set (30% των δεδομένων)
# ονομάστε τις μεταβλητές ως εξής:
# τα χαρακτηριστικά του train set: x_train
# τις κατηγορίες-στόχους του train set: y_train
# τα χαρακτηριστικά του test set: x_test
# τις κατηγορίες-στόχους του test set: y_test
x_test, y_test, x_train, y_train = [], [], [], []
##################
## Your code below
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler

#mnist_dataframe = pd.read_csv(path + "music_df_processed.csv",sep = ",",header=None)
#mnist_dataframe = mnist_dataframe.head(10000)

mnist_dataframe = data.reindex(np.random.permutation(data.index))
#XORISE se 30% kai 70%
train_set = mnist_dataframe[:int(0.7*len(mnist_dataframe))]
test_set = mnist_dataframe[int(0.7*len(mnist_dataframe)):int(len(mnist_dataframe))]

#print(type(train_set))
#print(type(test_set))

df = pd.DataFrame(train_set)
train_set = df.to_numpy()
df = pd.DataFrame(test_set)
test_set = df.to_numpy()

#print(train_set)

#print("TRAIN_DSET IS : ")
#for k in range(18):
#    print(train_set[0][k])
#print()
#print("")
#print("TEST_DSET IS : ")
#print(test_set[0])
#print("")

x_train = np.zeros((len(train_set),6))
x_test = np.zeros((len(test_set),6))
#y_train = np.ndarray((len(train_set),2),dtype = str)
#y_test = np.ndarray((len(test_set),2),dtype = str)

for i in range(len(train_set)):
    h = 0
    if ("popularity" in train_set[i]):
        #print("NAI YPARXEI EEE : ")
        continue
    #ΝΑΙ 4,5,7,8,10,13
    for j in range(18):
        if(j == 4 or j == 5 or j == 7 or j == 8 or j == 10 or j == 13):
            x_train[i][h] = train_set[i][j]
            h+=1 
        if(j == 17):
            y_train.append(train_set[i][j])

for i in range(len(test_set)):
    h = 0
    g = 0
    if ("popularity" in test_set[i]):
        #print("NAI YPARXEI EEE : ")
        continue
    #ΝΑΙ 4,5,7,8,10,13
    for j in range(18):
        if(j == 4 or j == 5 or j == 7 or j == 8 or j == 10 or j == 13):
            x_test[i][h] = test_set[i][j]
            h+=1
        if(j == 17):
            print(test_set[i][j])
            y_test.append(test_set[i][j])


def train_test_split(train_perc, data):
    n_elements = train_perc*data.shape[0]
    rand_nums = set()
    test_nums = []
    while(len(rand_nums) < n_elements):
        rabd_nums.add(random.randrange(0, data.shape[0]-1))
    for i in range(data.shape[0]-1):
        if i not in rand_nums:
            test_nums.append(i)
    return data.iloc[:, :].values[rand_nums], data.iloc[:, :].values[test_nums]

def show_image(features):
    img = features.reshape((17,17))
    plt.imshow(img)
    plt.show()

#x_train = train_dset
#x_test = test_dset
#y_train = parse_labels_and_features(pd.Series(train_dset))
#y_test = parse_labels_and_features(pd.Series(test_dset))

#print(x_train[i])
#show_image(x_train[i])
#print("Label = " + str(y_train[0]))

#%% md

## Μορφή των δεδομένων  

#Βεβαιωθείτε ότι τα δεδομένα σας έχουν τη σωστή μορφή εκτυπώνοντας τον αριθμό γραμμών και στηλών για τα x_test, y_test, x_train, y_train.
print("")
print("X_test is : \n")
print(x_test)
print("")
print("Y_test is : \n")
print(y_test)
print("")
print("X_train is : \n")
print(x_train)
print("")
print("Y_train is : \n")
print(y_train)
print("")
#%%

print("###################################################\n")
# Shape of x_test, y_test, x_train, y_train

print("Shape of X_test is : \n")
print(np.shape(x_test))
print("")
print("Shape of Y_test is : \n")
print(np.shape(y_test))
print("")
print("Shape of X_train is : \n")
print(np.shape(x_train))
print("")
print("Shape of Y_train is : \n")
print(np.shape(y_train))
print("")

#Αναφορικά με τις τιμές των χαρακτηριστικών, είναι σημαντικό να γνωρίζουμε το εύρος τους, δηλαδή τη μέγιστη και την ελάχιστη τιμή που λαμβάνει το κάθε χαρακτηριστικό. Εξερευνήστε το εύρος του κάθε χαρακτηριστικού στα train και test set. 

#%%

# Range of x_train, x_test columns for every character
def maximum(k, maxx):
    if(str(maxx) > str(k)):
        return maxx
    else:
        return k

def minimum(k,maxx):
    if(str(maxx) > str(k)):
        return k
    else:
        return maxx

megisto_kathe_charactiristiko_x_train = []
elaxisto_kathe_charactiristiko_x_train = []

for i in range(int(np.shape(x_train)[1])):
    megisto = x_train[0][i]
    elaxisto = x_train[0][i]
    for j in range(1,int(np.shape(x_train)[0])):
        megisto = maximum(megisto, x_train[j][i])
        elaxisto = minimum(elaxisto, x_train[j][i])
    megisto_kathe_charactiristiko_x_train.append(megisto)
    elaxisto_kathe_charactiristiko_x_train.append(elaxisto)

print("Megisto kathe charactiristiko of x train is : \n")
print(megisto_kathe_charactiristiko_x_train)
print("")

print("Elaxisto kathe charactiristiko of x train is : \n")
print(elaxisto_kathe_charactiristiko_x_train)
print("")

megisto_kathe_charactiristiko_x_test = []
elaxisto_kathe_charactiristiko_x_test = []

for i in range(int(np.shape(x_test)[1])):
    megisto = x_test[0][i]
    elaxisto = x_test[0][i]
    for j in range(1,int(np.shape(x_test)[0])):
        megisto = maximum(megisto, x_test[j][i])
        elaxisto = minimum(elaxisto, x_test[j][i])
    megisto_kathe_charactiristiko_x_test.append(megisto)
    elaxisto_kathe_charactiristiko_x_test.append(elaxisto)

print("Megisto kathe charactiristiko is of x test : \n")
print(megisto_kathe_charactiristiko_x_test)
print("")
print("Elaxisto kathe charactiristiko is of x test : \n")
print(elaxisto_kathe_charactiristiko_x_test)
print("")
print("###################################################\n")

diafora_x_test = []
diafora_x_train = []
for i in range(int(np.shape(x_test)[1])):
   check_megisto_kathe_charactiristiko_x_test = isinstance(megisto_kathe_charactiristiko_x_test[i], int) or isinstance(megisto_kathe_charactiristiko_x_test[i],float)
   check_elaxisto_kathe_charactiristiko_x_test = isinstance(elaxisto_kathe_charactiristiko_x_test[i], int) or isinstance(elaxisto_kathe_charactiristiko_x_test[i],float)
   check_megisto_kathe_charactiristiko_x_train = isinstance(megisto_kathe_charactiristiko_x_train[i], int) or isinstance(megisto_kathe_charactiristiko_x_train[i],float)
   check_elaxisto_kathe_charactiristiko_x_train = isinstance(elaxisto_kathe_charactiristiko_x_train[i], int) or isinstance(elaxisto_kathe_charactiristiko_x_train[i],float)
   if(check_megisto_kathe_charactiristiko_x_test and check_elaxisto_kathe_charactiristiko_x_test):   
      diafora_x_test.append(float(megisto_kathe_charactiristiko_x_test[i]) - float(elaxisto_kathe_charactiristiko_x_test[i]))
   if(check_megisto_kathe_charactiristiko_x_train and check_elaxisto_kathe_charactiristiko_x_train):   
      diafora_x_train.append(float(megisto_kathe_charactiristiko_x_train[i]) - float(elaxisto_kathe_charactiristiko_x_train[i]))

print("Range of x test : \n")
print(diafora_x_test)
print("")
print("Range of x train : \n")
print(diafora_x_train)
print("")
print("###################################################\n")

#print("Max value of x_train is: " + str(np.max(x_train[i])))
#print("Max value of x_test is: " + str(np.max(x_test[i])))

#print("Min value of x_train is: " + str(np.min(x_train[i])))
#print("Min value of x_test is: " + str(np.min(x_test[i])))

#ΑΠΑΝΤΗΣΗ-ΣΧΟΛΙΑΣΜΟΣ 1ου ΕΡΩΤΗΜΑΤΟΣ
#Έχουν τα χαρακτηριστικά μας περίπου το ίδιο εύρος;
#H απάντηση είναι ναι, καθώς στην πλειοψηφία των κατηγοριών ενδιαφέροντος, το εύρος μέγιστης-ελάχιστης τιμής είναι κοντά στο 0.9 , ενώ σε 2 κατηγορίες, η τιμή είναι σχεδόν μηδενικές

#ΑΠΑΝΤΗΣΗ-ΣΧΟΛΙΑΣΜΟΣ 2ου ΕΡΩΤΗΜΑΤΟΣ
#Είναι προφανές ότι στο 2ο ερώτημα, παρατηρούμε πως όλες οι τιμές βρίσκονται στο διάστημα [0,1], οπότε και πράγματι συμβαίνει αυτό στην περίπτωσή μας.

## STEP 2

from numpy import linalg
from collections import Counter 

class KNN:
  def __init__(self,x,y,k,distance="euclidian"):
    self.x = x
    self.y = y
    self.k = k
    self.distance = distance  
  
  ## Compute the distance between the two vectors img1 and img2
  # hint: use np.linalg.norm for eucledian
  # hint: use equation given above for cosine
  def get_distance(self,row1,row2):
    if self.distance=='euclidian':
      ##################
      ## Your code below
      dists = np.linalg.norm(row1-row2) 
      return dists
      ## Your code above
      ##################
    elif self.distance=='cosine':
      ##################
      ## Your code below
      nom = np.dot(row1, row2)
      row12 = np.linalg.norm(row1)
      row22 = np.linalg.norm(row2)
      denom = row12 * row22 
      dists = 1 - (nom / denom) 
      ## Your code above
      ##################
      return dists
    else:
      print("Error")

  ## Given an image as a vector, returns indexes of k nearest neighbors
  def get_knn(self,img):
    distances = list()
    x = self.x
    k = self.k    
    ans_indexes = np.zeros(k)
    ##################
    ## Your code below - populate the distances list
    # hint: you can use a for loop
    for index in x:
        #print(index)
        #print(img)
        dist = self.get_distance(index, img)
        #print(dist)
        distances.append(dist)
    ## Your code above
    ##################
    #print(distances)
    # Sort distances, and return the indexes of k first elements
    ans_indexes = np.argsort(distances,axis = None)[:k]
    return ans_indexes

  def most_frequent(self, List): 
      occurence_count = Counter(List) 
      return occurence_count.most_common(1)[0][0]
      '''
      occurence_count = {}
      print(List)
      for i in range(len(List)): #Counter(List)
          if (List[i][0] not in occurence_count):
              occurence_count[List[i]] = 0
          else:
              occurence_count[List[i]] += 1
      return max(occurence_count.values)
      '''
  ## Given an image as a vector, classify it according to KNN
  # hint: we have a list of k labels and want to return the most common one
  def classify(self,img):
      y = self.y
      nn_labels = [y[i] for i in self.get_knn(img)]  
      ##################
      ## Your code below    
      prediction = self.most_frequent(nn_labels) #in case of draw it chooses the first element appeared in nn_labels
      ## Your code above
      ###################
      return prediction

#MENEI EROTIMATIKO GIA EDW NA PAREI
#THA KANW ANTISTOIXISH KAI EINAI WS EKSIS :
genres = ["Electronic", "Rock", "Rap"]
my_dict = {"Electronic":0 , "Rock":1, "Rap":2}
for i in range(len(y_test)):
    if(y_test[i] == "Electronic"):
        y_test[i] = 0
    if(y_test[i] == "Rock"):
        y_test[i] = 1
    if(y_test[i] == "Rap"):
        y_test[i] = 2 

for i in range(len(y_train)):
    if(y_train[i] == "Electronic"):
        y_train[i] = 0
    if(y_train[i] == "Rock"):
        y_train[i] = 1
    if(y_train[i] == "Rap"):
        y_train[i] = 2 

y_train = pd.Series(y_train)
knn = KNN(x_train, y_train, k=5, distance='euclidian')

'''
img = x_test[np.random.randint(0,x_test.shape[0])]
print("Input image: ")
show_image(img)
print('Prediction : '+str(knn_e.classify(img)))
y_trains = pd.Series(y_train)
'''

#Test for euclidean distance
print(x_test)
#img = x_test[np.random.randint(0,x_test.shape[0])]
#img = pd.Series(img)
preds = [knn.classify(x_test[i]) for i in range(100)]
#y_tests = np.array([np.array(xi) for xi in y_test])
labels = [y_test[i] for i in range(100)]

eval = Evaluate(labels, preds)
eval.get_evaluation_report()

from sklearn.neighbors import KNeighborsClassifier

k = 5
knc = KNeighborsClassifier(n_neighbors = k)
knc.fit(x_train, y_train)
y_pred = knc.predict(x_test[:100])

eval = Evaluate(y_test[:100], y_pred)
eval.get_evaluation_report()
#Pws to ytest?
#eval = Evaluate(ytest[:100], y_pred)
#eval.get_evaluation_report()

#%%time
#print(x_test)
knc = KNN(x_train, y_train, k = 5, distance = 'euclidian')
y_pred = [knc.classify(x_test[i]) for i in range(100)]
eval = Evaluate(labels, y_pred)
eval.get_evaluation_report()

#%%time
knn = KNN(x_train, y_train, k = 5, distance = 'cosine')
y_pred = [knn.classify(x_test[i]) for i in range(5)]
labels = [y_test[i] for i in range(5)]
evalh = Evaluate(labels, y_pred)
evalh.get_evaluation_report()

#%%time
knc = KNeighborsClassifier(n_neighbors = 5)
knc.fit(x_train, y_train)
labels = [y_test[i] for i in range(100)]
y_pred = knc.predict(x_test[:100])
evalb = Evaluate(labels, y_pred)
evalb.get_evaluation_report()
#Για τους χρόνους εκτέλεσης για k = 50 τρέχουμε τα 3 παρακάτω κελιά:

#%%time
knn = KNN(x_train, y_train, k = 50, distance = 'euclidian')
preds = [knn.classify(x_test[i]) for i in range(100)]
labels = [y_test[i] for i in range(100)]
evalm = Evaluate(labels, preds)
evalm.get_evaluation_report()
#%%time
knn = KNN(x_train, y_train, k = 50, distance = 'cosine')
pred = [knn.classify(x_test[i]) for i in range(100)]
labeln = [y_test[i] for i in range(100)]
evals = Evaluate(labeln, pred)
evals.get_evaluation_report()
#%%time

knc = KNeighborsClassifier(n_neighbors = 50)
knc.fit(x_train, y_train)
y_pred = knc.predict(x_test[:100])
evalk = Evaluate(labels, y_pred)
evalk.get_evaluation_report()

#ΣΧΟΛΙΑΣΜΟΣ ΑΠΟΤΕΛΕΣΜΑΤΩΝ 
#Αναφορικά με τις παραδοχές, επίδοση, χρόνος εκτέλεσης, επίδραση παραμέτρου k
#Αυτό που παρατηρούμε είναι ότι προκύπτουν διαφορετικά αποτελέσματα και εξαρτάται από τις παραμέτρους
#Σε πρώτο βαθμό, βλέπουμε ότι το k έχει μικρή επίδραση στην αύξηση του αποτελέσματος, αλλά σίγουρα, όσο μεγαλύτερο είναι το k, δηλαδή όσο περισσότερα στοιχεία λαμβάνομε υπόψη με βάση το αποτέλεσμά τους,τόσο καλύτερη είναι η τελική απόδοση, αλλά με μικρή επίδραση
#Ο χρόνος εκτέλεσης σαφώς αυξάνεται με όσο μεγαλύτερο k έχουμε, δεδομένων των υπόλοιπων παραμέτρων. Αλλά και με δεδομένο k, επίσης όσο αυξάνεται το πλήθος των x_test,y_test λαμβάνουμε υπόψη, τόσο μεγαλύτερη είναι η ταχύτητα χρόνου, αλλά με πολύ μικρή επίδοση, στο αντικείμενο αυτό
#Και προφανώς, ο συνδυασμός αύξησης του k και των x_test,y_test πουυ εξετάζουμε, θα επιφέρει μεγαλύτερο χρόνο εκτέλεσης. Τέλος, παρατηρούμε ότι το cosine έχει μικρή αύξηση και αργή, αλλά με αύξηση τόσο του k και των παραμέτρων των test, τόσο καλύτερο γίνεται το αποτέλεσμα και τα αποτελέσματα που λαμβάνουμε είναι απολύτως λογικά.

## STEP 3

def discretize(x, num_of_classes = 5):  
    x_r = []
    for row in x:
        discrete = []
        for i, feature in enumerate(row):
            discrete_feature = [0] * num_of_classes
            for j, v in enumerate(np.linspace(0, 1, num_of_classes + 1)):
                if float(feature) < v:
                    break
            discrete_feature[j-1] = 1
            discrete += discrete_feature
        x_r.append(discrete)
    return np.array(x_r)

x_train_r = discretize(x_train)
x_test_r = discretize(x_test)

class NaiveBayes:
    def __init__(self,x,y):
      self.x = x
      self.y = y
      ## pC is a vector with the probability of each class
      self.pC = np.zeros((len(genres),))
      ## pxC is an array with all probabilities p(xi|C)
      self.pxC = np.zeros((x.shape[-1],len(genres))) ###shape[-1] how many pixels each image has
      ## Compute the probabilities
      self.compute_probabilities()

    def compute_probabilities(self):
      ## Compute p(C) for each class
      #print(self.pC)
      for label in self.y:
          #print(label)
          self.pC[label] += 1
      self.pC = self.pC/self.y.shape[0] #shape[0] how many pictures the training set has

      ## Compute p(xi|C) for each feature xi and class C
      # hint: you can use one or more for loops
      ###################
      ## Your code below
      num_quant = np.zeros((len(genres),))
      for i in range(len(self.y)):
        num = self.y[i]
        num_quant[num]+=1
        for bit in range(0,self.x.shape[-1]):
          if (self.x[i][bit] == 1): self.pxC[bit][num]+=1
    
      for i in range(len(genres)):
        for j in range(self.x.shape[-1]):
          self.pxC[j][i] = self.pxC[j][i]/num_quant[i]

      #Right but too slow implementation
      #for num in range(0,10):
      #    for bit in range(0,self.x.shape[-1]):
      #      num_quant = 0
      #      ones = 0
      #      zeros = 0
      #      for i in range(len(self.y)):
      #        if (self.y[i] == num):
      #          num_quant+=1
      #          if (self.x[i][bit] == 0): zeros+=1
      #          else: ones+=1
      #      self.pxC[bit][num] = ones/num_quant
                      
      ## Your code above
      ##################

    def predict(self,x):
        ## ~Probability of x belonging to each class
        ## (not actucal probability since we ignore denominator)
        pcX = np.ones((len(genres),))
        xsize = self.x.shape[-1]
        for i in range(len(genres)):
          # hint: We have probabilities p({x_j=1}|i) in self.pxC
          # We also need p({x_j=0}|i) for computing p(x|i)
          #################
          ## Your code below
          product = 1
          for bit in range(len(x)):
            if (x[bit] == 1):
              product = product*self.pxC[bit][i] 
            else:
              product = product*(1-self.pxC[bit][i])
          pcX[i] = product * self.pC[i]
          ## Your code above
          ##################
        return np.argmax(pcX)

y_trains = pd.Series(y_train)
nb = NaiveBayes(x_train_r, y_trains)
preds = [nb.predict(i) for i in x_test_r[:100]]
eval = Evaluate(y_test[:100], preds)
eval.get_evaluation_report()

#TO MONO THEMA EINAI TO INDEX APLA, OLA TA ALLA EINAI TELEIA FILE :)
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
y_pred = gnb.fit(x_train, y_train).predict(x_test[:100])

eval = Evaluate(y_test[:100], y_pred)
eval.get_evaluation_report()

#%%time
nb = NaiveBayes(x_train_r,y_train)
preds = [ nb.predict(i) for i in x_test_r[:100]]
evals = Evaluate(y_test[:100], preds)
evals.get_evaluation_report()
#%%time
gnb = GaussianNB()
y_pred = gnb.fit(x_train, y_train).predict(x_test[:100])
eval = Evaluate(y_test[:100], y_pred)
eval.get_evaluation_report()

#ΣΧΟΛΙΑΣΜΟΣ ΑΠΟΤΕΛΕΣΜΑΤΩΝ 
#Αναφορικά με τις παραδοχές, επίδοση, χρόνος εκτέλεσης, επίδραση bining/υπόθεσης κατανομής κλπ
#Η δική μας υλοποίηση έχει αρκετά μεγαλύτερο χρόνο εκτέλεσης από την έτοιμη της βιβλιοθήκης όμως η δική μας μέθοδος predict είναι πιο ακριβής και με μεγαλύτερο precision.

#Η δική μας υλοποίηση για τις 100 πρώτες τιμές του x_test,y_test έχει precision κοντά στο 0.65 και accuracy 0.64 ενώ η έτοιμη 0.63 και 0.61 αντίστοιχα.
#Επίσης, θα παρατηρούμε ότι τα μεγέθη percision και accuracy για τις δύο υλοποιήσεις αυξάνονται και κάποια στιγμή συγκλίνουν σε μία τιμή όσο αυξάνεται το πλήθος των στοιχείων που χρησιμοποιούμε για τον έλεγχο της απόδοσης του νευρωνικού.

#STEP 4

class Layer:
    def __init__(self):
        """Here we can initialize layer parameters (if any) and auxiliary stuff."""
        # A dummy layer does nothing
        pass
    
    def forward(self, input):
        """
        Takes input data of shape [batch, input_units], returns output data [batch, output_units]
        """
        # A dummy layer just returns whatever it gets as input.
        return input

    def backward(self, input, grad_output):
        # The gradient of a dummy layer is precisely grad_output, but we'll write it more explicitly
        num_units = input.shape[1]
        
        d_layer_d_input = np.eye(num_units)
        
        return np.dot(grad_output, d_layer_d_input) # chain rule



class ReLU(Layer):
    def __init__(self):
        """ReLU layer simply applies elementwise rectified linear unit to all inputs"""
        pass
    
    def forward(self, input):
        """Apply elementwise ReLU to [batch, input_units] matrix"""
        relu_forward = np.maximum(0, input)
        return relu_forward
    
    def backward(self, input, grad_output):
        """Compute gradient of loss w.r.t. ReLU input"""
        relu_grad = input > 0
        return grad_output*relu_grad

class Dense(Layer):
    def __init__(self, input_units, output_units, learning_rate = 0.1):
        self.input_units = input_units
        self.output_units = output_units
        
        self.learning_rate = learning_rate
        self.weights = np.random.normal(loc = 0.0,scale = np.sqrt(2 / (input_units + output_units)),size = (input_units, output_units))
        self.biases = np.zeros(output_units)
        
    def forward(self, input):
        """
        Perform an affine transformation:
        f(x) = <W*x> + b
        
        input shape: [number of inputs, input units]
        output shape: [number of inputs, output units]
        """
        ###################
        ## Your code below
        ## hint: numpy.dot
        output = np.dot(input, self.weights) + self.biases
        
        ## Your code above
        ##################
        return output

    def backward(self, input, grad_output):
        # compute d f / d x = d f / d dense * d dense / d x
        # where d dense/ d x = weights transposed
        grad_input = np.dot(grad_output, self.weights.T)

        # compute gradient w.r.t. weights and biases
        grad_weights = np.dot(input.T, grad_output)
        grad_biases = grad_output.mean(axis = 0) * input.shape[0]
        assert grad_weights.shape == self.weights.shape and grad_biases.shape == self.biases.shape

        # Here we perform a stochastic gradient descent step. 
        self.weights = self.weights - self.learning_rate * grad_weights
        self.biases = self.biases - self.learning_rate * grad_biases
        return grad_input

def softmax_crossentropy_with_logits(logits, reference_answers):
    logits_for_answers = logits[np.arange(len(logits)),reference_answers]
    xentropy = - logits_for_answers + np.log(np.sum(np.exp(logits),axis=-1))
    return xentropy

def grad_softmax_crossentropy_with_logits(logits, reference_answers):
    ones_for_answers = np.zeros_like(logits)
    ones_for_answers[np.arange(len(logits)),reference_answers] = 1
    softmax = np.exp(logits) / np.exp(logits).sum(axis=-1,keepdims=True)
    return (- ones_for_answers + softmax) / logits.shape[0]

from sklearn.neural_network import MLPClassifier

epochs = 25
mlp = MLPClassifier(hidden_layer_sizes=(10, 15, 20), max_iter = epochs)

mlp.fit(x_train,y_train)

y_pred = mlp.predict(x_test)
eval = Evaluate(y_test, y_pred)
eval.get_evaluation_report()

class MLP:
    def __init__(self, shapes, input_dim):
        self.shapes = shapes
        self.network = [Dense(input_dim, shapes[0])]
        self.network.append(ReLU())
        for i in range(1, len(self.shapes) - 1):
            self.network.append(Dense(shapes[i-1], shapes[i]))
            self.network.append(ReLU())
        self.network.append(Dense(shapes[i], shapes[-1]))

    def forward(self, X):
        """
        Αγόριθμος διφάνειας 33
        """
        activations = []
        input = X
        # Looping through each layer
        for l in self.network:
            ###################
            ## Your code below
            # hint: τροφοδοτούμε την έξοδο κάθε επιπέδου στο επόμενο
            input = l.forward(input)
            activations.append(input)
            ## Your code above
            ##################        
        assert len(activations) == len(self.network)
        return activations

    def predict(self,X):
        """
        Προβλέπει την έξοδο του δικτύου για ένα ή περισσότερα στιγμιότυπα εισόδου
        """
        logits = self.forward(X)[-1]
        return logits.argmax(axis = -1)

    def fit(self, X, y):
        # Get the layer activations
        layer_activations = self.forward(X)
        layer_inputs = [X]+layer_activations 
        logits = layer_activations[-1]

        # Compute the loss and the initial gradient
        loss = softmax_crossentropy_with_logits(logits,y)
        loss_grad = grad_softmax_crossentropy_with_logits(logits,y)

        # Propagate gradients through the network
        # Reverse propogation as this is backprop
        for layer_index in range(len(self.network))[::-1]:
            layer = self.network[layer_index]
            loss_grad = layer.backward(layer_inputs[layer_index],loss_grad) 
        return np.mean(loss)

#Αξιολόγηση ενός Multi-Layer Perceptron
#Αφού έχουμε κατασκευάσει τα παραπάνω είμαστε πλέον σε θέση να εκπαιδεύσουμε το MLP. Αυτό γίνεται καλώντας την μέθοδο fit. Στο παρακάτω κελί κώδικα ορίζεται το MLP του παραπάνω παραδείγματος και εκπαιδεύεται για 25 εποχές. Στο τέλος κάθε εποχής παρουσιάζονται τα αποτελέσματα του μαζί με μια γραφική των train και test accuracy.

from IPython.display import clear_output
import numpy as np

network = MLP([10, 15, 20, 3], len(inputs))

train_log = []
val_log = []

for epoch in range(100):
    network.fit(x_train, y_train)   
    train_log.append(np.mean(network.predict(x_train) == y_train))
    val_log.append(np.mean(network.predict(x_test) == y_test))
    #clear_output()
    print("Epoch", epoch)
    print("Train accuracy:", train_log[-1])
    print("Val accuracy:", val_log[-1])  
    plt.plot(train_log,label = 'train accuracy')
    plt.plot(val_log,label = 'val accuracy')
    plt.legend(loc = 'best')
    plt.grid()
    plt.show()

y_pred = network.predict(x_test)

eval = Evaluate(y_test, y_pred)
eval.get_evaluation_report()

#ΣΥΓΚΡΙΣΗ ΥΛΟΠΟΙΗΣΕΩΝ
#Πραγματοποιήσαμε δοκιμές για διαφορετικά πλήθη εποχών (παραπάνω φαίνονται τα αποτελέσματα για 100 εποχές). Όσον αφορά στη δική μας υλοποίηση καθώς περνάνε οι εποχές το val accuracy προσπαθεί να συγκλίνει στο train accuracy. Η δική μας υλοποίηση έχει μικότερες τιμές percision και accuracy (περίπου 0.648 για 100 εποχές) σε σχέση με την έτοιμη (περίπου 0.73693 για 25 εποχές και 0.7541 για 100 εποχές) και μεγαλύτερο χρόνο εκτέλεσης. Τέλος, και στις δύο υλοποιήσεις η αύξηση του πλήθους των εποχών έχει ως αποτέλεσμα της αύξηση της ακρίβειας του νευρωνικού.

#Αξιολόγηση- Συμπεράσματα
#ΚΝΝ: ακρίβεια η οποία ποικίλει ανάλογα με το k που θα βάλουμε,με το distance και με το πλήθος στοιχείων του x_test,y_test . Χρόνος εκτέλεσης μεγαλύτερος από 1 λεπτό για στοιχεία περισσότερα από 500 στο x_test,y_test.
#Naive Bayes: καλύτερη ακρίβεια είχε η δική μας υλοποίηση περίπου 0.65 αλλά και χρόνο εκτέλεσης περίπου 20 sec ενώ η έτοιμη είχε χρόνο εκτέλεσης περίπου 1 sec αλλά ακρίβεια περίπου 0.6.
#MLP: η έτοιμη υλοποίηση είχε καλύτερη ακρίβεια (> 0.72) και καλύτερο χρόνο εκτέλεσης (< 1 λεπτό ακόμα και για όλες τις εικόνες του x_test).
#Συνεπώς, η έτοιμη ΜLP αποτελεί την καλύτερη επιλογή. Η επιλογή μεταξύ των δύο πρώτων εξαρτάται από το αν είναι πιο επιθυμητή η μεγάλη ακρίβεια (ΚΝΝ) ή ο μικρός χρόνος εκτέλεσης (Naive Bayes).