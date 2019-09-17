dataset = [[90, 1.8], [75, 1.9], [130, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

for patient in dataset:
    weight, height = dataset[0]
    bmi = calculate_bmi(weight, height)
    print("Patient's BMI is: %f" % bmi)
