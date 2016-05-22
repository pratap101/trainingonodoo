from openerp import models, fields, api

class SerialNumber(models.Model):

    _inherit = 'stock.production.lot'
    
    sloter_date = fields.Date('Sloter Date', required=True)
    production_date = fields.Date('Production Date', required=True)
    batch_number = fields.Char('Batch Number', required=True)
    net_weight = fields.Float('Net Weight(Kg)', required=True)
    gross_weight = fields.Float('Gross Weight(Kg)', required=True)
