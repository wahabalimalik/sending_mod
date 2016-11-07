
from openerp import models, fields, api
class Wizard(models.TransientModel):
    _name = 'employee_payslip.hr.payslip1'
    @api.multi
    def hr_verify_sheet(self):
        result = self.env['hr.payslip'].browse(self._context.get('active_ids'))
        for line in result:
            test = self.env['hr.payslip']
            print test
            for t in test.browse(line.id):
                t.hr_verify_sheet()
            print "Code **************************"

    @api.multi
    def compute_sheet(self):
        result = self.env['hr.payslip'].browse(self._context.get('active_ids'))
        for line in result:
            test = self.env['hr.payslip']
            print test
            for t in test.browse(line.id):
                t.compute_sheet()
            print "Code **************************"
