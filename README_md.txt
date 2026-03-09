#Steps for running Protein molecular dynamics simulation 
Lysozyme_in_water.py
1. Open the python script
2. Write the name of the prepared .pdb file in the python script file
3. Write the name of the md output file without extension. (E.g.: "md_mol")
4. Save the file and run the script with the command
python Lysozyme_in_water.py

Make sure that the code is being run on the gpu server.

#Post MD Analysis
1. Run the script Lysozyme_mda.py
2. Enter the file names obtained after simulation.
3. Output will be the center.xtc file with backbone rmsd.xvg, rmsf.xvg, rog.xvg, hbond.xvg and sasa.xvg file
4. Make sure to check the x-axis values.

#Plotting Graphs
1. Run the python script visualisation.py
2. Enter the rmsd, rmsf, rog, hbond and sasa xvg files as input.
3. Out put will be in the form of plots in the jpeg file format.
