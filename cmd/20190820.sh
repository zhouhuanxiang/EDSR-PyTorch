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