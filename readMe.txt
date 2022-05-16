Required file changes:

• Go to ..\FaceMask_Detection\yolor-main\data
• Create custom.names:
    o Copy and paste the following classes:
        ▪ without_mask
        ▪ with_mask
        ▪ mask_weared_incorrect

o Create custom.yaml
o Copy and paste the respective paths and classes:
    ▪ train: ../data/train.txt
    ▪ val: ../data/test.txt
    ▪ names: ['without_mask', 'with_mask', 'mask_weared_incorrect']

• Go to ..\FaceMask_Detection\yolor-main\cfg
    o Create yolor_p6_custom.cfg
        ▪ Change the number of classes to 3 → lines: 1614, 1658, 1702, 1746
        ▪ Change the number of filters to 24 → [(number of classes + 5) * 5] → lines: 1605, 1649, 1693, 1737
        ▪ Change the number of filters to 24 → [(number of classes + 5) * 5] → for: # 207, # 208, # 209, # 210

Data Preparation:

• Run process.py in ..\FaceMask_Detection\process.py to resize and save the images to 640 by 640
• Run covert.py in ..\FaceMask_Detection\data\annotations\convert.py → Create text annotation files
• Copy the text annotation files to ..\FaceMask_Detection\data\images

Training:
Run the train.py → To train the model
    • Model → Yolor
    • python train.py --batch-size 2 --img 640 640 --data .\data\custom.yaml --cfg .\cfg\yolor_p6_custom.cfg --device 0 --name yolor_p6 --hyp .\data\hyp.scratch.640.yaml --epochs 300

Prediction:
    • Model/weights saved: \yolor-main\runs\train\yolor_p6\weights\best.pt
    • Run the detect.py → python .\detect.py --source .\inference\images\ --cfg .\cfg\yolor_p6_custom.cfg --weights .\yolor-main\runs\train\yolor_p6\weights\best.pt --conf 0.25 --img-size 640 --device 0 --names .\data\custom.names



Dataset download:

@misc{make ml,
title={Mask Dataset},
url={https://makeml.app/datasets/mask},
journal={Make ML}
}

Yolor:

@article{wang2021you,
  title={You Only Learn One Representation: Unified Network for Multiple Tasks},
  author={Wang, Chien-Yao and Yeh, I-Hau and Liao, Hong-Yuan Mark},
  journal={arXiv preprint arXiv:2105.04206},
  year={2021}
}
