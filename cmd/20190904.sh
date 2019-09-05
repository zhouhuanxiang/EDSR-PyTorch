CUDA_VISIBLE_DEVICES=0 nohup python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO \
--data_test KWAIVIDEO \
--crf 25 \
--patch_size 192 \
--batch_size 16 \
--model EDSR \
--log_name baseline \
> ~/zhouhuanxiang/baseline25 2>&1 &

CUDA_VISIBLE_DEVICES=1 nohup python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO \
--data_test KWAIVIDEO \
--crf 30 \
--patch_size 192 \
--batch_size 16 \
--model EDSR \
--log_name baseline \
> ~/zhouhuanxiang/baseline30 2>&1 &

CUDA_VISIBLE_DEVICES=2 nohup python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO \
--data_test KWAIVIDEO \
--crf 35 \
--patch_size 192 \
--batch_size 16 \
--model EDSR \
--log_name baseline \
> ~/zhouhuanxiang/baseline35 2>&1 &

CUDA_VISIBLE_DEVICES=3 nohup python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO \
--data_test KWAIVIDEO \
--crf 40 \
--patch_size 192 \
--batch_size 16 \
--model EDSR \
--log_name baseline \
> ~/zhouhuanxiang/baseline40 2>&1 &

CUDA_VISIBLE_DEVICES=6 nohup python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIVIDEO \
--data_test KWAIVIDEO \
--crf 45 \
--patch_size 192 \
--batch_size 16 \
--model EDSR \
--log_name baseline \
> ~/zhouhuanxiang/baseline45 2>&1 &

nohup python 2_patch.py > ~/zhouhuanxiang/patch 2>&1 &