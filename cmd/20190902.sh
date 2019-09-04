CUDA_VISIBLE_DEVICES=1 nohup python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO \
--data_test KWAIVIDEO \
--crf 30 \
--patch_size 80 \
--batch_size 2 \
--model EDSR \
--resume -1 \
--save_results \
--test_only \
> /home1/zhx/30 2>&1 &

CUDA_VISIBLE_DEVICES=0 nohup python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO \
--data_test KWAIVIDEO \
--crf 35 \
--patch_size 80 \
--batch_size 2 \
--model EDSR \
--resume -1 \
--save_results \
--test_only \
> /home1/zhx/35 2>&1 &


CUDA_VISIBLE_DEVICES=0 nohup python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO \
--data_test KWAIVIDEO \
--crf 40 \
--patch_size 80 \
--batch_size 2 \
--model EDSR \
--resume -1 \
--save_results \
--test_only \
> /home1/zhx/40 2>&1 &


