import pandas as pd

class Dataframe:
    def __init__(self, dataframe, dftype):
        self.df = pd.read_csv(dataframe)
        self.type = dftype
    def replace_country(self, country_to_replace):
        self.df.replace(country_to_replace,'I AM REPLACED YES',regex=True, inplace = True)
        return self.df

class ReportReviewer(Dataframe):
    def __init__(self, dataframe, dftype):
        super().__init__(dataframe, dftype)
        self.df = self.df.iloc[10:]  

class Custom(Dataframe):
    def __init__(self, dataframe, dftype):
        super().__init__(dataframe, dftype)
        self.df = self.df.iloc[20:]
    

class Report20(Dataframe):
    def __init__(self, dataframe, dftype):
        super().__init__(dataframe, dftype)
        self.df = self.df.iloc[30:]

class Reporttc(Dataframe):
    def __init__(self, dataframe, dftype):
        super().__init__(dataframe, dftype)
        self.df = self.df.iloc[40:]

w = ReportReviewer('mortalityRatePoisoning.csv','ReportReviewer')
x = Custom('mortalityRatePoisoning.csv','Custom')
y = Report20('mortalityRatePoisoning.csv','Report20')
z = Reporttc('mortalityRatePoisoning.csv','Reporttc')

control = Dataframe('mortalityRatePoisoning.csv','Poison')


#print(w.replace_country())
print(y.replace_country('Algeria'))
