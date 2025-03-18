# Written Assignment: Fine-Tuning Foundation Models with MACE

### Notebooks
- pre-processing of data
- re-estimating E0s via least squares
- analysis of model performance: loss, RMSEs, observables from MD

### CSD3 and FAST-pc scripts
- example slurm script used to run bash and python scripts...
    - `my_slurm_submit.wilkes3`
- example bash scripts for model training and fine-tuning models
    - `scratch_mace.sh`
    - `FT.sh`
    - `multihead_scratch_mace.sh`
    - `multihead_config.yaml`
    - `E0s_revPBE_D3.json`
- example python script for running MD on the CaCO3/H2O system
    - `caco3_MD.py`