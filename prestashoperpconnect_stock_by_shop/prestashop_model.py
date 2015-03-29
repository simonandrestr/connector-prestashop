# -*- coding: utf-8 -*-
###############################################################################
#
#   prestashoperpconnect_customize_example for OpenERP 
#   Copyright (C) 2013 Akretion (http://www.akretion.com).
#   @author Sébastien BEAU <sebastien.beau@akretion.com>
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

class prestashop_backend(orm.Model):
    _inherit = 'prestashop.backend'
    _columns = {
        'use_stock_by_shop': fields.boolean(u"Stock By Shop", help=u"Prestashop multishop can share product quantities. If you don't share it on your backend, you must activate this option."),
        'warehouse_id': fields.many2one(
            'stock.warehouse',
            'Warehouse',
            help='Warehouse used to compute the stock quantities.'
        ),
    }
    _defaults = {
        'use_stock_by_shop': False,
    }




