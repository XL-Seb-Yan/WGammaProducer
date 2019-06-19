#include "../interface/GenParticlesNtuplizer.h"

//===================================================================================================================        
GenParticlesNtuplizer::GenParticlesNtuplizer( std::vector<edm::EDGetTokenT<reco::GenParticleCollection>> tokens, 
					      NtupleBranches* nBranches ) 

   : CandidateNtuplizer( nBranches )
   , genParticlesToken_( tokens[0] )
{
    
}

//===================================================================================================================
GenParticlesNtuplizer::~GenParticlesNtuplizer( void )
{
}

//===================================================================================================================
bool GenParticlesNtuplizer::checkPDGID(int pdgid) {
    return ((fabs(pdgid) > 22 && fabs(pdgid) < 26) || pdgid == 35 || pdgid == 36);
}

//===================================================================================================================

int GenParticlesNtuplizer::photonOrigin(reco::GenParticle photon) {
    //implementation of a flag for the photon truth matching:
    //https://hypernews.cern.ch/HyperNews/CMS/get/susy-interpretations/192.html
    //-1: not a photon
    //0: direct prompt photons (prompt and delta R > 0.4)
    //1: fragmentation photons (prompt and delta R < 0.4)
    //2: non-prompt photons
    
    if (photon.pdgId() != 22) return -1;
    if (!photon.isPromptFinalState()) return 2;

    TLorentzVector photonP4; photonP4.SetPtEtaPhiE(photon.pt(),photon.eta(),photon.phi(),photon.energy());
    TLorentzVector partonP4;
    bool smallDR = false;
    for( unsigned p=0; p<genParticles_->size(); ++p ){
        if ((*genParticles_)[p].status() != 23) continue;
        if (!((*genParticles_)[p].pdgId() == 21 || (fabs((*genParticles_)[p].pdgId()) > 0 && fabs((*genParticles_)[p].pdgId()) <7))) continue;
        partonP4.SetPtEtaPhiE((*genParticles_)[p].pt(),(*genParticles_)[p].eta(),(*genParticles_)[p].phi(),(*genParticles_)[p].energy());
        double deltaR = photonP4.DeltaR(partonP4);
        smallDR |= (deltaR < 0.4);
    }
    if (smallDR) return 1;
    else return 0;
}


//===================================================================================================================
void GenParticlesNtuplizer::fillBranches( edm::Event const & event, const edm::EventSetup& iSetup ){
    
    event.getByToken(genParticlesToken_ , genParticles_);
    
    /* here we want to save  gen particles info*/
    
    std::vector<int> vDau ;
    std::vector<int> vMoth;
    int nMoth = 0;
    int nDau  = 0;
    nBranches_->genParticle_N = genParticles_->size();
    for( unsigned p=0; p<genParticles_->size(); ++p ){
        //store only gamma/Z/W/H/A0/H0 and Z/W/H/A0/H0 daughters: 22,23,24,25,35,36
        bool store = checkPDGID((*genParticles_)[p].pdgId()) || (*genParticles_)[p].pdgId() == 22;

        vDau.clear(); vMoth.clear();
        nDau = 0; nMoth = 0;
        
        for( unsigned int m=0; m<(*genParticles_)[p].numberOfMothers(); ++m ){
            vMoth.push_back( (*genParticles_)[p].mother(m)->pdgId() );
            nMoth++;
            store |= checkPDGID((*genParticles_)[p].mother(m)->pdgId());
        }
        if (!store) continue;
        
        //if( (*genParticles_)[p].status() != 3 ) continue;

        nBranches_->genParticle_pt    .push_back((*genParticles_)[p].pt()     );
        nBranches_->genParticle_px    .push_back((*genParticles_)[p].px()     );
        nBranches_->genParticle_py    .push_back((*genParticles_)[p].py()     );
        nBranches_->genParticle_pz    .push_back((*genParticles_)[p].pz()     );
        nBranches_->genParticle_eta   .push_back((*genParticles_)[p].eta()    );
        nBranches_->genParticle_mass  .push_back((*genParticles_)[p].mass()   );
        nBranches_->genParticle_phi   .push_back((*genParticles_)[p].phi()    );
        nBranches_->genParticle_e     .push_back((*genParticles_)[p].energy() );
        nBranches_->genParticle_status.push_back((*genParticles_)[p].status() );
        nBranches_->genParticle_pdgId .push_back((*genParticles_)[p].pdgId()  );

        nBranches_->genParticle_origin.push_back(photonOrigin((*genParticles_)[p]));
        
        for( unsigned int d=0; d<(*genParticles_)[p].numberOfDaughters(); ++d ){
            vDau.push_back( (*genParticles_)[p].daughter(d)->pdgId() );
            nDau++;
        }
        
        nBranches_->genParticle_nDau  .push_back( nDau  );
        nBranches_->genParticle_nMoth .push_back( nMoth );
        nBranches_->genParticle_mother.push_back( vMoth );
        nBranches_->genParticle_dau   .push_back( vDau  );
        
    }
    
    nBranches_->lheV_pt = 0.;
    nBranches_->lheNj = 0;
    nBranches_->lheHT = 0.;
}
