from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image as Img
import sqlite3

#Iniciamos una conexion a SQLite3 de manera global
conn = sqlite3.connect('proyectoFinal.db')

def main():
	#Obtenemos la lista de las Unidades Ejecutoras
	uuees = conn.execute('SELECT * FROM UUEE')
	#Obtenemos los expedientes existentes en caso que existan
	expedientes = conn.execute('SELECT * FROM MEXPEDIENTE')
	#Recorremos la lista de las UUEE 
	for uuee in uuees:
		#Asignamos la cantidad de numeros de expedientes que queremos consultar
		for x in range(1,2):
			cont=0
			#Recorremos los expedientes existentes
			for expediente in expedientes:
				#Comparamos si existen los expedientes
				if uuee[0]==expediente[2] and x==expediente[0]:
					cont=cont+1
			if cont==0:
				consultar(uuee[0],x)
			else:
				print ("Expediente "+str(x)+" del codigo "+str(uuee[0])+" ya esta registrado.")

	conn.close()

def consultar(sec,num):
	#Instanciamos el drive de Google Chrome
	driver = webdriver.Chrome("C:/webdrivers/chromedriver.exe")
	url = "http://apps2.mef.gob.pe/consulta-vfp-webapp/consultaExpediente.jspx"
	driver.get(url)
	#Obtenemos el input y le asignamos el codigo de la UUEE
	value=driver.find_element_by_name('secEjec')
	value.send_keys(sec)
	#Asignamos el numero de expediente
	expediente=driver.find_element_by_name('expediente')
	expediente.send_keys(num)
	#Solitamos la entrada del contenido del captcha por consola
	##################################################################################

	##################################################################################
	captcha = input("Introduce el captcha: ")
	j_captcha=driver.find_element_by_name('j_captcha')
	j_captcha.send_keys(captcha)
	#Se ejecuta el boton de submit
	driver.find_element_by_css_selector('.button').click()

	#Obtenemos todos los datos del resultado
	anioEje=driver.find_element_by_name('anoEje')
	anioEje=anioEje.get_attribute('value')
	entidad=driver.find_element_by_name('secEjec')
	entidad=entidad.get_attribute('value')
	entidadNombre = driver.find_element_by_name('secEjecNombre')
	entidadNombre = entidadNombre.get_attribute('value')
	expediente = driver.find_element_by_name('expediente')
	expediente = expediente.get_attribute('value')

	tipoOperacion = driver.find_element_by_name('tipoOperacion')
	tipoOperacion = tipoOperacion.get_attribute('value')
	tipoOperacionNombre=driver.find_element_by_name('tipoOperacionNombre')
	tipoOperacionNombre=tipoOperacionNombre.get_attribute('value')

	modalidadCompra=driver.find_element_by_name('modalidadCompra')
	modalidadCompra=modalidadCompra.get_attribute('value')
	modalidadCompraNombre=driver.find_element_by_name('modalidadCompraNombre')
	modalidadCompraNombre=modalidadCompraNombre.get_attribute('value')
	tipoProceso = driver.find_element_by_name('tipoProceso')
	tipoProceso = tipoProceso.get_attribute('value')

	tipoProcesoNombre = driver.find_element_by_name('tipoProcesoNombre')
	tipoProcesoNombre = tipoProcesoNombre.get_attribute('value')

	#Obtenemos la tabla del resultado para poder guarda la informacion
	table_id = driver.find_element(By.ID,'expedienteDetalles')
	rows = table_id.find_elements(By.TAG_NAME, "tr")
	for row in rows:
		ciclo = row.find_element_by_css_selector(".ciclo").text
		#Hacemos una condicion para no tomar una fila que no sea resultado (La cabecera de la tabla tiene las mismas clases)
		if ciclo !="Ciclo":
			fase = row.find_element_by_css_selector(".fase").text
			secuencia = row.find_element_by_css_selector(".secuencia").text
			correlativo = row.find_element_by_css_selector(".correlativo").text
			codDoc = row.find_element_by_css_selector(".codDoc").text
			numDoc = row.find_element_by_css_selector(".numDoc").text
			fecha = row.find_element_by_css_selector(".fecha").text
			ff = row.find_element_by_css_selector(".ff").text
			moneda = row.find_element_by_css_selector(".moneda").text
			monto = row.find_element_by_css_selector(".monto").text
			fechaHora = row.find_element_by_css_selector(".fechaHora").text
			#Guardamos los datos por fila del resultado en SQLite3
			conn.execute("insert into NEXPEDIENTE values('"+str(anioEje)+"','"+str(entidad)+"',"+
														"'"+str(entidadNombre)+"',"+
														"'"+str(expediente)+"',"+
														"'"+str(tipoOperacion)+"',"+
														"'"+str(tipoOperacionNombre)+"',"+
														"'"+str(modalidadCompra)+"',"+
														"'"+str(modalidadCompraNombre)+"',"+
														"'"+str(tipoProceso)+"','"+str(tipoOperacionNombre)+"')")

			conn.execute("insert into NEXPEDIENTE_DETALLE values('" + str(anioEje) + "','" + str(entidad) + "'," +
						 "'" + str(expediente) + "'," +
						 "'" + str(ciclo) + "'," +
						 "'" + str(fase) + "'," +
						 "'" + str(secuencia) + "'," +
						 "'" + str(correlativo) + "'," +
						 "'" + str(codDoc) + "'," +
						 "'" + str(numDoc) + "','" + str(fecha) + "','" + str(ff) + "'," +
						 "'" + str(moneda) + "','" + str(monto) + "','" + str(fechaHora) + "')")
			conn.commit()
	driver.close()


def recorta_captcha(imagen):
	w, h = imagen.size
	impix = imagen.load()
	imx = Img.new("RGB", (w, h))
	imx_pix = imx.load()
	for i in range(w):
		for j in range(h):
				imx_pix[i, j] = impix[i, j]

	imgareafil = Img.new("RGB", (w, h))
	imarfil_px = imgareafil.load()
	for i in range(w):
		for j in range(h):
			imarfil_px[i, j] = imx_pix[i, j]

	return imgareafil


#Inicia la funcion main
main()