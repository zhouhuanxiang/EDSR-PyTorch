import os
import socket
import argparse


test_video_ids = [
    # REDS
    # [
    #     '000', 
    #     '050', 
    #     '100', 
    #     '150', 
    #     '200'
    # ],
    # KWAIVIDEO
    [
        '15398963809',
        '15407349694',
        '15439392361',
        '15488420682',
        '15523784704',
        '16121597861',
        '16064993671',
        '15994056528',
        #
        '15406724531',
        '15627873950',
        '15690684867',
        '15752323646',
        '15991733137',
        '15898181711',
        '15836862878'
    ]
]

def parse_args():
    parser = argparse.ArgumentParser(description='extract raw frames')
    parser.add_argument('--models', nargs='+', 
                        help='tested models')
    parser.add_argument('--crf', nargs='+', 
                        help='crfs of tested datasets')
    args = parser.parse_args()

    return args

"""
python 4_build_results.py \
--models EDSR_r16_crf25 EDSR_r16_crf30 EDSR_r16_crf35 EDSR_r16_crf40 EDSR_r16_crf45 \
--crf 25 30 35 40 45

python 4_build_results.py \
--models RCAN_r16_crf35 RCAN_r16_crf45 \
--crf 35 45
"""
if __name__ == '__main__':
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

    args = parse_args()
    models = args.models
    for ii, model in enumerate(models):
        if mode == 'kwai27':
            video_folder = '/media/disk5/fordata/web_server/zhouhuanxiang/data/HD_UGC'
            result_src_folders = [
                '/media/disk5/fordata/web_server/zhouhuanxiang/log/'+model+'/results-KWAIVIDEO-crf'+args.crf[ii],
            ]
            result_dst_folders = [
                '/media/disk5/fordata/web_server/zhouhuanxiang/log/'+model+'/videos-KWAIVIDEO-crf'+args.crf[ii],
            ]
            ffmpeg = '/usr/local/share/ffmpeg_qlh/bin/ffmpeg '
        elif mode == 'kwai29':
            video_folder = '/media/disk1/fordata/web_server/zhouhuanxiang/data/HD_UGC'
            result_src_folders = [
                '/media/disk1/fordata/web_server/zhouhuanxiang/log/'+model+'/results-KWAIVIDEO-crf'+args.crf[ii],
            ]
            result_dst_folders = [
                '/media/disk1/fordata/web_server/zhouhuanxiang/log/'+model+'/videos-KWAIVIDEO-crf'+args.crf[ii],
            ]
            ffmpeg = 'ffmpeg ' 
        else:
            video_folder = '/home1/zhx/video-restoration/data/HD_UGC'
            result_src_folders = [
                '/home1/zhx/log/'+model+'/results-KWAIVIDEO-crf'+args.crf[ii],
            ]
            result_dst_folders = [
                '/home1/zhx/log/'+model+'/videos-KWAIVIDEO-crf'+args.crf[ii],
            ]
            ffmpeg = 'ffmpeg '

        for folder in result_dst_folders:
            if os.path.exists(folder):
                os.system('rm -rf '+folder)
            os.makedirs(folder, exist_ok=True)
            if os.path.exists(folder+'_tmp'):
                os.system('rm -rf '+folder+'_tmp')
            os.makedirs(folder+'_tmp', exist_ok=True)

        path_now = os.getcwd()
        for jj, folder in enumerate(result_src_folders):
            for vname in test_video_ids[jj]:
                fps = os.popen(ffmpeg+"-i "+os.path.join(video_folder, vname)+".mp4 2>&1 | sed -n \"s/.*, \(.*\) fp.*/\\1/p\"").read()
                fps = round(float(fps))
                path = os.path.join(result_src_folders[jj], vname)
                os.chdir(path)
                print(path, fps)

                # path0 = os.path.join(video_folder, vname+'.mp4')
                path0 = os.path.join(video_folder+'_crf'+str(args.crf[ii]), vname+'.mp4')
                path1 = os.path.join(result_dst_folders[jj]+'_tmp', vname+'_tmp.mp4')
                path2 = os.path.join(result_dst_folders[jj], vname+'.mp4')
                os.system(ffmpeg+'-r '+str(fps)+' -i img_%5d_x1_Result.png -movflags +faststart -max_interleave_delta 150000000 -max_muxing_queue_size 9999 -c:v libx265 -psnr -threads 6 -preset fast -c:a copy -profile:a aac_he -ac 2 -x265-params lossless=1  -tag:v hvc1  -pix_fmt yuv420p -y '+path1)
                # os.system(ffmpeg+'-i '+path0+' -i '+path1+' -filter_complex "[0:v:0]pad=iw*2:ih[bg]; [bg][1:v:0]overlay=w" -qp 10 '+path2)
                # os.system('rm '+path1)
        os.chdir(path_now)

        # zip -r /home1/zhx/1.zip /home1/zhx/log/EDSR_r16_crf25/videos-KWAIVIDEO-crf25 /home1/zhx/log/EDSR_r16_crf30/videos-KWAIVIDEO-crf30 /home1/zhx/log/EDSR_r16_crf35/videos-KWAIVIDEO-crf35 /home1/zhx/log/EDSR_r16_crf40/videos-KWAIVIDEO-crf40 /home1/zhx/log/EDSR_r16_crf45/videos-KWAIVIDEO-crf45

'''
ffmpeg -i .mp4 2>&1 | sed -n "s/.*, \(.*\) fp.*/\1/p"
ffmpeg -r 30 -i img_%5d_x1_Result.png -movflags +faststart -max_interleave_delta 150000000 -max_muxing_queue_size 9999 -c:v libx265 -psnr -threads 6 -preset fast -c:a copy -profile:a aac_he -ac 2 -x265-params lossless=1  -tag:v hvc1  -pix_fmt yuv420p -y chiji_Ad24DdIRwHI.mp4

'''

'''
zip -r /home1/zhx/1.zip /home1/zhx/log/EDSR_r16_crf25/videos-KWAIVIDEO-crf25 /home1/zhx/log/EDSR_r16_crf30/videos-KWAIVIDEO-crf30 /home1/zhx/log/EDSR_r16_crf35/videos-KWAIVIDEO-crf35 /home1/zhx/log/EDSR_r16_crf40/videos-KWAIVIDEO-crf40 /home1/zhx/log/EDSR_r16_crf45/videos-KWAIVIDEO-crf45

zip -r ~/zhouhuanxiang/1.zip /media/disk5/fordata/web_server/zhouhuanxiang/log/RCAN_r16_crf35/videos-KWAIVIDEO-crf35 /media/disk5/fordata/web_server/zhouhuanxiang/log/RCAN_r16_crf45/videos-KWAIVIDEO-crf45 
'''