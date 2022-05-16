# FaceMask Detection
## Introduction

Implementation of facemask detection with Yolor in PyTorch.

## SetUp

- Download the dataset from Kaggle [https://www.kaggle.com/datasets/andrewmvd/face-mask-detection]
- Clone the Yolor from GitHub repo [https://github.com/WongKinYiu/yolor] into a folder FaceMask_Detection

## Installation
- Install the requirements: pip install -r /yolor-main/requirements.txt

## Required file changes

- Go to ..\FaceMask_Detection\yolor-main\data
    - Create the file **custom.names**:
        - Copy and paste the following classes:
            - without_mask
            - with_mask
            - mask_weared_incorrect
    - Create the yaml file **custom.yaml**:
        - Copy and paste the respective paths and classes:
            - train: ../data/train.txt
            - val: ../data/test.txt
            - names: ['without_mask', 'with_mask', 'mask_weared_incorrect']
    
- Go to ..\FaceMask_Detection\yolor-main\cfg
    - Create the config file **yolor_p6_custom.cfg**:
        - Change the number of classes to 3  → lines: 1614, 1658, 1702, 1746
        - Change the number of filters to 24 → [(number of classes + 5) * 5] → lines: 1605, 1649, 1693, 1737
        - Change the number of filters to 24 → [(number of classes + 5) * 5] → for: # 207, # 208, # 209, # 210 lines:1569, 1573,1577 and 1581 respectively. Keep everything unchanged.

## Data Preparation

- Run process.py in ..\FaceMask_Detection\process.py to resize and save the images to 640 by 640
- Run covert.py in ..FaceMask_Detection\data\annotations\convert.py → Create text annotation files in Yolor format
- Copy the text annotation files to ..\FaceMask_Detection\data\images →  The  images and txt annotation files should be in the same folder

## Training
- Run the train.py → To train the model
- python train.py --batch-size 2 --img 640 640 --data .\data\custom.yaml --cfg .\cfg\yolor_p6_custom.cfg --device 0 --name yolor_p6 --hyp .\data\hyp.scratch.640.yaml --epochs 300
- The batch size and the number of epochs can be changed as required

## Prediction

- The best model saved: \yolor-main\runs\train\yolor_p6\weights\best.pt
- Run the detect.py → python .\detect.py --source .\inference\images\ --cfg .\cfg\yolor_p6_custom.cfg --weights .\yolor-main\runs\train\yolor_p6\weights\best.pt --conf 0.25 --img-size 640 --device 0 --names .\data\custom.names

## Results

The results are as follows:

![Test Image](https://github.com/arkanandi/facemask-detection/blob/ed89a98136ce7aa91f9d15c7a09f1952fb9a2758/yolor-main/inference/images/25.jpg)
*Test Image1*


## Citation

@misc{make ml,
title={Mask Dataset},
url={https://makeml.app/datasets/mask},
journal={Make ML}
}

@article{wang2021you,
  title={You Only Learn One Representation: Unified Network for Multiple Tasks},
  author={Wang, Chien-Yao and Yeh, I-Hau and Liao, Hong-Yuan Mark},
  journal={arXiv preprint arXiv:2105.04206},
  year={2021}
}
