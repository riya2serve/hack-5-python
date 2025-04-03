import streamlit as st
import pandas as pd
import numpy as np
import time # <- We'll need this later as well

from wf_sim import Population

st.title('Simple Wright-Fisher Simulation of Genetic Drift')

# Create a NEW Population
# These are the default values for pop. size (N) and derived allele frequency (f).
# N=10, f=0.2
p = Population()

"""Basic code to simulate wf and use streamlit LineChart 
to show the change through time"""

# Initialize chart with allele frequency of the derived allele. 
#`line_chart` expects a list, so we must wrap `p.f` in square brackets

chart = st.line_chart([p.f])

#for Challenge #1:
threshold = 0.001 #defining this as my threshold allele frequency
stable = 0  #empty counter for num. iterations passed with small change in frequency
max_stable = 2 #defining when I want it to stop 

prev_freq = None  #var to hold previous allele frequency

# Initially we'll run a loop 60 times
for i in range(1, 60):
    # Step 1 wf generation
    p.step(ngens=1)
    # Calculate the current derived allele frequency
    freq = np.sum(p.pop)/len(p.pop)
    # Update the chart to add the current allele frequency
    chart.add_rows([freq])

#check frequency change
    if prev_freq is not None and abs(freq - prev_freq) < threshold:
        stable += 1  # Increment stable count if change is small
    else:
        stable = 0  # Reset if significant change in frequency
# if frequency stable for `max_stable` iterations, BREAK the loop
    if stable >= max_stable:
        print("Frequency has stabilized. Exiting loop.")
        break

prev_freq = freq
time.sleep(0.05)

# Add a button to rerun the simulation
st.button("Rerun")

"""Streamlit can detect changes in the source code and suggest
user to re-run the code to incorporate the changes."""

# Challenge 1: End the visualization when no longer 'interesting'
# Challenge 2: Add slider to set number of wf generations to simulate
# Challenge 3: Add a progress bar
# Challenge 4: Add sliders to set N and f parameters for the pop





