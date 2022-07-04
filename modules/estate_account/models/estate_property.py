from odoo import api,fields,models

class InheritEstate(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
        values={
            'partner_id':self.partner_id,
            'move_type':'out_invoice',
            'journal_id': journal.id,
            'invoice_line_ids':[
                fields.Command.create({
                    'name':self.name,
                    'quantity':1,
                    'price_unit':self.selling_price*0.06
                }),
                fields.Command.create({
                    'name':'fee',
                    'quantity':1,
                    'price_unit':100
                }),
            ]
        }
        self.env['account.move'].create(values)
        return super().action_sold()

    
    