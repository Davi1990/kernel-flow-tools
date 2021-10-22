# -*- coding: utf-8 -*-
r"""
=================================
SNIRF HbM GLM Analysis
=================================


"""  

# sphinx_gallery_thumbnail_number = 1

# %%
# Importage
# --------------------------------------------------

# KF Tools and related imports
from kftools.data import fetch_file
from kftools.snirf import snirf_task_ana,plot_glm_contrast_topo


# %%
# Grab the data
# --------------------------------------------------

data_dir='.'
 
fetch_file(data_dir=data_dir, filetype='kp-snf-hbm',
           site='snic', task='ft', subid='sub001', sesid='ses02')


# %%
# Specify and run the GLM model
# ---------------------------------------------------

#f = 'snic_sub001_ft_ses02_0917-1313_kp-snf-hbm.snirf'
f = 'snic_sub001_ft_ses01_0909-1523_kp-snf-hbm.snirf'

res = snirf_task_ana(f)

res.keys()


# %%
# Look at GLM results
# ---------------------------------------------------

#glmest = res['glm_est']
#contrst = res['estmrg_LgtR']
#con = contrst.data

glmest = res['glm_est']
con = res['contrast_LgtR'].data
disp = plot_glm_contrast_topo(glmest, con,sphere='auto')