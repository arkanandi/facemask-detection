import glob
import os
import numpy as np
import cv2

current_dir = r"E:/yolor-main/data/images"
copy_dir = r"E:/yolor-main/data/images/"
split_percentage = 20
file_train = open("data/train.txt", "w")
file_test = open("data/test.txt", "w")

counter = 1
index_test = round(852 / split_percentage)  # 852 number of images
IMG_SIZE = 640


for pathAndFile in glob.iglob(os.path.join(current_dir, "*.png")):
    # image name and extension
    title, ext = os.path.splitext(os.path.basename(pathAndFile))
    # image --> resize image
    im = cv2.imread(pathAndFile)
    im_array = np.asarray(im)
    # pad it to 640 640
    padded_image = np.pad(im_array, pad_width=((0, 640 - im_array.shape[0]), (0, 640 - im_array.shape[1]), (0, 0)),
                          mode='constant')
    cv2.imwrite(copy_dir + title + '.png', padded_image)
    # save test and train images
    if counter == index_test:
        counter = 1
        file_test.write(current_dir + "/" + title + ".png" + "\n")
    else:
        file_train.write(current_dir + "/" + title + ".png" + "\n")
        counter = counter + 1


# close the test file
file_test.close()
# close the train file
file_train.close()
