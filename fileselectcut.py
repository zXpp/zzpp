# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:16:20 2017

@author: z81022868
"""

import tempfile, atexit, shutil
#import numpy as np

from guidata.dataset.datatypes import (DataSet, ObjectItem)
from guidata.dataset.dataitems import ( FilesOpenItem,
                             StringItem,DirectoryItem)

from guidata.dataset.qtwidgets import DataSetEditLayout, DataSetShowLayout
from guidata.dataset.qtitemwidgets import DataSetWidget


# Creating temporary files and registering cleanup functions
TEMPDIR = tempfile.mkdtemp(prefix="test_")
atexit.register(shutil.rmtree, TEMPDIR)

FILE_xlsm = tempfile.NamedTemporaryFile(suffix=".xlsm", dir=TEMPDIR)
atexit.register(FILE_xlsm.close)

class SubDataSet(DataSet):
    dir = DirectoryItem("Directory", TEMPDIR)
    #fname = FileOpenItem("Single file (open)", ("xlsm", "eta"), FILE_xlsm.name)
    fnames = FilesOpenItem("Multiple_files", "xlsm", FILE_xlsm.name)
    #fname_s = FileSaveItem("Single file (save)", "eta", FILE_ETA.name)

class SubDataSetWidget(DataSetWidget):
    klass = SubDataSet

class SubDataSetItem(ObjectItem):
    klass = SubDataSet

DataSetEditLayout.register(SubDataSetItem, SubDataSetWidget)
DataSetShowLayout.register(SubDataSetItem, SubDataSetWidget)


class TestExcel(DataSet):
    """
    zx_FileSelector
    """
    files = SubDataSetItem("ExcelFiles:")
    string = StringItem("SheetName:")
#==============================================================================
# if __name__ == "__main__":
#     # Create QApplication
#     import guidata
#     _app = guidata.qapplication()
#     #app.exec_()
#     e = TestParameters()
#     #e.view()
#     #e.floatarray[:, 0] = np.linspace( -5, 5, 50)
#     #print(e)
#     if e.edit():pass
# #        e.edit()
# #        print(e)
#     e.view()
#==============================================================================
    #e.files.fnames