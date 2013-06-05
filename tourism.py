import wx

import MySQLdb
db = MySQLdb.connect(host = "localhost",
                             user="root",
                             passwd = "",
                             db = "test")

class bucky(wx.Frame):
    
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Tracking Tourism Inflow in Nepal',size=(1500,1000))
        panel=wx.Panel(self)
        btnYoT=wx.Button(panel,label="Yearwise Total Visits",pos=(25,10),size=(250,40))
        btnYoTc=wx.Button(panel,label="Countrywise Total Visits",pos=(25,60),size=(250,40))
        btnCoTy=wx.Button(panel,label="Yearwise Total Visits of Countries",pos=(25,110),size=(250,40))
#        button2=wx.Button(panel,label="Age Group-wise Call Duration Distribution",pos=(1,31),size=(500,30))
#        button3=wx.Button(panel,label="Gender-wise Subscriber Distribution",pos=(1,61),size=(500,30))
#        button4=wx.Button(panel,label="Age-wise Subscriber Distribution",pos=(1,91),size=(500,30))
#        button5=wx.Button(panel,label="Age-group-wise Subscriber Distribution",pos=(1,121),size=(500,30))
#        button6=wx.Button(panel,label="Frequency Distribution of Number of Calls",pos=(1,151),size=(500,30))
#        button7=wx.Button(panel,label="Frequency Distribution of Time of Day of Calls",pos=(1,181),size=(500,30))
#        button8=wx.Button(panel,label="Frequency Distribution of Business/Non-Business Calls",pos=(1,211),size=(500,30))
#        button9=wx.Button(panel,label="Frequency Distribution of Calls in Day of Week",pos=(1,241),size=(500,30))
#        button10=wx.Button(panel,label="Frequency Distribution of Date-wise Calls",pos=(1,271),size=(500,30))
#        button11=wx.Button(panel,label="Frequency Distribution of Calls in 24 Hour",pos=(1,301),size=(500,30))
#        button12=wx.Button(panel,label="Age group and Gender-wise Subscriber Distribution",pos=(1,331),size=(500,30))
        self.Bind(wx.EVT_BUTTON,self.btnYoT,btnYoT)
        self.Bind(wx.EVT_BUTTON,self.btnYoTc,btnYoTc)
        self.Bind(wx.EVT_BUTTON,self.btnCoTy,btnCoTy)
#        self.Bind(wx.EVT_BUTTON,self.piebutton,button2)
#        self.Bind(wx.EVT_BUTTON,self.query1,button3)
#        self.Bind(wx.EVT_BUTTON,self.query2,button4)
#        self.Bind(wx.EVT_BUTTON,self.query3,button5)
#        self.Bind(wx.EVT_BUTTON,self.query4,button6)
#        self.Bind(wx.EVT_BUTTON,self.query5,button7)
#        self.Bind(wx.EVT_BUTTON,self.query6,button8)
#        self.Bind(wx.EVT_BUTTON,self.query7,button9)
#        self.Bind(wx.EVT_BUTTON,self.query8,button10)
#        self.Bind(wx.EVT_BUTTON,self.query9,button11)
#        self.Bind(wx.EVT_BUTTON,self.query10,button12)
        self.Bind(wx.EVT_CLOSE,self.closewindow)
                
    def btnYoT(self,event):
        #self.Close(True)
        
        year = []
        tot_yr =  []
                
        cursor2 = db.cursor()
        cursor2.execute("select year,sum(value) from trst_inflow group by year")
        numrows2 = int(cursor2.rowcount)
        
        for x in range(numrows2):
            row2 = cursor2.fetchone()
            year.append(row2[0])
            tot_yr.append(row2[1])
            
        cursor2.close()
        
        import matplotlib.pyplot as plt2
        plt2.figure(figsize = (10,10))
        plt2.xlabel("Year",fontdict={'fontsize':15})
        plt2.ylabel("Number of tourists",fontdict={'fontsize':15}) 
        plt2.plot(year,tot_yr,color='green', linestyle='solid',linewidth=5, marker='o',markerfacecolor='blue', markersize=12)
        plt2.title("Total number of tourists visiting Nepal from 2001-2011")
        plt2.show()
        
    def btnYoTc(self,event):
        #self.Close(True)
        cntry='none'
        country = ['Australia','Austria','Canada','China','Denmark','France','Germany','India','Italy','Japan','Netherlands','Spain','Switzerland','Srilanka','USA','UK','Others','NotSpecified']
        modal=wx.SingleChoiceDialog(None,"Select a country","Countries",country)
        if modal.ShowModal()==wx.ID_OK:
            cntry=modal.GetStringSelection()
        year = []
        tot_yr =  []
        
        if cntry!='none':        
            cursor2 = db.cursor()
            cursor2.execute("select year,value from trst_inflow where country='"+cntry+"'")
            numrows2 = int(cursor2.rowcount)
            
            for x in range(numrows2):
                row2 = cursor2.fetchone()
                year.append(row2[0])
                tot_yr.append(row2[1])
            
            
        tot_yr2 =  []
                
        cursor2.execute("select year,sum(value) from trst_inflow group by year")
        numrows2 = int(cursor2.rowcount)
        
        for x in range(numrows2):
            row2 = cursor2.fetchone()
            tot_yr2.append(row2[1])
        
        import matplotlib.pyplot as plt2
        plt2.figure(figsize = (10,10))
        plt2.xlabel("Year",fontdict={'fontsize':15})
        plt2.ylabel("Number of tourists",fontdict={'fontsize':15}) 
        plt2.plot(year,tot_yr,color='green', linestyle='solid',linewidth=5, marker='o',markerfacecolor='blue', markersize=12)
        plt2.plot(year,tot_yr2,color='red', linestyle='solid',linewidth=5, marker='o',markerfacecolor='blue', markersize=12)
        plt2.title("Total number of tourists of "+cntry+" visiting Nepal from 2001-2011")
        plt2.legend([cntry, 'Total'], loc='upper left')
        plt2.show()
    
    def btnCoTy(self,event):
        #self.Close(True)
        selY='-1'
        first=2001
        yr=[]
        while first<2012:
            yr.append(str(first))
            first=first+1
            print yr
        modal=wx.SingleChoiceDialog(None,"Select year","Years",yr)
        if modal.ShowModal()==wx.ID_OK:
            selY=modal.GetStringSelection()
            print selY
           
        #country=[] 
        country = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        cl=[]
        tot_cr =  []
        
        if selY!='-1':        
            cursor2 = db.cursor()
            cursor2.execute("select country,value from trst_inflow where year="+selY)
            numrows2 = int(cursor2.rowcount)
            
            for x in range(numrows2):
                row2 = cursor2.fetchone()
                cl.append(row2[0])
                tot_cr.append(row2[1])
            
            
        
        
        
        
        import matplotlib.pyplot as plt2
        fig=plt2.figure()
#        figsize = (10,10)
        ax = fig.add_subplot(1,1,1,)
#        n, bins, patches = ax.hist(measurements, bins=50, range=(graph_minimum, graph_maximum), histtype='bar')
        ax.set_xticks(range(1,18))
        ax.set_xticklabels(cl, rotation='vertical')
        plt2.xlabel("Year",fontdict={'fontsize':15})
        plt2.ylabel("Number of tourists",fontdict={'fontsize':15}) 
        plt2.plot(country,tot_cr,color='green', linestyle='solid',linewidth=5, marker='o',markerfacecolor='blue', markersize=12)
        plt2.title("Total number of tourists of different countries visiting Nepal in year "+selY)
        plt2.legend(["Year "], loc='upper left')
        plt2.show()
    
#    def piebutton(self,event):
#        age = ['below 20', '20-22','22-24','24-26','26-28','28-30','30-40','above 40']
#        avg_call_group =  [0, 0, 0, 0, 0, 0, 0, 0]
#                
#        cursor = db.cursor()
#        
#        cursor.execute("select p.age_group,sum(c.avg_duration) as age_avg_dur from demo p,(select  substring(trim(leading ' ' from card_no),4) as card_n, avg(duration) as avg_duration from call_details where service_key = 1 and card_no =calling_no group by card_no) as c where p.card_no = c.card_n group by p.age_group ")
#        numrows = int(cursor.rowcount)
#        
#        for x in range(numrows):
#            row = cursor.fetchone()
#            avg_call_group[x] =  row[1]
#        
#        cursor.close()
#        import matplotlib as mp
#        import matplotlib.pyplot as plt1
#        mp.rcParams['text.color'] = 'purple'
#        #mp.rcParams['lines.linewidth'] = 10
#        plt1.figure(figsize = (15,15))
#        exploding = [.90, .00, .00, .00 , .00, .00, .00, .00]
#        age = ['below 20', '20-22','22-24','24-26','26-28','28-30','30-40','40-50']
#        #figure = plot.figure()
#        #axis.pie(avg_call_group, labels=age)
#        #plt1.legend(title='Age-group wise call duration distribution')
#        plt1.pie(avg_call_group, labels= age, autopct='%1.3f%%', explode = exploding)
#        plt1.legend(age,title='Age-group wise call duration distribution', loc='lower right')
#        plt1.show()  
#     
#    def query1(self,event):
#        #self.Close(True)
#        gender = [0,1]
#        count =  [0,0]
#        
#        cursor2 = db.cursor()
#        cursor2.execute("select count(card_no) from demo group by gender")
#        numrows2 = int(cursor2.rowcount)
#        print numrows2
#        
#        for x in range(numrows2):
#            row2 = cursor2.fetchone()
#            count[x] =  row2[0]
#        
##        print "Males="+str(count[0])
##        print "Females="+str(count[1])
##        print "Totals:"+str(count[0]+count[1])
#        
#        cursor2.close()
#        import numpy as np
#        import matplotlib.pyplot as plt2
#        N = len(gender)
#        ind = np.arange(N) 
#        ax = plt2.figure(figsize = (6,6))
#        p = ax.add_subplot(111)
#        p.set_xticks(ind)
#        p.set_xticklabels(('male','female'))
##        plt2.xlabel("Gender(0 is male)",fontdict={'fontsize':15})
#        plt2.ylabel("Count",fontdict={'fontsize':15})
#        plt2.bar(gender,count,width=0.2,align='center')
#        plt2.show()   
#          
#    def query2(self,event):
#        #self.Close(True)
#        age = []
#        count = []
#        
#        cursor2 = db.cursor()
#        cursor2.execute("select count(card_no),age from demo group by age")
#        numrows2 = int(cursor2.rowcount)
#        
#        tot=0
#        for x in range(numrows2):
#            row2 = cursor2.fetchone()
#            if row2[1]>0:
#                age.append(row2[1])
#                count.append(row2[0])
#            tot+=row2[0] 
#        
#        print tot
#        
##        print "Males="+str(count[0])
##        print "Females="+str(count[1])
##        print "Totals:"+str(count[0]+count[1])
#        
#        cursor2.close()
#        
#        import matplotlib.pyplot as plt2
#        plt2.figure(figsize = (7,7))
#        plt2.xlabel("Age",fontdict={'fontsize':15})
#        plt2.ylabel("Count",fontdict={'fontsize':15})
#        plt2.bar(age,count,width=0.3,align='center')
#        plt2.show()
#        
#    def query3(self,event):
#        #self.Close(True)
#        age_gr = []
#        count = []
#        
#        cursor2 = db.cursor()
#        cursor2.execute("select count(card_no) from demo group by age_group")
#        numrows2 = int(cursor2.rowcount)
#        
#        tot=0
#        for x in range(numrows2):
#            row2 = cursor2.fetchone()
#            age_gr.append(x)
#            count.append(row2[0])
#            tot+=row2[0] 
#        
#        print tot
#        
##        print "Males="+str(count[0])
##        print "Females="+str(count[1])
##        print "Totals:"+str(count[0]+count[1])
#        
#        cursor2.close()
#        
#        import matplotlib.pyplot as plt2
#        plt2.figure(figsize = (4,4))
#        plt2.xlabel("Age Group",fontdict={'fontsize':15})
#        #  \n0:under 16 \n 1:16-20 \n i(<-N):16+5i-20+5i (i<4) \n 5:35-40 \n 6:40-50 \n 7:50 over
#        plt2.ylabel("Count",fontdict={'fontsize':15})
#        plt2.bar(age_gr,count,width=0.3,align='center')
#        plt2.show()
#          
#    def query4(self,event):
#        #self.Close(True)
#        calls = []
#        count = []
#        
#        cursor2 = db.cursor()
#        cursor2.execute("select count(card_no),ceil(duration/30) from fact_table group by ceil(duration/30)")
#        numrows2 = int(cursor2.rowcount)
#        
#        tot=0
#        temp=0
#        for x in range(numrows2):
#            row2 = cursor2.fetchone()
#            if int(row2[1])>(15*2):
#                calls.append(35)
#                temp+=row2[0]
#                count.append(temp)
#            else:
#                calls.append(int(row2[1]))
#                count.append(row2[0])
#                tot+=row2[0] 
#        
#        print tot
#        
##        print "Males="+str(count[0])
##        print "Females="+str(count[1])
##        print "Totals:"+str(count[0]+count[1])
#        
#        cursor2.close()
#        
#        import matplotlib.pyplot as plt2
#        plt2.figure(figsize = (7,7))
#        plt2.xlabel("Calls",fontdict={'fontsize':15})
#        plt2.ylabel("Count",fontdict={'fontsize':15})
#        plt2.bar(calls,count,width=0.3,align='center')
#        plt2.show()
#          
#    def query5(self,event):
#        #self.Close(True)
#        time_of_day = []
#        count = []
#        
#        cursor2 = db.cursor()
#        cursor2.execute("select count(card_no) from fact_table group by time_of_day")
#        numrows2 = int(cursor2.rowcount)
#        
#        tot=0
#        temp=0
#        for x in range(numrows2):
#            row2 = cursor2.fetchone()
#            time_of_day.append(x)
#            count.append(row2[0])
#            tot+=row2[0] 
#        
#        print tot
#        
##        print "Males="+str(count[0])
##        print "Females="+str(count[1])
##        print "Totals:"+str(count[0]+count[1])
#        
#        cursor2.close()
#        
#        import matplotlib.pyplot as plt2
#        plt2.figure(figsize = (7,7))
#        plt2.xlabel("Time of Day",fontdict={'fontsize':15})
#        plt2.ylabel("Count",fontdict={'fontsize':15})
#        plt2.bar(time_of_day,count,width=0.3,align='center')
#        plt2.show()
#        
#    def query6(self,event):
#        #self.Close(True)
#        busy_hr = []
#        count = []
#        
#        cursor2 = db.cursor()
#        cursor2.execute("select count(card_no) from fact_table group by IsBusinessHr")
#        numrows2 = int(cursor2.rowcount)
#        
#        tot=0
#        temp=0
#        for x in range(numrows2):
#            row2 = cursor2.fetchone()
#            busy_hr.append(x)
#            count.append(row2[0])
#            tot+=row2[0] 
#        
#        print tot
#        
##        print "Males="+str(count[0])
##        print "Females="+str(count[1])
##        print "Totals:"+str(count[0]+count[1])
#        
#        cursor2.close()
#        
#        import matplotlib.pyplot as plt2
#        plt2.figure(figsize = (7,7))
#        plt2.xlabel("Is Business Hour?",fontdict={'fontsize':15})
#        plt2.ylabel("Count",fontdict={'fontsize':15})
#        plt2.bar(busy_hr,count,width=0.3,align='center')
#        plt2.show()
#        
#    def query7(self,event):
#        #self.Close(True)
#        day_of_week = []
#        count = []
#        
#        cursor2 = db.cursor()
#        cursor2.execute("select count(card_no) from fact_table group by Day_of_week")
#        numrows2 = int(cursor2.rowcount)
#        
#        tot=0
#        temp=0
#        for x in range(numrows2):
#            row2 = cursor2.fetchone()
#            day_of_week.append(x)
#            count.append(row2[0])
#            tot+=row2[0] 
#        
#        print tot
#        
##        print "Males="+str(count[0])
##        print "Females="+str(count[1])
##        print "Totals:"+str(count[0]+count[1])
#        
#        cursor2.close()
#        
#        import matplotlib.pyplot as plt2
#        plt2.figure(figsize = (7,7))
#        plt2.xlabel("Day of Week",fontdict={'fontsize':15})
#        plt2.ylabel("Count",fontdict={'fontsize':15})
#        plt2.bar(day_of_week,count,width=0.3,align='center')
#        plt2.show()
#        
#    def query8(self,event):
#        #self.Close(True)
#        day = []
#        count = []
#        
#        cursor2 = db.cursor()
#        cursor2.execute("select count(card_no) from fact_table group by Day")
#        numrows2 = int(cursor2.rowcount)
#        
#        tot=0
#        temp=0
#        for x in range(numrows2):
#            row2 = cursor2.fetchone()
#            day.append(x+1)
#            count.append(row2[0])
#            tot+=row2[0] 
#        
#        print tot
#        
##        print "Males="+str(count[0])
##        print "Females="+str(count[1])
##        print "Totals:"+str(count[0]+count[1])
#        
#        cursor2.close()
#        
#        import matplotlib.pyplot as plt2
#        plt2.figure(figsize = (7,7))
#        plt2.xlabel("Day",fontdict={'fontsize':15})
#        plt2.ylabel("Count",fontdict={'fontsize':15})
#        plt2.bar(day,count,width=0.3,align='center')
#        plt2.show()
#        
#    def query9(self,event):
#        #self.Close(True)
#        fiveBit = []
#        count = []
#        
#        cursor2 = db.cursor()
#        cursor2.execute("select count(card_no) from fact_table group by (time_8bit-Mod(time_8bit,1000))/1000")
#        numrows2 = int(cursor2.rowcount)
#        print numrows2
#        
#        tot=0
#        for x in range(numrows2):
#            row2 = cursor2.fetchone()
#            fiveBit.append(x)
#            count.append(row2[0])
#            tot+=row2[0] 
#        
#        print tot
#        
##        print "Males="+str(count[0])
##        print "Females="+str(count[1])
##        print "Totals:"+str(count[0]+count[1])
#        
#        cursor2.close()
#        
#        import matplotlib.pyplot as plt2
#        plt2.figure(figsize = (7,7))
#        plt2.xlabel("Hours in Binary",fontdict={'fontsize':15})
#        plt2.ylabel("Count",fontdict={'fontsize':15})
#        plt2.bar(fiveBit,count,width=0.3,align='center')
#        plt2.show()
#    
#    def query10(self,event):
#        age_gr = []
#        countm = []
#        countf = []
#        
#        cursor1 = db.cursor()
#        cursor2 = db.cursor()
#        
#        cursor1.execute("select count(card_no) from demo  where gender = 0 group by age_group")
#        cursor2.execute("select count(card_no) from demo  where gender = 1 group by age_group")
#        
#        numrows1 = int(cursor1.rowcount)
#        #numrows2 = int(cursor2.rowcount)
#        
#        for x in range(numrows1):
#            row1 = cursor1.fetchone()
#            age_gr.append(x)
#            countm.append(row1[0])
#            row2 = cursor2.fetchone()
#            countf.append(row2[0])
#        #    avg_call_group[x] =  row[1]    
#        
#        
#        cursor1.close()
#        cursor2.close()
#        
#        
#        import numpy as np
#        import matplotlib.pyplot as plt
#        
#        #N = 5
#        #menMeans = [20, 35, 30, 35, 27]
#        #menStd =   [2, 3, 4, 1, 2]
#        
#        N = len(age_gr)
#        
#        ind = np.arange(N)  # the x locations for the groups
#        
#        width = 0.35       # the width of the bars
#        
#        fig = plt.figure()
#        ax = fig.add_subplot(111)
#        rects1 = ax.bar(ind, countf, width, color='b')
#        
#        #womenMeans = (25, 32, 34, 20, 25)
#        #womenStd =   (3, 5, 2, 3, 3)
#        rects2 = ax.bar(ind+width, countm, width, color='r')
#        
#        # add some
#        ax.set_ylabel('Scores')
#        ax.set_title('Scores by group and gender')
#        ax.set_xticks(ind+width)
#        # \n0:under 16 \n 1:16-20 \n i(<-N):16+5i-20+5i (i<4) \n 5:35-40 \n 6:40-50 \n 7:50 over
#        ax.set_xticklabels(('Under 16','16-20','21-25','26-30','31-35','36-40','40-50','Above 50'))
#        ax.legend( (rects1[0], rects2[0]), ('male', 'female') )
#        
#        def autolabel(rects):
#            # attach some text labels
#            for rect in rects:
#                height = rect.get_height()
#                ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height), ha='center', va='bottom')
#        
#        autolabel(rects1)
#        autolabel(rects2)
#        
#        plt.show()

    def closewindow(self,event):
        self.Destroy()
        
        
if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=bucky(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
        