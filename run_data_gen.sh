#!/bin/bash

year=$1
echo $year
python generate_data.py ${year}q1 > ${year}q1.tsv & python generate_data.py ${year}q2 > ${year}q2.tsv & python generate_data.py ${year}q3 > ${year}q3.tsv & python generate_data.py ${year}q4 > ${year}q4.tsv
