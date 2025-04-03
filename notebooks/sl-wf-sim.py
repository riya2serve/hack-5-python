import streamlit as st
import pandas as pd
import numpy as np
import time # <- We'll need this later as well

from wf_sim.py import Population

st.title('Simple Wright-Fisher Simulation of Genetic Drift')
