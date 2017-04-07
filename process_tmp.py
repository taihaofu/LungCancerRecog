import numpy as np
import os
import pretrain_mx
from multiprocessing import Pool
from functools import partial

mid_npy_folder = "./out_origin"
thread_num = 8
out_folder = "./out_origin_feat"

def process(pretrained_model, patient_id):
    patient_data = np.load("%s/%s.npy" % (mid_npy_folder, patient_id))
    pretrain_mx.calc_features(pretrained_model, patient_id, patient_data, out_folder)
    print("INFO: Saving segmented feature of patient %s ... ..." % patient_id)
    print "=============================================================="


patients = [ s[:-4] for s in os.listdir(mid_npy_folder) ]
pretrained_model = pretrain_mx.get_extractor()
func = partial(process, pretrained_model)
pool = Pool(thread_num)
pool.map(func, patients)
