#!/bin/bash


#rm -rf /uscms_data/d3/jjackso3/workspace/CMSSW_9_4_0/src/crab_jobs_2017B_Jun18/crab_Wgamma94XTuples_Jun18_2017B
#echo "B"
#crab submit -c VgammaTuplizer/Ntuplizer/crabconfigs/crab_2017B.py
#echo "C"
#crab submit -c VgammaTuplizer/Ntuplizer/crabconfigs/crab_2017C.py
#echo "D"
#crab submit -c VgammaTuplizer/Ntuplizer/crabconfigs/crab_2017D.py
#echo "E"
#crab submit -c VgammaTuplizer/Ntuplizer/crabconfigs/crab_2017E.py
#echo "F"
#crab submit -c VgammaTuplizer/Ntuplizer/crabconfigs/crab_2017F.py
#
#
echo "SingleMuon"


#echo "B"
#crab submit -c VgammaTuplizer/Ntuplizer/crabconfigs/crab_2017SingleMuonB.py
#echo "C"
#crab submit -c VgammaTuplizer/Ntuplizer/crabconfigs/crab_2017SingleMuonC.py
#echo "D"
#crab submit -c VgammaTuplizer/Ntuplizer/crabconfigs/crab_2017SingleMuonD.py
#echo "E"
#crab submit -c VgammaTuplizer/Ntuplizer/crabconfigs/crab_2017SingleMuonE.py
#echo "F"
#crab submit -c VgammaTuplizer/Ntuplizer/crabconfigs/crab_2017SingleMuonF.py



#echo "B"
#crab resubmit -c crab_jobs_2017F_Jul17/crab_Wgamma94XSingleMuonTuples_Jul17_2017F/ 
echo "C"
crab resubmit  crab_jobs_2017E_Jul17/crab_Wgamma94XSingleMuonTuples_Jul17_2017E/ 
echo "D"
crab resubmit  crab_jobs_2017D_Jul17/crab_Wgamma94XSingleMuonTuples_Jul17_2017D/ 
echo "E"
crab resubmit  crab_jobs_2017C_Jul17/crab_Wgamma94XSingleMuonTuples_Jul17_2017C/ 
echo "F"
crab resubmit  crab_jobs_2017B_Jul17/crab_Wgamma94XSingleMuonTuples_Jul17_2017B/ 
