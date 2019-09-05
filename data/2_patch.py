import os
import cv2
import csv
import glob
import socket
import random
import numpy as np
import matplotlib
matplotlib.use('Agg')
# matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
import csv

if socket.gethostname() == 'user-ubuntu':
    mode = 'lab'
elif socket.gethostname() == 'ubuntu':
    mode = 'lab'
elif socket.gethostname() == 'sd-bjpg-hg27.yz02':
    mode = 'kwai27'
elif socket.gethostname() == 'bjfk-hg29.yz02':
    mode = 'kwai29'
else:
    print('new server!')

if mode == 'kwai27':
    prefix = '/media/disk5/fordata/web_server/zhouhuanxiang/data/'
    ffmpeg = '/usr/local/share/ffmpeg_qlh/bin/ffmpeg '
elif mode == 'kwai29':
    prefix = '/media/disk1/fordata/web_server/zhouhuanxiang/data/'
    ffmpeg = 'ffmpeg '
else:
    prefix = '../../../data'
    ffmpeg = 'ffmpeg '


def get_patches(img1, img2, patch_size):
	h, w = img1.shape[:2]
	ix = random.randrange(0, w - patch_size + 1)
	iy = random.randrange(0, h - patch_size + 1)
	return ix, iy, img1[iy:iy + patch_size, ix:ix + patch_size, :], img2[iy:iy + patch_size, ix:ix + patch_size, :]

dataset_all = ['HD_UGC_raw', 'HD_UGC_crf25_raw', 'HD_UGC_crf30_raw', 'HD_UGC_crf35_raw', 'HD_UGC_crf40_raw', 'HD_UGC_crf45_raw']
dataset_GT = 'HD_UGC_raw'
dataset_crfs = ['HD_UGC_crf25_raw', 'HD_UGC_crf30_raw', 'HD_UGC_crf35_raw', 'HD_UGC_crf40_raw', 'HD_UGC_crf45_raw']
dataset_size = len(dataset_crfs)
#
dataset_all = [prefix + i for i in dataset_all]
dataset_GT = prefix + dataset_GT
dataset_crfs = [prefix + i for i in dataset_crfs]

video_names = glob.glob(os.path.join(dataset_GT, '*'))
video_names.sort()
video_names = [v.split('/')[-1] for v in video_names]

# mses = [[] for _ in range(dataset_size)]
mses = []

for vname in video_names:
    print(vname + '.mp4')
    frame_names = glob.glob(os.path.join(dataset_GT, vname, '*.png'))
    frame_names.sort()
    frame_names = [f.split('/')[-1] for f in frame_names]
    frame_size = len(frame_names)
    # 1. read all frames
    # raw_video_frames has (dataset_size + 1) elements with each element has (frame_size) raw frames
    raw_video_frames = []
    for dataset in dataset_all:
        raw_frames = []
        for fname in frame_names:
            img = cv2.imread(os.path.join(dataset, vname, fname))
            raw_frames.append(img)
        raw_video_frames.append(raw_frames)
    # 2. image level MSE error 
    # for i in range(dataset_size * frame_size):
    #     dataset_id = i // frame_size
    #     frame_id = i % frame_size
    #     mse = ((raw_video_frames[0][frame_id] - raw_video_frames[dataset_id + 1][frame_id])**2).mean()
    #     mses[dataset_id].append(mse)
    # 3. patch level MSE error
    for dataset_id, dataset in enumerate(dataset_crfs):
        for i in range(9 * 16 * 10):
        # for i in range(5):
            frame_id = random.randrange(0, frame_size)
            ix, iy, pt1, pt2 = get_patches(raw_video_frames[0][frame_id], raw_video_frames[dataset_id + 1][frame_id], 96)
            mse = ((pt1 - pt2)**2).mean()
            mses.append((dataset, vname, frame_names[frame_id], ix, iy, mse))

mses.sort(key=lambda tup: tup[5])
mses_size = len(mses)
head_ratio = 0.01
tail_ratio = 0.01
stride = (1.0 - head_ratio - tail_ratio) / dataset_size
for i in range(dataset_size):
    begin = int((head_ratio + i * stride) * mses_size)
    end = int((head_ratio + (i + 1) * stride) * mses_size)
    dataset_i = mses[begin:end]
    with open('mse_{}.csv'.format(i), 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(dataset_i) 
    # for i in dataset_i:
    #     print(i)
    # print('#########')

# print(mses)

# mses = np.array(mses)
# mse_mean = mses.mean(axis=1)
# mse_std = mses.std(axis=1)

# print(mse_mean)
# print(mse_std)

# fig = plt.figure()
# plt.errorbar(['crf25', 'crf30', 'crf35', 'crf40', 'crf45'], mse_mean, yerr=mse_std, fmt="o")
# # plt.show()
# plt.savefig('mse.pdf', dpi=500)
# plt.close(fig)