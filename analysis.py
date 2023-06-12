import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def filterFunction(col_series):
    result_df = col_series.to_frame()
    options = []
    # Iterate over the column
    for idx, value  in col_series.iteritems():
        for option in value.split(';'):
            if not option in result_df.columns:
                options.append(option)
                result_df[option] = False
            # Mark the value in the option column as True
            result_df.at[idx, option] = True
    return result_df[options]

data = pd.read_csv("/home/niteshpant/Desktop/data/survey_results_public.csv")

#print(data.head(10))
#print(data.columns)
#print(data.RemoteWork)             # remote, hybrid, in-person
#print(data.DatabaseHaveWorkedWith.value_counts().head(10))      # databases developer have worked with
#print(data.DatabaseHaveWorkedWith.head(10))
databaseData = data.dropna(subset=['DatabaseHaveWorkedWith'])
#db = databaseData['DatabaseHaveWorkedWith'].str.split(';', expand = True)
#print(db.stack().value_counts())
#result = filterFunction(databaseData.DatabaseHaveWorkedWith)
#print(result.head(10))

# gender of coder
'''
databaseData = data.dropna(subset=['Gender'])
#print(databaseData.Gender.value_counts())
gen = databaseData['Gender'].str.split(';', expand = True)
#print(gen.head(10))
#print(gen.stack().head(10))
#print(gen.stack().value_counts())
'''

# location/country of coder
'''
#print(databaseData.Country.value_counts().head())   # top 5 country developers
'''

'''
education = databaseData.EdLevel.value_counts().plot(kind='barh')
print(education)
education = databaseData.EdLevel.value_counts()
fig = plt.figure(figsize = (10, 5))
plt.barh(education.index, education.values, color ='maroon')
 
plt.xlabel("Courses")
plt.ylabel("No. of students")
plt.title("Education level of user")
plt.show()
'''

'''
dbData = databaseData["DatabaseHaveWorkedWith"].str.split(';', expand = True)
print(dbData.stack().value_counts())
dbData2 = databaseData["DatabaseWantToWorkWith"].str.split(';', expand = True)
print(dbData2.stack().value_counts())
'''

'''
# status of coder (student/ working professional/ freelancer etc)
newData = data.dropna(subset=["Employment"])
status = newData["Employment"].str.split(',', expand = True)
status = status.stack().value_counts().to_frame()
print(status)
#status = pd.DataFrame(status)     
status = status.reset_index()
status.columns = ["Status", "count"]
print(status)
'''