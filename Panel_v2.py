# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:23:13 2017
@author: z81022868
"""
#from __future__ import unicode_literals
#show=True
#from __future__ import print_function
import sys,os,codecs,shutil,tempfile,ctypes
import numpy as np
from PIL import Image,ImageFilter
from formater_OK import ppt_diago
#pypath=sys.argv[2]#os.path.realpath(sys.argv[0])
#pyrealpath=pypath.encode('utf-8')
##print pypath
#sys.path+=[os.getcwd(),os.path.join(pyrealpath,r"guidata\pyLib")]
#pptabspath=sys.argv[1][2:-1]
#width=sys.argv[3]
#raw=sys.argv[4]
#print raw
#raw=os.path.splitext(pptabspath)[0]#D:\zx\特性Glance格式转换工具需求分析

#print tmp
def Mbox(title, text, style):
	return ctypes.windll.user32.MessageBoxW(0, text, title, style)
#ctypes,
def renamePngs(path):#tmp/tmp2
	#dock=[]
	for root,dirs,files in os.walk(path):	#遍历统计
		for each in files:
			fileabs=os.path.join(root,each)#dirs=[]
			pre=os.path.splitext(fileabs)[0]
			nochang=pre.rpartition("_")#
			if len(nochang[-1])< len(nochang[-1].zfill(3)):
				shutil.move(fileabs,"_".join([nochang[0],nochang[-1].zfill(3)+r".png"]))
		break

def png2pngs(indir,outname):#indir :abso path;outname:abo
	abolist=[os.path.join(indir,x) for x in os.listdir(indir)]
	#print(abolist[0])
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

def pngs2xml(reldirlist,outname,newtit):#reldirlist=relativelist.相对路径的列表
	with codecs.open(os.path.join(pyrealpath,r"guidata\Tmp\VAN_Feature_Glance.xml"),'rb') as f1:
		content,begflag,endflag,new=f1.read(),'<image href="','</image>',[]
		titbeg,titend='<title>','</title>'
		#content=content.repalce("title>##NAME##</title","title>"+newtit+"</title")
		#matchline=[line for line in content if begflag in line][0]
		matchtag=content[content.find(begflag):content.rfind(endflag)+len(endflag)]
		oldstr=matchtag[matchtag.find(begflag)+len(begflag):matchtag.rfind('" hwFormat=')]
		#repeach=matchtag.replace(oldstr,ele)content[:content.index(begflag)]
		new.extend([matchtag.replace(oldstr,ele) for ele in reldirlist])
		titrep=content[:content.find(titbeg)+len(titbeg)]+newtit+content[content.rfind(titend):content.index(begflag)]
		xmlout=titrep+''.join(new)+content[content.rfind(endflag)+len(endflag):]
		out1=open(outname,'w')
		out1.write(xmlout.encode('gbk'))
		##print xmlout >out1,outname
		out1.close()
def pngs2html(reldirlist,outname,newtit):
	with codecs.open(os.path.join('',r"guidata\Tmp\Htmltemp.html"),'rb') as f2:
		content,begflag,endflag,new=f2.read(),'<img src="','</br>',[]
		titbeg,titend='<title>','</title>'
		#matchline=[line for line in content if begflag in line][0]
		#content=content.repalce("title>##NAME##</title","title>"+newtit+"</title")
		matchtag=content[content.find(begflag):content.rfind(endflag)+len(endflag)]
		oldstr=matchtag[matchtag.find(begflag)+len(begflag):matchtag.rfind('" display')]
		#repeach=matchtag.replace(oldstr,ele)content[:content.index(begflag)]
		new.extend([matchtag.replace(oldstr,ele) for ele in reldirlist])
		titrep=content[:content.find(titbeg)+len(titbeg)]+newtit+content[content.rfind(titend):content.index(begflag)]
		writeout=titrep+"".join(new)+content[content.rfind(endflag)+len(endflag):]
		out=open(outname,'w')
		out.write(writeout.encode('gbk'))
		out.close()
if __name__ == "__main__":

	if getattr(sys,'frozen',False):
		pyrealpath = sys._MEIPASS
	else:
		pyrealpath = os.path.split(os.path.realpath(__file__))[0]
	import guidata,subprocess
	_app = guidata.qapplication()
	if ppt_diago.edit():pass#如果面板被编辑过。
#print(ppt_diago)
	ppt_diago.view()
	args=ppt_diago.__dict__
	pptname = args["_PPTnames"][0]
	label=os.path.basename(pptname).split('.')[0]
	#print label--文件的名字，后缀之前的部分
	if pptname.find(" ") < 0 :#if filebam have jongg
		vbpptname=pptname
	else:
		vbpptname=chr(34)+args["_PPTnames"][0]+chr(34)
	raw=args["_outpath"]
	if raw.find(" ") < 0 :#if filebam have jongg
		vbout=raw
	else:
		vbout=chr(34)+raw+chr(34)
	width = args["_newsize"]
	#print raw---选择的输出路径，在该路径下生成以label 为名称的文件夹
	#pyrealpath=os.path.split(os.path.realpath(__file__))[0]#'os.path.split(sys.argv[0])[0]
	pdfout,tmp= 1,os.path.join(raw,label,str(width))
	#print pyrealpath
	tmp2 =os.path.join(raw,label,"Slides")
	newtitle=args["_outname"] if args["_outname"]!= '' else label
	#print tmp2---slide 的文件夹
	if 2 not in args["_outFormat"]:pdfout=0
	##################CHQ RU JIANQIE VB CHENGXU
	cmd=" ".join([os.path.join(pyrealpath,r"guidata\Tmp\wscript.exe ")+os.path.join(pyrealpath,r"guidata\Tmp\PPT_Panel.vbs"),vbpptname,str(width),vbout,str(pdfout)]).encode('gbk')
	#print cmd
 #cmd=" ".join([r"C:\Windows\system32\wscript.exe "+os.path.join(pyrealpath,r"guidata\Tmp\PPT_Panel.vbs"),vbpptname,str(width),vbout,str(pdfout)])
	child=subprocess.Popen(cmd)#
	child.wait()
	#print ('sucess')
	if os.path.exists(tmp) and os.path.exists(tmp2):#710cunzai
		renamePngs(tmp)
		renamePngs(tmp2)
		relativepath=["".join([r"..","\\",str(width),"\\",i]) for i in os.listdir(tmp)]#str(i).zfill(2)
		relativerawpath=["".join([r"..\Slides","\\",k]) for k in os.listdir(tmp2)]
		outdir=tempfile.mkdtemp(prefix=str(width)+"PPTMerged_",dir=os.path.join(raw,label))
		mergename_Sets=[r".pdf",r".png",r".html",r".xml",r'_raw.png',r"_raw.html",r"_raw.xml"]
		pdfname,lpngname,htmlname,xmlname,rlpngname,rawhtmlname,rawxmlname=[os.path.join(outdir,label+name) for name in mergename_Sets]
		if os.path.isfile("".join([raw,"\\",label,"\\",label,r".pdf"])):
			shutil.move("".join([raw,"\\",label,"\\",label,r".pdf"]),outdir)
		try:
			Mbox(u"我还在运行...",u'不要着急..我还在努力的拼...完成的时候还会看见我..',0)
			pngs2xml(relativepath,xmlname,newtitle)
			if 0 in args["_outFormat"]and args["_raw"]:
				pngs2xml(relativerawpath,rawxmlname,newtitle)

			pngs2html(relativepath,htmlname,newtitle)
			if 4 in args["_outFormat"] and args["_raw"]:
				pngs2html(relativerawpath,rawhtmlname,newtitle)
			if 1 in args["_outFormat"] and args["_resize"]:
				png2pngs(tmp,lpngname)#Imgarr,lpng=
			if 1 in args["_outFormat"] and args["_raw"]:
				png2pngs(tmp2,rlpngname)
			Mbox(u'哈哈我又出现啦', u'看见我应该就是成功了~~快去输出目录看一下 \n'+raw, 0)
			#print ('ok')
		except:
			print sys.exc_info()
			Mbox(u'Sorry', u'Something Error,Change filename to English and retry', 1)
			#raw_input('press anykey to exit')


"""
if os.path.isfile(pdfname) and os.path.isfile(lpngname) and os.path.isfile(htmlname) and os.path.isfile(xmlname):
	user32.MessageBoxA(0,"Finished Sucessdully! GO and Check Your file",'Ctypes',0)"""