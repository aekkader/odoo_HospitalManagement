from odoo import api, fields, models

class Partner(models.Model):
    _inherit = "res.partner"

    partner_rc = fields.Char(string='RC')
    partner_nif = fields.Char(string='NIF')
    partner_nis = fields.Char(string='NIS')
    partner_ai = fields.Char(string='AI')
    partner_rib = fields.Char(string='RIB')
    partner_tin = fields.Char(string='TIN')

class Company(models.Model):
    _inherit = "res.company"

    partner_rc = fields.Char(string='RC')
    partner_nif = fields.Char(string='NIF')
    partner_nis = fields.Char(string='NIS')
    partner_ai = fields.Char(string='AI')
    partner_rib = fields.Char(string='RIB')
    partner_tin = fields.Char(string='TIN')
