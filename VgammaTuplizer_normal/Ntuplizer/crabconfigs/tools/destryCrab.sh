#!/bin/bash

for dir in crab_jobs_2017*/*; do
  #crab kill $dir
  crab purge $dir
done
