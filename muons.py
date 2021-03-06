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

def leptons_from_event(tree):
    """
    
    """
    leptons = []
    n_leptons = tree.lep_n
    for i_lepton in range(n_leptons):
        p = four_momentum_of_lepton(i_lepton, tree)
        q = tree.lep_charge[i_lepton]
        particle = Particle(p,q)
        leptons.append(particle)
    return leptons

def pairs_from_particles(particles):
    '''
    '''
    pairs = []
    n_particles = len(particles)
    for i in range(n_particles):
        charge_i = particles[i].q
        for j in range(i+1 , n_particles):
            charge_j = particles[j].q
            if charge_i != charge_j:
                pair = (particles[i], particles[j])
                pairs.append(pair)
    return pairs

def mass_of_pair(pair):
    '''
    '''
    p1 = pair[0].p
    p2 = pair[1].p
    ppair = p1 + p2
    return ppair.M()

class Particle:
    def __init__(self, p,q):
        self.p = p
        self.q = q

if __name__ == '__main__':




    data = TChain("mini")
    data.Add("http://opendata.atlas.cern/release/samples/Data/DataMuons.root")

    num_events = data.GetEntries()
    print("Number of events = "+str(num_events))
    
    h_mpair = TH1F("mpair", "Invariant Mass of Leptons ; mass /Gev; freq",50,0,200)

    num_events_to_process = 10000
    for i_event in range(num_events_to_process):
        data.GetEntry(i_event)
        n_leptons = data.lep_n
        if n_leptons >= 2:
        #print("num of Leptons "+str(n_leptons))
            leptons = leptons_from_event(data)
            pairs = pairs_from_particles(leptons) 

        # TODO: treat casse of more than two leptons

 #       print("Leptons Pts are : "+str(pt1)+" , "+str(pt2))
            for pair in pairs:
                mpair = mass_of_pair(pair)/1000
#        print("Lepton Pt from vector = "+str(p1.Pt())+" , " +str(p2.Pt()) 
#        print("Invariant Mass of lepton pair = " +str(mpair))
                h_mpair.Fill(mpair)    #converts MeV to GeV
                
    h_mpair.Draw()
raw_input("Press any button to end program")
