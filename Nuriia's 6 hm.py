#1 matplotlib line
import matplotlib.pyplot as plt
import numpy as np
x =[1, 2, 3, 4]
y =[2, 4, 6, 8]
z =[1, 3, 5, 7]
c =[0, 2, 0, 2]
plt.plot(x, y, z, c)
plt.show()

#2 matplotlib bars
x = np.array(['Nuriia', 'Asiia', 'Aliia', 'Aiida'])
y = np.array([8, 5, 3, 11])
plt.barh(x,y, height = 0.5, color = 'red')
plt.show()

#3 matplotlib scatter
x = np.array([3, 4, 6, 2, 7, 8, 4, 9])
y = np.array([34, 65, 23, 67, 33, 55, 32, 12])
sizes = np.array([10, 20, 30, 40, 50, 60, 70, 80])
plt.scatter(x,y, s=sizes, alpha = 1, color = 'black')
plt.show()

#4 matplotlib pie chart
x = np.array([40, 24, 36])
y = ["Nuriia", "Aliia", "Aiida"]
plt.pie(x, labels = y)
plt.legend(title = "Friends salary")
plt.show()

#5 box Plot
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
np.random.seed()
data=pd.DataFrame({
    'day':['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'total_study_hours': [4, 2, 3, 4, 2]
})
sns.boxplot(x='day', y='total_study_hours', data=data)
plt.ylabel("Hours")
plt.show()

#6 violin plot
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
np.random.seed(1)
data = pd.DataFrame({
    'gender': np.repeat(['Male', 'Female'], 100),
    'study_hours': np.concatenate([
        np.random.normal(4.5, 1, 100),
        np.random.normal(5, 1.2, 100)
    ])
})
sns.violinplot(x='gender', y='study_hours', data=data)
plt.title('Violin Plot of Study Hours by Gender')
plt.ylabel('Hours')
plt.xlabel('Gender')
plt.show()

#7 2D Heatmap
import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("iris")
corr = data.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="YlGnBu", linewidths=0.5)
plt.title("Correlation Heatmap of Iris Dataset")
plt.show()


#8 Donut chart
labels = ['Math', 'English', 'Science', 'Art']
sizes = [30, 25, 25, 20]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
plt.pie(sizes, labels=labels, colors=colors, startangle=90, wedgeprops={'width': 0.4})
plt.title("Study Time Distribution by Subject")
plt.show()

#9 Stacked bar
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
reading = [2, 3, 4, 3, 2]
math = [3, 2, 4, 4, 3]
science = [1, 2, 1, 2, 3]
x = np.arange(len(days))
plt.bar(x, reading, label='Reading')
plt.bar(x, math, bottom=reading, label='Math')
plt.bar(x, science, bottom=np.array(reading)+np.array(math), label='Science')
plt.xticks(x, days)
plt.ylabel('Total Study Hours')
plt.title('Stacked Bar Chart of Study Time by Day')
plt.legend()
plt.show()

#10 Gantt Charts
tasks = {
    'Task': ['Research', 'Planning', 'Design', 'Coding', 'Testing'],
    'Start': ['2025-04-01', '2025-04-05', '2025-04-10', '2025-04-15', '2025-04-25'],
    'End':   ['2025-04-04', '2025-04-09', '2025-04-14', '2025-04-24', '2025-04-30']
}
df = pd.DataFrame(tasks)
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])
df['Duration'] = (df['End'] - df['Start']).dt.days
fig, ax = plt.subplots(figsize=(8, 4))
for i, task in df.iterrows():
    ax.barh(task['Task'], task['Duration'], left=task['Start'], color='skyblue')
ax.set_title("Project Gantt Chart")
ax.set_xlabel("Date")
ax.grid(True)
plt.tight_layout()
plt.show()

#11 polar plot
import numpy as np
import matplotlib.pyplot as plt

angles = np.linspace(0, 2 * np.pi, 6)
values = [2, 4, 1, 5, 3, 2]

plt.subplot(111, polar=True)
plt.plot(angles, values, marker='o')
plt.fill(angles, values, alpha=0.3)
plt.title("Полярный график")
plt.show()




