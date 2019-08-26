import os
import glob



src_paths = os.path.join('/home1/zhx/data/SR/Ground-truth', 'train_sharp')
dst_paths = os.path.join('/home1/zhx/data/SR/Ground-truth', 'train_sharp_video')

if not os.path.exists(dst_paths):
    os.mkdir(dst_paths)

src_paths_list = glob.glob(os.path.join(src_paths, '*'))
print('Total video number {}'.format(len(src_paths_list)))

for p in src_paths_list:
    print('Working in {}'.format(p))
    vname = p.split('/')[-1]
    vpath = os.path.join(dst_paths, vname+'.mp4')
    # if os.path.isfile(vpath):
    #     continue
    # if vname != '000':
    #     continue
    os.system('ffmpeg -r 30 -i '+p+ '/%8d.png -movflags +faststart -max_interleave_delta 150000000 -max_muxing_queue_size 9999 -c:v libx265 -psnr -threads 6 -preset fast -c:a copy -profile:a aac_he -ac 2 -x265-params lossless=1  -tag:v hvc1  -pix_fmt yuv420p -y '+vpath)