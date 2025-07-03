import pandas as pd

df = pd.read_csv('data/finanzas.csv')

print('\n -----------PRIMERAS FILAS--------------')
print(df.head())

print('\n -----------INFORMACIÓN GENERAL--------------')
print(df.info())

print('\n -----------Estadísticas generales (sólo para "Monto"):--------------')
print(df['Monto'].describe().round(0))

ingreso= df[df['Tipo']=='Ingreso'] #Crea un nuevo DATAFRAME que contenga los datos de la columna tipo en el dataframe anterior que sea igual a ingreso
egreso= df[df['Tipo']=='Egreso']
#Estas variables de convierten en un nuevo DATAFRAME

print(f"\n Total de ingresos: {ingreso['Monto'].sum():,.0f}.000")
print(f"\n Total de egresos: {egreso['Monto'].sum():,.0f}.000")

print("\n Egreso por categoría:")
print(f"{egreso.groupby('Categoría')['Monto'].sum().sort_values(ascending=False)}")