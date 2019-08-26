import os

# with open("valid-videos.txt", "r") as f:
# 	for root, dirs, files in os.walk("../data", topdown=False):
# 	   for name in files:
# 	      if name.split('.')[-1] == 'mp4':
# 	      	print(name.split('.')[0])
# 	      	f.write(name.split('.')[0])
# 	   # for name in dirs:
# 	   #    print(os.path.join(root, name))

# with open('videos.txt') as fp:
# 	line = fp.readline()
# 	while line:
# 		line = line[:-1]
# 		print(line)
# 		os.system('cp /home2/zhx/HD_UGC/{}.mp4 ../data/HD_UGC/{}.mp4'.format(line, line))
# 		line = fp.readline()

import os
import socket

mode = 'lab' if socket.gethostname() == 'user-ubuntu' or socket.gethostname() == 'ubuntu' else 'kwai'
if mode == 'kwai':
	prefix = '/media/disk5/fordata/web_server/zhouhuanxiang/data'
	ffmpeg = '/usr/local/share/ffmpeg_qlh/bin/ffmpeg '
	dest = '/media/disk5/fordata/web_server/zhouhuanxiang/data/'
else:
	prefix = '/home1/zhx/video-restoration/data/'
	ffmpeg = 'ffmpeg '
	dest = '/home1/zhx/video-restoration/data/'

for crf in [30, 35, 40]:
	datasets = [['HD_UGC', 'HD_UGC_crf'], ['REDS', 'REDS_crf']]
	for dataset in datasets:
		src_path = os.path.join(prefix, dataset[0])
		dst_path = os.path.join(prefix, dataset[1]+str(crf))
		if not os.path.exists(dst_path):
			os.mkdir(dst_path)
		print("Creating destination path {} ...".format(dst_path))
		for file in sorted(os.listdir(src_path)):
			if not file.endswith(".mp4"):
				continue
			fname=file.split(".")[0]
			print('Compressing video {} ...'.format(fname))
			os.system(ffmpeg+"-i "+dest+dataset[0]+"/"+fname+".mp4 -movflags +faststart -max_interleave_delta 150000000 -max_muxing_queue_size 9999 -c:v libx265 -psnr -threads 16 -preset fast -c:a copy -profile:a aac_he -ac 2 -crf "+str(crf)+" -x265-params psnr=1:ssim=1:fakeparams=no  -tag:v hvc1  -pix_fmt yuv420p -y "+dst_path+"/"+fname+".mp4")
