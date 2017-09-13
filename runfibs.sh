#!/bin/bash

if [ -e "fibs.csv" ]; then
   if [ -e "fibs.csv.bak" ]; then
      echo "A backup already exists. The program was forced to quit without overwriting."
      exit 1
   fi
   mv fibs.csv fibs.csv.bak
   echo "created backup file fibs.csv.bak"
fi

touch "fibs.csv"
for i in $(seq 10000); do
   #output=echo ./fib.py $i
   echo -n "$(./fib.py $i)," >> fibs.csv
done
