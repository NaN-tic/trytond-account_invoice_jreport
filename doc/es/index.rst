=============================
Informe de facturación Jasper
=============================

El módulo **Informe de facturación Jasper** reemplaza el informe de facturación
por defecto por un informe de Jasper.

Fichero configuración trytond
-----------------------------

Se puede configurar si se desea renderizar el informe de factua cuando se contabiliza
una factura en la seccion 'jasper':

.. code-block:: python

    [jasper]
    post_invoice = (default: True)
