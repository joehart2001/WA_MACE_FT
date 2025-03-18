from mace.cli.eval_configs import main as mace_eval_configs_main
import sys
import argparse

def eval_mace(configs, model, output):
    sys.argv = ["program", "--configs", configs, "--model", model, "--output", output]
    mace_eval_configs_main()

parser = argparse.ArgumentParser(description="Evaluate MACE model.")
parser.add_argument("training_set_sizes", type=int, nargs="+", help="List of training set sizes (e.g., 10 20 30)")
args = parser.parse_args()

for training_set_size in args.training_set_sizes:
#    print(f"Evaluating training set, size = {training_set_size}")
    # Evaluate the training set
#    eval_mace(
#        configs=f"/home/jh2536/rds/hpc-work/training_val_sets/training_set_{training_set_size}_revPBE_D3.xyz",
#        model=f"/home/jh2536/FT_mace/MACE_medium_rerun_revPBE_D3_{training_set_size}.model",
#        output=f"/home/jh2536/FT_mace/evaluation/outputs_eval/FT_rerun_medium_rev_PBE_D3_{training_set_size}_eval_train_medium.xyz"
#    )

    print("Evaluating test set...")
    # Evaluate the test set
    eval_mace(
        configs=f"/home/jh2536/rds/hpc-work/training_val_sets/validation_set_100_revPBE_D3.xyz",
        model=f"/home/jh2536/scratch_mace/models/MACE_model_scratch_newE0s_revPBE_D3_{training_set_size}_stagetwo.model",
        output=f"/home/jh2536/scratch_mace/evaluation/outputs_eval/scratch_newE0s_revPBE_D3_{training_set_size}_eval_test.xyz"
    )
