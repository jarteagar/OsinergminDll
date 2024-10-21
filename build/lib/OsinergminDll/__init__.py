import requests
import xml.etree.ElementTree as ET

def prueba():

    # URL del webservice
    httpsDesa = "https://scopwsdesa.osinergmin.gob.pe:443/scopws/diensten/PriceService"
    usuario = "87654321"
    codigo = "49"
    precio = 12.5
    descuento = 12.0
    unidad = "G"
    login = "3345400"

    # XML Header, Body y Footer usando comillas triples para cadenas multilínea
    # http://www.osinergmin.gob.pe/PriceService

    XmlHeader = f'''<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:ser="http://services.webservices.scop.osinergmin.com">
        <soap:Header/>
        <soap:Body>
            <ser:registraPriceLiquidos>
                <ordenPedido>
                    <API></API>
                    <actividad></actividad>
                    <afectoIGV></afectoIGV>
                    <afectoISC></afectoISC>
                    <claveUsuario>{usuario}</claveUsuario>
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

    XmlBody = f'''
                    <detalles>
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
                    <loginUsuario>{login}</loginUsuario>
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

    # Unir las partes del XML
    xml = XmlHeader + XmlBody + XmlFooter

    # Definir los encabezados
    headers = {
        'Content-Type': 'application/soap+xml',  # Especifica que el contenido es XML
        'SOAPAction': 'http://www.osinergmin.gob.pe/PriceService/registraPriceLiquidos',
    }

    # Realizar la solicitud POST
    response = requests.post(httpsDesa, data=xml, headers=headers)

    resultado =""
    # Comprobar la respuesta
    if response.status_code == 200:
        #print("Solicitud exitosa:")

        # Parsear la respuesta XML
        response_content = response.content
        root = ET.fromstring(response_content)

        resultado = root.find('.//resultado').text
        #print("Resultado:", resultado)
    else:
        #print("Error en la solicitud:", response.status_code, response.content)
        resultado = f"Error en la solicitud: {response.status_code}, {response.content}"