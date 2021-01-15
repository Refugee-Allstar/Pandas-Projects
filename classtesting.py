import pandas as pd

class ExcelTemplate:
    
    df = pd.read_excel('SampleData.xlsx', sheet_name='SalesOrders')
    
    def __init__(self):
        self.df = ExcelTemplate.df

    def delete_rows(self, num_rows):
        return self.df.iloc[num_rows:]
        #self.filter = ExcelTemplate.df[ExcelTemplate.df['Region']==region]
        
    @staticmethod
    def over_hundred(df, cutoff):
        return df[df['Total'] > cutoff]


dataframe1 = ExcelTemplate()

print(dataframe1.delete_rows(10))


dataframe2 = ExcelTemplate()
print(dataframe2.df)







#test_frame1 = ExcelTemplate(7)
#test_frame2 = ExcelTemplate(0)

#test_frame3 = ExcelTemplate(7, 'Central')
#test_frame4 = ExcelTemplate(1, 'East')
#test_frame5 = ExcelTemplate(1)
#print(test_frame5.over_hundred(test_frame5.filter, 500))
#print(test_frame3.over_hundred(test_frame3.filter, 250))
