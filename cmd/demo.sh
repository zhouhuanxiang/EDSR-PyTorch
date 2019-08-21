EDSR RCAN

(n_resblocks, patch_size) =
    (16, 96),
    (8, 96),
    (16, 48),
    (8, 96)

# 2019.8.14 
# RCAN r16p96 on lab
nohup \
python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /home1/zhx/video-restoration/data \
--data_train REDS+KWAIVIDEO \
--data_test KWAIVIDEO+REDS \
--n_GPUs 4 --used_GPUs 0 7 8 9 \
--ext img \
--scale 1 \
--patch_size 96 \
--batch_size 4 \
--model RCAN \
--save /home1/zhx/log/RCAN_r16 \
--save_results \
--test_every 4000 \
--load /home1/zhx/log/RCAN_r16 \
--resume -1 \
--test_only \
> /home1/zhx/RCAN 2>&1 &

## here !!! 2019.8.20
# EDSR r8p96 on 166.111.80.18
CUDA_VISIBLE_DEVICES=0 nohup \
python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /home1/zhx/video-restoration/data \
--data_train REDS+KWAIVIDEO \
--data_test KWAIVIDEO+REDS \
--crf 25 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 96 \
--n_resblocks 8 \
--batch_size 64 \
--model EDSR \
--save /home1/zhx/log/EDSR_r8_crf25 \
--save_results \
--test_every 1000 \
--load /home1/zhx/log/EDSR_r8_crf25 \
--resume -1 \
--test_only \
> /home1/zhx/EDSR_r8_crf25 2>&1 &

CUDA_VISIBLE_DEVICES=1 nohup \
python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /home1/zhx/video-restoration/data \
--data_train REDS+KWAIVIDEO \
--data_test KWAIVIDEO+REDS \
--crf 30 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 96 \
--n_resblocks 8 \
--batch_size 64 \
--model EDSR \
--save /home1/zhx/log/EDSR_r8_crf30 \
--save_results \
--test_every 1000 \
--load /home1/zhx/log/EDSR_r8_crf30 \
--resume -1 \
--test_only \
> /home1/zhx/EDSR_r8_crf30 2>&1 &

CUDA_VISIBLE_DEVICES=2 nohup \
python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /home1/zhx/video-restoration/data \
--data_train REDS+KWAIVIDEO \
--data_test KWAIVIDEO+REDS \
--crf 35 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 96 \
--n_resblocks 8 \
--batch_size 64 \
--model EDSR \
--save /home1/zhx/log/EDSR_r8_crf35 \
--save_results \
--test_every 1000 \
--load /home1/zhx/log/EDSR_r8_crf35 \
--resume -1 \
--test_only \
> /home1/zhx/EDSR_r8_crf35 2>&1 &

CUDA_VISIBLE_DEVICES=3 nohup \
python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /home1/zhx/video-restoration/data \
--data_train REDS+KWAIVIDEO \
--data_test KWAIVIDEO+REDS \
--crf 40 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 96 \
--n_resblocks 8 \
--batch_size 64 \
--model EDSR \
--save /home1/zhx/log/EDSR_r8_crf40 \
--save_results \
--test_every 1000 \
--load /home1/zhx/log/EDSR_r8_crf40 \
--resume -1 \
--test_only \
> /home1/zhx/EDSR_r8_crf40 2>&1 &

nohup \
CUDA_VISIBLE_DEVICES=3 python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /home1/zhx/video-restoration/data \
--data_train REDS+KWAIVIDEO \
--data_test KWAIVIDEO+REDS \
--crf 45 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 96 \
--n_resblocks 8 \
--batch_size 64 \
--model EDSR \
--save /home1/zhx/log/EDSR_r8_crf45 \
--save_results \
--test_every 1000 \
> /home1/zhx/EDSR_r8_crf45 2>&1 &


################
# EDSR r16p96 on kwai
nohup \
python ~/zhouhuanxiang/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /media/disk5/fordata/web_server/zhouhuanxiang/data \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--n_GPUs 4 --used_GPUs 0 7 8 9 \
--ext img \
--scale 1 \
--patch_size 192 \
--batch_size 32 \
--model EDSR \
--save /media/disk5/fordata/web_server/zhouhuanxiang/log/EDSR_r16 \
--save_results \
--test_every 4000 \
--load /media/disk5/fordata/web_server/zhouhuanxiang/log/EDSR_r16 \
--resume -1 \
--test_only \
> ~/zhouhuanxiang/edsr 2>&1 &
# EDSR r8p96 on kwai
nohup \
python ~/zhouhuanxiang/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /media/disk5/fordata/web_server/zhouhuanxiang/data \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--n_GPUs 4 --used_GPUs 0 7 8 9 \
--ext img \
--scale 1 \
--patch_size 192 \
--n_resblocks 8 \
--batch_size 32 \
--model EDSR \
--save /media/disk5/fordata/web_server/zhouhuanxiang/log/EDSR_r8 \
--save_results \
--test_every 4000 \
> ~/zhouhuanxiang/edsr 2>&1 &


# EDSR baseline model (x2) + JPEG augmentation
#python main.py --model EDSR --scale 2 --patch_size 96 --save edsr_baseline_x2 --reset
#python main.py --model EDSR --scale 2 --patch_size 96 --save edsr_baseline_x2 --reset --data_train DIV2K+DIV2K-Q75 --data_test DIV2K+DIV2K-Q75

# EDSR baseline model (x3) - from EDSR baseline model (x2)
#python main.py --model EDSR --scale 3 --patch_size 144 --save edsr_baseline_x3 --reset --pre_train [pre-trained EDSR_baseline_x2 model dir]

# EDSR baseline model (x4) - from EDSR baseline model (x2)
#python main.py --model EDSR --scale 4 --save edsr_baseline_x4 --reset --pre_train [pre-trained EDSR_baseline_x2 model dir]

# EDSR in the paper (x2)
#python main.py --model EDSR --scale 2 --save edsr_x2 --n_resblocks 32 --n_feats 256 --res_scale 0.1 --reset

# EDSR in the paper (x3) - from EDSR (x2)
#python main.py --model EDSR --scale 3 --save edsr_x3 --n_resblocks 32 --n_feats 256 --res_scale 0.1 --reset --pre_train [pre-trained EDSR model dir]

# EDSR in the paper (x4) - from EDSR (x2)
#python main.py --model EDSR --scale 4 --save edsr_x4 --n_resblocks 32 --n_feats 256 --res_scale 0.1 --reset --pre_train [pre-trained EDSR_x2 model dir]

# MDSR baseline model
#python main.py --template MDSR --model MDSR --scale 2+3+4 --save MDSR_baseline --reset --save_models

# MDSR in the paper
#python main.py --template MDSR --model MDSR --scale 2+3+4 --n_resblocks 80 --save MDSR --reset --save_models

# Standard benchmarks (Ex. EDSR_baseline_x4)
#python main.py --data_test Set5+Set14+B100+Urban100+DIV2K --data_range 801-900 --scale 4 --pre_train download --test_only --self_ensemble

#python main.py --data_test Set5+Set14+B100+Urban100+DIV2K --data_range 801-900 --scale 4 --n_resblocks 32 --n_feats 256 --res_scale 0.1 --pre_train download --test_only --self_ensemble

# Test your own images
#python main.py --data_test Demo --scale 4 --pre_train download --test_only --save_results

# Advanced - Test with JPEG images 
#python main.py --model MDSR --data_test Demo --scale 2+3+4 --pre_train download --test_only --save_results

# Advanced - Training with adversarial loss
#python main.py --template GAN --scale 4 --save edsr_gan --reset --patch_size 96 --loss 5*VGG54+0.15*GAN --pre_train download

# RDN BI model (x2)
#python3.6 main.py --scale 2 --save RDN_D16C8G64_BIx2 --model RDN --epochs 200 --batch_size 16 --data_range 801-805 --patch_size 64 --reset
# RDN BI model (x3)
#python3.6 main.py --scale 3 --save RDN_D16C8G64_BIx3 --model RDN --epochs 200 --batch_size 16 --data_range 801-805 --patch_size 96 --reset
# RDN BI model (x4)
#python3.6 main.py --scale 4 --save RDN_D16C8G64_BIx4 --model RDN --epochs 200 --batch_size 16 --data_range 801-805 --patch_size 128 --reset

# RCAN_BIX2_G10R20P48, input=48x48, output=96x96
# pretrained model can be downloaded from https://www.dropbox.com/s/mjbcqkd4nwhr6nu/models_ECCV2018RCAN.zip?dl=0
#python main.py --template RCAN --save RCAN_BIX2_G10R20P48 --scale 2 --reset --save_results --patch_size 96
# RCAN_BIX3_G10R20P48, input=48x48, output=144x144
#python main.py --template RCAN --save RCAN_BIX3_G10R20P48 --scale 3 --reset --save_results --patch_size 144 --pre_train ../experiment/model/RCAN_BIX2.pt
# RCAN_BIX4_G10R20P48, input=48x48, output=192x192
#python main.py --template RCAN --save RCAN_BIX4_G10R20P48 --scale 4 --reset --save_results --patch_size 192 --pre_train ../experiment/model/RCAN_BIX2.pt
# RCAN_BIX8_G10R20P48, input=48x48, output=384x384
#python main.py --template RCAN --save RCAN_BIX8_G10R20P48 --scale 8 --reset --save_results --patch_size 384 --pre_train ../experiment/model/RCAN_BIX2.pt

