Youtube link: https://youtu.be/SFiIGIefw1Y

###### Number of filters
By increasing the number of filters for convolutional layers from 32 to 100, it significantly increased the proccessing time of the AI. From 12ms/step to an average of 44ms/step. The increment of the number of filters does not seem to increase the test accuracy significantly as well (0.0535 to 0.0559). 
###### Size of kernal
Increasing the size of the kernal from 3x3 to 7x7 significantly increased the training accuracy as well as testing accuracy (0.0535 to 0.8445) without affecting the processing time.

###### Size of hidden layers
Increasing the size of hidden layer from 128 to 300 greatly increased the training and testing accuracy from 0.0535 to 0.7567. This increment also affected the processing time from 12ms/step to 21ms/step.

###### Number of hidden layers

Increasing the number of hidden layer from 1 to 3 also increased the training and testing accuracy from 0.0535 to 0.4865 and it did not affect the processing time

###### Pool Size

Increasing pool size from 2x2 to 5x5 did not affect the testing accuracy but significantly reduces the processing speed from 12ms/step to 6ms/step.


###### Experimentation
Since we found out that increasing the number of hidden layer and size of kernal increses the training accuracy without affecting the processing time, i have increased both of them together (7x7 and 3layers) and got a testing accuracy of 0.9129 and processing time of 13ms/step. 
Since we have such an high accuracy, we can try to reduce the processing time by increasing the pool size from 2x2 to 5x5. However, it slightly reduced the testing accuracy to 0.8568 and processing time to 9ms/step. This result is expected because increasing pool size reduces the amount of features the AI needs to learn which increases processing time but it might remove some important feature as well, hence the reduction in accuracy. 
Overall training a neural network is trying to find the optimal tradeoff between accuracy and processing speed. 
