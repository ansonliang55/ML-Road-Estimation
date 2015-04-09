"""
Written by: Wenjie Zi

This is the handler of benchmark
"""
import numpy as np
#@input: start time and end time
#@output: the last of the time

def countTime(startTime, endTime):
    lastTime = endTime - startTime
    print ('Time used: %f')%lastTime
    return lastTime

#@input: 2D result of the prediction
#        2D labels
#@output: the probility of accuracy in superpixel level

def accuracyOfSuperpixels(file_num,valid_files, valid_data, clf, valid_labels):
    count_correct=0
 #   print valid_files.shape
    indices = []
    for i in range(0, valid_files.shape[0]):
        if valid_files[i] == file_num:
                indices.append(i)
    indices = np.array(indices)
    total_samples = indices.shape[0]
    print "total_samples: %d"%total_samples
    for i in range(0,total_samples):
        if clf.predict(valid_data[indices[i]]) == valid_labels[indices[i]]:
                count_correct+=1
    print ('Validation Accuracy (Superpixel level): %2.2f%%')%(100.0*count_correct/total_samples)
    return 100.0*count_correct/total_samples
#@input: 2D result of the prediction
#        2D labels
#@output: the probility of accuracy in pixel level
def accuracyOfPixels(file_num,valid_files, superpixels, valid_data, clf, valid_pixels_labels):
    count_correct = 0
    total_count = 0
    indicess = []
    for i in range(0, valid_files.shape[0]):
        if valid_files[i] == file_num:
                indicess.append(i)
    indicess = np.array(indicess)
    total_samples = indicess.shape[0]
    for i in range(0,total_samples):
        temp = np.array(superpixels[file_num][0])
 #       index = []
        temp2 = np.array(valid_pixels_labels[file_num][0])
        index = np.where(temp2 == i)
#        for j in range(0, temp.shape[0]):
#            for k in range(0, temp.shape[1]):
#               if temp[j][k] == i:
#                    index.append([j,k])
        index = np.array(index)
        total_count = total_count + index.shape[0]
        predict_result = clf.predict(valid_data[indicess[i]])
        for j in range(0,index.shape[0]): 
            if predict_result == temp2[index[j][0]][index[j][1]]:
               count_correct+=1
    print ('Validation Accuracy (Pixel level): %2.2f%%')%(100.0*count_correct/total_count)