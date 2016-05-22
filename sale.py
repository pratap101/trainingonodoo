from openerp import models, fields, api

class SerialNumber(models.Model):

    _inherit ='sale.order'
    
    customer_code = fields.Char('Customer Code', required=True)
    delivery_person = fields.Many2one('res.partner', string = 'Delivery Person', required=True)
    branch = fields.Char('Branch', required=True)  
    payment_mode = fields.Selection([
                                ('cash','Cash'),
                                ('credit','Credit'),
                                ('cheque','Cheque')], string='Payment Mode', required=True, default='cash')
                                
    
    
    
    
