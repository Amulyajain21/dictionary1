import tkinter as tk
import requests
import json
import xlwt
import xlrd
#import vlc
from xlutils.copy import copy
app_id='28a38761'
app_key='2c1ebea46528df2b1d54d4a7906201f2'
language='en'

def done():
    global value1
    value1=''
    word_id=enter.get()
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  + language + '/'  + word_id.lower()
    patt0=xlwt.easyxf('font: name Times New Roman,color-index red ,bold on',num_format_str='#,##0.00')
    patt1=xlwt.easyxf('font: name Times New Roman,color-index blue,bold off')
    rb=xlrd.open_workbook('Dictionary2.xls')
    r=rb.sheet_by_index(0)
    i=r.nrows
    wb=copy(rb)
    flag=False
    for j in range(i):
     if(r.cell(j,0).value==word_id):
        flag=True
        break
    if(flag==True):
        print("....this word already exists in dictionary...")
        #print(r.cell(j,1).value)
        meaning=r.cell(j,1).value
        example=r.cell(j,2).value
        all_data=f"""

         meaning: {meaning}
         example: {example}
         """
        #tk.Label(root, text="value already exist in dictionary").grid(row=6,column=0)

        tk.Label(root, text=all_data).grid(row=7,column=0)


    else:
         
        req = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
        a=req.json()
        meaning=a['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        example=a['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['text']
        all_data=f"""

         meaning: {meaning}
         example: {example}
         """
        #tk.Label(root, text="value entered in dictionary").grid(row=6,column=0)

        tk.Label(root, text=all_data).grid(row=7,column=2)

        
        #p=vlc.MediaPlayer(a['results'][0]['lexicalEnteries'][0]['pronunciations'][0]['audioFile'])
        ws=wb.get_sheet(0)
        ws.write(i,0,word_id,patt0)
        ws.write(i,1,meaning,patt1)
        ws.write(i,2,example,patt1)
        wb.save("Dictionary2.xls")
        print("value entered in dictionary")
        value1=meaning
        #tk.Label(root, text=value1).grid(row=3,column=2,columnspan=3)

root = tk.Tk()
root.grid()
root.geometry("1000x1000")
root.configure(background="grey")
tk.Label(root, text="enter word",fg="black",bg="grey").grid(row=0,column=0,sticky="E",pady=50,padx=50)
enter = tk.Entry(root)
enter.grid(row=0, column=1)
tk.Button(root,text='submit',command=done).grid(row=2,column=1)







