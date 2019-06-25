#!/bin/bash

for dir in crab_jobs_WgammaMC_2017_Jul18/*; do
  crab status $dir
done
