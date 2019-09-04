# lab 36
# RCAN 30 40
# RNAN 30 40
CUDA_VISIBLE_DEVICES=0 python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 30 \
--patch_size 80 \
--batch_size 8 \
--model RCAN \
--resume -2 \
--test_only \
--save_results \
> ~/zhouhuanxiang/tRCAN_r10r16_crf30 2>&1 &

CUDA_VISIBLE_DEVICES=1 nohup python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 40 \
--patch_size 80 \
--batch_size 8 \
--model RCAN \
--resume -2 \
--test_only \
--save_results \
> ~/zhouhuanxiang/tRCAN_r10r16_crf40 2>&1 &

CUDA_VISIBLE_DEVICES=2 nohup python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 30 \
--patch_size 80 \
--batch_size 8 \
--model RNAN \
--chop \
--resume -2 \
--test_only \
--save_results \
> ~/zhouhuanxiang/tRNAN_r10_crf30 2>&1 &

CUDA_VISIBLE_DEVICES=3 nohup python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 40 \
--patch_size 80 \
--batch_size 8 \
--model RNAN \
--chop \
--resume -2 \
--test_only \
--save_results \
> ~/zhouhuanxiang/tRNAN_r10_crf40 2>&1 &

# lab 18
# EDSR 25 30 35 40 45

CUDA_VISIBLE_DEVICES=1 nohup python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 25 \
--patch_size 80 \
--batch_size 8 \
--model EDSR \
--resume -1 \
--test_only \
--save_results \
> /home1/zhx/tEDSR_r16_crf25 2>&1 &

CUDA_VISIBLE_DEVICES=1 nohup python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 30 \
--patch_size 80 \
--batch_size 8 \
--model EDSR \
--resume -1 \
--test_only \
--save_results \
> /home1/zhx/tEDSR_r16_crf30 2>&1 &

CUDA_VISIBLE_DEVICES=1 nohup python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 35 \
--patch_size 80 \
--batch_size 8 \
--model EDSR \
--resume -1 \
--test_only \
--save_results \
> /home1/zhx/tEDSR_r16_crf35 2>&1 &

CUDA_VISIBLE_DEVICES=2 nohup python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 40 \
--patch_size 80 \
--batch_size 8 \
--model EDSR \
--resume -1 \
--test_only \
--save_results \
> /home1/zhx/tEDSR_r16_crf40 2>&1 &

CUDA_VISIBLE_DEVICES=2 nohup python /home1/zhx/video-restoration/codes/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 45 \
--patch_size 80 \
--batch_size 8 \
--model EDSR \
--resume -1 \
--test_only \
--save_results \
> /home1/zhx/tEDSR_r16_crf45 2>&1 &

# kwai
# RCAN    35 45
# RNAN 25 35 45

CUDA_VISIBLE_DEVICES=0 python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 35 \
--patch_size 80 \
--batch_size 8 \
--model RCAN \
--resume -2 \
--test_only \
--save_results \
> ~/zhouhuanxiang/tRCAN_r10r16_crf35 2>&1 &

CUDA_VISIBLE_DEVICES=1 nohup python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 45 \
--patch_size 80 \
--batch_size 8 \
--model RCAN \
--resume -2 \
--test_only \
--save_results \
> ~/zhouhuanxiang/tRCAN_r10r16_crf45 2>&1 &

CUDA_VISIBLE_DEVICES=2 nohup python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 25 \
--patch_size 80 \
--batch_size 6 \
--model RNAN \
--chop \
--resume -2 \
--test_only \
--save_results \
> ~/zhouhuanxiang/tRNAN_r10_crf25 2>&1 &

CUDA_VISIBLE_DEVICES=3 nohup \
python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 35 \
--patch_size 80 \
--batch_size 6 \
--model RNAN \
--chop \
--resume -2 \
--test_only \
--save_results \
> ~/zhouhuanxiang/tRNAN_r10_crf35 2>&1 &

CUDA_VISIBLE_DEVICES=4 nohup \
python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 45 \
--patch_size 80 \
--batch_size 6 \
--model RNAN \
--chop \
--resume -2 \
--test_only \
--save_results \
> ~/zhouhuanxiang/tRNAN_r10_crf45 2>&1 &
