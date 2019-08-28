#lab

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
--test_every 1000 \
--chop


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
--save ~/zhouhuanxiang/log/RNAN_crf25 \
--save_results \
--test_every 1000 \
--chop \
> ~/zhouhuanxiang/RNAN_r10_crf25 2>&1 &

CUDA_VISIBLE_DEVICES=1 nohup \
python ~/zhouhuanxiang/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /media/disk5/fordata/web_server/zhouhuanxiang/data \
--data_train REDS+KWAIVIDEO \
--data_test KWAIVIDEO+REDS \
--crf 30 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--n_resgroups 10 \
--batch_size 6 \
--model RNAN \
--save ~/zhouhuanxiang/log/RNAN_crf30 \
--save_results \
--test_every 1000 \
--chop \
> ~/zhouhuanxiang/RNAN_r10_crf30 2>&1 &

CUDA_VISIBLE_DEVICES=2 nohup \
python ~/zhouhuanxiang/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /media/disk5/fordata/web_server/zhouhuanxiang/data \
--data_train REDS+KWAIVIDEO \
--data_test KWAIVIDEO+REDS \
--crf 35 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--n_resgroups 10 \
--batch_size 6 \
--model RNAN \
--save ~/zhouhuanxiang/log/RNAN_crf35 \
--save_results \
--test_every 1000 \
--chop \
> ~/zhouhuanxiang/RNAN_r10_crf35 2>&1 &

CUDA_VISIBLE_DEVICES=3 nohup \
python ~/zhouhuanxiang/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /media/disk5/fordata/web_server/zhouhuanxiang/data \
--data_train REDS+KWAIVIDEO \
--data_test KWAIVIDEO+REDS \
--crf 40 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--n_resgroups 10 \
--batch_size 6 \
--model RNAN \
--save ~/zhouhuanxiang/log/RNAN_crf40 \
--save_results \
--test_every 1000 \
--chop \
> ~/zhouhuanxiang/RNAN_r10_crf40 2>&1 &

CUDA_VISIBLE_DEVICES=4 nohup \
python ~/zhouhuanxiang/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /media/disk5/fordata/web_server/zhouhuanxiang/data \
--data_train REDS+KWAIVIDEO \
--data_test KWAIVIDEO+REDS \
--crf 45 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--n_resgroups 10 \
--batch_size 6 \
--model RNAN \
--save ~/zhouhuanxiang/log/RNAN_crf45 \
--save_results \
--test_every 1000 \
--chop \
> ~/zhouhuanxiang/RNAN_r10_crf45 2>&1 &
