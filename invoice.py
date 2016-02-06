#This file is part account_invoice_jreport module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['InvoiceReport']
__metaclass__ = PoolMeta


class InvoiceReport:
    __name__ = 'account.invoice.jreport'

    @classmethod
    def execute(cls, ids, data):
        pool = Pool()
        Config = pool.get('account.configuration')
        config = Config(1)
        parameters = {
            'invoice_qty_decimal': config.invoice_qty_decimal
            }
        if 'parameters' in data:
            data['parameters'].update(parameters)
        else:
            data['parameters'] = parameters
        return super(InvoiceReport, cls).execute(ids, data)
