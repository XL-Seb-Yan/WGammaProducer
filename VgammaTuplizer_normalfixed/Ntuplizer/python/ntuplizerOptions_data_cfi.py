import FWCore.ParameterSet.Config as cms

config = dict()

#--------- general ----------#
config["SPRING16"] = False
config["RUNONMC"] = False
config["USEJSON"] = False
config["JSONFILE"] = "Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
config["BUNCHSPACING"] = 25
config["USENOHF"] = False
config["FILTEREVENTS"] = False

#--------- basic sequences ----------#
config["DOPHOTONS"] = True
config["DOGENPARTICLES"] = False
config["DOGENJETS"] = False
config["DOGENEVENT"] = False
config["DOLHEEVENT"] = False
config["DOPILEUP"] = False
config["DOELECTRONS"] = False
config["DOELECTRONIDVARS"] = False
config["DOELECTRONISOVARS"] = False
config["DOMUONS"] = False
config["DOMUONIDVARS"] = False
config["DOMUONISOVARS"] = False
config["DOTAUS"] = False
config["DOAK8JETS"] = True
config["DOAK4JETS"] = True
config["DOJETIDVARS"] = False
config["DOVERTICES"] = True
config["DOTRIGGERDECISIONS"] = True
config["DOTRIGGEROBJECTS"] = False
config["DOHLTFILTERS"] = True
config["DOMISSINGET"] = False
config["DOTAUSBOOSTED"] = False
config["DOMETSVFIT"] = False
config["DOSEMILEPTONICTAUSBOOSTED"] = False

#--------- AK8 jets reclustering ----------#
config["ADDAK8GENJETS"] = False #! Add AK8 gen jet collection with pruned and softdrop mass
config["DOAK8RECLUSTERING"] = True
config["DOAK8PRUNEDRECLUSTERING"] = True #! To add pruned jet and pruned subjet collection (not in MINIAOD)
config["DOAK8PUPPI"] = True
config["DOAK10TRIMMEDRECLUSTERING"] = False
config["DOHBBTAG"] = False #Higgs-tagger
config["UpdateJetCollection"] = True #needed for Higgs-tagger in 80X

#--------- MET reclustering ----------#
config["DOMETRECLUSTERING"] = False

#--------- JEC ----------#
config["CORRJETSONTHEFLY"] = True
config["CORRMETONTHEFLY"] = True
config["GETJECFROMDBFILE"] = False # If not yet in global tag, but db file available
