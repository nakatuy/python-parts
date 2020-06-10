import os
import PyPDF2
import datetime

############# 実行DirをPythonプログラムファイルのある場所に移動 #############
os.chdir(os.path.dirname(os.path.abspath(__file__))) #pythonの実行Dirを移動する

############# 出力ファイル名を時間で指定
date = datetime.datetime.now()

############# コンソール表示
print("")
print("========== PDFツール Ver.202006 ==========")
print("")
pdf_function = input("PDFモード選択 [回転：r] [結合：m] → ") #PDFモード選択

############# PDF 回転関数 #############
def pdf_rotater(PDF,angle):
    File = open(PDF, "rb")
    Reader = PyPDF2.PdfFileReader(File)
    Writer = PyPDF2.PdfFileWriter()
    for page in range(Reader.numPages):
        obj = Reader.getPage(page)
        obj.rotateClockwise(angle)
        Writer.addPage(obj)

    Output = open(OutputName, "wb")
    Writer.write(Output)
    Output.close()
    File.close()

    return 

############# PDF 結合関数 #############
def pdf_marge(PDF1,PDF2):
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

    return

############# メインプログラム #############
if pdf_function == "r":
    PDF = input("ファイルを選択（ファイルパス） → ") #入力ファイル名
    angle = int(input("回転する角度を入力してください（90,180,270) → ")) #回転角度
    OutputName = "Rotate-" + str(date.year) + str(date.month) + str(date.day) + str(date.hour) + str(date.minute) + str(date.second) + ".pdf" #出力ファイル名

    pdf_rotater(PDF,angle)

if pdf_function == "m":
    PDF1 = input("ファイル１を選択（ファイルパス） → ") #入力ファイル１
    PDF2 = input("ファイル２を選択（ファイルパス） → ") #入力ファイル２
    OutputName = "Marge-" + str(date.year) + str(date.month) + str(date.day) + str(date.hour) + str(date.minute) + str(date.second) + ".pdf" #出力ファイル名

    pdf_marge(PDF1,PDF2)


print("")
print(str(OutputName) + "が出力されました")
print("")
input("何かキーを押すと終了します")