import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/finanzas.csv')

df['Fecha'] = pd.to_datetime(df['Fecha'])

ingreso = df[df['Tipo']=='Ingreso']
egreso = df[df['Tipo']=='Egreso']

# ===========================
# 🥧 1. Gráfico de pastel: gastos por categoría
# ===========================

gastos_categoria = egreso.groupby('Categoría')['Monto'].sum()

plt.figure(figsize=(7,7))
plt.pie(gastos_categoria, labels=gastos_categoria.index, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Distribución de gastos por categoría')
plt.tight_layout()
plt.savefig('data/gastos_por_categoria.png')
plt.show()

# ===========================
# 📊 2. Gráfico de barras: ingresos vs gastos por día
# ===========================

df_diario = df.groupby(['Fecha','Tipo'])['Monto'].sum().unstack(fill_value=0)

df_diario.plot(kind='bar', stacked=False , figsize=(7,7))
plt.title("Ingresos vs Gasto por día")
plt.xlabel("Fecha")
plt.ylabel("Monto")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('data/ingreso_vs_gastos_por_dia.png')
plt.show()

# ===========================
# 📈 3. Gráfico de saldo acumulado
# ===========================

df['Signo'] = df['Tipo'].apply(lambda x: 1 if x == 'Ingreso' else -1)
df['Saldo'] = df['Monto'] * df['Signo']
df['Saldo Acumulado'] = df.sort_values('Fecha')['Saldo'].cumsum()

plt.figure(figsize=(10,5))
sns.lineplot(data=df, x='Fecha', y='Saldo Acumulado', marker='o')
plt.title('Grafico de saldo acumulado')
plt.xlabel('Fecha')
plt.ylabel('Saldo')
plt.grid(True)
plt.tight_layout()
plt.savefig('data/saldo_acumulado.png')
plt.show()

