# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SituationComptable(models.Model):
    _name = "situation.comptable"
    _description = "Situation Comptable"

    sca = fields.Char(string='SCA')
    sys_ctrl = fields.Char(string="SYSTÈME DE CONTRÔLE D'AMBIANCE")

    # QUANTITE : contractuel precedente mois cumul 
    qty_contractuel = fields.Float(string="Contractuel")
    qty_precedente = fields.Float(string="precedente")
    qty_mois = fields.Float(string="mois")
    qty_cumul = fields.Float(string="cumul")

    # PU 
    pu = fields.Float(string="PU")

    # MONTANTS : contractuel precedente mois total 
    mnt_contractuel = fields.Float(string="Contractuel", compute='_mnt_contractuel')
    mnt_precedente = fields.Float(string="precedente", compute='_mnt_precedente')
    mnt_mois = fields.Float(string="mois", compute='_mnt_mois')
    mnt_total = fields.Float(string="total", compute='_mnt_total')

    project_id = fields.Many2one('project.project', string='Projet')
    client_id = fields.Many2one('res.partner', string='Client', domain="[('customer_rank', '=', True)]")
    # client_id = fields.Many2one('res.partner', string='Client')

    def name_get(self):
        result = []
        for decompte in self:
            name = decompte.sys_ctrl
            result.append((decompte.id, name))
        return result

    @api.depends('qty_contractuel', 'pu')
    def _mnt_contractuel(self):
        for r in self:
            r.mnt_contractuel = r.qty_contractuel * r.pu

    @api.depends('qty_precedente', 'pu')
    def _mnt_precedente(self):
        for r in self:
            r.mnt_precedente = r.qty_precedente * r.pu

    @api.depends('qty_mois', 'pu')
    def _mnt_mois(self):
        for r in self:
            r.mnt_mois = r.qty_mois * r.pu

    @api.depends('qty_cumul', 'pu')
    def _mnt_total(self):
        for r in self:
            r.mnt_total = r.qty_cumul * r.pu