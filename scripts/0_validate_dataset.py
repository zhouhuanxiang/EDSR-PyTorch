import os
import glob
import socket
import cv2

mode = 'lab' if socket.gethostname() == 'user-ubuntu' or socket.gethostname() == 'ubuntu' else 'kwai'

if mode == 'kwai':
    prefix = '/media/disk5/fordata/web_server/zhouhuanxiang/data'
    ffmpeg = '/usr/local/share/ffmpeg_qlh/bin/ffmpeg '
else:
    prefix = '/home1/zhx/video-restoration/data/'
    ffmpeg = 'ffmpeg '

#  l1 loss 
for crf in [25, 30, 35, 40, 45]:
    path0 = os.path.join(prefix, 'HD_UGC_raw')
    path1 = os.path.join(prefix, 'HD_UGC_crf'+str(crf)+'_raw')

    files0 = glob.glob(os.path.join(path0, '*', '*.png'))
    files1 = glob.glob(os.path.join(path1, '*', '*.png'))
    files0.sort()
    files1.sort()

    for i in range(100, len(files0)):
        img0 = cv2.imread(files0[i])
        img1 = cv2.imread(files1[i])
        img0 = img0.astype('float')
        img1 = img1.astype('float')
        l1 = abs(img0 - img1).sum() / img0.size
        print(files0[i], files1[i])
        print(l1)

        if i == 200:
            break
    break
        
