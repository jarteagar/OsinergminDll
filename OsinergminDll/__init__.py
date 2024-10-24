import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def OSVersion():
    nota ='''Notas de la version***********************************
        Version 1.3

        en ultimo parametro "nOpcion" tiene 2 valores:
        0 = envia el XML 
        1 = muestra el XML que se va a enviar
        2 = muestra el XML de respuesta

        el 5to parametro "mData" es un diccionario, puede tener
        uno o mas registros, se recomienda enviar sólo un registro
        a fin de obtener el error de cada producto al ser enviado
        '''
    return nota

def OSPriceService(cHttps,cClave,cLogin,cProd,mData,nOpcion):

    # URL del webservice
    #cHttps = "https://scopwsdesa.osinergmin.gob.pe:443/scopws/diensten/PriceService" entorno: prueba o desarrollo
    #cClave = "87654321"
    #cLogin = "3345400"

    #cProd: CL, GLPE, GLPG, segun esto se selecciona la estructura XML

    #mData, es una matriz que debe tener:
    #codigo = "49"
    #precio = 12.5
    #descuento = 12.0
    #unidad = "G"
    #asumimos que tiene: 
    ## Lista inicial de diccionarios (varios productos)
    #mData = [
    #    {"codigo": "49", "precio": 12.5, "descuento": 12.0, "unidad": "G"},
    #    {"codigo": "50", "precio": 15.0, "descuento": 10.0, "unidad": "Kg"},
    #    {"codigo": "51", "precio": 20.0, "descuento": 5.0, "unidad": "L"}
    #]

    #codigo =""
    #unidad =""
    #precio = 0.0
    #descuento = 0.0
    marca =""
    tipo ="27"

    XmlBodyDetalle = ""
    
    if cProd == 'CL':
        XmlHeader = f'''<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:ser="http://services.webservices.scop.osinergmin.com">
            <soap:Header/>
            <soap:Body>
                <ser:registraPriceLiquidos>
                    <ordenPedido>
                        <API></API>
                        <actividad></actividad>
                        <afectoIGV></afectoIGV>
                        <afectoISC></afectoISC>
                        <claveUsuario>{cClave}</claveUsuario>
                        <codigoAerolinea></codigoAerolinea>
                        <codigoAutorizacion></codigoAutorizacion>
                        <codigoDGHCliente></codigoDGHCliente>
                        <codigoEquivalenteMayorista1></codigoEquivalenteMayorista1>
                        <codigoEquivalenteMayorista2></codigoEquivalenteMayorista2>
                        <codigoEquivalentePlanta1></codigoEquivalentePlanta1>
                        <codigoEquivalentePlanta2></codigoEquivalentePlanta2>
                        <codigoEquivalenteProductor></codigoEquivalenteProductor>
                        <codigoEstado></codigoEstado>
                        <codigoMayorista></codigoMayorista>
                        <codigoMayoristaDestino></codigoMayoristaDestino>
                        <codigoMayoristaDestinoEquivalente></codigoMayoristaDestinoEquivalente>
                        <codigoMayoristaEquivalente></codigoMayoristaEquivalente>
                        <codigoMayoristaOrigen></codigoMayoristaOrigen>
                        <codigoMayoristaOrigenEquivalente></codigoMayoristaOrigenEquivalente>
                        <codigoOrigen></codigoOrigen>
                        <codigoOsinergCliente></codigoOsinergCliente>
                        <codigoOsinergComprador></codigoOsinergComprador>
                        <codigoPlanta></codigoPlanta>
                        <codigoPlantaDestino></codigoPlantaDestino>
                        <codigoPlantaDestinoEquivalente></codigoPlantaDestinoEquivalente>
                        <codigoPlantaEquivalente></codigoPlantaEquivalente>
                        <codigoPlantaOrigen></codigoPlantaOrigen>
                        <codigoPlantaOrigenEquivalente></codigoPlantaOrigenEquivalente>
                        <codigoProducto></codigoProducto>
                        <codigoProveedor></codigoProveedor>
                        <codigoTransporte></codigoTransporte>
                        <codigoUnidadOperativa></codigoUnidadOperativa>
                        <codigoUsuario></codigoUsuario>
                        <cola></cola>
                        <descripcionEstado></descripcionEstado>'''
        XmlBody = '''   <detalles>
                            <cantidad1></cantidad1>
                            <cantidad2></cantidad2>
                            <cantidadDespachada></cantidadDespachada>
                            <cantidadSolicitada></cantidadSolicitada>
                            <cantidadVendida></cantidadVendida>
                            <codigoEstado></codigoEstado>
                            <codigoMarca></codigoMarca>
                            <codigoMotivoRechazo></codigoMotivoRechazo>
                            <codigoProcedencia></codigoProcedencia>
                            <codigoProducto>{codigo}</codigoProducto>
                            <codigoUnidad>{unidad}</codigoUnidad>
                            <densidadObservada></densidadObservada>
                            <descripcionEstado></descripcionEstado>
                            <detallePedido></detallePedido>
                            <factorAPI></factorAPI>
                            <factorApor></factorApor>
                            <factorComp></factorComp>
                            <fechaDespacho></fechaDespacho>
                            <fechaVenta></fechaVenta>
                            <idProducto></idProducto>
                            <placaTransporte></placaTransporte>
                            <precio>{precio}</precio>
                            <precioConDescuento>{descuento}</precioConDescuento>
                            <precioGalon></precioGalon>
                            <temperatura></temperatura>
                            <tipoUsuario></tipoUsuario>
                            <zonaPrecios></zonaPrecios>
                        </detalles>'''
        XmlFooter = f'''
                        <direccionDestino></direccionDestino>
                        <direccionDestinoVenta></direccionDestinoVenta>
                        <dua1></dua1>
                        <dua2></dua2>
                        <dua3></dua3>
                        <fechaCompra></fechaCompra>
                        <fechaEntrega></fechaEntrega>
                        <fechaFactura></fechaFactura>
                        <fechaModificacion></fechaModificacion>
                        <fechaRegistro></fechaRegistro>
                        <fechaVenta></fechaVenta>
                        <flagFactura></flagFactura>
                        <formaVenta></formaVenta>
                        <horaModificacion></horaModificacion>
                        <horaRegistro></horaRegistro>
                        <horaVenta></horaVenta>
                        <idProducto></idProducto>
                        <isStock></isStock>
                        <listaTransporte></listaTransporte>
                        <loginUsuario>{cLogin}</loginUsuario>
                        <medioTransporte></medioTransporte>
                        <nombreAerolinea></nombreAerolinea>
                        <numeroEntrega></numeroEntrega>
                        <numeroFactura></numeroFactura>
                        <numeroGuia></numeroGuia>
                        <ordenPedido></ordenPedido>
                        <placaTransporte></placaTransporte>
                        <rucComprador></rucComprador>
                        <rucMayorista1></rucMayorista1>
                        <rucMayorista2></rucMayorista2>
                        <serieNumeroFactura></serieNumeroFactura>
                        <serieNumeroGuia></serieNumeroGuia>
                        <temperatura></temperatura>
                        <tipoCambio></tipoCambio>
                        <tipoOrden></tipoOrden>
                        <tipoTransaccion></tipoTransaccion>
                        <tipoVentaFactor></tipoVentaFactor>
                        <volumenSolicitado></volumenSolicitado>
                        <volumenVenta></volumenVenta>
                        <vuelo></vuelo>
                    </ordenPedido>
                </ser:registraPriceLiquidos>
            </soap:Body>
        </soap:Envelope>'''
    elif cProd == 'GLPE':
        XmlHeader =f'''<soap:Envelope xmlns:soap=""http://www.w3.org/2003/05/soap-envelope"" xmlns:ser="http://services.webservices.scop.osinergmin.com">
    <soap:Header/>
    <soap:Body>
        <ser:registraPriceCilindrosGlp>
            <ordenPedido>
                <loginUsuario>{cLogin}</loginUsuario>
                <claveUsuario>{cClave}</claveUsuario>'''       
        XmlBody ='''
                <detalles>
                    <codigoProducto>{codigo}</codigoProducto>
                    <precio>{precio}</precio>
                    <codigoMarca>{marca}</codigoMarca>
                    <tipoUsuario>{tipo}</tipoUsuario>
                </detalles>'''
        XmlFooter ='''
            </ordenPedido>
        </ser:registraPriceCilindrosGlp>
    </soap:Body>
    </soap:Envelope>'''
    elif cProd == 'GLPG':
        XmlHeader =f'''<soap:Envelope xmlns:soap=""http://www.w3.org/2003/05/soap-envelope"" xmlns:ser="http://services.webservices.scop.osinergmin.com">
    <soap:Header/>
        <soap:Body>
            <ser:registraPriceLiquidos>
                <ordenPedido>
                    <loginUsuario>{cLogin}</loginUsuario>
                    <claveUsuario>{cClave}</claveUsuario>'''
        XmlBody ='''
                    <detalles>
                        <codigoProducto>{codigo}</codigoProducto>
                        <precio>{precio}</precio>
                        <codigoUnidad>{unidad}</codigoUnidad>
                    </detalles>'''
        XmlFooter ='''
                </ordenPedido>
            </ser:registraPriceLiquidos>
        </soap:Body>
    </soap:Envelope>'''
    
    #iteramos el detalle
    for itm in mData:
        if cProd == 'CL':     
            XmlBodyDetalle += XmlBody.format(codigo =itm['codigo'], unidad = itm['unidad'], precio = itm['precio'], descuento = itm['descuento'])

    # Unir las partes del XML
    xml = XmlHeader + XmlBodyDetalle + XmlFooter
    resultado =""

    # Definir los encabezados
    headers = {
        'Content-Type': 'application/soap+xml',  # Especifica que el contenido es XML
        'SOAPAction': 'http://www.osinergmin.gob.pe/PriceService/registraPriceLiquidos',
    }

    if nOpcion == 1:
        resultado = xml #solo muestra el xml que se va a enviar
    elif nOpcion ==0 or nOpcion == 2:
    
        # Realizar la solicitud POST
        #cHttps: definir el link del entorno de pruebas o de desarrollo
        response = requests.post(cHttps, data=xml, headers=headers)

        
        # Comprobar la respuesta
        if response.status_code == 200:
            #print("Solicitud exitosa:")

            # Parsear la respuesta XML
            response_content = response.content
            root = ET.fromstring(response_content)
            fecha =""
            hora = ""

            codResul = root.find('.//resultado').text  #codigo del resultado

            if nOpcion ==2:
                resultado = f'''{response_content}''' 
            else:
                if codResul =="1":
                    #exito
                    fecha = root.find('.//fechaRegistro').text
                    hora = root.find('.//horaRegistro').text
                    resultado = f"R0|{codResul}|{fecha}|{hora}"
                else:
                    resultado = f'''R1|{codResul}|{datetime.now().date()}|{datetime.now().strftime("%H:%M:%S")}'''
        else:
            #print("Error en la solicitud:", response.status_code, response.content)
            resultado = f"RE|Error en la solicitud: {response.status_code}, {response.content}"
        
    return resultado