{
    'name': 'Xmarts Reporte orden de compra interm',
    'version': '13',
    'category': "",
    'description': """ Purchase Order in spanish Report 
                      Reporte Orden de Compra
    """,
    'author':'Xmarts',
    'depends': ['base','purchase'],
    'data': [
        "report/po_spanish.xml",
        "views/purchase_order.xml"
    ],
    'qweb': [
        ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
