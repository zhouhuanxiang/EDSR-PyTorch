import os
import socket

test_video_ids = [
    # REDS
    [
        '000', 
        '050', 
        '100', 
        '150', 
        '200'
    ],
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

mode = 'lab' if socket.gethostname() == 'user-ubuntu' else 'kwai'
model = 'EDSR'
if mode == 'lab':
    result_src_folders = [
        '/home1/zhx/log/'+model+'/results-REDS',
        '/home1/zhx/log/'+model+'/results-KWAIVIDEO',
    ]
    result_dst_folders = [
        '/home1/zhx/log/'+model+'/videos-REDS/',
        '/home1/zhx/log/'+model+'/videos-KWAIVIDEO/'
    ]
    ffmpeg = 'ffmpeg '
else:
    result_src_folders = [
        '/home/wev_server/zhouhuanxiang/log/'+model+'/results-REDS',
        '/home/wev_server/zhouhuanxiang/log/'+model+'/results-KWAIVIDEO',
    ]
    result_dst_folders = [
        '/home/wev_server/zhouhuanxiang/log/'+model+'/videos-REDS',
        '/home/wev_server/zhouhuanxiang/log/'+model+'/videos-KWAIVIDEO',
    ]
    ffmpeg = '/usr/local/share/ffmpeg_qlh/bin/ffmpeg '

for folder in result_dst_folders:
    os.makedirs(folder, exist_ok=True)

path_now = os.getcwd()
for i, folder in enumerate(result_src_folders):
    for vname in test_video_ids[i]:
        path = os.path.join(result_src_folders[i], vname)
        os.chdir(path)
        print(path)
        # os.system(ffmpeg+'-i img_%5d_x1_GT.png -movflags +faststart -max_interleave_delta 150000000 -max_muxing_queue_size 9999 -c:v libx265 -psnr -threads 6 -preset fast -c:a copy -profile:a aac_he -ac 2 -x265-params lossless=1  -tag:v hvc1  -pix_fmt yuv420p -y '+os.path.join(result_dst_folders[i], vname+'_high.mp4'))
        # os.system(ffmpeg+'-i img_%5d_x1_Compressed.png -movflags +faststart -max_interleave_delta 150000000 -max_muxing_queue_size 9999 -c:v libx265 -psnr -threads 6 -preset fast -c:a copy -profile:a aac_he -ac 2 -x265-params lossless=1  -tag:v hvc1  -pix_fmt yuv420p -y '+os.path.join(result_dst_folders[i], vname+'_high.mp4'))
        os.system(ffmpeg+'-i img_%5d_x1_Result.png -movflags +faststart -max_interleave_delta 150000000 -max_muxing_queue_size 9999 -c:v libx265 -psnr -threads 6 -preset fast -c:a copy -profile:a aac_he -ac 2 -x265-params lossless=1  -tag:v hvc1  -pix_fmt yuv420p -y '+os.path.join(result_dst_folders[i], vname+'.mp4'))
os.chdir(path_now)