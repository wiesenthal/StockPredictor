#!/bin/bash

year=$1
echo start:
date +"%H-%M-%S"
echo $year
python StockPrice.py ${year}q1 > /dev/null & python StockPrice.py ${year}q2 > /dev/null & python StockPrice.py ${year}q3 > /dev/null & python StockPrice.py ${year}q4 > /dev/null
echo end:
date +"%H-%M-%S"
