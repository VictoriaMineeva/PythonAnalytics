import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar

# Создание случайных данных о продажах
np.random.seed(0)  # Для воспроизводимости результатов
months = [calendar.month_name[i] for i in range(1, 13)]
sales_data = {
    'Month': np.random.choice(months, size=100),
    'Revenue': np.random.randint(1000, 5000, size=100)
}

# Преобразование данных в DataFrame
sales_df = pd.DataFrame(sales_data)

# Анализ данных
sales_by_month = sales_df.groupby('Month')['Revenue'].sum()

# Визуализация результатов
plt.figure(figsize=(10, 6))
sales_by_month.plot(kind='bar', color='skyblue')
plt.title('Monthly Sales Revenue (Random Data)')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()