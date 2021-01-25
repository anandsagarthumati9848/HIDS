# Data-driving-cyber-security-research-using-machine-learning-tactics

Abstract:
The main goal of this research is to derive the challenges in intrusion based cyber security systems and providing the solutions using current bigdata and machine learning techniques. IDS monitors the system for malicious activity and protects a computer from unauthorized access from intruders.  Here we are going to build a host based intrusion detector which is capable of differentiating between the intrusion attack and normal attack. 


# Host-based Intrusion Detection Using System Calls

     This program is inspired by the Computer Immune System project by UNM Computer Science Department. Hence, our data processing procedure mostly follows the UNM project (https://www.cs.unm.edu/~immsec/systemcalls.htm). The only difference is that we will use Machine Learning algorithms to train our model to detect host-based intrusions. Thanks to the Computer Science Department in UNM, we have access to the same data that they used to train their model in the Computer Immune System project. Therefore, we will use the majority of UNM data as a foundation to train our model, and on top of that, we will generate some of our own normal as well as intrusion data in a controlled environment. That way, we have a diverse data pool to better train our model. 
     
     Each program in an operating system has its own unique sequences of system calls that distinguishes itself from another program. We will take advantage of these signature sequences by collecting system calls sequences during normal usage in different programs (such as sendmail, login and ps, inetd, lpr, ftp, etc.) then comparing them against the live traces from system log, that way we can train the model to recognize the normal pattern in each program. Before the model can be trained, we need to process the collected system calls sequences and save them in the normal database. For each system call, we save its 6 subsequent system calls. For example, the sequence is: open, read, mmap, mmap, open, mmap, close.   
     Open is saved as a root of a tree with 6 child nodes corresponding to its subsequent position. Position 1: read. Position 2: mmap. Position 3: mmap. Position 4: open. Position 5: mmap. Position 6: close. Hence, a tree of system call open will look like below:
                    |open
     |read  |mmap  |mmap  |open  |mmap  |close
  
     As new traces of system calls are processed, the tree will expand with more system calls in each child node. At the same time, we need to collect system calls sequences during intrusions on each of the program mentioned above. Once the model can sufficiently recognize the normal pattern, we will run it against the intrusion data. If a sequence does not match with the normal database, that will be counted as a mismatch. For each specific program, we need to set up different mismatch threshold to classify it as an anomaly. If it can detect intrusion incidents from the intrusion database, then we will proceed to the testing phase, where a combination of "unseen" normal data and intrusion data is tested. 
