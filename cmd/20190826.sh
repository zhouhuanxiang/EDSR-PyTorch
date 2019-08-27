#lab
# EDSR 25 35 45
# RCAN 25

CUDA_VISIBLE_DEVICES=0 nohup python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /home1/zhx/video-restoration/data \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 25 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--n_resblocks 16 \
--batch_size 8 \
--model EDSR \
--save /home1/zhx/log/EDSR_r16_crf25 \
--test_every 1000 \
--chop \
--resume -1 \
--last_epoch 4 \
> /home1/zhx/EDSR_r16_crf25 2>&1 &
# 4

CUDA_VISIBLE_DEVICES=1 nohup python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /home1/zhx/video-restoration/data \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 35 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--n_resblocks 16 \
--batch_size 8 \
--model EDSR \
--save /home1/zhx/log/EDSR_r16_crf35 \
--test_every 1000 \
--chop \
--resume -1 \
--last_epoch 2 \
> /home1/zhx/EDSR_r16_crf35 2>&1 &
# 2

CUDA_VISIBLE_DEVICES=2 nohup python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /home1/zhx/video-restoration/data \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 45 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--n_resblocks 16 \
--batch_size 8 \
--model EDSR \
--save /home1/zhx/log/EDSR_r16_crf45 \
--test_every 1000 \
--chop \
--resume -1 \
--last_epoch 4 \
> /home1/zhx/EDSR_r16_crf45 2>&1 &
# 4

CUDA_VISIBLE_DEVICES=3 nohup python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /home1/zhx/video-restoration/data \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 25 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--n_resgroups 10 \
--n_resblocks 16 \
--batch_size 8 \
--model RCAN \
--save /home1/zhx/log/RCAN_r10r16_crf25 \
--test_every 1000 \
--chop \
--resume -1 \
--last_epoch 4 \
> /home1/zhx/RCAN_r10r16_crf25 2>&1 &
# 4

# kwai
# RCAN    35 45
# RNAN 25 35 45

CUDA_VISIBLE_DEVICES=0 nohup python ~/zhouhuanxiang/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /media/disk5/fordata/web_server/zhouhuanxiang/data \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 35 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--n_resgroups 10 \
--n_resblocks 16 \
--batch_size 8 \
--model RCAN \
--save /media/disk5/fordata/web_server/zhouhuanxiang/log/RCAN_r10r16_crf35 \
--test_every 1000 \
--chop \
--resume -1 \
--last_epoch 1 \
> ~/zhouhuanxiang/RCAN_r10r16_crf35 2>&1 &

CUDA_VISIBLE_DEVICES=1 nohup python ~/zhouhuanxiang/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /media/disk5/fordata/web_server/zhouhuanxiang/data \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 45 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--n_resgroups 10 \
--n_resblocks 16 \
--batch_size 8 \
--model RCAN \
--save /media/disk5/fordata/web_server/zhouhuanxiang/log/RCAN_r10r16_crf45 \
--test_every 1000 \
--chop \
> ~/zhouhuanxiang/RCAN_r10r16_crf45 2>&1 &

CUDA_VISIBLE_DEVICES=2 nohup python ~/zhouhuanxiang/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /media/disk5/fordata/web_server/zhouhuanxiang/data \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 25 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--n_resgroups 10 \
--batch_size 6 \
--model RNAN \
--save /media/disk5/fordata/web_server/zhouhuanxiang/log/RNAN_r10_crf25 \
--test_every 1000 \
--chop \
> ~/zhouhuanxiang/RNAN_r10_crf25 2>&1 &

CUDA_VISIBLE_DEVICES=3 nohup \
python ~/zhouhuanxiang/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /media/disk5/fordata/web_server/zhouhuanxiang/data \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 35 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--n_resgroups 10 \
--batch_size 6 \
--model RNAN \
--save /media/disk5/fordata/web_server/zhouhuanxiang/log/RNAN_r10_crf35 \
--test_every 1000 \
--chop \
> ~/zhouhuanxiang/RNAN_r10_crf35 2>&1 &

CUDA_VISIBLE_DEVICES=4 nohup \
python ~/zhouhuanxiang/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /media/disk5/fordata/web_server/zhouhuanxiang/data \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 45 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--n_resgroups 10 \
--batch_size 6 \
--model RNAN \
--save /media/disk5/fordata/web_server/zhouhuanxiang/log/RNAN_r10_crf45 \
--test_every 1000 \
--chop \
> ~/zhouhuanxiang/RNAN_r10_crf45 2>&1 &
