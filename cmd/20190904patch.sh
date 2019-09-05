CUDA_VISIBLE_DEVICES=0 python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIPATCH \
--data_test KWAIPATCH \
--crf 40 \
--patch_size 80 \
--batch_size 16 \
--model EDSR \
--log_name patch \
> ~/zhouhuanxiang/patch40 2>&1 &

CUDA_VISIBLE_DEVICES=1 python ~/zhouhuanxiang/EDSR-PyTorch/src/main.py \
--data_train KWAIPATCH \
--data_test KWAIPATCH \
--crf 45 \
--patch_size 80 \
--batch_size 16 \
--model EDSR \
--log_name patch \
> ~/zhouhuanxiang/patch45 2>&1 &