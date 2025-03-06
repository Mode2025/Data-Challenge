
import os
import pathlib
import pandas as pd
import numpy as np


# Class containing fluence information for each element
class Fluence:
    def __init__(self, data, name, u, element_name=None, symbol=None):
        self.data = data
        self.name = name
        self.element_name = element_name
        self.u = u
        self.symbol = symbol

        ### Units ###
        # u:  atomic mass units
        # energy:  MeV/u
        # differential flux:  cm^-2 * s^-1 * (MeV/u)^-1
        # integral flux:  cm^-2 * s^-1

        self.energy = data[:, 0]
        self.differential_flux = data[:, 1]
        self.integral_flux = data[:, 2]


# Add fluence for solar protons
fluences = []
f = "fluences/solar_protons.csv"
data = pd.read_csv(f, header=1).to_numpy()
name = pathlib.Path(f).stem
u = 1.008
fluences.append(Fluence(data, name, u))


# Add fluence for galactic cosmic radiation
files = []
for f in os.listdir("fluences/galactic_cosmic_radiation"):
    files.append(f"fluences/galactic_cosmic_radiation/{f}")
for f in files:
    with open(f, 'r') as file:
        rl = file.readlines()
        element_name = rl[1].strip().split(sep=",")[1]
        symbol = rl[2].strip().split(sep=",")[1]
        u = float(rl[3].strip().split(sep=",")[1])
    data = pd.read_csv(f, header=4).to_numpy()
    name = pathlib.Path(f).stem
    fluences.append(Fluence(data, name, u, element_name, symbol))


# The "fluences" variable now contains all fluence information.
