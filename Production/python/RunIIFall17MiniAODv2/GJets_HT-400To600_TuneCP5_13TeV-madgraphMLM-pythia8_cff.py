import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/040C3A4B-B5C5-E811-9109-3417EBE64BE8.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/0E8A317B-41C6-E811-ABF7-008CFAFC0416.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/186CC54B-ECC5-E811-8F6D-3417EBE6451F.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/201923A4-F9C5-E811-8B49-7CD30AB15C58.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/2026D97A-41C6-E811-989B-509A4C748A71.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/2088EAE6-DAC5-E811-AFC9-008CFAFBEA7E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/221DBC7B-41C6-E811-B116-7CD30ACE22CC.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/2263957A-41C6-E811-8829-7CD30AD09D2A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/2868BA6C-D9C5-E811-941F-7CD30AB0532E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/2EBF1367-05C6-E811-84F2-3417EBE64426.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/32193C7C-41C6-E811-9975-7CD30ACE24A6.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/38D78E7E-41C6-E811-8F9E-7CD30AD0944E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/3A44247A-41C6-E811-9DE2-7CD30AD096BE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/3ED3CC5B-10C6-E811-A669-3417EBE644F2.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/40A6397A-41C6-E811-8B74-7CD30AD0A684.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/4AB5441F-DDC5-E811-ADBA-509A4C730E2E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/5A49DEDC-FFC5-E811-BDAA-509A4C858AF3.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/5EBA6441-C3C5-E811-AA66-7CD30AD09010.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/6290D49D-DBC5-E811-A75D-509A4C730E2E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/729BBD9C-FBC5-E811-B669-3417EBE64BB8.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/7459017B-41C6-E811-B8DE-3417EBE643DE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/74EABB6A-D9C5-E811-A51A-509A4C730E2E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/8CA0F0DC-C8C5-E811-B7DC-3417EBE64426.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/98A2EE1A-BBC5-E811-A0A3-509A4C70AB6E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/9CAEED48-B5C5-E811-87D7-509A4C748A08.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/A0F51173-EEC5-E811-9C8C-7CD30AD0A7D4.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/A6ECE040-BEC5-E811-987A-509A4C748AB0.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/AAA34778-41C6-E811-A026-3417EBE649DE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/ACE5E45D-0CC6-E811-A8BA-3417EBE6458E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/B00D5BF5-D2C5-E811-8980-008CFAFC5E40.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/C046231A-E8C5-E811-9492-008CFAF74B22.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/C094F960-F5C5-E811-8930-509A4C844A32.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/C639667A-41C6-E811-A70B-7CD30AD09D24.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/D0E1826A-05C6-E811-BCAD-7CD30AB0532E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/D4530F7C-41C6-E811-927A-008CFAFC5E40.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/E406EE7F-41C6-E811-91C0-509A4C749113.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/E6288E00-02C6-E811-A21D-3417EBE6446E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/EC156D3E-DEC5-E811-A690-3417EBE722FA.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/ECF12AF1-FFC5-E811-B123-008CFAF74B22.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/EE6A3BAC-F0C5-E811-88FB-7CD30AD0A7D4.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/042EED72-49AD-E811-B125-7CD30AD097C0.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/124E7D20-BFAD-E811-9BB7-7CD30AD0A690.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/2CF7264B-0FAD-E811-87CC-008CFAFC0122.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/30018B88-85AF-E811-A909-7CD30AB05490.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/369F153D-FAAC-E811-994B-509A4C72D497.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/38C9313B-FAAC-E811-BB91-3417EBE6470E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/44019717-3FAB-E811-8DFF-008CFAF724BE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/483634B3-89AD-E811-A7E5-509A4C72D497.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/488BDB65-A3AD-E811-A33D-7CD30ACDCF08.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/4CFFD3B8-67AD-E811-B3F5-7CD30AD0991C.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/4E2B802E-63AD-E811-B9F9-008CFAFBDE0C.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/50004037-7DAD-E811-BC7D-7CD30AD097C0.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/5A518C53-0FAD-E811-9035-509A4C7489AF.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/62D7423D-FAAC-E811-89F2-509A4C748068.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/66B4BF5F-5EAF-E811-B31B-F04DA275C2CE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/66F8AFFD-83AD-E811-9C6E-3417EBE6444D.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/6A25D50E-8BAD-E811-968E-7CD30AD09316.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/78A5046E-5AAD-E811-8DFB-7CD30ACDC7B2.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/7A6DA256-5FAD-E811-8955-7CD30AD0991C.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/8805153A-FAAC-E811-8E78-509A4C838C93.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/94014FA3-53AD-E811-8C82-3417EBE2F2F5.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/9CFC5150-0FAD-E811-A736-509A4C7489AF.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/A0C40523-A1AF-E811-A978-509A4C8339CD.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/ACCD4ABE-6CAD-E811-8330-3417EBE6459A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/BC55C164-A3AD-E811-8C69-7CD30ACDCF08.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/C01E4E3C-FAAC-E811-88C9-509A4C748068.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/C0B18A5E-D0AD-E811-A5C6-3417EBE64BE8.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/C63D5537-37AD-E811-B9FD-008CFAFBE5CE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/C8F55AE7-8EAE-E811-A1B4-509A4C74D077.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/D43D3A35-7DAD-E811-8D0E-509A4C748A17.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/DA0A5A26-75AE-E811-A249-509A4C748A49.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/DE89C564-A3AD-E811-A2C9-7CD30ACDCF08.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/E09E2135-24AD-E811-88E6-3417EBE722FA.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/E47848A2-1BAD-E811-B33D-3417EBE64BA0.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/E66C6087-85AF-E811-8DD8-008CFAFBF6CC.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/E80F3922-BFAD-E811-94AC-008CFAFC03F8.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/F02B597D-3EAD-E811-8FB1-008CFAFBE70C.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/F4C8DF4D-0FAD-E811-B30D-008CFAFC0122.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/F4D94124-39AD-E811-AB63-509A4C84EB39.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/F629EC62-A3AD-E811-93BF-7CD30ACDCF08.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/FAA668A2-1BAD-E811-8138-3417EBE64BA0.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/610000/E2EDA226-89C5-E811-A0FE-509A4C8605EA.root',
] )
