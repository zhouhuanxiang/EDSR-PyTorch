import os
import glob
from data import srdata

class REDS(srdata.SRData):
    def __init__(self, args, name='REDS', train=True, benchmark=False):
        data_range = [r.split('-') for r in args.data_range.split('/')]
        if train:
            data_range = data_range[0]
        else:
            if args.test_only and len(data_range) == 1:
                data_range = data_range[0]
            else:
                data_range = data_range[1]

        self.begin, self.end = list(map(lambda x: int(x), data_range))
        super(REDS, self).__init__(
            args, name=name, train=train, benchmark=benchmark
        )
        #  modify some cfgs
        self.input_large = True

    def _scan(self):
        names_hr = sorted(
            glob.glob(os.path.join(self.dir_hr, '*/*' + self.ext[0]))
        )
        names_lr = [[] for _ in self.scale]
        for si, s in enumerate(self.scale):
            names_lr[si] = sorted([i.replace('REDS_crf25_raw', 'REDS_crf45_raw') for i in names_hr])
        if not self.train and not self.test_only:
            names_hr = names_hr[:100]
            names_lr = names_lr[:100]
        print("######## REDS dataset size {} ########".format(len(names_hr)))
        return names_hr, names_lr

    def _set_filesystem(self, dir_data):
        super(REDS, self)._set_filesystem(dir_data)
        # self.dir_hr = os.path.join(self.apath, 'DIV2K_`train`_HR')
        # self.dir_lr = os.path.join(self.apath, 'DIV2K_train_LR_bicubic')
        # if self.input_large: self.dir_lr += 'L'
        self.apath = dir_data
        if self.train:
            self.dir_hr = os.path.join(self.apath, 'REDS_crf25_raw')
            self.dir_lr = os.path.join(self.apath, 'REDS_crf45_raw')
        else:
            self.dir_hr = os.path.join(self.apath, 'REDS_crf25_raw_test')
            self.dir_lr = os.path.join(self.apath, 'REDS_crf45_raw_test')
        
