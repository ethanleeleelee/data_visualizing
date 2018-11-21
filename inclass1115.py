#!/usr/bin/env python
# coding: utf-8

# In[7]:


from bokeh.io import output_notebook, push_notebook, show
from bokeh.plotting import figure, output_file, show

p = figure(plot_width = 400, plot_height = 400)
p.line([1,2,3,4,5],[5,4,3,2,1], line_width = 2)
show(p)
output_notebook()
#output_file("line.html")


# In[13]:


from bokeh.io import output_notebook, push_notebook, show
from bokeh.plotting import figure, output_file, show

p = figure(plot_width = 400, plot_height = 400)
p.step([1,2,3,4,5],[5,3,2,4,3], line_width = 2, mode="after")
show(p)
output_notebook()


# In[15]:


#陣列取物
a = [[1,2,3],[4,5,6]]
a[1][1]


# In[18]:


from bokeh.io import output_notebook, push_notebook, show
from bokeh.plotting import figure, output_file, show

p = figure(plot_width = 400, plot_height = 400)
p.multi_line([[1,3,2],[1,4,6,6]], [[2,1,4],[4,7,8,5]], color = ["navy","gold"], alpha = [0.4,0.8], line_width = [4,2])
show(p)
output_notebook()


# In[19]:


from bokeh.plotting import figure, output_file, show

p = figure(plot_width = 400, plot_height = 400)
p.square([1,3,5,7,9],[2,4,6,8,10], size = 20, color = "navy", alpha = 1.2)
show(p)
output_notebook()


# In[20]:


from bokeh.plotting import figure, output_file, show

p = figure(plot_width = 400, plot_height = 400)
p.circle([1,3,5,7,9],[10,7,5,7,10], size = 20, color = "navy", alpha = 1.2)
show(p)
output_notebook()


# In[41]:


import pprint
import pymysql.cursors
pp = pprint.PrettyPrinter(indent=4)

connection = pymysql.connect(host="localhost",
                            user="root",password="mpyhacct012",db="technews",
                            charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    sql = "SELECT `*` FROM `technews`.`articles` WHERE `share` between 50 and 100"
    cursor.execute(sql)
    results = cursor.fetchall()
#pp.pprint(result)
#print(result)


datas = []
index = []
count = 1
for result in results:
    datas.append(result["share"])
    index.append(count)
    count += 1
print(datas)
print(index)


from bokeh.io import output_notebook, push_notebook, show
from bokeh.plotting import figure, output_file, show

p = figure(plot_width = 400, plot_height = 400)
p.line(index, datas, line_width = 2, color = "navy")
show(p)
output_notebook()

connection.close

    


# In[10]:


import pprint
import pymysql.cursors
pp = pprint.PrettyPrinter(indent=4)

connection = pymysql.connect(host="localhost",
                            user="root",password="mpyhacct012",db="technews",
                            charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    sql = "SELECT `*` FROM `technews`.`ptt_crawler`"
    cursor.execute(sql)
    results = cursor.fetchall()
#pp.pprint(results)

datas=[]
index=[]
count = 0

for result in results:
    datas.append(result["push"])
    count += 1
    index.append(count)
"""
print(datas)
print(index)
"""

from bokeh.io import output_notebook, push_notebook, show
from bokeh.plotting import figure, output_file, show

p = figure(plot_width = 800, plot_height = 800)
p.vbar(x = index, width = 0.5, bottom = 0, top = datas, color = "navy")
show(p)
output_notebook()

connection.close


# In[ ]:




