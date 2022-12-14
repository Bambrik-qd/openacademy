# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Open-academy course'
    name = fields.Char(string="Title", required=True)
    description = fields.Text()


class openacademy(models.Model):
     _name = 'openacademy.openacademy'
     _description = 'open-academy'

     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

     @api.depends('value')
     def _value_pc(self):
         for record in self:
             record.value2 = float(record.value) / 100
    