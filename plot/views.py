from django.shortcuts import render,HttpResponse
from .models import Line_plot,Bar_plot,Radar_plot,Scatter_plot,Area_plot,Pie_plot,Histogram_plot,Box_plot,StackedBar_plot,Heatmap_plot
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
import base64
import io
import pandas as pd

# Create your views here.

def img_scr():
    buffer=io.BytesIO() 
    plt.savefig(buffer,format='png') 
    img=base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    return img

def line_chart():
    data=Line_plot.objects.all()
    month=[obj.month for obj in data]
    sales=[obj.sales for obj in data]
    df=pd.DataFrame({'month':month,'sales':sales})
    plt.clf()
    plt.figure(figsize=(5,5))
    plt.plot(month,sales)
    plt.title('The monthly sales data change over the year', fontsize=10)
    plt.xlabel('months',fontsize=8, color='blue')
    plt.xticks(rotation=25,fontsize=8)
    plt.yticks(fontsize=8)
    plt.ylabel('sales',fontsize=8, color='red')
    plt.legend(loc='upper left', fontsize=6)
    img=img_scr()
    print(plt)
    plt.close()
    return img,df.to_html(classes='table',index=False)

def bar_chart():
    data=Bar_plot.objects.all()
    department=[obj.department for obj in data]
    revenues=[obj.revenue for obj in data]
    bar_table=pd.DataFrame({'Department':department,'Revenues':revenues}).to_html(classes='table',index=False)
    plt.clf()
    plt.figure(figsize=(5,5))
    plt.bar(department,revenues)
    plt.title('The revenues generated by departments in the company for the last quarter', fontsize=8)
    plt.xlabel('department',fontsize=8, color='blue')
    plt.ylabel('revenue',fontsize=8, color='red')
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.legend(loc="upper left", fontsize=6)
    img=img_scr()
    plt.close()
    return img,bar_table

def rader_chart():
    data = Radar_plot.objects.all()
    aspect = [obj.aspect for obj in data]
    score = [obj.score for obj in data]
    rader_table = pd.DataFrame({'Aspect': aspect, 'Score': score}).to_html(classes='table', index=False)
    plt.clf()
    plt.figure(figsize=(5, 5))
    plt.bar(aspect, score, color='skyblue', edgecolor='black')
    plt.xlabel('Aspect', fontsize=8, color='blue')
    plt.ylabel('Score', fontsize=8, color='red')
    plt.title('Radar Plot Sales', fontsize=10)
    plt.xticks(rotation=25, fontsize=8)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    plt.legend(loc='upper left',fontsize=6)
    img = img_scr()
    plt.close()
    return img, rader_table


def scatter_chart():
    data=Scatter_plot.objects.all()
    hours_studied=[obj.hoursstudied for obj in data]
    exam_scores=[obj.examscore for obj in data]
    scatter_table=pd.DataFrame({'Hours':hours_studied,'Exam score':exam_scores}).to_html(classes='table',index=False)
    plt.clf()
    plt.figure(figsize=(5,5))
    plt.scatter(hours_studied, exam_scores, color='purple', edgecolors='black', alpha=0.6)
    plt.xlabel('Hours Studied', fontsize=8, color='blue')
    plt.ylabel('Exam Score', fontsize=8, color='red')
    plt.title('Scatter Plot of Hours Studied vs Exam Score', fontsize=10)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.grid(True)
    plt.legend(loc="upper left", fontsize=6)
    plt.tight_layout()
    img=img_scr()
    plt.close()
    return img,scatter_table

def area_chart():
    data=Area_plot.objects.all()
    month=[obj.month for obj in data]
    new_customer=[obj.newcustomer for obj in data]
    old_customer=[obj.oldcustomer for obj in data]
    area_table=pd.DataFrame({'Month':month,'New customers':new_customer,'Old customers':old_customer}).to_html(classes='table',index=False)
    plt.clf()
    plt.figure(figsize=(5,5))
    plt.fill_between(month, new_customer, color='blue', alpha=0.8)
    plt.fill_between(month,old_customer,color='lightgreen',alpha=0.8)
    plt.xlabel('Month', fontsize=8, color='blue')
    plt.ylabel('Number of Customers', fontsize=8, color='red')
    plt.title('Area Plot of Customers Over Time', fontsize=10)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    plt.legend(loc="upper left", fontsize=6)
    img=img_scr()
    plt.close()
    return img,area_table

def pie_chart():
    data=Pie_plot.objects.all()
    companies=[obj.company for obj in data]
    sales=[obj.marketshare for obj in data]
    pie_table=pd.DataFrame({'Company':companies,'Sales':sales}).to_html(classes='table',index=False)
    plt.clf()
    plt.figure(figsize=(5,5))
    plt.pie(sales, labels=companies, autopct='%1.1f%%')
    plt.title('Pie Plot of Company Sales', fontsize=10)
    plt.axis('equal')
    plt.legend(loc="upper left",fontsize=6)
    img=img_scr()
    plt.close()
    return img,pie_table

def histogram_chart():
    data=Histogram_plot.objects.all()
    age_groups=[obj.agegroup for obj in data]
    customers=[obj.customers for obj in data]
    histo_table=pd.DataFrame({'Age groups':age_groups,'customers':customers}).to_html(classes='table',index=False)
    plt.clf()
    plt.figure(figsize=(5,5))
    plt.bar(age_groups, customers, color='orange', edgecolor='black')
    plt.xlabel('Age Group', fontsize=8, color='blue')
    plt.ylabel('Number of Customers', fontsize=8, color='red')
    plt.title('Histogram of Customer Age Groups', fontsize=10)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    plt.legend(loc="upper left", fontsize=6)
    img=img_scr()
    plt.close()
    return img,histo_table

def box_chart():
    data=Box_plot.objects.all()
    department=[obj.department for obj in data]
    mean=[obj.mean for obj in data]
    median=[obj.median for obj in data]
    maxi=[obj.max for obj in data]
    q1=[obj.q1 for obj in data]
    q2=[obj.q2 for obj in data]
    data_for_boxplot = [ mean, q1, median, q2, maxi]
    box_table=pd.DataFrame({'Department':department,'Mean':mean,'Q1':q1,'Median':median,'Q2':q2,'Maximum':maxi}).to_html(classes='table',index=False)
    plt.clf()
    plt.figure(figsize=(5,5))
    plt.boxplot(data_for_boxplot, vert=True, patch_artist=True, labels=['Mean', 'q1', 'Median', 'Q2', 'Max'])
    plt.title("Box Plot",fontsize=10)
    plt.xlabel("Category",fontsize=8, color='blue')
    plt.ylabel("Values",fontsize=8, color='red')
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.legend(loc="upper left", fontsize=6)
    img=img_scr()
    plt.close()
    return img,box_table

def stacked_bar_chart():
    data=StackedBar_plot.objects.all()
    quater=[obj.quater for obj in data]
    electronics=[obj.electronics for obj in data]
    furniture=[obj.furniture for obj in data]
    clothing=[obj.clothing for obj in data]
    total=[obj.total for obj in data]
    stacked_table=pd.DataFrame({'Quater':quater,'Electronics':electronics,'Furniture':furniture,'Clothing':clothing,'Total':total}).to_html(classes='table',index=False)
    bar_width = 0.35
    index = np.arange(len(quater))
    plt.clf()
    plt.figure(figsize=(5,5))
    plt.bar(index, electronics, bar_width, label="Electronics")
    plt.bar(index, furniture, bar_width, bottom=electronics, label="Furniture")
    plt.bar(index, clothing, bar_width, bottom=np.array(electronics)+np.array(furniture), label="Clothing")
    plt.xlabel('Quarter',fontsize=8, color='blue')
    plt.ylabel('Sales',fontsize=8, color='red')
    plt.title('Sales by Department for each Quarter',fontsize=10)
    plt.xticks(index, quater,fontsize=8)
    plt.yticks(fontsize=8)
    plt.legend(loc="upper left", fontsize=6)
    img=img_scr()
    plt.close()
    return img,stacked_table

def heatmap_chart():
    data = Heatmap_plot.objects.all()
    region = [obj.region for obj in data]
    jan = [obj.january for obj in data]
    feb = [obj.february for obj in data]
    mar = [obj.march for obj in data]
    apl = [obj.april for obj in data]
    may = [obj.may for obj in data]
    heat_table = pd.DataFrame({'Region': region, 'Jan': jan, 'Feb': feb, 'Mar': mar, 'Apr': apl, 'May': may}).to_html(classes='table', index=False)
    plt.clf()
    heatmap_data = np.array([jan, feb, mar, apl, may])
    plt.figure(figsize=(5, 5))
    plt.imshow(heatmap_data, cmap='coolwarm', interpolation='nearest', aspect='auto')
    plt.xlabel('Month', fontsize=10, color='blue')
    plt.ylabel('Region', fontsize=10, color='red')
    plt.xticks(ticks=np.arange(5), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May'], fontsize=8)
    plt.yticks(ticks=np.arange(len(region)), labels=region, fontsize=8)
    plt.colorbar(label='Sales/Values')
    plt.title('Heatmap of Sales or Data over Time by Region', fontsize=10)
    plt.legend(loc='upper left',fontsize=6)
    img = img_scr()
    plt.close()
    return img,heat_table

def home(request):
    line_img,line_table=line_chart()
    bar_img,bar_table=bar_chart()
    radar_img,rader_table=rader_chart()
    scatter_img,scatter_table=scatter_chart()
    area_img,area_table=area_chart()
    pie_img,pie_table=pie_chart()
    histo_img,histo_table=histogram_chart()
    box_img,box_table=box_chart()
    stacked_img,stacked_table=stacked_bar_chart()
    heat_img,heat_table=heatmap_chart()
    plot_type=None

    if request.method=='POST':
        plot_type=request.POST.get('plots','line_plot')

    charts={'Line chart':{'img':line_img,'table':line_table,'title':'Line chart'},
            'Bar chart':{'img':bar_img,'table':bar_table,'title':'Bar chart'},
            'Rader chart':{'img':radar_img,'table':rader_table,'title':'Radar chart'},
            'Scatter chart':{'img':scatter_img,'table':scatter_table,'title':'Scatter chart'},
            'Area chart':{'img':area_img,'table':area_table,'title':'Area chart'},
            'Pie chart':{'img':pie_img,'table':pie_table,'title':'Pie chart'},
            'Histogram':{'img':histo_img,'table':histo_table,'title':'Histogram chart'},
            'Box chart':{'img':box_img,'table':box_table,'title':'Box chart'},
            'Stacked bar':{'img':stacked_img,'table':stacked_table,'title':'Stacked chart'},
            'Heatmap chart':{'img':heat_img,'table':heat_table,'title':'Heatmap chart'}
            }
    chart_select = charts.get(plot_type)
    chart_rest = {key: val for key, val in charts.items() if key != plot_type}

    return render(request,'home.html',{'chart_select':chart_select,'chart_rest':chart_rest})