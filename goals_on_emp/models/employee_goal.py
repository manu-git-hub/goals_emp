from odoo import fields, models, api

class Employee(models.Model):
    _inherit = 'hr.employee'

    employee_goal = fields.Text(string='Employee Goal', track_visibility='onchange')
    company_goal = fields.Text(string='Company Goal', track_visibility='onchange')

    @api.depends('company_id')
    def _compute_is_admin(self):
        for employee in self:
            employee.is_admin = employee.company_id and employee.company_id.user_has_groups('base.group_system')

    is_admin = fields.Boolean(compute='_compute_is_admin', string='Is Admin', store=True)

    @api.model
    def create(self, vals):
        employee = super(Employee, self).create(vals)
        if self.env.user.has_group('base.group_system'):
            employee.is_admin = True
        return employee

    def write(self, vals):
        if not self.env.user.has_group('base.group_system'):
            vals.pop('company_goal', None)
        res = super(Employee, self).write(vals)
        return res
