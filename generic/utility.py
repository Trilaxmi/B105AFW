import openpyxl
class Excel:
    @staticmethod
    def get_data(filepath,sheet_name,row,col):
      try:
           wb= openpyxl.load_workbook(filepath)
           sheet=wb[sheet_name]
           value=sheet.cell(row,col).value
           if value==None:
               print("Cell value is NONE")
               value=""
      except Exception as e:
           print(str(e))
           value=""

      return value
