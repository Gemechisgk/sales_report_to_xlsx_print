from odoo import models
from datetime import datetime

class SalesReportXLS(models.AbstractModel):
    _name = 'report.iats_sales_report_print.report_sale_orde_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        date_from = data['date_from']
        date_to = data['date_to']

        sheet = workbook.add_worksheet('Daily Sales Report')
        bold = workbook.add_format({'bold': True})

        # Write headers
        sheet.write(0, 0, 'Order Date', bold)
        sheet.write(0, 1, 'Order Number', bold)
        sheet.write(0, 2, 'Customer', bold)
        sheet.write(0, 3, 'Total Amount', bold)

        row = 1
        orders = self.env['sale.order'].search([
            ('date_order', '>=', date_from),
            ('date_order', '<=', date_to),
            ('state', '=', 'sale')
        ])

        for order in orders:
            order_date = datetime.strptime(str(order.date_order), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
            sheet.write(row, 0, order_date)
            sheet.write(row, 1, order.name)
            sheet.write(row, 2, order.partner_id.name)
            sheet.write(row, 3, order.amount_total)
            row += 1