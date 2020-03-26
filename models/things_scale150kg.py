from odoo import models, fields


class ThingsScale150kg(models.Model):
    _name = 'things.scale150kg'
    _inherit = 'things.basis'

#     # every thing sends and/or receives data
#     # through one and only one gate
#     gate_scale150kg_id = fields.Many2one('things.gate',
#                 string='Gate',
#                 required = True)
    
# class ThingsGate(models.Model):
#     _inherit = 'things.gate'

#     thing_scale150kg_ids = fields.One2many(
#         'thing.scale150kg',
#         'gate_scale150kg_id', string='Scale 150kg')
    

