from odoo import fields, models, api

class Employee(models.Model):
    _inherit = 'hr.employee'

    employee_goal = fields.Text(string='Employee Goal')
    company_goal = fields.Text(string="Company Goal")

  
