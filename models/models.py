# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class open_a(models.Model):
#     _name = 'open_a.open_a'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Course(models.Model):
    _name = 'billdemy.course'

    name = fields.Char(string="Title", required=True)
    custom_id = fields.Char(string="Course ID")
    description = fields.Text()
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many(
        'billdemy.session', 'course_id', string="Sessions")
    

class Session(models.Model):
    _name = 'billdemy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('billdemy.course',
        ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

