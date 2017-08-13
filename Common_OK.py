# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see guidata/__init__.py for details)

"""
All guidata DataItem objects demo
A DataSet object is a set of parameters of various types (integer, float,
boolean, string, etc.) which may be edited in a dialog box thanks to the
'edit' method. Parameters are defined by assigning DataItem objects to a
DataSet class definition: each parameter type has its own DataItem class
(IntItem for integers, FloatItem for floats, StringItem for strings, etc.)
"""

from __future__ import print_function

SHOW = True # Show test in GUI-based test launcher

import os,shutil

from guidata.dataset.datatypes import DataSet, BeginGroup, EndGroup,GetAttrProp, FuncProp,DataSetGroup
from guidata.dataset.dataitems import (IntItem, BoolItem,MultipleChoiceItem,FilesOpenItem,StringItem,FileSaveItem,DirectoryItem)


# Creating temporary files and registering cleanup functions
#TEMPDIR = tempfile.mkdtemp(prefix="test_",dir=os.getcwd())
#atexit.register(shutil.rmtree, TEMPDIR)
#FILE_ETA = tempfile.NamedTemporaryFile(suffix=".eta", dir=TEMPDIR)
#atexit.register(FILE_ETA.close)
#FILE_ppt = tempfile.NamedTemporaryFile(suffix=".ppt", dir=TEMPDIR)
#atexit.register(FILE_ppt.close)

class TestParameters(DataSet):
    """
    PPT_Converter:Based on Glance
Choose according to your demond
    """
    def updatedir(self, item, value):
        print("\nitem: ", item, "\nvalue:", value)
        if self.PPTnames and value[0] :
            self.outpath = os.path.split(value[0])[0]
            print(os.path.split(value[0]))
            if len(value) > 0:#如果只是选择了单个文件
                self.outprefix=os.path.basename(value[0]).split('.')[0]

            else:#选了多个文件
                self.outpath = os.getcwdu()
                self.outprefix= None
            self.WebTitle=self.outprefix
            print("\nitem: ", self.outpath, "\nvalue:", self.WebTitle)
            #self.ImagesDirName=str(self.newsize)
#			self.htmlTitle=self.outprefix
    #fname = FileOpenItem("Open file", "ppt", FILE_ppt.name)
    #_eg = StartGroup("Convert_Mode")
    g0=BeginGroup("Select Your PPTs to Manipulate")
    PPTnames = FilesOpenItem("OpenPPTs", ("ppt", "pptx"),help="Select your PPT files",all_files_first=True).set_prop('display',callback=updatedir)##list
    outpath = DirectoryItem("OutPath",
				help="Select the output path.\nDefault is the path where you choose your PPT").set_prop('display',active=True)
    WebTitle=StringItem('HTML/XML Title\n(Glance)',
					help="The Title of the generated html/xml file.\nDefault is the PPT's filename").set_prop('display',active=True)
    outprefix=StringItem('OutFilePrefix',help="The prefix of generated file .\nDefault is the ppt name ").set_prop('display',active=True)
    _g0=EndGroup("Select Your PPTs to Manipulate")

    g1=BeginGroup("Select Your Convert_Mode")
#    outMode = MultipleChoiceItem("",
#                                  ["Raw", "Resized",
#                                   ],help="(default concated)",default=(1,)).horizontal(1)#.set_pos(col=1)
    raw=BoolItem("Raw",default=False,help="Those Generated Files will Use Pngs Exported from PPT Slides Without any Crop or Resize").set_pos(col=0)
    _prop = GetAttrProp("resize")
    #choice = ChoiceItem('Choice', choices).set_prop("display", store=_prop)
    resize = BoolItem("Resized",default=True,help="Means You Want to Resize those Raw Pngs Before Use Them In Your Final Formats\ ").set_pos(col=1).set_prop("display", store=_prop)
    newsize = IntItem("NewSize\n(width_dpi)", default=709, min=0, help="The Value Must be lower than the raw png's Width!",max=2160, slider=True).set_prop("display",active=FuncProp(_prop, lambda x: x))
    ImagesDirName=StringItem('ImagesDirName',
		help="The DirName of Resized Pngs used in Html/Xml/LongPng file.\nDefault is the Png wideth size If You Leave It Empty").set_prop('display',active=FuncProp(_prop, lambda x: x))

    _g1 = EndGroup("Select Your Convert_Mode")
    g2=BeginGroup("Which Format Do U Want To Generate")
    must=BoolItem("Pngs",default=True,help="You Cannot Remove Pngs If You Want to Get Other Types.").set_prop("display",active=0).set_pos(col=0)
    outFormat = MultipleChoiceItem("Optional",
                                  ["Long_Png","PDF","HTML","XML"],help="(Default all,But I won't give U the Long_Png with Raw Pngs.\nAnd the 1st choice('Pngs') is default to generate.)",
                                  default=(1,2,3)).horizontal(1).set_pos(col=1)
    _g2=EndGroup("Which Format Do U Want To Generate")


    #_eg = EndGroup("Convert_Mode")
#ORI=os.sep
#os.sep="\\"
ppt_diago = TestParameters("Glance")
ppt_qg=TestParameters("QuickGuide")
#excel_diago = TestParameters("Excel")

if __name__ == "__main__":
#     #Create QApplication
     import guidata,subprocess
     _app = guidata.qapplication()
     if ppt_diago.edit():#如果面板被编辑过。
         pass#print(ppt_diago)
     ppt_diago.view()
     args=ppt_diago.__dict__
     pptname=args["_PPTnames"][0]#+chr(34)chr(34)+
     newsize=args["_newsize"]
     outpath=args["_outpath"]
     pdfout=1
     if 2 not in args["_outFormat"]:
         pdfout=0
#     cmd=r"C:\Windows\system32\wscript.exe D:\untar\selfwidth\dist\dist\11PPTiSuiteSelfWidth.vbs "
#     cmd+= ur' '.join([pptname,str(newsize),outpath,str(pdfout)])#4 parameters)                                                                                                     outpath])
#     subprocess.Popen(cmd)