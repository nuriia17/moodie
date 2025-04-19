import pandas as pd
students = {"Matmie the best":40, "Mat Dais":35, "COMIE":45, "COMEC":50}
students_series = pd.Series(students)
print(students_series)
print(type(students))
import pandas as pd
months = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], index=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
print(months)
print(type(months))
import pandas as pd
exam_data = {
    'name':["Anastasia", "Dima", "Katherine", "James", "Emily", "Michael", "Matthew", "Laura", "Kevin", "Jonas"],
    'score':[12.5, 9, 16.5, 'np.nan', 9, 20, 14.5, 'np.nan', 8, 19],
    'attempts':[1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify':['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

filtered_df = df[df['qualify']== "yes" ]
print("number of attempts in the examination is greater than 2:")
print(filtered_df)


