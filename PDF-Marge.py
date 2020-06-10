import os
import PyPDF2
import datetime

############# 実行DirをPythonプログラムファイルのある場所に移動 #############
os.chdir(os.path.dirname(os.path.abspath(__file__))) #pythonの実行Dirを移動する

############# 出力ファイル名を時間で指定
date = datetime.datetime.now()
OutputName = "Marge-" + str(date.year) + str(date.month) + str(date.day) + str(date.hour) + str(date.minute) + str(date.second) + ".pdf"

############# コンソール表示
print("")
print("========== ２つのPDFファイルを結合します ==========")
print("")
PDF1 = input("ファイル１を選択（ファイルパス） → ") #入力ファイル１
PDF2 = input("ファイル２を選択（ファイルパス） → ") #入力ファイル２


############# メインプログラム #############
File1 = open(PDF1, "rb")
File2 = open(PDF2, "rb")
Reader1 = PyPDF2.PdfFileReader(File1)
Reader2 = PyPDF2.PdfFileReader(File2)
Writer = PyPDF2.PdfFileWriter()

for page in range(Reader1.numPages):
    Obj = Reader1.getPage(page)
    Writer.addPage(Obj)

for page in range(Reader2.numPages):
    Obj = Reader2.getPage(page)
    Writer.addPage(Obj)


OutputFile = open(OutputName, "wb")
Writer.write(OutputFile)
OutputFile.close()
File1.close()
File2.close()

print("Finish")