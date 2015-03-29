# -*- coding: utf-8 -*-/
##############################################################################
#
#    Prestashoperpconnect : OpenERP-PrestaShop connector
#    Copyright (C) 2013 Akretion (http://www.akretion.com/)
#    Copyright 2013 Camptocamp SA
#    Copyright 2015 MyPC
#    @author: Guewen Baconnier
#    @author: Alexis de Lattre <alexis.delattre@akretion.com>
#    @author Sébastien BEAU <sebastien.beau@akretion.com>
#    @author Simon ANDRE <simonandre.stras@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import logging
from openerp.addons.connector.queue.job import job
from openerp.addons.prestashoperpconnect.connector import add_checkpoint
from openerp.addons.prestashoperpconnect.unit.import_synchronizer import (
        import_batch, 
        PrestashopImportSynchronizer, 
        BatchImportSynchronizer
    )
from prestapyt import PrestaShopWebServiceError
from ..backend import prestashop_warehouse

_logger = logging.getLogger(__name__)


@prestashop_warehouse
class BatchWarehouseImport(BatchImportSynchronizer):
    _model_name = 'prestashop.warehouse',

@prestashop_warehouse
class WarehouseImport(PrestashopImportSynchronizer):
    _model_name = 'prestashop.warehouse',

@job
def import_warehouses(session, backend_id):
    import_batch(
        session, 'prestashop.warehouse', backend_id
    )