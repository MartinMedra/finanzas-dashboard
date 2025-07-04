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
#autopct='%1.1f%%' se utiliza para mostra el porcentaje con 1 decimal ej: 25.3%------ 
#startangle = 140 gira el grafico para que empiece con un angulos de 140, solo es estetico
#labels=gastos_categoria.index utiliza el nombre de las categorias para usarlos como etiquetas
plt.axis('equal')  # Hace que el círculo se vea bien
plt.title('Distribución de gastos por categoría')
plt.tight_layout() #Optimiza los margenes para que los elementos no se corten ni se encimen
plt.savefig('data/gastos_por_categoria.png')
plt.show()

# ===========================
# 📊 2. Gráfico de barras: ingresos vs gastos por día
# ===========================

df_diario = df.groupby(['Fecha','Tipo'])['Monto'].sum().unstack(fill_value=0) #Agrupa los datos por fecha y tipo
#unstack() convierte la columna tipo en columnas separadas (ingreso y egreso)
#fill_value=0 Si no hubo ingreso o gasto en un día, pone 0 en vez de NaN
df_diario.plot(kind='bar', stacked=False , figsize=(7,7)) #Dibuja un grafico de barras
#stacked=False para que las barras de ingreso se muestren una al lado de la otra y no apiladas
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

df['Signo'] = df['Tipo'].apply(lambda x: 1 if x == 'Ingreso' else -1)#Crea una nueva columna llamada Signo que vale 1+ si es ingreso, -1 si es egreso

df['Saldo'] = df['Monto'] * df['Signo']
df['Saldo Acumulado'] = df.sort_values('Fecha')['Saldo'].cumsum()
#sort_values() asegura que las fechas estén en orden cronologico
#cumsum() calcula la suma acumulada del saldo
# Día 1: +100
# Día 2: -30 → saldo = 70
# Día 3: +20 → saldo = 90


plt.figure(figsize=(10,5))
sns.lineplot(data=df, x='Fecha', y='Saldo Acumulado', marker='o') #seaborn para darle un toque más moderno a la tabla
#marker='o' se utiliza para dibujar una linea con puntos
plt.title('Grafico de saldo acumulado')
plt.xlabel('Fecha')
plt.ylabel('Saldo')
plt.grid(True)
plt.tight_layout()
plt.savefig('data/saldo_acumulado.png')
plt.show()

