from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'
    user_type = fields.Selection([
        ('admin', 'Admin'),
        ('saleperson', 'Salsperson'),
        ('sales_manager', 'Sales Manager'),
        ('contractor', 'Contractor'),
        ('qcmanager', 'QC Manager'),
        ('qc', 'QC')
    ], string="User Type", default='admin')
    country_id = fields.Many2one('library.country', string="Location#", tracking=True)
    team_id = fields.Many2one('crm.team', string="Team Under")

