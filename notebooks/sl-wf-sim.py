import streamlit as st
import pandas as pd
import numpy as np
import time # <- We'll need this later as well

from wf_sim import Population

st.title('Simple Wright-Fisher Simulation of Genetic Drift')

# Create a NEW Population
# As a reminder these are the default values for population size (N)
# and initial derived allele frequency (f).
#   N=10, f=0.2
p = Population()

"""Basic code to simulate wf and use streamlit LineChart 
to show the change through time"""

# Initialize chart with allele frequency of the derived allele. 
#`line_chart` expects a list, so we must wrap `p.f` in square brackets

# Initially we'll run a loop 50 times
for i in range(1, 50):
    # Step 1 wf generation
    p.step(ngens=1)
    # Calculate the current derived allele frequency
    freq = np.sum(p.pop)/len(p.pop)
    # Update the chart to add the current allele frequency
    chart.add_rows([freq])
    # sleep for a small amount of time so you can watch the animation
    time.sleep(0.05)

# Add a button to rerun the simulation
st.button("Rerun")

