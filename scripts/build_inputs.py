import os

test_video_ids = [
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

src_folder = '/home1/zhx/video-restoration/data'
dst_folder = '/home1/zhx/video-restoration/data/Input'
os.makedirs(dst_folder, exist_ok=True)

for crf in ['', '_crf25', '_crf30', '_crf35', '_crf40', '_crf45']:
    os.makedirs(os.path.join(dst_folder, 'HD_UGC'+crf), exist_ok=True)
    for vid in test_video_ids:
        os.system('mv '+os.path.join(src_folder, 'HD_UGC'+crf, vid+'.mp4')+' '+os.path.join(dst_folder, 'HD_UGC'+crf, vid+'.mp4'))

