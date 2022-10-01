#!/usr/bin/env python
# coding: utf-8

# In[38]:


#python subplot
#plot 1
import numpy as np
import matplotlib.pyplot as ppt
x=np.array([1,3,5,7])
y=np.array([2,4,6,8])
ppt.subplot(1,2,1)
ppt.plot(x,y)
ppt.grid()
ppt.xlabel("price of a chocolate")
ppt.ylabel("Quantity of chocolate in grams")
ppt.title("Sale overview",color="hotpink")
ppt.show()
#ppt subplot shows that the graph is must plot in first row and first coloum of the table




import numpy as np 
import matplotlib.pyplot as ppt
x=np.array([10,20,30,40])
y=np.array([200,150,300,150])
ppt.grid()
ppt.subplot(1,2,2)
ppt.plot(x,y)
ppt.title("YEAR SALES OIF CHOCOLATE",color="red")
ppt.ylabel("No of chocolate sale per day")
ppt.xlabel("productive ")
ppt.show()


# In[37]:


#Draw 2 plots on top of each other:
import matplotlib.pyplot as ppt 
import numpy as np
x=np.array([1,2,3,4,5,6])
y=np.array([11,12,13,14,15,16])
ppt.grid()
ppt.subplot(2,1,1)
ppt.plot(x,y)
ppt.show()


#plot 2
y=np.array([10,20,30,40,50])
x=np.array([1,2,3,4,5])
ppt.subplot(2,1,2)
ppt.plot(x,y)
ppt.show()


# In[39]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()


# In[47]:


import numpy as np
import matplotlib.pyplot as ppt
x=np.array([2018,2019,2020,2021,2022])
y=np.array([300,150,100,80,120])
ppt.subplot(1,2,1)
ppt.plot(x,y)
ppt.title("SALES OF A SWIFT CAR")
ppt.xlabel("Year")
ppt.ylabel("Number of car sale")
ppt.grid()
ppt.suptitle("car sale in a CITY SHOWROOM")
ppt.show()

#plot#2
x=np.array([2018,2019,2020,2021,2022])
y=np.array([350,290,200,150,330])
ppt.subplot(1,2,2)
ppt.plot(x,y)
ppt.title("SALES OF A Tata CAR")
ppt.xlabel("Year")
ppt.ylabel("Number of car sale")
ppt.grid()
ppt.suptitle("car sale in a CITY SHOWROOM")
ppt.show()





# In[52]:


#code for scatter data
import numpy as np
import matplotlib.pyplot as ppt
x=np.array([1,2,3,4,5,6,7,8,9])
y=np.array([10,20,30,40,50,60,70,80,90])
ppt.scatter(x,y)
ppt.show()


# In[53]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()


# In[56]:


#code for scatter
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()


# In[63]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x,y)


# In[64]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()


# In[65]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.scatter(x,y,s=sizes)
ppt.show()


# In[66]:


x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()


# In[70]:


x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.9)

plt.show()


# In[71]:


import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()


# In[74]:


import matplotlib.pyplot as ppt
import numpy as np
x=np.random.randint(100,size=(120))
y=np.random.randint(100,size=(120))
color=np.random.randint(100,size=(120))
sizes=12*np.random.randint(120,size=(120))
ppt.scatter(x,y, c=color, s=sizes, alpha=1, cmap='nipy_spectral')
ppt.colorbar()
ppt.show()


# In[77]:


x=np.array([3,5,8,6,10])
y=np.array(["a","b","c","d","e"])
ppt.bar(y,x)
ppt.show()


# In[78]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()


# In[79]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()


# In[80]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "hotpink")
plt.show()


# In[81]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.2)
plt.show()


# In[82]:


#barh is used for revesed graph
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x,y,color="red")
plt.show()


# In[88]:


#@historiese
import numpy as np
import matplotlib.pyplot as ppt
y=np.random.normal(10,150,250)
ppt.hist(y,color="pink")
ppt.show()


# In[89]:


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 


# In[97]:


import matplotlib.pyplot as plt
import numpy as np

y=np.array([40,50,60])
my_labels=["apple","mango","bannana"]
plt.pie(y,labels=my_labels)
plt.show()           


# In[100]:


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y,labels=mylabels,startangle = 90)
plt.show()


# In[105]:


#exporing the position data in the system of data
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0, 0.3, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 


# In[109]:


y=np.array([40,45,50,56])
mylabel=["Apples", "Bananas", "Cherries", "Dates"]
mycolor=["red","pink","green","yellow"]
myexplore=[0,0,0,0.4]
plt.pie(y,labels=mylabel,colors=mycolor,explode=myexplore)
plt.show()


# In[113]:


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show()


# In[119]:


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title="Name of the fruits")
plt.show()


# In[ ]:




