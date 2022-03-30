#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import random
random.seed(43)


import matplotlib.pyplot as plt


# In[ ]:


np.random.seed(43)
a = np.random.randn(1000,4)
a


# In[ ]:


np.random.seed(43)
b = np.random.randn(1000,4)
b


# In[ ]:


np.random.seed(43)
c = np.random.randn(1000,1)
c


# In[ ]:


class nn(object):
    """
    Class constructor.
    """
    def __init__(self,x0:np.ndarray,y0:np.ndarray,lr:float=0.001,n_iters:int=1000):
        """
        Constructor method.
        """
        self.x0 = x0
        self.y0 = y0
        assert(type(x0)==np.ndarray and type(y0)==np.ndarray)
        
        
        
        self.lr = lr
        self.n_iters = n_iters
        
        
        self.m, self.n = np.shape(self.x0)[0], np.shape(self.x0)[1]
    
        self.w = np.random.randn(self.n,1)
        self.b = 0
        
        
    
    
    def create_array(self):
        """Creates a list
        :return:
        :rtype: list
        """
        
        self.array = []
        
        return self.array
    
    
    
    
    def sigmoid(self,z):
        """Non-linear activation function.
        :return: 
        :rtype: 
        """
        return 1/(1+np.exp(-z))
    
    
    
    
    def forward_propagate_vectorised(self):
        """Forward propagation. Vectorised Implementation.
        :return: 
        :rtype: 
        """
        
        if np.shape(self.x0)[1] == np.shape(self.w)[0]:
            
            A = self.sigmoid(np.matmul(self.x0,self.w)+self.b)
            
            if np.shape(A) == (np.size(A,0),np.size(self.w,1)):
            
            
                cost = (-1/self.m)*np.sum(self.y0*np.log(A)+(1-self.y0)*(np.log(1-A)))
            
            
                d_w = (1/self.m)*np.matmul(self.x0.T,(A-self.y0))
                d_b = (1/self.m)*np.sum(A-self.y0)
        
            
                gradients = {
                        "d_w":d_w,
                        "d_b":d_b
                    }
                
            
            else:
                print(f"must be of shape ({np.size(A,0)},{np.size(self.w,1)})")
                
        else:
            
            print(f"{np.shape(self.x0)[1]} not equal to {np.shape(self.w)[0]}")
        
        
        
        return cost, gradients
    
    
    
    
    
    def forward_propagate_not_vectorised(self):
         """Forward propagation. Non-Vectorised Implementation.
        :return: 
        :rtype: 
        """
            
        h = np.zeros((1000,1))
        
        for i in range(len(self.x0)):
        
            for j in range(len(self.w[0])):
        
                for k in range(len(self.w)):
        
                    h[i][j] += self.x0[i][k]*self.w[k][j]
        
        B = self.sigmoid(h + self.b)
        
        
        #calculate cost using a for loop
        
        c_m = 0
        
        for z in range(self.m):
            
            c_m += (self.y0[z]*np.log(B[z])+(1-self.y0[z])*(np.log(1-B[z])))
        
        cost = (-1/self.m)*c_m
        
        cost = float(cost)
        
        
        
        
        
        d_w1 = (1/self.m)*np.matmul((self.x0).T,(B-self.y0))
        
        
        
        
        d_b1 = 0
        
        for e in range(self.m):
            
            d_b1 += B[e]-self.y0[e]
        
        d_b1 = (1/self.m)*d_b1
        
        d_b1 = float(d_b1)
        
        
        
        gradients = {
                "d_w1":d_w1,
                "d_b1":d_b1
            }
        
        return cost, gradients
    
    
    
    
    def gradient_descent(self):
        """The below functions runs gradient descent.
        :return: Optimal parameters w,b
        :rtype: np.array
        """
        
        costs = self.create_array()
        
            
        for i in range(self.n_iters):
            
            c,g = self.forward_propagate_vectorised()
            
            self.w = self.w - self.lr*g["d_w"]
            self.b = self.b - self.lr*g["d_b"]
    
            costs.append(c)
            
            if i % 100 ==0:
                print(f"Costs after iter {i}:{c}")
        
        params = {
            "w": self.w,
            "b": self.b
            }
        
        plt.plot(costs)
        
        return params


# In[ ]:


neural_nets = nn(a,c,0.005,2500)


# In[ ]:


neural_nets.forward_propagate_vectorised()


# In[ ]:


neural_nets.forward_propagate_not_vectorised()


# In[ ]:


neural_nets.gradient_descent()


# In[ ]:





# In[ ]:




