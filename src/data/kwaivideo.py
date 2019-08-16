import os
import glob
from data import srdata

class KWAIVIDEO(srdata.SRData):
    def __init__(self, args, name='KWAIVIDEO', train=True, benchmark=False):
        data_range = [r.split('-') for r in args.data_range.split('/')]
        if train:
            data_range = data_range[0]
        else:
            if args.test_only and len(data_range) == 1:
                data_range = data_range[0]
            else:
                data_range = data_range[1]

        self.begin, self.end = list(map(lambda x: int(x), data_range))
        super(KWAIVIDEO, self).__init__(
            args, name=name, train=train, benchmark=benchmark
        )
        #  modify some cfgs
        self.input_large = True

    def _scan(self):
        # names_hr, names_lr = super(KWAIVIDEO, self)._scan()

        names_hr = sorted(
            glob.glob(os.path.join(self.dir_hr, '*/*' + self.ext[0]))
        )
        print("######## dataset size {} ########".format(len(names_hr)))
        names_lr = [[] for _ in self.scale]
        for f in names_hr:
            # filename, _ = os.path.splitext(os.path.basename(f))
            for si, s in enumerate(self.scale):
                # names_lr[si].append(os.path.join(
                #     self.dir_lr, '{}.png'.format(
                #         filename
                #     )
                # ))
                names_lr[si].append(f.replace('HD_UGC_crf25_raw', 'HD_UGC_crf45_raw'))

        names_hr = names_hr[self.begin - 1:self.end]
        names_lr = [n[self.begin - 1:self.end] for n in names_lr]

        return names_hr, names_lr

    def _set_filesystem(self, dir_data):
        super(KWAIVIDEO, self)._set_filesystem(dir_data)
        # self.dir_hr = os.path.join(self.apath, 'DIV2K_`train`_HR')
        # self.dir_lr = os.path.join(self.apath, 'DIV2K_train_LR_bicubic')
        # if self.input_large: self.dir_lr += 'L'
        self.apath = dir_data
        self.dir_hr = os.path.join(self.apath, 'HD_UGC_crf25_raw')
        self.dir_lr = os.path.join(self.apath, 'HD_UGC_crf45_raw')
        

