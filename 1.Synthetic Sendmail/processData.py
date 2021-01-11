# This script translates syscall number into system call name using the syscallMap file in this repository. 
# To Run: python3 processData.py
# Enter data file you want to translate. If it's not in the same directory, enter the file path.
# Do the same thing for mapping file.
# Specify output file name

import numpy as np
import pandas as pd

fileName = input("Enter data file location: ") 
#print(fileName) 
mapFile = input("Enter mapping file location: ")

outFile = input("Enter outfile location: ")
##print(outFile) 

df = pd.read_csv(str(fileName), sep = ' ',  header = None)
df = df.drop(labels=[2,3], axis=1)
df = df.rename(columns= {0:"PID", 1:"Syscall"})
syscalls = pd.read_csv(mapFile, sep=' ',header = None, names=['SyscallNum', 'Name'])

from contextlib import redirect_stdout
f = open(str(outFile), 'w+')

print('Mapping syscall...')
i = 0 

for x in df.index:
  #print (df['Syscall'][x])
  found = 0     # this counter double check if we use the right mapping file. If it's the incorrect one, some syscall will not be translated.
  i += 1
  for y in syscalls.index:
    if(df['Syscall'][x] == syscalls['SyscallNum'][y]):
      found = 1
      print(df['PID'][x], " ", syscalls['Name'][y], file=f)
      #print(df['PID'][x], " ", syscalls['Name'][y])
  if(found == 0):
    print(df['PID'][x], "  unknown ", df['Syscall'][x], file=f)
    print("Line ", i," :", df['PID'][x], "  unknown ", df['Syscall'][x] )
f.close()
