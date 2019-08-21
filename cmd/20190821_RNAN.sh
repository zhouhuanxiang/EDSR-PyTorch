CUDA_VISIBLE_DEVICES=0 python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /home1/zhx/video-restoration/data \
--data_train REDS+KWAIVIDEO \
--data_test KWAIVIDEO+REDS \
--crf 25 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--n_resgroups 10 \
--batch_size 6 \
--model RNAN \
--save /home1/zhx/log/RNAN_crf25 \
--save_results \
--test_every 1000

# kwai


CUDA_VISIBLE_DEVICES=0 nohup \
python ~/zhouhuanxiang/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /media/disk5/fordata/web_server/zhouhuanxiang/data \
--data_train REDS+KWAIVIDEO \
--data_test KWAIVIDEO+REDS \
--crf 25 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--n_resgroups 10 \
--batch_size 6 \
--model RNAN \
--save /home1/zhx/log/RNAN_crf25 \
--save_results \
--test_every 1000 \
> /home1/zhx/RNAN_r10_crf25 2>&1 &