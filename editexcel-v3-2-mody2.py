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
		sheet.col(xlcol).width=256*int(width) #鍒楀涓?0涓瓧绗︾殑瀹藉�?
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

			table=data.sheet_by_name(tablename)#閫氳繃鍚嶇О鑾峰彇
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
	#####���
			'''
			#�ж��Ƿ��кϲ���Ԫ��
	#��ǰ10�У���ȡ�������������б�ţ�׼��д�룻
	#���ϲ���Ԫ�񣬻�ȡ�豸�����ͺ����б�ţ�׼��д��
	#�Ժϲ���Ԫ�������'''
			copy_col,ser,name=[],[],[]
			#==============================================================================
			'''Ҫ���ҵ����˵����λ�ã��ڴ�����������3����Ԫ��ʼ������
		Ҫ�ж��ǲ��Ǻ��еĹ����������Ƕ�Ӧ�Ĳ�Ū���ˡ�
	 Ҫ�ж��ǲ����жٺţ��滻��<p></p>
	�С�һ��������������񡢹��������Ƿ��ڸ��е�����ֵ�У�ȥ�ظ���
	�������汾�š�������֧������
				'''
			para=OrderedDict()
			devs_Paravalue=OrderedDict()
			##print 'extracting parameters����'
			for col_ind in range(0,ncols):
				col_cont=table.col_values(col_ind)
				"""鑾峰彇鍙傛暟�?"""
				if ('�����' or '����' or '���' or '�汾֧�����' or '֧������') not in col_cont[:20] :
					#col_cont=table.col_values(col_ind)
					contain=[]
					if 'һ�����' in col_cont:
						for ele in enumerate(col_cont):
							if ele[1] not in ['','һ�����']:
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



					if unicode(u'�������') in col_cont:
						for ele in enumerate(col_cont):
							if ele[1] not in ['',unicode(u'�������')]:

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
					if unicode(u'�������') in col_cont:
						for ele in enumerate(col_cont):
							if ele[1] not in ['',unicode(u'�������')]:

								contain.append(ele)
								para['3rd-category']=contain
					if unicode(u'�����') in col_cont:
						for ele in enumerate(col_cont):
							if ele[1] != unicode(u'�����'):

								contain.append(ele)
								para['4rd-cate']=contain
								cate_4=[x[1] for x in contain]
								cate_4.reverse()
						ser.append(cate_4)
			#####璁惧鍖?

					if unicode(u'֧������') in col_cont :

						dev_name=col_cont[col_cont.index(unicode(u'֧������'))-2] if col_cont[col_cont.index(unicode(u'֧������'))-2] != '' else col_cont[col_cont.index(unicode(u'֧������'))-3] #2,3,4琛屽悎骞朵簡
						#dev_name=dev_name_list[0].encode("GB18030")
						name.append(dev_name)
						col_ind+=1
						col_cont=table.col_values(col_ind)
						if unicode(u'���˵��') in col_cont:

							#鐢▁lrd璇诲叆鐨勮��鏍兼槸鍙�?浜嗭紝涓嶈兘淇�?
							##print '����'
							dev_val=col_cont[col_cont.index(unicode(u'���˵��'))+3:]  ##绌轰�?,7l涓よ�?

							if dev_name not in devs_Paravalue.keys():
								devs_Paravalue[dev_name.encode("GB18030")]=dev_val
							else:
								#print col_ind ," : col",dev_name ,u' �Ѿ����ڣ�����Դ�������!'
								sys.exit()

				else:
					 continue
			minn=min(map(len,ser))-1#serr=ser[:]
			ddd=[ser[1][:minn][::-1],ser[2][:minn][::-1]]


			#file2=os.path.join(os.getcwd(),'Data_out.xlsx')



			##print '\nData extracted sucessfully! Now writing to new file����\n'
			oltdata=DataFrame(devs_Paravalue.values(),index=name)
			oltdata2=oltdata.transpose()
			oltpara=DataFrame(ddd,index=['compareTypeInfo','compareItem'])
			oltpara2=oltpara.transpose()
			oltall=oltpara2.join(oltdata2,how='outer')
			oltall2=oltall.drop_duplicates()

			excelname=os.path.join(outdir,"Data_out.xlsx")
			setColWidth(excelname,'�Ƚ���Ϣ',oltall2.shape[1],200)
			##print u'鐢熸垚鏂囦欢鐨勫垪����缃�?0 涓┖��楃��藉�?
			if not os.path.exists(os.path.join(os.getcwd(),excelname)):
				setColWidth(excelname,'�Ƚ���Ϣ',oltall2.shape[1],200)
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
				oltall2.to_excel(ss,'�Ƚ���Ϣ',index=False)
				ss.save()
				#print 'Finished,go and check the new file DataOut.xlsm under this path!','\n'

				##print time.strftime('%Y-%m-%d %A %X %Z',time.localtime(time.time()))
				#time.sleep(3)
				#raw_input('press enter key to exit')
		except:
			print "Unexpected error at your sheetname:", sys.exc_info() # �℃�?
			#raw_input('press enter key to exit')
	except:
		print "Unexpected error at your sheetname:", sys.exc_info() # sys.exc_info()杩斿洖鍑洪敊淇℃�?
		#raw_input('press enter key to exit') #杩欏効鏀句竴涓瓑寰呰緭鍏ユ槸涓轰簡涓嶈�绋嬪簭閫€鍑?
except:
	print "Unexpected error at your file,check your filename....." ,sys.exc_info() # sys.exc_info()杩斿洖鍑洪敊淇℃�?
	#raw_input('press enter key to exit') #杩欏効鏀句竴涓瓑寰呰緭鍏ユ槸涓轰簡涓嶈�绋嬪簭閫�