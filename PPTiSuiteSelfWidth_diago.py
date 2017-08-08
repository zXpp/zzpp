# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:23:13 2017

@author: z81022868
"""
#from __future__ import unicode_literals

import sys,os,tempfile,codecs,shutil,numpy as np#ctypes,
from formater_OK import ppt_diago
from PIL import Image,ImageFilter
from Tkinter import Tk,Entry,Button
from time import sleep
import win32com.client


##@ pptDecorate
#def PptExportSlides(pname,label,outdir,pdfname):#tmp/tmp2
#
#	app='PowerPoint'
#	w = win32com.client.DispatchEx('{}.Application'.format(app))
#	w.Visible = 1
#	ppt = w.Presentations.Open(pname)#*args:abs
#	sliCount = ppt.Slides.Count
#	#label = os.path.basename(pname).split('.')[0]
#	#outdir = os.path.split(pname)[0]
#	#os.mkdir(outdir)
#	#pdfname=os.path.join(outdir,label+r".pdf")
#	ppt.SaveAs(pdfname, 32)
#	for i,slide in enumerate(ppt.Slides):
#			slide.Select
#			fullpath = os.path.join(tmp2,label+"_"+str(i+1).zfill(3)+r".png")
#			slide.Export(fullpath, "PNG")
#	ppt.close()
#	w.Quit()
class PngsKit():
	def __init__(self,newwid,abspnglst,savedir):
		#self.out=mode[0]#判断是否需要pngsnewwid=None,abspnglst=None,savedir=None
		#self.raneed=mode[1]#判断是否需要rawslides
		#self.reneed=mode[3]#判断是否需要resizedpngs
		self.newwid=newwid
		self.rawspath=abspnglst
		self.count=len(abspnglst)
		self.resizepath=savedir
	def sigResize(self,ima,index):
		im=Image.open(ima)
		self.ratio=float(self.newwid/im.size[0])
		resizer=im.resize((int(self.newwid),int(im.size[1]*self.ratio)))#dpi
		rename=os.path.join(self.resizepath,label+"_"+str(index).zfill(3)+r".png")
		resizer.save(rename,"PNG")
	def multiResize(self,mode_long,l,rl):##abspnglst:位slides的绝对位置,pattern[0]
		#base=Image.open(self.abspnglst[0])#copty the first slides
		#cpbase=base.copy()
		for i,img in enumerate(self.rawspath):
			self.sigResize(img,i)
#==============================================================================
# 			if mode_long[0] == 2 :
# 				if mode_long[1]:#if need raw concated longpngs
# 					self.pngs2Png(self.rawspath,rl)#abs is a list ,with slides abopath as the element
# 				if mode_long[2]:
# 					self.pngs2Png(self.resizepath,l)#savedir is a string ,means outdir
#==============================================================================

#	def pngs2Png(self,indir,outname):#indir :abso path;outname:abo
#		if type(indir)!=list:
#			abolist=map(lambda x:os.path.join(indir,x),os.listdir(indir))
#		#print(abolist[0])
#		else:
#			abolist=indir
#		baseimg=Image.open(abolist[0])
#		baseimg=baseimg.convert('RGB')
#		#baseimg=baseimg.filter(ImageFilter.DETAIL)#细节滤波，细节更明显
#		sz=baseimg.size
#		#basemat=np.atleast_2d(baseimg)
#		new=Image.new("RGB")
#		for i in abolist:
#			ea=Image.open(i)
#			for top in range(0,new.size[1],ea.size[1]):
#				new.paste(ea,(0,top))
#				break
#		new.save(outname)
	def png2pngs(indir,outname):#indir :abso path;outname:abo
		if type(indir)!=list:
			abolist=map(lambda x:os.path.join(indir,x),os.listdir(indir))
		#print(abolist[0])
		else:
			abolist=indir
		baseimg=Image.open(abolist[0])
		baseimg=baseimg.convert('RGB')
		baseimg=baseimg.filter(ImageFilter.DETAIL)#细节滤波，细节更明显
		sz=baseimg.size
		basemat=np.atleast_2d(baseimg)
		for i in range(1,len(abolist)):
			file=abolist[i]
			im=Image.open(file)
			if im.mode != "RGB":#转化成统一通道数RGB
				 conmode=im.convert("RGB")
				 im=conmode
			im=im.resize(sz,Image.ANTIALIAS)#每一张图都切割成第一张大小
			mat=np.atleast_2d(im)
			#print(file)
			basemat=np.append(basemat,mat,axis=0)
		final_img=Image.fromarray(basemat)
		final_img.save(outname,"PNG")

	def pngs2xml(reldirlist,outname):#reldirlist=relativelist.相对路径的列表
		with codecs.open(os.path.join(pyrealpath,r"util\Tmp\VAN_Feature_Glance.xml"),'rb') as f1:
			content,begflag,endflag,new=f1.read(),'<image href="','</image>',[]
			#matchline=[line for line in content if begflag in line][0]
			matchtag=content[content.find(begflag):content.rfind(endflag)+len(endflag)]
			oldstr=matchtag[matchtag.find(begflag)+len(begflag):matchtag.rfind('" hwFormat=')]
			#repeach=matchtag.replace(oldstr,ele)
			new.extend([matchtag.replace(oldstr,ele) for ele in reldirlist])
			xmlout=content[:content.index(begflag)]+''.join(new)+content[content.rfind(endflag)+len(endflag):]
			out1=open(outname,'w')
			out1.write(xmlout)
			##print xmlout >out1,outname
			out1.close()
	def pngs2html(reldirlist,outname):
		  with codecs.open(os.path.join(pyrealpath,r"util\Tmp\Htmltemp.html"),'rb') as f2:
			content,begflag,endflag,new=f2.read(),'<img src="','</br>',[]
			#matchline=[line for line in content if begflag in line][0]
			matchtag=content[content.find(begflag):content.rfind(endflag)+len(endflag)]
			oldstr=matchtag[matchtag.find(begflag)+len(begflag):matchtag.rfind('" display')]
			#repeach=matchtag.replace(oldstr,ele)
			new.extend([matchtag.replace(oldstr,ele) for ele in reldirlist])
			writeout=content[:content.index(begflag)]+"".join(new)+content[content.rfind(endflag)+len(endflag):]
			out=open(outname,'w')
			out.write(writeout)
			out.close()

if __name__ == "__main__":
	import guidata
	_app = guidata.qapplication()
	if ppt_diago.edit():print(ppt_diago)#如果面板被编辑过。
	#ppt_diago.view()

	#args=GetDiagoArgs(ppt_diago.__dict__)#dict
	args=ppt_diago.__dict__
	#pypath=ur'D:\untar\selfwidth\dist\dist'#sys.argv[2]#vbspath
	#pyrealpath=pypath.encode('utf-8')
	#mode={"ra":args["_raw"],"re":args["_outpath"]}#ra:raw;re:resize
	pptsets=args["_PPTnames"]
	width=args["_newsize"] #* int(args["_resize"])
	coor=dict(zip(["Pngs","lPngs","Pdf","Html","Xml"],args["_outFormat"]))
	pattern=map(lambda x:[coor[x],int(args["_raw"]),int(args["_resize"])],coor.keys())
	mode=dict(zip(["Pngs","lPngs","Pdf","Html","Xml"],pattern))#y要考虑本不都输出的青睐
	mergename_Sets=[r".pdf",r".png",r".html",r".xml",r'_raw.png',r"_raw.html",r"_raw.xml"]
	for ppt_each in pptsets:
		label=os.path.basename(ppt_each).split(".")[0]
		raw=os.path.join(args["_outpath"],label)
		tmp,tmp2=raw+"\\"+str(width),raw+r'\Slides'
	if os.path.isdir(tmp):pass
	else:
		os.makedirs(tmp)
	if os.path.isdir(tmp2):pass
	else:
		os.makedirs(tmp2)
	pdfname,lpngname,htmlname,xmlname,rlpngname,rawhtmlname,rawxmlname=map(lambda x :os.path.join(raw,label+x),mergename_Sets)
	#先导出所有的slide和pdf
	app='PowerPoint'
	w = win32com.client.DispatchEx('{}.Application'.format(app))
	sleep(1)
	w.Visible = 1
	w.DisplayAlerts = False
	ppt = w.Presentations.Open(ppt_each)#*args:abs
	sleep(3)
	sliCount = ppt.Slides.Count
	k=0
	for k,slide in enumerate(ppt.Slides):
		slide.Select
		sleep(2)
		name=label+"_"+str(k).zfill(3)+r".PNG"#ppt count starts from 1 not 0
		fullpath= os.path.join(tmp2,name)
		sleep(1)
		slide.Export(fullpath,"PNG")
		sleep(2)
	ppt.SaveAs(pdfname, 32)
	sleep(2)
	ppt.close()
	w.Quit()
	#PptExportSlides(ppt_each,label,tmp2,pdfname)
	abolist_raw=map(lambda x:os.path.join(tmp2,x),os.listdir(tmp2))
	abolist=map(lambda x:os.path.join(tmp,x),os.listdir(tmp))
	pngkit=PngsKit(width,abolist_raw,tmp)#pngkit=PngsKit()
	pngkit.multiResize(mode["lPngs"],l=lpngname,rl=rlpngname)
#(self,mode,newwid,abspnglst,savedir,label):newwid=width,abspnglst=abolist_raw,label=label,savedir=abolist

	#############################################################################################
	if os.path.exists(tmp) and os.path.exists(tmp2):#710cunzai
		#destdir=raw+r"\Out_merged"#直接在目标文件夹下生产ImageMagick-7.0.6-Q16\tmp
		#renamePngs(tmp)
		#renamePngs(tmp2)
		relativepath=["".join([r"..","\\",width,"\\",i]) for i in os.listdir(tmp)]#str(i).zfill(2)
		relativerawpath=["".join([r"..\Slides","\\",i]) for i in os.listdir(tmp2)]
		outdir=tempfile.mkdtemp(prefix=width+"PPTMerged_",dir=raw)
		if os.path.isfile("".join([raw,"\\",label,r".pdf"])):
			shutil.move("".join([raw,"\\",label,r".pdf"]),outdir)
		if mode["Xml"][0] and  mode["Xml"][2]:
		  pngs2xml(relativepath,xmlname)
		if mode["Xml"][0] and  mode["Xml"][1]:
		  pngs2xml(relativerawpath,rawxmlname)
		if mode["Html"][0] and  mode["Html"][2]:
		  pngs2html(relativepath,htmlname)
		if mode["Html"][0] and  mode["Html"][1]:
		  pngs2html(relativerawpath,rawhtmlname)
		#print "Html,Xml,Pdf Files Gentrenated Successfully!"
		#print "Concatenating Resized pngs to longpng......"
		if mode["lPngs"][0] and  mode["lPngs"][2]:
		  pngs2Png(tmp,lpngname)#Imgarr,lpng=
		#print "Concatenating Raw slides to rawlongpng......"
		if mode["lPngs"][0] and  mode["lPngs"][1]:
		  pngs2Png(tmp2,rlpngname)

"""
if os.path.isfile(pdfname) and os.path.isfile(lpngname) and os.path.isfile(htmlname) and os.path.isfile(xmlname):
	user32.MessageBoxA(0,"Finished Sucessdully! GO and Check Your file",'Ctypes',0)"""