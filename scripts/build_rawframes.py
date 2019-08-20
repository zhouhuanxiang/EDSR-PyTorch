import argparse
import sys
import os
import os.path as osp
import glob
from pipes import quote
from multiprocessing import Pool, current_process

import cv2
import socket


def dump_frames(vid_item):
    full_path, vid_path, vid_id = vid_item
    vid_name = vid_path.split('.')[0]
    out_full_path = osp.join(out_dir, vid_name)
    try:
        os.mkdir(out_full_path)
    except OSError:
        pass

    # Read frame by ffmpeg
    os.system(ffmpeg+'-i '+full_path+' -vf fps=5 '+out_full_path+'/img_%05d.png -hide_banner')
    
    ## Read frames by opencv
    # video = cv2.VideoCapture(full_path) 
    # success, frame = video.read()
    # count = 0
    # while success:
    #     if count % 5 == 0:
    #         cv2.imwrite('{}/img_{:05d}.png'.format(out_full_path, count // 5), frame) 
    #     success, frame = video.read()
    #     count += 1

    print('video {} extracted'.format(vid_name))
    sys.stdout.flush()
    return True


def parse_args():
    parser = argparse.ArgumentParser(description='extract raw frames')
    parser.add_argument('--num_worker', type=int, default=8)
    parser.add_argument('--path', nargs='+', 
                        help='path(s) of video folder to be extracted')
    parser.add_argument("--ext", type=str, default='mp4', choices=['avi', 'mp4', 'webm'], 
                        help='video file extensions')
    args = parser.parse_args()

    return args

'''
nphup \
python /home1/zhx/video-restoration/scripts/build_rawframes.py --env lab --path HD_UGC_crf25 HD_UGC_crf45 REDS_crf25 REDS_crf45 \
> /home1/zhx/ffmpeg 2>&1 &

python build_rawframes.py --path HD_UGC_crf25 HD_UGC_crf45
'''

if __name__ == '__main__':
    args = parse_args()
    
    mode = 'lab' if socket.gethostname() == 'user-ubuntu' else 'kwai'
    if mode == 'kwai':
        prefix = '/media/disk1/fordata/web_server/zhouhuanxiang/data'
        ffmpeg = '/usr/local/share/ffmpeg_qlh/bin/ffmpeg '
    else:
        prefix = '../../../data'
        ffmpeg = 'ffmpeg '

    for path in args.path:
        src_dir = osp.join(prefix, path)
        out_dir = osp.join(prefix, path+'_raw')
        if not osp.isdir(out_dir):
            print('Creating folder: {}'.format(out_dir))
            os.makedirs(out_dir)

        print('Reading videos from folder')
        print('Extension of videos: ', args.ext)
        fullpath_list = glob.glob(src_dir + '/*.' + args.ext)
        print('Total number of videos found: ', len(fullpath_list))
        vid_list = list(map(lambda p: p.split('/')[-1], fullpath_list))

        pool = Pool(args.num_worker)
        pool.map(dump_frames, zip(
                fullpath_list, vid_list, range(len(vid_list))))
