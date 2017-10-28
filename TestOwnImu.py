# -*- coding:utf-8 -*-
# Created by steve @ 17-10-28 上午10:10
'''
                   _ooOoo_ 
                  o8888888o 
                  88" . "88 
                  (| -_- |) 
                  O\  =  /O 
               ____/`---'\____ 
             .'  \\|     |//  `. 
            /  \\|||  :  |||//  \ 
           /  _||||| -:- |||||-  \ 
           |   | \\\  -  /// |   | 
           | \_|  ''\---/''  |   | 
           \  .-\__  `-`  ___/-. / 
         ___`. .'  /--.--\  `. . __ 
      ."" '<  `.___\_<|>_/___.'  >'"". 
     | | :  `- \`.;`\ _ /`;.`/ - ` : | | 
     \  \ `-.   \_ __\ /__ _/   .-` /  / 
======`-.____`-.___\_____/___.-`____.-'====== 
                   `=---=' 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
         佛祖保佑       永无BUG 
'''

import numpy as np
import matplotlib.pyplot as plt


from fusion import Fusion

import time
# import utime

if __name__ == '__main__':
    dir_name = '/home/steve/Data/IU/92/'
    imu_data = np.loadtxt(dir_name+ 'imu.txt',
                          delimiter=',')

    fuse = Fusion()

    attitude = np.zeros([imu_data.shape[0],3])

    for i in range(imu_data.shape[0]):
        fuse.update(imu_data[i,1:4],imu_data[i,4:7],imu_data[i,7:10])
        # time.sleep(0.005)
        if i % 200 == 0:
            print("attitude:{:7.3f} {:7.3f} {:7.3f}".format(
                fuse.heading,
                fuse.pitch,
                fuse.roll
            ))
        attitude[i,0] = fuse.heading
        attitude[i,1] = fuse.pitch
        attitude[i,2] = fuse.roll


    imu_data[:,7:10] = attitude/180.0*np.pi
    np.savetxt(dir_name+'imu_att.txt',imu_data,delimiter=',')


    plt.figure()
    plt.title('attitude')
    for i in range(attitude.shape[1]):
        plt.plot(attitude[:,i],'-+',label=str(i))
    plt.grid()
    plt.legend()
    plt.show()
