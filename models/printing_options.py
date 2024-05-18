from odoo import models, fields, api

class PrintingOptions(models.TransientModel):
    _name = 'printing.options'
    _description = 'Printing Options'

    today = fields.Boolean(string='Today')
    date_from = fields.Date(string='Starting From')
    date_to = fields.Date(string='Until')

    def generate_sale_xlsx_report(self):
        data = {
            'date_from': self.date_from,
            'date_to': self.date_to,
        }
        return self.env.ref('iats_sales_report_print.sales_order_xlsx').report_action(self, data=data)