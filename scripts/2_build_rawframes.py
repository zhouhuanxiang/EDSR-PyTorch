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
    full_path, vid_path, vid_id, no_clean = vid_item
    vid_name = vid_path.split('.')[0]
    out_full_path = osp.join(out_dir, vid_name)
    try:
        os.mkdir(out_full_path)
    except OSError:
        pass

    # Read frame by ffmpeg
    os.system(ffmpeg+'-i '+full_path+' '+out_full_path+'/img_%05d.png -hide_banner')
    
    ## Read frames by opencv
    # video = cv2.VideoCapture(full_path) 
    # success, frame = video.read()
    # count = 0
    # while success:
    #     if count % 5 == 0:
    #         cv2.imwrite('{}/img_{:05d}.png'.format(out_full_path, count // 5), frame) 
    #     success, frame = video.read()
    #     count += 1

    # clean
    if not no_clean:
        imgs_path = glob.glob(os.path.join(out_full_path, '*.png'))
        imgs_path.sort()
        imgs_path_1 = imgs_path[0::5]
        imgs_path_2 = list(set(imgs_path) - set(imgs_path_1))
        for i in imgs_path_2:
            os.system('rm ' + i)

    print('video {} extracted'.format(vid_name))
    sys.stdout.flush()
    return True


def parse_args():
    parser = argparse.ArgumentParser(description='extract raw frames')
    parser.add_argument('--num_worker', type=int, default=8)
    parser.add_argument('--no_clean', action='store_true',
                        help='extract all frames')
    parser.add_argument('--path', nargs='+', 
                        help='path(s) of video folder to be extracted')
    parser.add_argument("--ext", type=str, default='mp4', choices=['avi', 'mp4', 'webm', 'flv'], 
                        help='video file extensions')
    args = parser.parse_args()

    return args

'''
python 2_build_rawframes.py --path REDS REDS_crf25 REDS_crf30 REDS_crf35 REDS_crf40 REDS_crf45

python 2_build_rawframes.py --path HD_UGC HD_UGC_crf25 HD_UGC_crf30 HD_UGC_crf35 HD_UGC_crf40 HD_UGC_crf45
'''

if __name__ == '__main__':
    args = parse_args()
    
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
        prefix = '/media/disk5/fordata/web_server/zhouhuanxiang/data'
        ffmpeg = '/usr/local/share/ffmpeg_qlh/bin/ffmpeg '
    if mode == 'kwai29':
        prefix = '/media/disk1/fordata/web_server/zhouhuanxiang/data'
        ffmpeg = 'ffmpeg '
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
        pool.map(dump_frames, zip(fullpath_list, vid_list, range(len(vid_list)), [args.no_clean] * len(fullpath_list)))
