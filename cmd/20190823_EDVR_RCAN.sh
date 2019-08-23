CUDA_VISIBLE_DEVICES=5 nohup \
python ~/zhouhuanxiang/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /media/disk5/fordata/web_server/zhouhuanxiang/data \
--data_train REDS+KWAIVIDEO \
--data_test KWAIVIDEO+REDS \
--crf 40 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--batch_size 6 \
--model EDSR \
--save ~/zhouhuanxiang/log/EDSR_r16_crf40 \
--test_every 1000 \
> ~/zhouhuanxiang/EDSR_r16_crf40 2>&1 &

CUDA_VISIBLE_DEVICES=6 nohup \
python ~/zhouhuanxiang/video-restoration/codes/EDSR-PyTorch/src/main.py \
--dir_data /media/disk5/fordata/web_server/zhouhuanxiang/data \
--data_train REDS+KWAIVIDEO \
--data_test KWAIVIDEO+REDS \
--crf 40 \
--n_GPUs 1  \
--ext img \
--scale 1 \
--patch_size 80 \
--batch_size 6 \
--model RNAN \
--save ~/zhouhuanxiang/log/RNAN_r10r16_crf40 \
--test_every 1000 \
> ~/zhouhuanxiang/RNAN_r10r16_crf40 2>&1 &