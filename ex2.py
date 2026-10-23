import pandas as pd

patients = pd.DataFrame({
    "patientid": ["P01", "P02", "P03", "P04", "P05", "P06"],
    "heartrate": [72, 88, 105, 64, 112, 79]
})

# Filtrer patienter med puls over 100
high_hr = patients[patients["heartrate"] > 100]

print(high_hr)
