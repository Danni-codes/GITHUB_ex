import pandas as pd
import numpy as np

patients = pd.DataFrame({
    "patientid": ["P01", "P02", "P03", "P04", "P05", "P06"],
    "glucosemmol_l": [4.8, 6.1, 8.4, 5.2, 7.2, 3.9]
})

patients["glucose_status"] = np.where(
    patients["glucosemmol_l"] < 4.0,
    "low",
    np.where(
        patients["glucosemmol_l"] >= 7.0,
        "high",
        "normal"
    )
)

print(patients)