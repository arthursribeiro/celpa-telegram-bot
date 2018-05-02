import xlwings as xw
xlfile = 'MacroJPG.xlsm'
wb = xw.Book(xlfile)
macro = wb.macro('ExportarAreaParaJPG')
macro()

print 'Finished!'