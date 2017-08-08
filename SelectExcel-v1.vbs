Set argv = WScript.Arguments
if argv.Count<1 then
	WScript.Quit
end if
xlname = argv(0)
sep = InStrRev(xlname, ".")
if sep = -1 then
	msgbox("No extension detected in xlname: " + xlname)
	WScript.Quit
end if
ext = right(xlname, len(xlname) - sep)

'fullname = left(xlname, sep) + "pdf"
if ext = "xlsm" Or ext = "xlsx" then
	'msgbox(xlname)
	'iSaveAsFileType = 32'pdf
else
	msgbox("Sorry~Not the Specific Excel")
	WScript.Quit
end if

Sub Callpy(xl_name)
	Dim wshShell, fso, loc, cmd,xlpath
	Set fso = CreateObject("Scripting.FileSystemObject")
	loc = fso.GetAbsolutePathName(".")
	'WScript.Echo loc' 你在什么地方点击右键菜单的export pptisuite
	'~ cmd = "%ComSpec% /k python.exe " + loc + "\all.py"
	xlpath=xl_name
	Set wshShell = CreateObject("WScript.Shell")
	scriptpath = fso.GetParentFolderName(Wscript.ScriptFullName)'vbs 程序的放的地方。就是d:\untar\latest
	'WScript.Echo scriptpath
	'WScript.Echo xlpath
	'cmd = "%ComSpec% /keditexcel-v3-2-mody2 "+scriptpath+"\dist\editexcel-v3-2-mody1\editexcel-v3-2-mody1.exe "+pptpath
	cmd = "%ComSpec% /k "+scriptpath+"\dist\editexcel-v3-2-mody2.exe "+ xlpath
	'cmd = "%ComSpec% /k "+"D:\untar\util\python.exe "+scriptpath+"\editexcel-v3-2-mody2.py "+ xlpath
	'WScript.Echo cmd
	
	wshShell.Run cmd,0
End Sub
'ppPres.SaveAs Get_AbsolutePath & exportPreName &".pdf",32,false

Callpy(xlname)

