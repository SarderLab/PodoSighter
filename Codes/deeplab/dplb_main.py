import os
import shutil
import glob
import random



cmd4 = "python3.5 train.py \
    --logtostderr \
    --training_number_of_steps=50000 \
    --learning_rate_decay_step=500 \
    --train_split=\"train\" \
    --base_learning_rate=0.0001 \
    --adan_learning_rate=0.0001 \
    --model_variant=\"xception_65\" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --train_crop_size=\"256,256\" \
    --train_batch_size=1 \
    --dataset=\"PC1\" \
    --Fine_tune_batch_norm=False \
    --tf_initial_checkpoint=\"/hdd/d8/dplb/xception/model.ckpt\" \
    --Initialize_last_layer = False \
    --Last_layers_contain_logits_only = True \
    --train_logdir=\"./models/train_log\" \
    --dataset_dir=\"/hdd/d8/dplb/PC1/tfrecord\""
os.system(cmd4)  

cmd5 = "python3 vis.py \
    --logtostderr \
    --vis_split=\"val\" \
    --model_variant=\"xception_65\" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --vis_crop_size=\"1200,1200\" \
    --max_number_of_iterations=1 \
    --dataset=\"PC1\" \
    --checkpoint_dir=\"./models/train_log\" \
    --vis_logdir=\"./models/vis_log\" \
    --dataset_dir=\"/hdd/d8/dplb/PC1/tfrecord\""
os.system(cmd5)  
