# -*- coding: utf-8 -*-
###############################################################################
#
#   prestashoperpconnect_stock_by_shop for OpenERP 
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


{   'name': 'Prestashop Connector Stock By Product',
    'version': '1.0.0',
    'category': 'Connector',
    'depends': ['prestashoperpconnect',
                ],
    'author': "MyPC,Odoo Community Association (OCA)",
    'license': 'AGPL-3',
    'description': """
Prestashop Connector Stock By Product
=====================================



""",
    'data': [
        'views/backend.xml',
    ],
    'installable': True,
    'application': False,
}