# MIT-Live Lpr Data Description:

MIT dataset is included in the UNM data repository: https://www.cs.unm.edu/~immsec/data/live-lpr.html 
In 1997, they have collected live normal datafor lpr for 2 weeks using 77 hosts. A synthetic attack script was written to exploit vulnerabilities from the older versionsof lpr. MIT data also has the same format as UNM data, where each file contains 2 numeric columns: PID and System call number.

# Data Usage:

2703 Normal datasets are extracted from lpr-live-mit-new.tar.gz folder, and they sorted by their filenames which contain the original log date. With such large amount of data, we only use the ones collected in March 1997 and combine them into folder mit-lpr-mar.txt.

Intrusion data is found in 1 file exploit-ai.int.

To run the candidate algorithms with MIT Live Lpr dataset, open Final_Version_HIDS.ipynb in Google Colab, then load mit-lpr-mar.txt and exploit-ai.int files. Select Runtime and then Run All to run all blocks of codes. You should see results from each code block as the python notebook is running.
