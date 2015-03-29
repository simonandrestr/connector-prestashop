# -*- coding: utf-8 -*-
##############################################################################
#
#    Prestashoperpconnect : OpenERP-PrestaShop connector
#    Copyright 2013 Camptocamp SA
#    Copyright (C) 2013 Akretion (http://www.akretion.com/)
#    Copyright (C) 2015 MyPC
#    @author: Guewen Baconnier
#    @author: Alexis de Lattre <alexis.delattre@akretion.com>
#    @author Sébastien BEAU <sebastien.beau@akretion.com>
#    @author Arthur Vuillard
#    @author Simon ANDRE
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import logging
from openerp.addons.prestashoperpconnect.unit.backend_adapter import GenericAdapter
from ..backend import prestashop_warehouse

_logger = logging.getLogger(__name__)


@prestashop_warehouse
class WarehouseAdapter(GenericAdapter):
    _model_name = 'prestashop.warehouse'
    _prestashop_model = 'warehouses'
