from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Wgamma2017_ZJetsToQQ_HT400to600_%s'%"Jul18"
config.General.workArea = 'crab_jobs_WgammaMC_2017_%s'%"Jul18"
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'VgammaTuplizer/Ntuplizer/config_generic.py'
config.JobType.inputFiles=[]
config.JobType.sendExternalFolder = True
config.Data.inputDataset = '/ZJetsToQQ_HT400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 30
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'Wgamma2017_ZJetsToQQ_HT400to600_%s'%"Jul18"
config.Site.storageSite = 'T3_US_FNALLPC'

