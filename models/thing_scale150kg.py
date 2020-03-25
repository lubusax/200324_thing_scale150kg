from odoo import models, fields


class ThingsThing(models.Model):
    _inherit = 'base.thing'
    _name = 'things.thing.scale150kg'

    # every thing sends and/or receives data
    # through one and only one gate
    gate_id = fields.Many2one('things.gate',
                string='Gate',
                required = True)
    
class ThingsGate(models.Model):
    _inherit = 'things.gate'

    thing_scale150kg_ids = fields.One2many(
        'things.thing.scale150kg',
        'gate_id', string='Scale 150kg')
    

