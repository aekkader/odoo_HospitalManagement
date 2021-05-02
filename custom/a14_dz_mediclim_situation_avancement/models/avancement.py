# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SituationAvancement(models.Model):
    _name = "situation.avancement"
    _description = "Situation Avancement"

    # label_avancement = fields.Char(string='Label')
    qty_avancement = fields.Float(string="Qty")

    select_avancement = fields.Selection(selection='_comptable_sys_ctrl', string="SYSTEME DE CONTROLE")
    
    project_id = fields.Many2one('project.project', string='Projet')

    @api.onchange('project_id')
    def _comptable_sys_ctrl(self):
        choise = []
        # comptable_ = self.env['situation.comptable'].search([])
        # comptable_ = self.env['situation.comptable'].search([['project_id', '=', self.project_id.id],])
        comptable_ = self.env['situation.comptable'].search([('project_id', '=', 1)])
        # prod_categ_ids = self.env['custom.product.category'].search([('id', '=', self.custom_product_category_ids.id)])
        if comptable_:
            for amen_id in comptable_:
                choise.append((str(amen_id.id), str(amen_id.sys_ctrl)))
        # print(comptable_)
        return choise

    """
    # select_avancement= fields.Selection(selection=lambda self: self._comptable_sys_ctrl())
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    #     ('other', 'Other'),
    # ], required=True, default='male')
    
    def _comptable_sys_ctrl(self):
        comptable_sys_ctrl = [('yes', 'Yes'), ('no', 'No')]
        # comptable_sys_ctrl = dict(self.env['situation.comptable'].search([]).sys_ctrl)
        # categ_val = dict(self._columns['sec_catoegory'].selection).get(categ)
        # env['account.invoice']._columns['payment_method'].selection
        # comptable_sys_ctrl = dict(self.env['situation.comptable']._columns['sys_ctrl'].selection)[o.sys_ctrl]
        # dict(env['account.invoice']._columns['state'].selection)[o.state]

        return comptable_sys_ctrl
"""


"""
    myfield = fields.Selection(selection='_get_selection', string='What do you want ?') 

    @api.onchange('building')
	def _get_selection(self):
		choise = []
		ret_ids = self.env['sim.mymod'].search([['cols', '=', self.building.id],])
		for amen_id in ret_ids:
            amenity_obj = self.env['sim.mymod'].browse(amen_id.id)
            print amenity_obj.id
            print amenity_obj.name
            choise.append(str(amenity_obj.id), str(amenity_obj.name))
            print choise  
		return choise
"""
