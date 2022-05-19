# -*- coding: utf-8 -*-
print("------------------------------------------------------")
print("---------------- Metadata Information ----------------")
print("------------------------------------------------------")
print("")

print("In the name of God")
print("Project: AutoCML: Automatic Comparative Machine Learning in COVID-19 Detection Model")
print("Creator: Mohammad Reza Saraei")
print("Contact: m.r.saraei@seraj.ac.ir")
print("University: Seraj Institute of Higher Education")
print("Supervisor: Dr. Saman Rajebi")
print("Created Date: May 20, 2022")
print("") 


print("----------------------------------------------------")
print("------------------ Import Libraries ----------------")
print("----------------------------------------------------")
print("")

# Import Libraries for Python
import pandas as pd

print("----------------------------------------------------")
print("------------------ Data Ingestion ------------------")
print("----------------------------------------------------")
print("")

# Import DataFrames (.csv) by Pandas Library
df_PLS = pd.read_csv(r"D:\My Papers\2020 - 2030\Journal Paper\Journal of Communications Technology and Electronics [IF=0.5] (2022)\CoV19 Dataset\Detection\Encoded Data\CoV19_PLS_Encoded.csv")
df_CLS = pd.read_csv(r"D:\My Papers\2020 - 2030\Journal Paper\Journal of Communications Technology and Electronics [IF=0.5] (2022)\CoV19 Dataset\Detection\Encoded Data\CoV19_CLS_Encoded.csv")
df_EHR = pd.read_csv(r"D:\My Papers\2020 - 2030\Journal Paper\Journal of Communications Technology and Electronics [IF=0.5] (2022)\CoV19 Dataset\Detection\Encoded Data\CoV19_EHR_Encoded.csv")
df_PCR = pd.read_csv(r"D:\My Papers\2020 - 2030\Journal Paper\Journal of Communications Technology and Electronics [IF=0.5] (2022)\CoV19 Dataset\Detection\Encoded Data\CoV19_PCR_Encoded.csv")

# Fusion of DataFrames
df = pd.concat([df_PLS, df_CLS, df_EHR, df_PCR], axis = 1)            
# df = np.concatenate((df_PLS, df_CLS, df_EHR, df_PCR), axis = 1)

# Delet Column "Gender" from Dataframe
df = df.drop("Gender", axis = 1)

print("------------------------------------------------------")
print("----------------- Data Annotation --------------------")
print("------------------------------------------------------")
print("")

# [0 = Not-Confirmed]
# [1 = Suspected (Needing Lung CT)]
# [2 = Suspected (Needing CBC, ESR, LDH, D-Dimer, & CRP)]
# [3 = Confirmed]

df['Target'] = 0                                                    
#range(0, len(df))

def target(row):
    if   ((row['RT_PCR'] == 1) | (row['RT_PCR'] == 2)):
        return "3" 
    elif (row['RT_PCR'] == 0)  & ((row['Dyspnea'] == 1) | (row['LoS_M_C'] == 1) | (row['Ch_P'] == 1)):
        return "1"
    elif (row['RT_PCR'] == 0) & ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4) | (row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3) | (row['Cough'] == 1) | (row['Cough'] == 2) | (row['Cough'] == 3) | (row['Fatigue'] == 1) | (row['Fatigue'] == 2) | (row['Headache'] == 1) | (row['LoT_S'] == 1) | (row['GI'] == 1) | (row['Dyspnea'] == 1) | (row['LoS_M_C'] == 1) | (row['Ch_P'] == 1)):
        return "2"
    elif (row['RT_PCR'] == 0) & ((row['Pyrexia'] == 0) & (row['Hypoxemia'] == 0) & (row['Cough'] == 0) & (row['Fatigue'] == 0) & (row['Headache'] == 0) & (row['LoT_S'] == 0) & (row['GI'] == 0) & (row['Dyspnea'] == 0) | (row['LoS_M_C'] == 0) | (row['Ch_P'] == 0)):
        return "0"
    else:
        return "0"

df = df.assign(Target=df.apply(target, axis = 1))

print("")

print("----------------------------------------------------")
print("----------------- Saving Outputs -------------------")
print("----------------------------------------------------")
print("")

# Save DataFrame After Encoding
df.to_csv(r"D:\My Papers\2020 - 2030\Journal Paper\Journal of Communications Technology and Electronics [IF=0.5] (2022)\CoV19 Dataset\Detection\Annotated Data\CoV19_Data_Annotated.csv", index = False)

print("----------------------------------------------------")
print("--------- Thank you for waiting, Good Luck ---------")
print("--------- Signature: Mohammad Reza Saraei ----------")
print("----------------------------------------------------")

