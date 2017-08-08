# -*- coding: gb18030 -*-
"""
Created on Wed Jul 12 13:23:35 2017

@author: z81022868
"""
from __future__ import unicode_literals
import re,sys,os
from re import sub as sub
from re import compile as compile
from pandas import DataFrame as DataFrame
from pandas import ExcelWriter as ExcelWriter
from collections import OrderedDict
from xlrd import open_workbook as open_workbook
from xlwt import Workbook as Workbook

def setColWidth(excelname,sheetname,dataframe_cols,width):
	file2=Workbook(encoding='gb18030')
	#fie2name=excelname.decode("GBK",'ignore')
	sheet = file2.add_sheet(sheetname)
	for xlcol in range(dataframe_cols+10):
		sheet.col(xlcol).width=256*int(width) #閸掓顔旀稉?0娑擃亜鐡х粭锔炬畱鐎硅棄瀹?
	file2.save(excelname)
#=******************************************************************************************************************************************
try:
	path=sys.argv[1]#abs path
	outdir=os.path.split(path)[0]
	##print path

	try:
		data = open_workbook(path)#huo qu merged cell
		##print 'OK\n','now input sheet name of the input excel file ','\n'
		#if not sheet:
		sheet='OLT'
		tablename=sheet.decode('gbk').strip()
		#tablename='OLT'#raw_input().decode('gbk').split('#')[0].strip()
		#''.join(raw_input().decode('gbk').strip().splitlines())#raw_input().decode("gbk").strip()
		try:#tablename =tmpname#

			table=data.sheet_by_name(tablename)#闁俺绻冮崥宥囆為懢宄板絿
			#print 'OK , The output excel named: DataOut.xlsx will be at current path'
			##print 'sheet data read sucessfully',path,'  ',tablename,'\n'

#==============================================================================
#		 else:
#			 #print("Error,please press any key to exit.....")
#			 time.sleep(3)
#			 sys.exit()
#==============================================================================
		#hangshu lieshu
			nrows = table.nrows
			ncols = table.ncols
			##print table.name," rows:",table.nrows,"cols:",table.ncols
	#####你好
			'''
			#判断是否有合并单元格
	#读前10列，获取三级规格参数做行标号，准备写入；
	#读合并单元格，获取设备具体型号做列标号，准备写入
	#对合并单元格尽心填充'''
			copy_col,ser,name=[],[],[]
			#==============================================================================
			'''要先找到规格说明的位置，在从他乡下数第3个单元格开始拷数据
		要判断是不是呵行的规格参数级别是对应的不弄错了。
	 要判断是不是有顿号，替换成<p></p>
	有“一级参数、耳机规格、规格项的列是否在该列的数组值中，去重复”
	不读“版本号、描述、支持属性
				'''
			para=OrderedDict()
			devs_Paravalue=OrderedDict()
			##print 'extracting parameters……'
			for col_ind in range(0,ncols):
				col_cont=table.col_values(col_ind)
				"""閼惧嘲褰囬崣鍌涙殶閻?"""
				if ('规格编号' or '描述' or '序号' or '版本支持情况' or '支持属性') not in col_cont[:20] :
					#col_cont=table.col_values(col_ind)
					contain=[]
					if '一级规格' in col_cont:
						for ele in enumerate(col_cont):
							if ele[1] not in ['','一级规格']:
								contain.append(ele)
						para['1st-category']=contain

						col_list=[]
						col_list.append(contain[0][1])
						for i in range(contain[0][0]+1,len(col_cont)):
							if col_cont[i] == '':
								if col_cont[i-1] == unicode(u''):
									col_list.append(col_list[-1])
								else:
									col_list.append(col_cont[i-1])
							else:
								col_list.append(col_cont[-1])
						#copy_col=replaceEmpty(col_cont[:],contain)
						col_list.reverse()
						ser.append(col_list)



					if unicode(u'二级规格') in col_cont:
						for ele in enumerate(col_cont):
							if ele[1] not in ['',unicode(u'二级规格')]:

								contain.append(ele)
								para['2rd-category']=contain
						col_list=[]
						col_list.append(contain[0][1])
						for i in range(contain[0][0]+1,len(col_cont)):
							if col_cont[i] == unicode(u''):
								if col_cont[i-1] == unicode(u''):
									col_list.append(col_list[-1])
								else:
									col_list.append(col_cont[i-1])
							else:
								col_list.append(col_cont[-1])
						col_list.reverse()
						ser.append(col_list)
					if unicode(u'三级规格') in col_cont:
						for ele in enumerate(col_cont):
							if ele[1] not in ['',unicode(u'三级规格')]:

								contain.append(ele)
								para['3rd-category']=contain
					if unicode(u'规格项') in col_cont:
						for ele in enumerate(col_cont):
							if ele[1] != unicode(u'规格项'):

								contain.append(ele)
								para['4rd-cate']=contain
								cate_4=[x[1] for x in contain]
								cate_4.reverse()
						ser.append(cate_4)
			#####鐠佹儳顦崠?

					if unicode(u'支持属性') in col_cont :

						dev_name=col_cont[col_cont.index(unicode(u'支持属性'))-2] if col_cont[col_cont.index(unicode(u'支持属性'))-2] != '' else col_cont[col_cont.index(unicode(u'支持属性'))-3] #2,3,4鐞涘苯鎮庨獮鏈电啊
						#dev_name=dev_name_list[0].encode("GB18030")
						name.append(dev_name)
						col_ind+=1
						col_cont=table.col_values(col_ind)
						if unicode(u'规格说明') in col_cont:

							#閻⑩杹lrd鐠囪鍙嗛惃鍕€冮弽鍏兼Ц閸欘亣顕?娴滃棴绱濇稉宥堝厴娣囶喗鏁?
							##print '……'
							dev_val=col_cont[col_cont.index(unicode(u'规格说明'))+3:]  ##缁岃桨绨?,7l娑撱倛顢?

							if dev_name not in devs_Paravalue.keys():
								devs_Paravalue[dev_name.encode("GB18030")]=dev_val
							else:
								#print col_ind ," : col",dev_name ,u' 已经存在，请检查源表格数据!'
								sys.exit()

				else:
					 continue
			minn=min(map(len,ser))-1#serr=ser[:]
			ddd=[ser[1][:minn][::-1],ser[2][:minn][::-1]]


			#file2=os.path.join(os.getcwd(),'Data_out.xlsx')



			##print '\nData extracted sucessfully! Now writing to new file……\n'
			oltdata=DataFrame(devs_Paravalue.values(),index=name)
			oltdata2=oltdata.transpose()
			oltpara=DataFrame(ddd,index=['compareTypeInfo','compareItem'])
			oltpara2=oltpara.transpose()
			oltall=oltpara2.join(oltdata2,how='outer')
			oltall2=oltall.drop_duplicates()

			excelname=os.path.join(outdir,"Data_out.xlsx")
			setColWidth(excelname,'比较信息',oltall2.shape[1],200)
			##print u'閻㈢喐鍨氶弬鍥︽閻ㄥ嫬鍨€瑰€燁啎缂冾喕璐?0 娑擃亞鈹栫€涙顑佺€硅棄瀹?
			if not os.path.exists(os.path.join(os.getcwd(),excelname)):
				setColWidth(excelname,'比较信息',oltall2.shape[1],200)
			else:
				ss=ExcelWriter(excelname)

				pattern=r'^(.*(?:[^\W\d_]*))\n(.+)$'
				reg=compile(pattern,re.M)
				for dcol in oltall2.columns[2:]:
					for drow in range(oltall2.shape[0]-1):
						if not isinstance(oltall2[dcol].iloc[drow],str)and not isinstance(oltall2[dcol].iloc[drow],unicode):
							oltall2[dcol].iloc[drow]=str(oltall2[dcol].iloc[drow])
						check=reg.findall(oltall2[dcol].iloc[drow])#.iat[drow,dcol])
						if check:
							oltall2[dcol].iloc[drow]=sub(reg,r'<p>\1</p> <p>\2</p>',oltall2[dcol].iloc[drow])
				#pattern='\n'
				# for dcol in oltall2.columns:
					# finded=oltall2[dcol][oltall2[dcol].str.contains(pattern,na=False)]
					# oltall2[dcol]=oltall2[dcol].str.replace('\n','</p> <p>')
					# for index_re in finded.index:
						# oltall2[dcol][index_re]=u'<p>'+oltall2[dcol][index_re]+u'</p>'
				# #oltall2.replace(to_replace='\n',value='<p></p>')
				oltall2.to_excel(ss,'比较信息',index=False)
				ss.save()
				#print 'Finished,go and check the new file DataOut.xlsm under this path!','\n'

				##print time.strftime('%Y-%m-%d %A %X %Z',time.localtime(time.time()))
				#time.sleep(3)
				#raw_input('press enter key to exit')
		except:
			print "Unexpected error at your sheetname:", sys.exc_info() # 団剝浼?
			#raw_input('press enter key to exit')
	except:
		print "Unexpected error at your sheetname:", sys.exc_info() # sys.exc_info()鏉╂柨娲栭崙娲晩娣団剝浼?
		#raw_input('press enter key to exit') #鏉╂瑥鍔归弨鍙ョ娑擃亞鐡戝鍛扮翻閸忋儲妲告稉杞扮啊娑撳秷顔€缁嬪绨柅鈧崙?
except:
	print "Unexpected error at your file,check your filename....." ,sys.exc_info() # sys.exc_info()鏉╂柨娲栭崙娲晩娣団剝浼?
	#raw_input('press enter key to exit') #鏉╂瑥鍔归弨鍙ョ娑擃亞鐡戝鍛扮翻閸忋儲妲告稉杞扮啊娑撳秷顔€缁嬪绨柅鈧