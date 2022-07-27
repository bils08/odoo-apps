# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class my_item(models.Model):
    _name = 'my.item'

    name = fields.Char(string='Name')
    tanggal = fields.Date(string='Tanggal')
    status = fields.Selection([('draft','Draft'),('approved','Approved'),('rejected','Rejected')], default='draft')
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
