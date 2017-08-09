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

import os,shutil,datetime

from guidata.dataset.datatypes import DataSet, BeginGroup, EndGroup,GetAttrProp, FuncProp,DataSetGroup
from guidata.dataset.dataitems import (IntItem, BoolItem,TextItem,DateTimeItem,
                             MultipleChoiceItem,FilesOpenItem,
                             StringItem,
                             DirectoryItem)


# Creating temporary files and registering cleanup functions
#TEMPDIR = tempfile.mkdtemp(prefix="test_",dir=os.getcwd())
#atexit.register(shutil.rmtree, TEMPDIR)
#FILE_ETA = tempfile.NamedTemporaryFile(suffix=".eta", dir=TEMPDIR)
#atexit.register(FILE_ETA.close)
#FILE_ppt = tempfile.NamedTemporaryFile(suffix=".ppt", dir=TEMPDIR)
#atexit.register(FILE_ppt.close)

class TestParameters(DataSet):
    """
    PPT Converter
Choose according to your function
    """

    #fname = FileOpenItem("Open file", "ppt", FILE_ppt.name)
    #_eg = StartGroup("Convert_Mode")
    PPTnames = FilesOpenItem("Open_files", ("ppt", "pptx"),help="Input your PPT file")##list
    outpath = DirectoryItem("OutDirectory",default=PPTnames._props["data"]["basedir"],help="default is the PPt path")
    outname=StringItem('Outlabel',help="default is the ppt name ")
    dtime = DateTimeItem("Date/time", default=datetime.datetime(2017, 10, 10))#text = TextItem("Text")
    g1=BeginGroup("Convert_Mode")
#    outMode = MultipleChoiceItem("",
#                                  ["Raw", "Resized",
#                                   ],help="(default concated)",default=(1,)).horizontal(1)#.set_pos(col=1)
    raw=BoolItem("Raw",default=False,help="normal mode").set_pos(col=0)
    _prop = GetAttrProp("resize")
    #choice = ChoiceItem('Choice', choices).set_prop("display", store=_prop)
    resize = BoolItem("Resized",default=True,help="normal mode").set_pos(col=1).set_prop("display", store=_prop)
    newsize = IntItem("NewSize(width_dpi)", default=709, min=0, help="if changed,dpi",max=2160, slider=True).set_pos(col=2).set_prop("display",
                                  active=FuncProp(_prop, lambda x: x)).set_pos(col=2)
    _g1 = EndGroup("Convert_Mode")
    outFormat = MultipleChoiceItem("OuterForm",
                                  ["Pngs","Con_Pngs","PDF","HTML","XML"],help="(default all)",
                                  default=(0,1,2,3,4),
                                  ).horizontal(1)


    #_eg = EndGroup("Convert_Mode")

ppt_diago = TestParameters()
#excel_diago = TestParameters("Excel")

if __name__ == "__main__":
#     #Create QApplication
     import guidata,subprocess
     _app = guidata.qapplication()
#
#    #ppt = TestParameters()
#    #e.floatarray[:, 0] = np.linspace( -5, 5, 50)
#    #print(e)
     #g = DataSetGroup( [ppt_diago, excel_diago], title='Office group' )
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
     cmd=r"C:\Windows\system32\wscript.exe D:\untar\selfwidth\dist\dist\11PPTiSuiteSelfWidth.vbs "
     cmd+= ur' '.join([pptname,str(newsize),outpath,str(pdfout)])#4 parameters)                                                                                                     outpath])
     subprocess.Popen(cmd)