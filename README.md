## Files for Creating Jet Energy Correction Plots

The `qcd_processor.ipynb` notebook utilizes coffea's processor to fill histograms using the root files in `/samples`, which are corrected using the pileup weights found in `/data`. The histograms are then dumped into pkl files which are not included do to their large size.

The notebook `jec_computations.ipynb` uses the pkl files to plot jet $p_{T}$ response histograms, and fits them to a gaussian function. The means, widths, and their respective errors are then put in a CSV file for analyzing.

Lastly, `jer_plotting.ipynb` file is used to plot the JER curves as functions of the jet $p_{T}$ for all datasets. The next goal will be to produced these curves for different values of the pseudorapidity parameter $\eta$.