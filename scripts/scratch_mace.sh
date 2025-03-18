#!/bin/bash

mace_run_train \
    --name="MACE_model_scratch_newE0s_revPBE_D3_10" \
    --train_file="/home/jh2536/rds/hpc-work/training_val_sets/training_set_10_revPBE_D3.xyz" \
    --valid_fraction=0.1 \
    --test_file="/home/jh2536/rds/hpc-work/training_val_sets/validation_set_100_revPBE_D3.xyz" \
    --energy_key="rPBED3_energy" \
    --forces_key="rPBED3_forces" \
    --config_type_weights='{"Default":1.0}' \
    --E0s='{1:-193.22235627360988,6:-9.372691857682717,8:-104.96354768256703,20:-6.357579367893548}' \
    --model="MACE" \
    --hidden_irreps='128x0e + 128x1o' \
    --r_max=6.0 \
    --batch_size=2 \
    --max_num_epochs=20 \
    --swa \
    --start_swa=10 \
    --ema \
    --ema_decay=0.99 \
    --amsgrad \
    --restart_latest \
    --device=cuda
