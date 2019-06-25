# VgammaTuplizer

Ntuplizer for searches for heavy resonances decaying to dibosons

## installation instructions

Setting up CMSSW (for september reprocessing):

```
cmsrel CMSSW_9_4_0
cd CMSSW_9_4_0/src
cmsenv
```


### updates of latest cut-based electron ID and MVAID. HEEP are default in 94X
(https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2 and 
```
cd $CMSSW_BASE/src
cmsenv
git cms-init
git cms-merge-topic lsoffi:CMSSW_9_4_0_pre3_TnP
git cms-merge-topic guitargeek:ElectronID_MVA2017_940pre3
scram b -j 8
cd $CMSSW_BASE/external
cd slc6_amd64_gcc630/
git clone https://github.com/lsoffi/RecoEgamma-PhotonIdentification.git data/RecoEgamma/PhotonIdentification/data
cd data/RecoEgamma/PhotonIdentification/data
git checkout CMSSW_9_4_0_pre3_TnP
cd $CMSSW_BASE/external
cd slc6_amd64_gcc630/
git clone https://github.com/lsoffi/RecoEgamma-ElectronIdentification.git data/RecoEgamma/ElectronIdentification/data
cd data/RecoEgamma/ElectronIdentification/data
git checkout CMSSW_9_4_0_pre3_TnP
cd $CMSSW_BASE/src
scram b distclean
scramv1 b -j 16
```




### getting the ntuplizer codes
```
cd $CMSSW_BASE/src
git clone https://github.com/jjackson12/VgammaTuplizer 
cd VgammaTuplizer
git remote add Wgam https://github.com/jjackson12/VgammaTuplizer
git fetch Wgam
git checkout -b Dev_9_4_0 Wgam/94X_dev
cd ..
scram b -j8
```




### running for data only! Set the proper flags in python/ntuplizerOptions_generic_cfi.py

```
cmsRun config_generic.py 

```

### for running on MC... Set the proper flags in python/ntuplizerOptions_generic_cfi.py or change import at the beginning of config_generic to point to python/ntuplizerOptions_MC2017_cfi.py

```
cmsRun config_2017MC.py 

```

to recluster jets and MET, or to add the Higgs-tagger the following flags can be changed:
```
config["DOAK8RECLUSTERING"] = False
config["DOHBBTAG"] = False
config["DOAK8PRUNEDRECLUSTERING"] = False
config["DOMETRECLUSTERING"] = False
```
If you want to use Higgs tagger the first two flags must all be set to True.

### Batch submission

Crab jobs can be run via crab config files in [crabconfigs](Ntuplizer/crabconfigs/)

NOTE: Crab will import much of the Electron and Photon ID packages imported locally above. These are too large and Crab will crash, telling you you have too much data. This should be fixable by removing the extraneous files in the "data" directories wihin the imported packages, i.e., directories/files dated previous to 2017
