# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:23:13 2017

@author: z81022868
"""
#from __future__ import unicode_literals

import sys,os,tempfile,codecs,shutil#ctypes,
#dd=[i for i in os.listdir(os.getcwd()) if os.path.isdir(i)]

#sys.path.append(r"util\pyLib")
#import ,img2pdf
import numpy as np
from PIL import Image,ImageFilter
#from fpdf import FPDF as FPDF
#user32 = ctypes.cdll.user32
# win32api.ShellExecute(0, 'open', 'ppt2png.vbs', '','',1)
pypath=sys.argv[2]#os.path.realpath(sys.argv[0])
pyrealpath=pypath.encode('utf-8')
#print pypath
sys.path+=[os.getcwd(),os.path.join(pyrealpath,r"util\pyLib")]
pptabspath=sys.argv[1]#u"C:\\Users\\z81022868\\Desktop\\通过建立组件库提升FLASH动画开发效率优秀实践g00175366.ppt"#
#a=u'C:\\Users\\z81022868\\Desktop\\\xcd\xa8\xb9\xfd\xbd\xa8\xc1\xa2\xd7\xe9\xbc\xfe\xbf\xe2\xcc\xe1\xc9\xfdFLASH\xb6\xaf\xbb\xad\xbf\xaa\xb7\xa2\xd0\xa7\xc2\xca\xd3\xc5\xd0\xe3\xca\xb5\xbc\xf9g00175366.ppt'
#print pptabspath
##print type(pptabspath)
width=sys.argv[3]
#print width
raw=sys.argv[4]
#print raw
#raw=os.path.splitext(pptabspath)[0]#D:\zx\特性Glance格式转换工具需求分析
pptname=os.path.basename(pptabspath).split(".")[0]##特性Glance格式转换工具需求分析
#chouse=os.path.splitext(pptpath)[0]#r"D:\zx\DL\ppt2png\Wei\Finished"#PPT文件名
tmp=raw+"\\"+width.encode('utf-8') #r'C:\Program Files (x86)\11sample-1.0\710'destination)
tmp2=raw+r'\Slides'.encode('utf-8')
#print tmp

def renamePngs(path):#tmp/tmp2
    #dock=[]
    for root,dirs,files in os.walk(path):    #遍历统计
        for each in files:
            fileabs=os.path.join(root,each)#dirs=[]
            pre=os.path.splitext(fileabs)[0]
            nochang=pre.rpartition("_")#
            if len(nochang[-1])< len(nochang[-1].zfill(3)):
                shutil.move(fileabs,"_".join([nochang[0],nochang[-1].zfill(3)+r".png"]))
        break
   ##print files
    #return dock#absfile
#def getpngnum(path):
#    count=0
#    for root,dirs,files in os.walk(path):    #遍历统计
#      for each in files:
#              os.rename(each,)
#             count += 1   #统计文件夹下文件个数
#    return count
''''''
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
    #return sz

def pngs2pdf(indir,outname,size):#size
 #from fpdf import FPDF
 #import os
    #p:poritate (width,height) abd wid>height,'L':(height,width) and height<width
    pdf = FPDF('P','pt',size) if size[1] == max(size) else FPDF('L','pt',size[::-1])#708*1278pt---point
    pdf.set_xy(0,0)
    pdf.set_margins(0,0,0)
    pdf.auto_page_break

    for img in os.listdir(indir):
        suffix=os.path.splitext(img)[1][1:]
        if suffix in ['png','PNG']:
            #print img
            pdf.add_page(same=True)
            pdf.image(os.path.join(indir,img),x=0,y=0)
    pdf.output(outname,'F')#pdf.output(os.path.join(indir,"merged.pdf"),'F')

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

#os.path.join(r"..","710","".join([pptname,"_",str(i),r".png"]))
if os.path.exists(tmp) and os.path.exists(tmp2):#710cunzai
	#destdir=raw+r"\Out_merged"#直接在目标文件夹下生产ImageMagick-7.0.6-Q16\tmp
	renamePngs(tmp)
	renamePngs(tmp2)
	relativepath=["".join([r"..","\\",width,"\\",i]) for i in os.listdir(tmp)]#str(i).zfill(2)
	relativerawpath=["".join([r"..\Slides","\\",i]) for i in os.listdir(tmp2)]
	outdir=tempfile.mkdtemp(prefix=width+"PPTMerged_",dir=raw)
# 	if os.path.exists(outdir) and os.stat(outdir).st_ctime < time.time():
#      outdir=outdir+"latest"
#     #subprocess.check_call(ren diakabc.spc sisc.spa)os.rmdir(outdir)#pdf2htmlEX-win32\
	#os.makedirs(outdir)
	#shutil.move(chouse+r'\out',outdir)
	mergename_Sets=[r".pdf",r".png",r".html",r".xml",r'_raw.png',r"_raw.html",r"_raw.xml"]
	#mergename_Sets=[r"\mergedraw.pdf",r"\merged.pdf",r"\merged.png",r"\merged.html",r"\merged.xml",r'\merged_raw.png',r"\merged_raw.html",r"\merged_raw.xml"]
	#rpdfname,pdfname,lpngname,htmlname,xmlname,rlpngname,rawhtmlname,rawxmlname=[outdir+name for name in mergename_Sets]
	pdfname,lpngname,htmlname,xmlname,rlpngname,rawhtmlname,rawxmlname=[os.path.join(outdir,pptname+name) for name in mergename_Sets]
	if os.path.isfile("".join([raw,"\\",pptname,r".pdf"])):
		shutil.move("".join([raw,"\\",pptname,r".pdf"]),outdir)
	pngs2xml(relativepath,xmlname)
	pngs2xml(relativerawpath,rawxmlname)
	pngs2html(relativepath,htmlname)
	pngs2html(relativerawpath,rawhtmlname)
	#print "Html,Xml,Pdf Files Gentrenated Successfully!"
	#print "Concatenating Resized pngs to longpng......"
	png2pngs(tmp,lpngname)#Imgarr,lpng=
	#print "Concatenating Raw slides to rawlongpng......"
	png2pngs(tmp2,rlpngname)
	#print "Finished Sucessdully! GO and Check Your file\n"
	#raw_input("Press any key to exit......")
	##print "Concatenating Resized Pngs to Pdf....."
	#pngs2pdf(tmp,pdfname,s710)
#        #print "Concatenating Raw Pngs to Pdf....."
	#pngs2pdf(tmp2,rpdfname,sizeraw)
"""
if os.path.isfile(pdfname) and os.path.isfile(lpngname) and os.path.isfile(htmlname) and os.path.isfile(xmlname):
	user32.MessageBoxA(0,"Finished Sucessdully! GO and Check Your file",'Ctypes',0)"""