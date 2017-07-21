# -*- coding: gb18030 -*-
"""
Created on Wed Jul 12 13:23:35 2017

@author: z81022868
"""
from __future__ import unicode_literals
import pandas as pd
import xlrd,xlwt
from collections import OrderedDict
import sys,os,re
from fileselectcut import TestExcel

'''
确保是文本类型，不然连接会丢失。*****************************
如果要可以获取合并单元格，就要转化为xls格式。注意不然获取合并单元格的操作不能用
unicode不用加U
gbk的编码就要加Ｂ
一次执行一个文件，文件名和表格名都要在一行，如果分很多行，默认为该多行的组合为目标变量。文件名和表革命开头和结尾不能有空格,英文要在英文输入法下输入。
'''
#==============================================================================
def getDevPrior(label,single_col,col_series=[]):
    contain=[]
#     if label.decode('gbk') in single_col:#单行{一级规格、耳机规格}
    for ele in enumerate(single_col) :#col_cont为表格中该列下区域
        if ele and ele[1] not in ['',b'',label.decode('gbk')]:
            contain.append(ele)
    if contain:
        batch_fill=[]#批量填充重复值之后的列

        batch_fill.append(contain[0][1])#整机规格
        for i in range(contain[0][0]+1,len(single_col)):
            if single_col[i] in [b'','']:
                if single_col[i-1] in [b'','']:
                        batch_fill.append(batch_fill[-1])
                else:
                        batch_fill.append(single_col[i-1])
            else:
                batch_fill.append(single_col[i])
        batch_fill.reverse()
        col_series.append(batch_fill)#存放行参数的总容器
    return col_series
#==============================================================================

def setColWidth(excelname,sheetname,dataframe_cols,width):
    file2=xlwt.Workbook(encoding='gb18030')
    #fie2name=excelname.decode("GBK",'ignore')
    sheet = file2.add_sheet(sheetname)
    for xlcol in range(dataframe_cols+10):
        sheet.col(xlcol).width=256*int(width)
    file2.save(excelname)
def prompt():
    #print "Unexpected error at your file,check your filename....." ,sys.exc_info()
    raw_input('press enter key to exit')
if __name__ == "__main__":
    # Create QApplication
    import guidata
    _app = guidata.qapplication()
    #app.exec_()
    e = TestExcel()
    #e.view()
    #e.floatarray[:, 0] = np.linspace( -5, 5, 50)
    ##print(e)
    if e.edit():pass
#        e.edit()
#        #print(e)
    e.view()
    e.files.fnames
#if __name__=="__main__":
    try:
        filedir,files=e.files.dir,e.files.fnames#路径+路径文件
        sheet=e.string
        for excelfile in files:
#        #print '将待转化文件移到本目录下:并输入完整文件及扩展名。完成后输入# 如：OLT 业务框和单板Spec数据模型.xlsm#'
#        tpath='OLT 业务框和单板Spec数据模型.xlsm#'.decode('gbk').split('#')[0].strip()#raw_input('Now input your filename:').decode('gbk').split('#')[0].strip()
#        #print 'Successfully input excelname !Finding && reading the input file ……'
#
#        path=os.path.join(os.getcwd(),tpath)
#        try:

            data = xlrd.open_workbook(excelfile)#huo qu merged cell
            #print 'OK\n','now 输入文件中数据表的表名。完成后输入#,如: OLT#','\n'
            tablename=sheet.decode('gbk').strip()#raw_input('Now input your sheetname:').decode('gbk').split('#')[0].strip()
            try:
                table=data.sheet_by_name(tablename)#闁俺绻冮崥宥囆為懢宄板絿
                #print 'OK , The output excel named: DataOut.xlsx will be at current path'
                nrows,ncols = table.nrows,table.ncols
                '''
                #判断是否有合并单元格;#读前10列，获取三级规格参数做行标号，准备写入；#读合并单元格，获取设备具体型号做列标号，准备写入#对合并单元格尽心填充'''
                copy_col,name=[],[]
                #==============================================================================
                '''先找到规格说明的位置，在从他向下数第3个单元格开始拷数据要判断是不是该行的规格参数级别是对应的不弄错了。要判断是不是有文本中有\n（末尾的忽略），替换成<p></p>
                "一级参数、二级规格、规格项的列是否在该列的数组值中，去重"  不读“版本号、描述"等列'''
                para=OrderedDict()
                devs_Paravalue=OrderedDict()
                #print 'extracting parameters……'
                for col_ind in range(0,ncols):
                    col_cont=table.col_values(col_ind)
                    if ('规格编号' or '描述' or '序号' or '版本支持情况' or '支持属性') not in col_cont[:20] :

                        if '一级规格' in col_cont:
                            tmp_ser1=getDevPrior('一级规格',col_cont)
                            #print '一级规格完成'
                        elif '二级规格' in col_cont:
                            tmp_ser2=getDevPrior('二级规格',col_cont,col_series=tmp_ser1)
                            #print '二级规格完成'
                        elif '三级规格' in col_cont:
                            ser=getDevPrior('三级规格',col_cont,col_series=tmp_ser2)
                        elif unicode(u'规格项') in col_cont:
                            cate_4=[]
                            for ele in enumerate(col_cont):

                                if ele and ele[1] != unicode(u'规格项'):
                                    #para['4rd-cate']=contain
                                    cate_4.append(ele[1])
                            if cate_4:
                                cate_4.reverse()
                                ser.append(cate_4)
                                #print '规格项完成'
                        elif unicode(u'支持属性') in col_cont :

                            dev_name=col_cont[col_cont.index(unicode(u'支持属性'))-2] if col_cont[col_cont.index(unicode(u'支持属性'))-2] not in ['', b''] else col_cont[col_cont.index(unicode(u'支持属性'))-3] #2,3,4
                            #dev_name=dev_name_list[0].encode("GB18030")
                            name.append(dev_name)
                            col_ind+=1
                            col_cont=table.col_values(col_ind)
                            if unicode(u'规格说明') in col_cont:
#                                #print '……',
#                                for x in range(len(col_cont)):
#                                    if col_cont[x] not in [b'','','规格说明']:
#                                        beg_ind=x
#                                        break
                                dev_val=col_cont[col_cont.index('规格说明')+3:]  ##缁岃桨绨?,7l娑撱倛顢?

                                if dev_name not in devs_Paravalue.keys():
                                     devs_Paravalue[dev_name.encode("GB18030")]=dev_val

                                else:
                                     #print col_ind ," : col",dev_name ,u' 已经存在，请检查源表格数据!'
                                     sys.exit()
                    else:
                         continue

                minn=min(map(len,ser))-1#serr=ser[:]
                ddd=[ser[1][:minn][::-1],ser[2][:minn][::-1]]

                #print '\nData extracted sucessfully! Now writing to new file……\n'
                oltdata=pd.DataFrame(devs_Paravalue.values(),index=name,columns=range(len(ser[2][:minn][::-1]))).transpose()
                #oltdata2=oltdata
                oltpara=pd.DataFrame(ddd,index=['compareTypeInfo','compareItem']).transpose()
                #oltpara2=oltpara
                oltall=oltpara.join(oltdata,how='outer')
                oltall.drop_duplicates(cols=["compareItem"],inplace=True)

                excelout=os.path.join(filedir,"Data_out.xlsx")
                setColWidth(excelout,'比较信息',oltall.shape[1],200)

                if not os.path.exists(os.path.join(os.getcwd(),excelout)):
                    setColWidth(excelout,'比较信息',oltall.shape[1],200)
                else:
                    pattern=r'^(.*(?:[^\W\d_]*))\n(.+)$'
                    reg=re.compile(pattern,re.M)
                    for dcol in oltall.columns[2:]:#range(oltall.shape[1]-1):
                        for drow in range(oltall.shape[0]-1):
                            if not isinstance(oltall[dcol].iloc[drow],str)and not isinstance(oltall[dcol].iloc[drow],unicode):
                                oltall[dcol].iloc[drow]=str(oltall[dcol].iloc[drow])
                            check=reg.findall(oltall[dcol].iloc[drow])#.iat[drow,dcol])
                            if check:
                                oltall[dcol].iloc[drow]=re.sub(reg,r'<p>\1</p> <p>\2</p>',oltall[dcol].iloc[drow])
#                        finded=oltall[dcol][oltall[dcol].str.contains(pattern,na=False)]
#                        #print finded
#                        if finded:
#                            for ind in finded.index:
#                                oltall[dcol][ind]=oltall[dcol][ind].replace(pattern,'<p>\1</p> <p>\2</p>')
#                        #print oltall[dcol]
#                        for index_re in finded.index[0]:
#                            oltall[dcol][index_re]=u'<p>'+oltall[dcol][index_re]+u'</p>'
#                    #oltall2.replace(to_replace='\n',value='<p></p>')
                    ss=pd.ExcelWriter(excelout)
                    oltall.to_excel(ss,'比较信息',index=False)
                    ss.save()
                    #print 'Finished,go and check the new file DataOut.xlsm under this path!'
                    #print time.strftime('%Y-%m-%d %A %X %Z',time.localtime(time.time()))
                    time.sleep(3)
                    raw_input('press enter key to exit')
    #==============================================================================
            except:
                prompt()
#        except:
#            prompt()
    except:
        prompt()