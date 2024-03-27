import awkward as ak
import numpy as np
import coffea
import uproot
import hist
import vector
from coffea import util, processor
from coffea.nanoevents import NanoEventsFactory, NanoAODSchema, BaseSchema
from collections import defaultdict
import correctionlib
from coffea import nanoevents, util
np.seterr(divide='ignore', invalid='ignore')
import glob as glob
import re
import itertools
from coffea.lookup_tools import extractor
from coffea.jetmet_tools import JECStack, CorrectedJetsFactory

class util_binning :

    def __init__(self):
        
        self.dataset_axis = hist.axis.StrCategory([], growth=True, name="dataset", label="Primary dataset")
        self.frac_axis = hist.axis.Regular(300, 0, 2, name="frac", label="Ratio")
        self.eta_axis = hist.axis.Regular(100, -8.1, 8.1, name="eta", label="$\eta$")
        self.phi_axis = hist.axis.Regular(100, -2*np.pi, 2*np.pi, name="phi", label="$\phi$")
        self.pt_axis = hist.axis.Regular(500, 0, 13500, name="pt", label="$p_T$")
        
        self.rho_axis = hist.axis.Regular(100, 0, 101, name="rho", label=r"$\rho$")
        self.npvs_axis = hist.axis.Regular(190, 0, 191, name="npvs", label="$N_{PV}$")
        self.npu_axis = hist.axis.Regular(60, 0, 120, name="npu", label="$N_{PU}$")
      
    
def GetPUSF(IOV, nTrueInt, var='nominal'):
    
    corrlib_namemap = {
    "2016APV":"2016preVFP_UL",
    "2016":"2016postVFP_UL",
    "2017":"2017_UL",
    "2018":"2018_UL"
    }
    
    fname = "data/pu_weights/" + corrlib_namemap[IOV] + "/puWeights.json.gz"
    hname = {
        "2016APV": "Collisions16_UltraLegacy_goldenJSON",
        "2016"   : "Collisions16_UltraLegacy_goldenJSON",
        "2017"   : "Collisions17_UltraLegacy_goldenJSON",
        "2018"   : "Collisions18_UltraLegacy_goldenJSON"
    }
    
    evaluator = correctionlib.CorrectionSet.from_file(fname)
    return evaluator[hname[IOV]].evaluate(np.array(nTrueInt), var)


def gaussian_function(x, amplitude, mean, standard_dev):
    return amplitude * np.exp(- (x - mean)**2 / (2. * standard_dev**2))
