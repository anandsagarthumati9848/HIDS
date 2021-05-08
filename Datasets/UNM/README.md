# UNM Data Description:

In 1996, the University of New Mexico (UNM) uses strace to capture system call sequences from 10 different programs: synthetic sendmail, synthetic ftp, synthetic lpr, live lpr, xlock, live named, login and ps, inetd, sendmail and stide. 
Each of them contains normal and intrusion data, except sendmail dataset. Therefore, we do use sendmail in our experiment.
Some of them are live data, and some are synthetic data. Live data were recorded during normal usage, whereas synthetic data were collected using scripts that simulate both normal and anomalous behaviors. Each dataset includes sequential traces of multiple processes from the start until the end. Since processes run simultaneously, the sequence trace from a specific process ID (PID) can be interrupted by the traces of other PIDs. 

The UNM data format contains 2 integer columns: PID and System Call number. Additionally, there is no time frame nor user ID in the data as they have already been processed; however, the sequences of system calls are listed in order. Since different programs with different versions were used to generate the data, most dataset has their own mapping file. A mapping file contains a list of system call name in order, in which the index (starting from 0) corresponds to the system call number in the dataset. Due to a large number of data files, we were able to map the system call numbers to their names in some files. 


# Data Usage:

 1. Synthetic Sendmail: https://www.cs.unm.edu/~immsec/data/synth-sm.html

  From the link above, there two types of Synthetic Sendmail: UNM Synthetic Sendmail and CERT Synthetic Sendmail. There is sufficient normal and intrusion data from the first type, so we only use UNM Synthetic Sendmail. 

  To run the candidate algorithms with UNM Synthetic Sendmail dataset, open Final_Version_HIDS.ipynb in Google Colab, then load the files from /1.Synthetic Sendmail/normal-data/ directory as normal data and the files from /1.Synthetic Sendmail/intrusion-trace-data/ as intrusion data. 

  In the first code block under Section Processing Data section, look for the line: '## Uncomment each line to load Normal data' and uncomment csv_file next to Synthetic Sendmail to load normal dataset. Look for the line: '## Uncomment each line to load Intrusion data:' and uncomment csv_file next to Synthetic Sendmail to load intrusion dataset.
  
  Select Runtime and then Run All to run all blocks of codes. You should see results from each code block as the python notebook is running.

2. Synthetic Ftp: https://www.cs.unm.edu/~immsec/data/synth-ftp.html

  To run the candidate algorithms with UNM Synthetic Ftp dataset, open Final_Version_HIDS.ipynb in Google Colab, then load the files from /2.Synthetic Ftp/normal/ directory as normal data and the file from /2.Synthetic Ftp/intrusion/ as intrusion data. 

  In the first code block under Section Processing Data section, look for the line: '## Uncomment each line to load Normal data' and uncomment csv_file next to Synthetic Ftp to load normal dataset. Look for the line: '## Uncomment each line to load Intrusion data:' and uncomment csv_file next to Synthetic Ftp to load intrusion dataset.
  
  Select Runtime and then Run All to run all blocks of codes. You should see results from each code block as the python notebook is running.

3. Synthetic Lpr: https://www.cs.unm.edu/~immsec/data/synth-lpr.html
  To run the candidate algorithms with UNM Synthetic Lpr dataset, open Final_Version_HIDS.ipynb in Google Colab, then load the files from /3.Synthetic Lpr/normal/ directory as normal data and the file from /3.Synthetic Lpr/intrusion/ as intrusion data. 

  In the first code block under Section Processing Data section, look for the line: '## Uncomment each line to load Normal data' and uncomment csv_file next to Synthetic Lpr to load normal dataset. Look for the line: '## Uncomment each line to load Intrusion data:' and uncomment csv_file next to Synthetic Lpr to load intrusion dataset.
  
  Select Runtime and then Run All to run all blocks of codes. You should see results from each code block as the python notebook is running.

4. Live Lpr: https://www.cs.unm.edu/~immsec/data/live-lpr.html
   
   From the link above, there two types of Live Lpr: UNM Live Lpr and MIT Live Lpr. Below is the intruction to use UNM Live Lpr. The instruction for MIT Live Lpr is included in the README.md from /Datasets/MIT/live lpr/ directory. 
   Normal data is extracted from traces.tar, which contains 1234 files. Intrusion data is extracted from lprcp-unm-new.tar, which contains 4298 files. Since there are lots of normal data, we only use the ones that were collected in October and November: lpr-normal-10.txt and lpr-normal-11.txt. We concat intrusion traces from all of intrusion dataset into exploit-unm.int.  
   
  To run the candidate algorithms with UNM Live Lpr dataset, open Final_Version_HIDS.ipynb in Google Colab, then load the files from /4.Live Lpr/normal/ directory as normal data and the file from /4.Live Lpr/intrusion/ as intrusion data. 

  In the first code block under Section Processing Data section, look for the line: '## Uncomment each line to load Normal data' and uncomment csv_file next to Live Lpr to load normal dataset. Look for the line: '## Uncomment each line to load Intrusion data:' and uncomment csv_file next to Live Lpr to load intrusion dataset.
  
  Select Runtime and then Run All to run all blocks of codes. You should see results from each code block as the python notebook is running.


5. 
