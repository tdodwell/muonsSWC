#!/usr/bin/env python

from ROOT import TChain, TLorentzVector, TH1F

def four_momentum_of_lepton(i_lepton, tree):
    pt = tree.lep_pt[i_lepton]
    eta = tree.lep_eta[i_lepton]
    phi = tree.lep_phi[i_lepton]
    e = tree.lep_E[i_lepton]
    p = TLorentzVector()
    p.SetPtEtaPhiE(pt,eta, phi, e)
    return p

data = TChain("mini")
data.Add("http://opendata.atlas.cern/release/samples/Data/DataMuons.root")

num_events = data.GetEntries()
print("Number of events = "+str(num_events))

h_mpair = TH1F("mpair", "Invariant Mass of Leptons ; mass /Gev; freq",50,0,200)

num_events_to_process = 1000
for i_event in range(num_events_to_process):
    data.GetEntry(i_event)
    n_leptons = data.lep_n
    if n_leptons >= 2:
        print("num of Leptons "+str(n_leptons))
        assert(n_leptons==2)
        pt1 = data.lep_pt[0]
        pt2 = data.lep_pt[1]
        print("Leptons Pts are : "+str(pt1)+" , "+str(pt2))    
        p1 = four_momentum_of_lepton(0,data)
        p2 = four_momentum_of_lepton(1,data)
        print("Lepton Pt from vector = "+str(p1.Pt())+" , " +str(p2.Pt()) )
        ppair = p1 + p2
        mpair = ppair.M()
        print("Invariant Mass of lepton pair = " +str(mpair))
        h_mpair.Fill(mpair/1000)    #converts MeV to GeV

h_mpair.Draw()
raw_input("Press any button to end program")
