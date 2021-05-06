# Data-driving-cyber-security-research-using-machine-learning-tactics

Abstract:

The main goal of this research is to overcome the challenges in intrusion based cyber security systems and providing the solutions using current big data and machine learning techniques. Our host-based intrusion system monitors the system during normal usage as well as malicious activities  is capable of distinguishing normal usage from abnormal activitie; therefore, prevent imminent intrusions from happening. 


# Host-Based Intrusion Detection Using System Calls

     This program is inspired by the Computer Immune System project by UNM Computer Science Department. Hence, our data processing procedure mostly follows the UNM project (https://www.cs.unm.edu/~immsec/systemcalls.htm). The only difference is that we will tokenize system calls into sequences of 6-ngrams, and then use Machine Learning algorithms to train the models to detect host-based intrusions. Thanks to the Computer Science Department in UNM, MIT and UNSW at he Australian Defence Force Academy, we have access to the huge amount of host-based intrusion data. We will use the majority of UNM data (except Sendmail dataset), MIT Live Lpr and ADFA-LD datasets. 
     
     Each program in an operating system has its own unique sequences of system calls that distinguishes itself from another program. We will take advantage of these signature sequences by collecting system calls sequences during normal usage in different programs (such as sendmail, login and ps, inetd, lpr, ftp, etc.) then comparing them against the live traces from system log, that way we can train the model to recognize the normal pattern in each program. Before the model can be trained, we need to process the collected system calls into 6-ngrams sequences. 
     For example, the sequence is: open, read, mmap, mmap, open, mmap, close.   
     There resulting sequences are:
                                   open, read, mmap, mmap, open, mmap
                                   read, mmap, mmap, open, mmap, close
    
    This process is applied to normal sequences and intrusion sequences from UNM, MIT and ADFA-LD datasets. Bytokenizing into a sequence of 6-grams, we increase the amount of data for training as well as testing purposes.  Inaddition, the number of features will decrease when a trace is tokenized into smaller chunks, this will increase the efficiency of training as well as testing performances. We proceed to clean data by removing any rows or sequences that appear in both normal data and intrusion data. This step draws distinctive characteristics between the 2 classes and effectively boost machine learning performance. A row with normal sequence is labeled 0, whereas the one with intrusion sequence is labeled 1. We use normal data and intrusion data from each dataset to create a sample pool. If it is imbalanced, we use bootstrapping method create a balanced sample of normal sequences and intrusion sequences. Then, we split the sample into training and testing sets in a 70-30 ratio. By training with only signature sequences from both classes, we increase the model accuracy and recall (true positive rate) as well as decrease its false positive rate. 
