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
    parser.add_argument('--data_crfs', nargs='+', 
                        help='crfs of tested datasets')
    args = parser.parse_args()

    return args

if __name__ == '__main__':
    mode = 'lab' if socket.gethostname() == 'user-ubuntu' or socket.gethostname() == 'ubuntu' else 'kwai'
    args = parse_args()
    models = args.models
    for i, model in enumerate(models):
        if mode == 'lab':
            video_folder = '/home1/zhx/video-restoration/data/HD_UGC'
            result_src_folders = [
                # '/home1/zhx/log/'+model+'/results-REDS',
                '/home1/zhx/log/'+model+'/results-KWAIVIDEO-crf'+args.crf[i],
            ]
            result_dst_folders = [
                # '/home1/zhx/log/'+model+'/videos-REDS/',
                '/home1/zhx/log/'+model+'/videos-KWAIVIDEO-crf'+args.crf[i],
            ]
            ffmpeg = 'ffmpeg '
        else:
            video_folder = '/media/disk5/fordata/web_server/zhouhuanxiang/data/HD_UGC'
            result_src_folders = [
                # '/media/disk5/fordata/web_server/zhouhuanxiang/log/'+model+'/results-REDS',
                '/media/disk5/fordata/web_server/zhouhuanxiang/log/'+model+'/results-KWAIVIDEO',
            ]
            result_dst_folders = [
                # '/media/disk5/fordata/web_server/zhouhuanxiang/log/'+model+'/videos-REDS',
                '/media/disk5/fordata/web_server/zhouhuanxiang/log/'+model+'/videos-KWAIVIDEO',
            ]
            ffmpeg = '/usr/local/share/ffmpeg_qlh/bin/ffmpeg '

        for folder in result_dst_folders:
            os.makedirs(folder, exist_ok=True)

        path_now = os.getcwd()
        for i, folder in enumerate(result_src_folders):
            for vname in test_video_ids[i]:
                fps = os.popen(ffmpeg+"-i "+os.path.join(video_folder, vname)+".mp4 2>&1 | sed -n \"s/.*, \(.*\) fp.*/\\1/p\"").read()
                fps = round(float(fps))
                path = os.path.join(result_src_folders[i], vname)
                os.chdir(path)
                # print(ffmpeg+"-i "+os.path.join(video_folder, vname)+".mp4 2>&1 | sed -n \"s/.*, \(.*\) fp.*/\\1/p\"")
                # print(round(float(os.system(ffmpeg+"-i "+os.path.join(video_folder, vname)+".mp4 2>&1 | sed -n \"s/.*, \(.*\) fp.*/\\1/p\""))))
                print(path, fps)
                # os.system(ffmpeg+'-r '+fps+'-i img_%5d_x1_GT.png -movflags +faststart -max_interleave_delta 150000000 -max_muxing_queue_size 9999 -c:v libx265 -psnr -threads 6 -preset fast -c:a copy -profile:a aac_he -ac 2 -x265-params lossless=1  -tag:v hvc1  -pix_fmt yuv420p -y '+os.path.join(result_dst_folders[i], vname+'_high.mp4'))
                # os.system(ffmpeg+'-r '+fps+'-i img_%5d_x1_Compressed.png -movflags +faststart -max_interleave_delta 150000000 -max_muxing_queue_size 9999 -c:v libx265 -psnr -threads 6 -preset fast -c:a copy -profile:a aac_he -ac 2 -x265-params lossless=1  -tag:v hvc1  -pix_fmt yuv420p -y '+os.path.join(result_dst_folders[i], vname+'_high.mp4'))
                os.system(ffmpeg+'-r '+str(fps)+' -i img_%5d_x1_Result.png -movflags +faststart -max_interleave_delta 150000000 -max_muxing_queue_size 9999 -c:v libx265 -psnr -threads 6 -preset fast -c:a copy -profile:a aac_he -ac 2 -x265-params lossless=1  -tag:v hvc1  -pix_fmt yuv420p -y '+os.path.join(result_dst_folders[i], vname+'.mp4'))
        os.chdir(path_now)