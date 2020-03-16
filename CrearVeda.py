import arcpy
from arcpy import env

# Input parameters
gdb = r'\\atlantico2\Consultores Asociados\Biblioteca\SIG\RES2182_2016\Test_Veda\BD_ANLA_3116.gdb'
dataSet = env.workspace = r'\\atlantico2\Consultores Asociados\Biblioteca\SIG\RES2182_2016\Test_Veda\BD_ANLA_3116.gdb\T_20_BIOTICO_CONTI_COSTE'

# Creating PuntoMuestreoVeda
arcpy.CreateFeatureclass_management(dataSet, "PuntoMuestreoVeda", "POINT")
FC = dataSet + '\\PuntoMuestreoVeda'
arcpy.AddField_management(FC, "EXPEDIENTE", "TEXT", field_precision=20)
arcpy.AddField_management(FC, "OPERADOR", "TEXT", field_precision=100)
arcpy.AddField_management(FC, "PROYECTO", "TEXT", field_precision=100)
arcpy.AddField_management(FC, "VEREDA", "TEXT", field_precision=255)
arcpy.AddField_management(FC, "MUNICIPIO", "TEXT", field_precision=5)
arcpy.AddField_management(FC, "DEPARTAMENTO", "TEXT", field_precision=2)
arcpy.AddField_management(FC, "ID_VEDA", "TEXT", field_precision=10)
arcpy.AddField_management(FC, "N_COBERTURA", "TEXT", field_precision=255)
arcpy.AddField_management(FC, "NOMENCLATURA", "TEXT", field_precision=255)
arcpy.AddField_management(FC, "DESCRIPCION", "TEXT", field_precision=255)
arcpy.AddField_management(FC, "FECHA_MUESTRA", "DATE")
arcpy.AddField_management(FC, "OBSERVACIONES", "TEXT", field_precision=255)
arcpy.AddField_management(FC, "ESTE", "DOUBLE")
arcpy.AddField_management(FC, "NORTE", "DOUBLE")

arcpy.AssignDomainToField_management(FC, "MUNICIPIO", "Dom_Departamento")
arcpy.AssignDomainToField_management(FC, "DEPARTAMENTO", "Dom_Municipio")

# Creating MedidaVeda
arcpy.CreateFeatureclass_management(dataSet, "MedidaVeda", "POLYGON")
FC = dataSet + '\\MedidaVeda'

arcpy.AddField_management(FC, "EXPEDIENTE",  "TEXT",  field_precision=20)
arcpy.AddField_management(FC, "OPERADOR",  "TEXT",  field_precision=100)
arcpy.AddField_management(FC, "PROYECTO",  "TEXT",  field_precision=100)
arcpy.AddField_management(FC, "VEREDA",  "TEXT",  field_precision=255)
arcpy.AddField_management(FC, "MUNICIPIO",  "TEXT",  field_precision=5)
arcpy.AddField_management(FC, "DEPARTAMENTO",  "TEXT",  field_precision=2)
arcpy.AddField_management(FC, "MEDIDA_MANEJO",  "TEXT",  field_precision=3)
arcpy.AddField_management(FC, "COBERTURA",  "TEXT",  field_precision=255)
arcpy.AddField_management(FC, "NOMENCLATURA",  "TEXT",  field_precision=255)
arcpy.AddField_management(FC, "OBSERVACIONES",  "TEXT",  field_precision=255)
arcpy.AddField_management(FC, "AREA_ha",  "Double")

arcpy.AssignDomainToField_management(FC, "MUNICIPIO", "Dom_Departamento")
arcpy.AssignDomainToField_management(FC, "DEPARTAMENTO", "Dom_Municipio")

# Creating Med_Manejo
domName = "Med_Manejo"
inField = "MEDIDA_MANEJO"

# Process: Create the coded value domain
arcpy.CreateDomain_management(gdb, domName, "Tipo de medida de manejo;", "TEXT", "CODED")

	# Store all the domain values in a dictionary with the domain code as the "key" and the 
	# domain description as the "value" (domDict[code])
domDict = {"100":"Reubicación", "200":"Rescate", "300":"Traslado", "400":"Compensación", "500":"Otro"}
    
    # Process: Add valid material types to the domain
    # use a for loop to cycle through all the domain codes in the dictionary
for code in domDict:        
	arcpy.AddCodedValueToDomain_management(gdb_1, domName, code, domDict[code])
    
    # Process: Constrain the material value of distribution mains
arcpy.AssignDomainToField_management(FC, inField, domName)

out_name = "MuestreoVedaTB"
# Execute CreateTable
arcpy.CreateTable_management(gdb_1, out_name)
FC=r'\\atlantico2\Consultores Asociados\Biblioteca\SIG\RES2182_2016\Test_Veda\BD_ANLA_3116.gdb\MuestreoVedaTB'
arcpy.AddField_management(FC, "EXPEDIENTE",  "TEXT",  field_precision=20)
arcpy.AddField_management(FC, "ID_VEDA",  "TEXT",  field_precision=10)
arcpy.AddField_management(FC, "DIVISION",  "TEXT",  field_precision=50)
arcpy.AddField_management(FC, "CLASE",  "TEXT",  field_precision=50)
arcpy.AddField_management(FC, "ORDEN",  "TEXT",  field_precision=50)
arcpy.AddField_management(FC, "FAMILIA",  "TEXT",  field_precision=50)
arcpy.AddField_management(FC, "GENERO",  "TEXT",  field_precision=50)
arcpy.AddField_management(FC, "ESPECIE",  "TEXT",  field_precision=50)
arcpy.AddField_management(FC, "N_COMUN",  "TEXT",  field_precision=50)
arcpy.AddField_management(FC, "CATEG_CIT",  "DOUBLE")
arcpy.AddField_management(FC, "CATEG_UICN",  "DOUBLE")
arcpy.AddField_management(FC, "CATE_MINIS",  "DOUBLE")
arcpy.AddField_management(FC, "T_DISTRIB",  "DOUBLE")
arcpy.AddField_management(FC, "VEDA",  "DOUBLE")
arcpy.AddField_management(FC, "RESOLUCION",  "TEXT",  field_precision=20)
arcpy.AddField_management(FC, "ENTID_VEDA",  "DOUBLE")
arcpy.AddField_management(FC, "VIGEN_VEDA",  "DOUBLE")
arcpy.AddField_management(FC, "T_TAMANO",  "SHORT")
arcpy.AddField_management(FC, "FORM_CRECIM",  "TEXT",  field_precision=3)
arcpy.AddField_management(FC, "PORTE",  "TEXT",  field_precision=3)
arcpy.AddField_management(FC, "TIPO_PLANTA",  "TEXT",  field_precision=3)
arcpy.AddField_management(FC, "NO_VASCULAR",  "TEXT",  field_precision=3)
arcpy.AddField_management(FC, "INDIVIDUOS",  "LONG")
arcpy.AddField_management(FC, "ABUNDANCIA",  "DOUBLE")
arcpy.AddField_management(FC, "ABUND_REL",  "DOUBLE")
arcpy.AddField_management(FC, "FRECUENCIA",  "DOUBLE")
arcpy.AddField_management(FC, "FRECU_REL",  "DOUBLE")
arcpy.AddField_management(FC, "FITOSANITARIO",  "TEXT",  field_precision=3)
arcpy.AddField_management(FC, "MEDIDA_MANEJO",  "TEXT",  field_precision=3)
arcpy.AddField_management(FC, "OBSERV",  "TEXT",  field_precision=255)


arcpy.AssignDomainToField_management(FC, "CATEG_CIT",  "Dom_Apendice")
arcpy.AssignDomainToField_management(FC, "CATEG_UICN",  "Dom_Amenaza")
arcpy.AssignDomainToField_management(FC, "CATE_MINIS",  "Dom_Amenaza")
arcpy.AssignDomainToField_management(FC, "T_DISTRIB",  "Dom_Tipo_Distribu")
arcpy.AssignDomainToField_management(FC, "VEDA",  "Dom_Veda")
arcpy.AssignDomainToField_management(FC, "ENTID_VEDA",  "Dom_EntidadVeda")
arcpy.AssignDomainToField_management(FC, "VIGEN_VEDA",  "Dom_Vigencia")


#Creacion de dominios MuestreoVedaTB
#Dom_T_Tamano
gdb_1 = r'\\atlantico2\Consultores Asociados\Biblioteca\SIG\RES2182_2016\Test_Veda\BD_ANLA_3116.gdb'
inField = "T_TAMANO"
domName = "Dom_T_Tamano"
# Process: Create the coded value domain
arcpy.CreateDomain_management(gdb_1, domName, "Categoría de tamaño para el individuo identificado", "SHORT", "CODED")

# Store all the domain values in a dictionary with the domain code as the "key" and the 
# domain description as the "value" (domDict[code])
domDict = {100:"Renuevo o plántula", 200:"Brinzal" , 300: "Latizal o Fustal (especies arbóreas y helechos arborescentes)"}
    
    # Process: Add valid material types to the domain
    # use a for loop to cycle through all the domain codes in the dictionary
for code in domDict:        
	arcpy.AddCodedValueToDomain_management(gdb_1, domName, code, domDict[code])
    
    # Process: Constrain the material value of distribution mains
arcpy.AssignDomainToField_management(FC, inField, domName)

#
inField = "FORM_CRECIM"
domName = "Dom_Form_Crecim"
# Process: Create the coded value domain
arcpy.CreateDomain_management(gdb_1, domName, "Forma y sustrato de crecimiento de la especie", "TEXT", "CODED")

# Store all the domain values in a dictionary with the domain code as the "key" and the 
# domain description as the "value" (domDict[code])
domDict = {"100":"Terrícola (Suelo)", "200":"Materia orgánica en descomposición", "300":"Folícola (Hoja)", "400": "Rupícola (roca)", "500": "Cortícola (Corteza)"}
    
    # Process: Add valid material types to the domain
    # use a for loop to cycle through all the domain codes in the dictionary
for code in domDict:        
	arcpy.AddCodedValueToDomain_management(gdb_1, domName, code, domDict[code])
    
    # Process: Constrain the material value of distribution mains
arcpy.AssignDomainToField_management(FC, inField, domName)


inField = "PORTE"
domName = "Dom_Porte"
# Process: Create the coded value domain
arcpy.CreateDomain_management(gdb_1, domName, "Aspecto general de la especie vegetal identificada", "TEXT", "CODED")

# Store all the domain values in a dictionary with the domain code as the "key" and the 
# domain description as the "value" (domDict[code])
domDict = {"100": "Árbol", "200": "Arbusto", "300": "Herbáceas"}
    
    # Process: Add valid material types to the domain
    # use a for loop to cycle through all the domain codes in the dictionary
for code in domDict:        
	arcpy.AddCodedValueToDomain_management(gdb_1, domName, code, domDict[code])
    
    # Process: Constrain the material value of distribution mains
arcpy.AssignDomainToField_management(FC, inField, domName)


inField = "TIPO_PLANTA"
domName = "Dom_Tipo_Planta"
# Process: Create the coded value domain
arcpy.CreateDomain_management(gdb_1, domName, "Categorización del tipo de planta", "TEXT", "CODED")

# Store all the domain values in a dictionary with the domain code as the "key" and the 
# domain description as the "value" (domDict[code])
domDict = {"100": "Vascular", "200": "No vascular"}
    
# Process: Add valid material types to the domain
# use a for loop to cycle through all the domain codes in the dictionary
for code in domDict:        
	arcpy.AddCodedValueToDomain_management(gdb_1, domName, code, domDict[code])
    
# Process: Constrain the material value of distribution mains
arcpy.AssignDomainToField_management(FC, inField, domName)


inField = "NO_VASCULAR"
domName = "Dom_NoVascular"
# Process: Create the coded value domain
arcpy.CreateDomain_management(gdb_1, domName, "Categoría para especies identificadas no vasculares", "TEXT", "CODED")

# Store all the domain values in a dictionary with the domain code as the "key" and the 
# domain description as the "value" (domDict[code])
domDict = {"100": "Bromelias", "200": "Orquídeas", "300": "Musgos", "400": "Hepáticas", "500": "Anthoceros", "600": "Líquenes"}
    
# Process: Add valid material types to the domain
# use a for loop to cycle through all the domain codes in the dictionary
for code in domDict:        
	arcpy.AddCodedValueToDomain_management(gdb_1, domName, code, domDict[code])
    
# Process: Constrain the material value of distribution mains
arcpy.AssignDomainToField_management(FC, inField, domName)