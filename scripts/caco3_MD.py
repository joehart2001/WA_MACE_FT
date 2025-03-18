from mace.calculators import mace_mp
from ase import build

from ase.md import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
from ase import Atoms
from ase.build import bulk
from ase.visualize import view
import numpy as np
from ase.build import add_vacuum
from ase.optimize import LBFGS, BFGS
from ase import Atom

from ase.io.trajectory import Trajectory
from ase.md import Langevin, Bussi
from ase import io


#macemp = mace_mp(dispersion=True, default_dtype="float64")
mace_FT = mace_mp(model="/home/raid/jh2536/WA_FT_mace/MD/MACE_medium_newE0s_revPBE_D3_100.model", dispersion=True, default_dtype="float64", device='cuda', enable_cueq=True)

CaCO3 = io.read("/home/raid/jh2536/WA_FT_mace/MD/CaCO3_frame.xyz")





#--------------------------------MD--------------------------------

import time
start_time = time.time()

def printenergy(a=CaCO3):
    epot = a.get_potential_energy() / len(a)
    ekin = a.get_kinetic_energy() / len(a)
    elapsed_time = time.time() - start_time
    elapsed_min, elapsed_sec = divmod(elapsed_time, 60)
    print('Energy per atom: Epot = %.3feV  Ekin = %.3feV (T=%3.0fK)  '
          'Etot = %.3feV Time Elapsed: %dm %.1fs' % (epot, ekin, ekin / (1.5 * units.kB), epot + ekin, int(elapsed_min), int(elapsed_sec)))


def remove_COM_velocity(atoms):
    momenta = atoms.get_momenta()
    total_momentum = momenta.sum(axis=0)
    total_mass = atoms.get_masses().sum()
    com_velocity = total_momentum / total_mass
    atoms.set_momenta(momenta - com_velocity * atoms.get_masses()[:, np.newaxis])

    
CaCO3.calc = mace_FT
T_init = 600  # Initial temperature in K
MaxwellBoltzmannDistribution(CaCO3, temperature_K=T_init)
remove_COM_velocity(CaCO3)


dyn = Bussi(CaCO3, 1 * units.fs, T_init, 0.01)
n_steps = 250000

dyn.attach(printenergy, interval = 1000) 

traj = Trajectory('/home/raid/jh2536/WA_FT_mace/MD/CaCO3_modified_FT_100_600K_250000.traj', 'w', CaCO3)
dyn.attach(traj.write, interval = 10)
printenergy()
dyn.run(n_steps)
