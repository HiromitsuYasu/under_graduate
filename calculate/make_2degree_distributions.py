import ROOT as r
from montecarlo_sigma_after import montecarlo_sigma_after
from montecarlo_sigma_before import montecarlo_sigma_before
r.gROOT.SetBatch()

# fetch
hist_structure = montecarlo_sigma_after()
hist_flux = montecarlo_sigma_before()
# normalization
hist_structure.Scale(1 / hist_structure.Integral(0, 100))
hist_flux.Scale(1 / hist_flux.Integral(0, 100))
# settings
hist_structure.SetLineColor(2) # red
hist_flux.SetLineColor(4) # blue
hist_structure.SetTitle("structure (red), flux (blue), n_bins=100;theta [rad];Proportional to Prob")
hist_flux.SetTitle("structure (red), flux (blue), n_bins=100;theta [rad];Proportional to Prob")

canvas = r.TCanvas()
#hist_parent.Draw()
hist_flux.Draw("hist")
hist_structure.Draw("SAME hist")

canvas.SaveAs("two_degree_distributions.png")