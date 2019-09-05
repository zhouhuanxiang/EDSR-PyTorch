import glob
import socket

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
if mode == 'kwai29':
    prefix = '/media/disk1/fordata/web_server/zhouhuanxiang/data/'
    ffmpeg = 'ffmpeg '
else:
    prefix = '../../../data'
    ffmpeg = 'ffmpeg '


a01 = sorted(glob.glob(prefix+'HD_UGC_raw/*/*.png'))
a02 = sorted(glob.glob(prefix+'HD_UGC_crf25_raw/*/*.png'))
a03 = sorted(glob.glob(prefix+'HD_UGC_crf30_raw/*/*.png'))
a04 = sorted(glob.glob(prefix+'HD_UGC_crf35_raw/*/*.png'))
a05 = sorted(glob.glob(prefix+'HD_UGC_crf40_raw/*/*.png'))
a06 = sorted(glob.glob(prefix+'HD_UGC_crf45_raw/*/*.png'))

a02 = [i.replace(prefix+'HD_UGC_crf25_raw', prefix+'HD_UGC_raw') for i in a02]
a03 = [i.replace(prefix+'HD_UGC_crf30_raw', prefix+'HD_UGC_raw') for i in a03]
a04 = [i.replace(prefix+'HD_UGC_crf35_raw', prefix+'HD_UGC_raw') for i in a04]
a05 = [i.replace(prefix+'HD_UGC_crf40_raw', prefix+'HD_UGC_raw') for i in a05]
a06 = [i.replace(prefix+'HD_UGC_crf45_raw', prefix+'HD_UGC_raw') for i in a06]


print(len(a01)) # 108630
print(len(a02)) # 108630
print(len(a03)) # 0
print(len(a04)) # 108630
print(len(a05)) # 67721
print(len(a06)) # 0
print(a01 == a02)
print(a01 == a03)
print(a01 == a04)
print(a01 == a05)
print(a01 == a06)
print('##########')

a11 = glob.glob(prefix+'HD_UGC_raw_test/*/*.png')
a12 = glob.glob(prefix+'HD_UGC_crf25_raw_test/*/*.png')
a13 = glob.glob(prefix+'HD_UGC_crf30_raw_test/*/*.png')
a14 = glob.glob(prefix+'HD_UGC_crf35_raw_test/*/*.png')
a15 = glob.glob(prefix+'HD_UGC_crf40_raw_test/*/*.png')
a16 = glob.glob(prefix+'HD_UGC_crf45_raw_test/*/*.png')

a12 = [i.replace(prefix+'HD_UGC_crf25_raw', prefix+'HD_UGC_raw') for i in a12]
a13 = [i.replace(prefix+'HD_UGC_crf30_raw', prefix+'HD_UGC_raw') for i in a13]
a14 = [i.replace(prefix+'HD_UGC_crf35_raw', prefix+'HD_UGC_raw') for i in a14]
a15 = [i.replace(prefix+'HD_UGC_crf40_raw', prefix+'HD_UGC_raw') for i in a15]
a16 = [i.replace(prefix+'HD_UGC_crf45_raw', prefix+'HD_UGC_raw') for i in a16]


print(len(a11)) # 108630
print(len(a12)) # 108630
print(len(a13)) # 0
print(len(a14)) # 108630
print(len(a15)) # 67721
print(len(a16)) # 0

print(a11 == a12)
print(a11 == a13)
print(a11 == a14)
print(a11 == a15)
print(a11 == a16)
print('##########')

a21 = sorted(glob.glob(prefix+'REDS_raw/*/*.png'))
a22 = sorted(glob.glob(prefix+'REDS_crf25_raw/*/*.png'))
a23 = sorted(glob.glob(prefix+'REDS_crf30_raw/*/*.png'))
a24 = sorted(glob.glob(prefix+'REDS_crf35_raw/*/*.png'))
a25 = sorted(glob.glob(prefix+'REDS_crf40_raw/*/*.png'))
a26 = sorted(glob.glob(prefix+'REDS_crf45_raw/*/*.png'))

a22 = [i.replace(prefix+'REDS_crf25_raw', prefix+'REDS_raw') for i in a22]
a23 = [i.replace(prefix+'REDS_crf30_raw', prefix+'REDS_raw') for i in a23]
a24 = [i.replace(prefix+'REDS_crf35_raw', prefix+'REDS_raw') for i in a24]
a25 = [i.replace(prefix+'REDS_crf40_raw', prefix+'REDS_raw') for i in a25]
a26 = [i.replace(prefix+'REDS_crf45_raw', prefix+'REDS_raw') for i in a26]

print(len(a21)) # 108630
print(len(a22)) # 108630
print(len(a23)) # 0
print(len(a24)) # 108630
print(len(a25)) # 67721
print(len(a26)) # 0

print(a21 == a22)
print(a21 == a23)
print(a21 == a24)
print(a21 == a25)
print(a21 == a26)
print('##########')

a31 = glob.glob(prefix+'REDS_raw_test/*/*.png')
a32 = glob.glob(prefix+'REDS_crf25_raw_test/*/*.png')
a33 = glob.glob(prefix+'REDS_crf30_raw_test/*/*.png')
a34 = glob.glob(prefix+'REDS_crf35_raw_test/*/*.png')
a35 = glob.glob(prefix+'REDS_crf40_raw_test/*/*.png')
a36 = glob.glob(prefix+'REDS_crf45_raw_test/*/*.png')

a32 = [i.replace(prefix+'REDS_crf25_raw', prefix+'REDS_raw') for i in a32]
a33 = [i.replace(prefix+'REDS_crf30_raw', prefix+'REDS_raw') for i in a33]
a34 = [i.replace(prefix+'REDS_crf35_raw', prefix+'REDS_raw') for i in a34]
a35 = [i.replace(prefix+'REDS_crf40_raw', prefix+'REDS_raw') for i in a35]
a36 = [i.replace(prefix+'REDS_crf45_raw', prefix+'REDS_raw') for i in a36]

print(len(a31)) # 108630
print(len(a32)) # 108630
print(len(a33)) # 0
print(len(a34)) # 108630
print(len(a35)) # 67721
print(len(a36)) # 0

print(a31 == a32)
print(a31 == a33)
print(a31 == a34)
print(a31 == a35)
print(a31 == a36)