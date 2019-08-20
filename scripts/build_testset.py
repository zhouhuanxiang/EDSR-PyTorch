import os

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

dataset_dirs = [
    [
        'REDS_crf25',
        'REDS_crf45'
    ],
    [
        'HD_UGC_crf25',
        'HD_UGC_crf45'
    ]
]

mode = 'lab'
if mode == 'kwai':
    prefix = '/media/disk1/fordata/web_server/zhouhuanxiang/data'
else:
    prefix = '../data'

for i, dataset in enumerate(dataset_dirs):
    for d in dataset:
        if not os.path.exists(os.path.join(prefix, d+'_raw_test')):
            os.mkdir(os.path.join(prefix, d+'_raw_test'))
        for v in test_video_ids[i]:
            # delete the video raw frames from train set
            if os.path.exists(os.path.join(prefix, d+'_raw', v)):
                print('deleting video {} from trainset'.format(os.path.join(prefix, d+'_raw', v)))
                os.system('rm -rf '+os.path.join(prefix, d+'_raw', v))
            src_path = os.path.join(prefix, d, v+'.mp4')
            dst_path = os.path.join(prefix, d+'_raw_test', v)
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
            if mode == 'kwai':
                os.system('/usr/local/share/ffmpeg_qlh/bin/ffmpeg -i '+src_path+' '+dst_path+'/img_%05d.png -hide_banner')
            else:
                os.system('ffmpeg -i '+src_path+' '+dst_path+'/img_%05d.png -hide_banner')        
    
