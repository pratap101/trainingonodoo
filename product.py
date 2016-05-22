
from openerp import models, fields, api

class Product(models.Model):
    
    _inherit = 'product.template'
    
    name = fields.Char('Saboor Name', required=True)
    vendor_name = fields.Char('Vendor Name', required=True)
    customer_name = fields.Char('Customer Name', required=True)
    country = fields.Many2one('res.country', string='Country', required=True)
    supplier = fields.Many2one('res.partner', string='Supplier', required=True)
    brand = fields.Char('Brand', required=True)
    product_form = fields.Selection([
                                   ('a','a'),
                                   ('b','b')],string= "Product Form", required=True)
                                   
    part = fields.Selection([
                           ('ss','ss'),
                           ('ff','ff')], string="Part", required=True)
    disassembly = fields.Selection([
                                 ('ww','ww'),
                                 ('rr','rr')], string="Disassembly", required=True)
                                  
                                  
                                  
    serial_prefix = fields.Char('Serial Prefix', required=True)
    
    
                                   
