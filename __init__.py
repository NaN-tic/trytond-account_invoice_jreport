#This file is part account_invoice_jreport module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .invoice import *
from .configuration import *

def register():
    Pool.register(
        AccountConfiguration,
        AccountConfigurationCompany,
        module='account_invoice_jreport', type_='model')
    Pool.register(
        InvoiceReport,
        module='account_invoice_jreport', type_='report')
