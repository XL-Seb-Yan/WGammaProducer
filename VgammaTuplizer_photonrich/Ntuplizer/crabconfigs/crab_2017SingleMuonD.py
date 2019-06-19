from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Wgamma94XSingleMuonTuplesPhotonrich_%s_2017D'%"Apr19"
config.General.workArea = 'crab_jobs_2017D_%s'%"Apr19"
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/afs/cern.ch/work/x/xuyan/work5/CMSSW_9_4_0/src/VgammaTuplizer/Ntuplizer/config_generic_muon.py'
config.JobType.inputFiles=[
        '/afs/cern.ch/work/x/xuyan/work5/CMSSW_9_4_0/src/VgammaTuplizer/Ntuplizer/JSON/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSONv1.txt'
]
config.JobType.sendExternalFolder = True
config.Data.inputDataset = '/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 30
config.Data.lumiMask='/afs/cern.ch/work/x/xuyan/work5/CMSSW_9_4_0/src/VgammaTuplizer/Ntuplizer/JSON/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSONv1.txt'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'Wgamma94XSingleMuonTuplesPhotonrich_%s_2017D'%"Apr19"
config.Site.storageSite = 'T3_US_Brown'