import sqlite3

def main():
	conn = sqlite3.connect('proyectoFinal.db')
	conn.execute("Create Table if not exists UUEE(SEC_EJEC INT,NOMBRE_UUEE TEXT,RUC TEXT)")
	conn.execute("insert into UUEE values(86,'CONSEJO NACIONAL DE CIENCIA, TECNOLOGIA E INNOVACION - CONCYTEC','20135727394')")
	conn.execute("insert into UUEE values(198,'CONSEJO NACIONAL DE LA MAGISTRATURA','20194484365')")
	conn.execute("insert into UUEE values(1409,'CONSERVACION DE BOSQUES','20546871330')")
	conn.execute("insert into UUEE values(75,'CONSERVATORIO NACIONAL DE MUSICA','20160213345')")
	conn.execute("insert into UUEE values(3,'PRESIDENCIA DEL CONSEJO DE MINISTROS','20168999926')")
	conn.commit()
	conn.execute("Create Table if not exists NEXPEDIENTE(ANIO TEXT,"+
													"ENTIDAD TEXT,"+
													"ENTIDAD_NOMBRE TEXT,"+
													"EXPEDIENTE TEXT,"+
													"TIPO_OPERACION TEXT,"+
													"TIPO_OPERACION_NOMBRE TEXT,"+
													"MODALIDAD TEXT,"+
													"MODALIDAD_NOMBRE TEXT,"+
													"TIPO_PROCESO TEXT,"+
													"TIPO_PROCESO_NOMBRE TEXT)")
	conn.commit()
	conn.execute("Create Table if not exists NEXPEDIENTE_DETALLE(ANIO TEXT," +
				 "ENTIDAD TEXT," +
				 "EXPEDIENTE TEXT," +
				 "CICLO TEXT," +
				 "FASE TEXT," +
				 "SEC TEXT," +
				 "CORR TEXT," +
				 "DOC TEXT," +
				 "NUMERO TEXT," +
				 "FECHA TEXT," +
				 "FF TEXT," +
				 "MONEDA TEXT," +
				 "MONTO TEXT," +
				 "FECHA_PROCESO TEXT)")
	conn.commit()
	conn.close()

main()