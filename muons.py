#!/usr/bin/env python

from ROOT import TChain
from ROOT import TLorentzVector
data = TChain("mini")
data.Add("http://opendata.atlas.cern/release/samples/Data/DataMuons.root")

num_events = data.GetEntries()
print("Number of events = "+str(num_events))

num_events_to_process = 100
for i_event in range(num_events_to_process):
    data.GetEntry(i_event)
    n_leptons = data.lep_n
    if n_leptons >= 2:
        print("num of Leptons "+str(n_leptons))
        assert(n_leptons==2)
        pt1 = data.lep_pt[0]
        pt2 = data.lep_pt[1]
        print("Leptons Pts are : "+str(pt1)+" , "+str(pt2))
        p1 = TLorentzVector()
        p1.SetPtEtaPhiE(pt1, data.lep_eta[0], data.lep_phi[0], data.lep_E[0])
        print("First lepton Pt from vector = "+str(p1.Pt()))
