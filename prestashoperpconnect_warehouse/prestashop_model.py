# -*- coding: utf-8 -*-
###############################################################################
#
#   prestashoperpconnect_customize_example for OpenERP 
#   Copyright (C) 2013 Akretion (http://www.akretion.com).
#   @author Sébastien BEAU <sebastien.beau@akretion.com>
#   prestashoperpconnect_warehouse for OpenERP 
#   Copyright (C) 2015 MyPC (http://www.mypc-concept.fr).
#   @author Simon ANDRE <simonandre.stras@gmail.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp.osv import orm, fields
from openerp.addons.connector.session import ConnectorSession
from openerp.addons.prestashoperpconnect_warehouse.unit.import_synchronizer import import_warehouses


class prestashop_backend(orm.Model):
    _inherit = 'prestashop.backend'

    def _select_versions(self, cr, uid, context=None):
        """ Available versions

        Can be inherited to add custom versions.
        """
        versions = super(prestashop_backend, self)._select_versions(cr, uid, context=context)
        versions.append(('1.6-warehouse', '1.6 Warehouse'))
        return versions

    _columns = {
        'version': fields.selection(
            _select_versions,
            string='Version',
            required=True),
        }
    
    def import_warehouses(self, cr, uid, ids, context=None):
        """ Import prestashop warehouse."""
        if not isinstance(ids, (list, tuple)):
            ids = [ids]
        session = ConnectorSession(cr, uid, context=context)
        for backend_record in self.browse(cr, uid, ids, context=context):
            import_warehouses.delay(session, backend_record.id)
        return True


class prestashop_warehouse(orm.Model):
    _name = 'prestashop.warehouse'
    _inherit = 'prestashop.binding'
    _inherits = {'stock.warehouse': 'openerp_id'}
    _description = 'Prestashop Warehouse'

    _columns = {
        'openerp_id': fields.many2one(
            'stock.warehouse',
            string='Warehouse',
            required=True,
            readonly=True,
            ondelete='cascade'
        ),
    }

    _sql_constraints = [
        ('prestashop_uniq', 'unique(backend_id, prestashop_id)',
         'A shop with the same ID on PrestaShop already exists.'),
    ]


class stock_warehouse(orm.Model):
    _inherit = 'stock.warehouse'

    _columns = {
        'prestashop_bind_ids': fields.one2many(
            'prestashop.warehouse', 'openerp_id',
            string='PrestaShop Bindings',
            readonly=True),
    }