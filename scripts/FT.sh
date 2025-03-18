#!/bin/bash

mace_run_train \
    --name="MACE_medium_newE0s_revPBE0_D3_10" \
    --foundation_model="medium" \
    --multiheads_finetuning=True \
    --train_file="/home/jh2536/rds/hpc-work/training_val_sets/training_set_10_revPBE0_D3.xyz" \
    --valid_fraction=0.1 \
    --test_file="/home/jh2536/rds/hpc-work/training_val_sets/validation_set_100_revPBE0_D3.xyz" \
    --energy_key="rPBE0D3_energy" \
    --forces_key="rPBE0D3_forces" \
    --energy_weight=1.0 \
    --forces_weight=10.0 \
    --stress_weight=1.0 \
    --E0s=" {1: -193.1263432216216,6: -9.372201995172574,8: -104.91407156904245,20: -6.357089505383404}" \
    --lr=0.0001 \
    --scaling="rms_forces_scaling" \
    --batch_size=2 \
    --max_num_epochs=20 \
    --ema \
    --ema_decay=0.99999 \
    --force_mh_ft_lr=True \
    --amsgrad \
    --device=cuda \
    --enable_cueq=True \
    --pt_train_file="mp" \
    --default_dtype="float64" \
    --seed=3
