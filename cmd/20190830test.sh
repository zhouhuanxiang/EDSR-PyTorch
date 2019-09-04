CUDA_VISIBLE_DEVICES=0 python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 25 \
--patch_size 80 \
--batch_size 8 \
--model EDSR \
--resume -1 \
--test_only \
--save_results \
> ~/zhouhuanxiang/tEDSR_r16_crf25 2>&1 &

CUDA_VISIBLE_DEVICES=0 nohup python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 30 \
--patch_size 80 \
--batch_size 8 \
--model EDSR \
--resume -1 \
--test_only \
--save_results \
> ~/zhouhuanxiang/tEDSR_r16_crf30 2>&1 &

CUDA_VISIBLE_DEVICES=1 nohup python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 35 \
--patch_size 80 \
--batch_size 8 \
--model EDSR \
--resume -1 \
--test_only \
--save_results \
> ~/zhouhuanxiang/tEDSR_r16_crf35 2>&1 &

CUDA_VISIBLE_DEVICES=1 nohup python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 40 \
--patch_size 80 \
--batch_size 8 \
--model EDSR \
--resume -1 \
--test_only \
--save_results \
> ~/zhouhuanxiang/tEDSR_r16_crf40 2>&1 &

CUDA_VISIBLE_DEVICES=2 nohup python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO+REDS \
--data_test KWAIVIDEO+REDS \
--crf 45 \
--patch_size 80 \
--batch_size 8 \
--model EDSR \
--resume -1 \
--test_only \
--save_results \
> ~/zhouhuanxiang/tEDSR_r16_crf45 2>&1 &