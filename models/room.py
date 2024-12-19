from odoo import models, fields

class Room(models.Model):
    _name = 'ensa.room'
    _description = 'Room'

    name = fields.Char(string='Room Name', required=True)
    capacity = fields.Integer(string='Capacity', required=True)
