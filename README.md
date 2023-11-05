<h1>Doorvel - Ejercicio BACK 2.0</h1>

<h2>Como aborde el problema</h2>
<h3>Import/Export</h3>
<p>Lo primero fue crear mi models con el nombre de las columnas del excel, de ahi importar los datos del excel a la base de datos esto lo hice desde el admin con la biblioteca from import_export.admin import ImportExportModelAdmin, para cuando ingrese al admin poder importar el archivo</p>


<h3>Replicando funcionalidad</h3>
<p>Lo primero fue buscar la manera que lo iba a filtar lo cual fue por zipcode, de ahi para poder iterar la manera mas facil que se me ocurrio fue convertirlo en un dataframe de pandas para que me sea mas facil iterar con la funcionalidad de iterrows() ya de ahi solo fue replicar el formato del json prorporcionado</p>



<h3>Deploy del API</h3>
<p>Para mi en lo personal esta parte fue la que me tomo mas tiempo ya que nunca habia deployado un proyecto siempre habia trabajado con localhost y no me habia tomado la molestia de subir proyectos a la nube, Asi que me tomo tiempo encontrar un buen lugar donde alojarlo, hasta que encontre PythonAnywhere y me resulto ya bastante facil
</p>

<h3>Link del proyecto: https://chucito.pythonanywhere.com/zipcode/64000 como el parametro lo trabje con el url basta con ingresar el zipcode despues de  link/zipcode/<CodigoPostalAqui>
