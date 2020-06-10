import os
import PyPDF2
import datetime

############# 実行DirをPythonプログラムファイルのある場所に移動 #############
os.chdir(os.path.dirname(os.path.abspath(__file__))) #pythonの実行Dirを移動する

############# 出力ファイル名を時間で指定
date = datetime.datetime.now()
OutputName = "Rotate-" + str(date.year) + str(date.month) + str(date.day) + str(date.hour) + str(date.minute) + str(date.second) + ".pdf"


############# コンソール表示
print("")
print("========== PDFファイルを回転させます ==========")
print("")
PDF = input("ファイルを選択（ファイルパス） → ") #入力ファイル名
angle = int(input("回転する角度を入力してください（90,180,270) → ")) #回転角度

############# メインプログラム #############
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

print("Finish")