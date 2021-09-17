import argparse
from setLog import log, orbError
import os
import sys
import cv2
def judgeExitFloder(filename):
    if not os.path.exists(filename):
        log.logger.error(filename+" isn't exit")
        sys.exit()
def orbCalcSimilarity(nameA, nameB, showPicture=False):
    imagePathA = os.path.join(args.file1, nameA)
    imagePathB = os.path.join(args.file2, nameB)
    try:
        img1 = cv2.imread(imagePathA, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(imagePathB, cv2.IMREAD_GRAYSCALE)
        if showPicture:
            cv2.imshow("grayImg1", img1)
    except:
        log.logger.error(nameA + " or " + nameB + " read image failed")
    try:
    #     初始化orb
        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)
        if not len(kp1):
            if nameA in orbFailName:
                return -1
            else:
                orbFailName.append(nameA)
                log.logger.error(nameA+" orb can't detect anyway")
                orbError.logger.error(nameB + " orb can't detect anyway")
            return -1
        if not len(kp2):
            if nameB in orbFailName:
                return -1
            else:
                orbFailName.append(nameB)
                log.logger.error(nameB + " orb can't detect anyway")
                orbError.logger.error(nameB + " orb can't detect anyway")
            return -1
        # 提取并计算特征点
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        # knn筛选结果
        matches = bf.knnMatch(des1, trainDescriptors=des2, k=2)
        # 查看最大匹配点数目
        good = [m for (m, n) in matches if m.distance < 0.75 * n.distance]
        # print(len(good))
        # print(len(matches))
        similary = len(good) / len(matches)
        log.logger.info(nameA + " 与 "+nameB + " 的相似度为：%s"%similary)
        return similary
    except:
        log.logger.error(nameA+" or "+nameB+" orb failed")
        orbError.logger.error(nameA+" or "+nameB+" orb failed")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file1", "-f1", type=str, default="./90", help="first Files to compare")
    parser.add_argument("--file2", "-f2", type=str, default="./0", help="second Files to compare")
    parser.add_argument("--output", "-o", type=str, default="./output", help="output file for compare result")
    args = parser.parse_args()
    log.logger.info("this tool is write by YunXiaoD,if you have questions, please send e-mail 6958653042@qq.com to contact me")
    judgeExitFloder(args.file1)
    judgeExitFloder(args.file2)

    listFileA = os.listdir(args.file1)
    listFileB = os.listdir(args.file2)

    orbFailName = []
    for imageNameA in listFileA:
        for imageNameB in listFileB:
#             orb对比
            orbCalcSimilarity(imageNameA,imageNameB)
