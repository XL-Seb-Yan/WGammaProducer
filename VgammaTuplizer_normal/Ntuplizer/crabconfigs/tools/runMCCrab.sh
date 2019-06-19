#!/bin/bash

for f in VgammaTuplizer/Ntuplizer/crabconfigs/crab_MC2017*.py; do
  crab submit $f
done
