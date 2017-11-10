#!/usr/bin/env python

from ROOT import TChain
data = TChain("mini")
data.Add("http://opendata.atlas.cern/release/samples/Data/DataMuons.root")

num_events = data.GetEntries()
print("Number of events = "+str(num_events))

num_events_to_process = 10
for i_event in range(num_events_to_process):
    data.GetEntry(i_event)
    n_leptons = data.lep_n
    print("num of Leptons "+str(n_leptons))

