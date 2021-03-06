import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/08014622-804D-E711-823D-001E67792844.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0CAF6064-664E-E711-ADA0-1CB72C1B63C2.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2045E993-824D-E711-BBC8-0025905C2D9A.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/22804E76-854D-E711-A47B-001E6779254C.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2A188AD5-534E-E711-BF0E-00269E95B014.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/32E0FAAA-6A4E-E711-8DA4-20CF3027A561.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3682DFA8-AA4E-E711-A4FA-0CC47A4D767A.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3E14A940-464E-E711-8BB5-002590DE7230.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/429D09A3-414E-E711-A6E9-0242AC110008.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/52F791F0-5A4F-E711-916F-0CC47A57CE00.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6019EC21-7E4D-E711-B8DD-001E67792760.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/60CAA440-A04D-E711-947C-141877638819.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6AF02574-474E-E711-9E56-3417EBE528F1.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7088DAF7-854D-E711-84C8-0025904C51FC.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/70D6E2BA-8F4D-E711-ADFE-141877640173.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/78BFFA32-C24E-E711-B04E-0025904B2C4C.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7ABDC52D-6B4E-E711-A40C-D067E5F923BB.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7C902577-474E-E711-8D52-A0369FD20CF0.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8286FA2A-724E-E711-B5E5-001C23C0C7AB.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/82F37830-4F4E-E711-94BB-002590A80E1E.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/90C066E8-504E-E711-A24A-0090FAA57720.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/96DAC7E3-514E-E711-A948-0025904B7FC4.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9A7430EE-DE50-E711-876A-7845C4FC3A40.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AC58CB51-4C4E-E711-8FA8-A0369F30FFD2.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CAF79200-504E-E711-A36D-A0369F83628A.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D04EFF40-AB4D-E711-9203-7CD30AD08884.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D4B8AD40-8A4D-E711-B730-0017A4770C70.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/DA8C2A38-4F4E-E711-AE8A-10BF481A01ED.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E0289A79-744E-E711-A4E7-848F69FD29BB.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E40F3C61-D550-E711-97A6-848F69FD24D2.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E8B41200-504E-E711-AB30-0025905C54D8.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/EA40FA64-4D4E-E711-BE9C-002590E7D7DE.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F0831476-474E-E711-9FD0-0026B927865E.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F29728C5-9C4D-E711-B3DB-002590FD0F36.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F6E61174-DC4F-E711-8829-008CFA165FD0.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F8A59A17-8C4E-E711-A4C5-0CC47A4C8E66.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FE0313AA-C24E-E711-AA52-FA163E4F1151.root',
       '/store/mc/RunIISummer16MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FEE29CD3-864D-E711-B644-48FD8EE739FF.root',
] )
