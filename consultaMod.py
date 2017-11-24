import sqlite3

def main():
	conn = sqlite3.connect('proyectoFinal.db')
	conn.commit()
	rows = conn.execute('SELECT * FROM NEXPEDIENTE')
	for row in rows:
		print("AÑO", "COD", "ENTIDAD", "EXPEDIENTE", "COD", "OPERACION", "COD", "MODALIDAD", "COD", "PROCESO")
		print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
		rowsDet = conn.execute("SELECT * FROM NEXPEDIENTE_DETALLE WHERE ANIO = '"+row[0]+"'"+
							   "AND ENTIDAD = '"+row[1]+"'"+
							   "AND EXPEDIENTE = '"+row[3]+"'")
		print("AÑO", "ENTIDAD", "EXPEDIENTE", "CICLO", "FASE", "SEC", "CORR", "DOC", "NUMERO", "FECHA")
		for rowDet in rowsDet:
			print(rowDet[0], rowDet[1], rowDet[2], rowDet[3], rowDet[4], rowDet[5], rowDet[6], rowDet[7], rowDet[8], rowDet[9])
	conn.close()

main()