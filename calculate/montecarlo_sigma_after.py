import numpy as np
import math
import matplotlib.pyplot as plt
import sigma_used_book 
import theta_y_fixed 
import ROOT as r
from copy import copy
r.gROOT.SetBatch()

def montecarlo_sigma_after():
    Q2_rand = 0.001 + (0.99 - 0.001) * np.random.rand(10**7)
    y_rand = 0.001 + (0.99 - 0.001) * np.random.rand(10**7)
    cross_section = sigma_used_book.crosssection(y_rand, Q2_rand)
    theta = theta_y_fixed.theta(y_rand, Q2_rand)

    hist_root = r.TH1D("theta", "used structure function directly;theta [rad];event", 100, 0, 0.5)
    hist_root.FillN(10**6, np.nan_to_num(theta), np.nan_to_num(cross_section))
    for i in range(hist_root.GetNbinsX()): hist_root.SetBinError(i, 0)
    hist_root.SetBinContent(1, 0)
    canvas = r.TCanvas()
    hist_root.Draw("hist")
    canvas.SaveAs("theta_distribution_after.png")
    return copy(hist_root)

montecarlo_sigma_after()
    
"""
plt.hist(
    theta/np.pi,
    weights=cross_section,
    range=(0, 1.0),
    bins= 30,
    )
plt.xlabel("theta [rad/pi]")
plt.ylabel("proportional to prob")
plt.title("structure")
plt.show()
"""