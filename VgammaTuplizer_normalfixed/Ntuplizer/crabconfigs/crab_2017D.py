from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Wgamma94XSinglePhoton_%s_2017D'%"Jun25"
config.General.workArea = 'crab_jobs_2017D_photon%s'%"Jun25"
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'config_generic_data.py'
config.JobType.inputFiles=[
        'JSON/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSONv1.txt'
]
config.JobType.sendExternalFolder = True
config.Data.inputDataset = '/SinglePhoton/Run2017D-31Mar2018-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 30
config.Data.lumiMask='JSON/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSONv1.txt'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'Wgamma94XSinglePhoton_%s_2017D'%"Jun25"
config.Site.storageSite = 'T3_US_Brown'
