import pandas as pd

patients = pd.DataFrame({ 
    "patientid": ["P01", "P02", "P03", "P04", "P05"], 
    "spo2before": [94, 91, 96, 89, 93], 
    "spo2_after": [97, 95, 97, 94, 96] 
})


patients["spo2_change"] = patients["spo2_after"] - patients["spo2before"]
maxchange = patients["spo2_change"].idxmax()


print(patients)
print(patients["spo2_change"][maxchange])

