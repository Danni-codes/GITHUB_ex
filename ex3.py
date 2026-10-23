import pandas as pd

bp = pd.DataFrame({ 
    "patient_id": ["P01", "P02", "P03", "P04", "P05"], 
    "systolic": [118, 135, 142, 125, 155], 
    "diastolic": [76, 82, 91, 79, 95] 
})

avg_mean_systolic = bp["systolic"].mean()
avg_mean_diastolic = bp["diastolic"].mean()

print(avg_mean_systolic)
print(avg_mean_diastolic)