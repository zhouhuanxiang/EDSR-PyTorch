import os
import glob
from data import srdata
import csv
import socket
import re

class KWAIPATCH(srdata.SRData):
    def __init__(self, args, name='KWAIPATCH', train=True, benchmark=False):
        #  modify some cfgs
        self.input_large = True
        self.crf = args.crf
        self.train = train

        data_range = [r.split('-') for r in args.data_range.split('/')]
        if train:
            data_range = data_range[0]
        else:
            if args.test_only and len(data_range) == 1:
                data_range = data_range[0]
            else:
                data_range = data_range[1]

        self.begin, self.end = list(map(lambda x: int(x), data_range))

        # read patch info from csv
        if self.train:
            csv_filename_map = {
                '25': 'mse_0.csv',
                '30': 'mse_1.csv',
                '35': 'mse_2.csv',
                '40': 'mse_3.csv',
                '45': 'mse_4.csv'
            }
            if socket.gethostname() == 'sd-bjpg-hg27.yz02':
                mode = 'kwai27'
                prefix = '/media/disk5/fordata/web_server/zhouhuanxiang/'
            elif socket.gethostname() == 'bjfk-hg29.yz02':
                mode = 'kwai29'
                prefix = '/media/disk1/fordata/web_server/zhouhuanxiang/'
            else:
                print('new server!')
            with open(os.path.join(prefix, 'patch_csv', csv_filename_map[self.crf]), 'r') as readFile:
            # with open(os.path.join(prefix, 'patch_csv/tmp', csv_filename_map[self.crf]), 'r') as readFile:
                reader = csv.reader(readFile)
                self.patches = list(reader)
                print('total {} patches in rank crf={}'.format(len(self.patches), self.crf))
                if mode == 'kwai29':
                    # self.patches = list(map(lambda x: (x[0].replace('disk5', 'disk1'), x[1], x[2], x[3], ), self.patches))
                    for i in range(len(self.patches)):
                        self.patches[i][0] = self.patches[i][0].replace('disk5', 'disk1')
        
        super(KWAIPATCH, self).__init__(
            args, name=name, train=train, benchmark=benchmark
        )

    def _scan(self):
        if self.train:
            # dataset video frame x y mse
            # /media/disk5/fordata/web_server/zhouhuanxiang/data/HD_UGC_crf35_raw	15390986900	img_00031.png	36	88	2.336950231
            names_lr = list(map(lambda x: os.path.join(x[0], x[1], x[2]), self.patches))
            names_hr = list(map(lambda x: re.sub(r'HD_UGC_crf\d+_raw', 'HD_UGC_raw', x), names_lr))
            offset = list(map(lambda x: [int(x[3]), int(x[4])], self.patches))
            names_lr = [names_lr]
            # print(names_lr)
            # print(names_hr)
            # print(offset)
        else:
            names_hr = sorted(
                glob.glob(os.path.join(self.dir_hr, '*/*' + self.ext[0]))
            )
            names_lr = [[] for _ in self.scale]
            for si, s in enumerate(self.scale):
                names_lr[si] = sorted([i.replace('HD_UGC_raw', 'HD_UGC_crf'+self.crf+'_raw') for i in names_hr])
            if not self.test_only:
                names_hr = names_hr[500:3500:150]
                names_lr[0] = names_lr[0][500:3500:150]
                # names_hr = names_hr[0:50]
                # names_lr[0] = names_lr[0][0:50]
                offset = []
        print("######## KWAIPATCH dataset size {} ########".format(len(names_hr)))
        return names_hr, names_lr, offset

    def _set_filesystem(self, dir_data):
        super(KWAIPATCH, self)._set_filesystem(dir_data)
        # self.dir_hr = os.path.join(self.apath, 'DIV2K_`train`_HR')
        # self.dir_lr = os.path.join(self.apath, 'DIV2K_train_LR_bicubic')
        # if self.input_large: self.dir_lr += 'L'
        self.apath = dir_data
        if self.train:
            self.dir_hr = os.path.join(self.apath, 'HD_UGC_raw')
            self.dir_lr = os.path.join(self.apath, 'HD_UGC_crf'+self.crf+'_raw')
        else:
            self.dir_hr = os.path.join(self.apath, 'HD_UGC_raw_test')
            self.dir_lr = os.path.join(self.apath, 'HD_UGC_crf'+self.crf+'_raw_test')
            # self.dir_hr = os.path.join(self.apath, 'GAME_crf'+self.crf+'_raw_test')
            # self.dir_lr = os.path.join(self.apath, 'GAME_crf'+self.crf+'_raw_test')
        

