# -*- coding: utf-8 -*-
# © 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# © 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


def pre_init_hook(cr):
    """Loaded before installing the module.

    None of this module's DB modifications will be available yet.

    If you plan to raise an exception to abort install, put all code inside a
    ``with cr.savepoint():`` block to avoid broken databases.

    :param openerp.sql_db.Cursor cr:
        Database cursor.
    """
    raise NotImplementedError


def post_init_hook(cr, registry):
    """Loaded after installing the module.

    This module's DB modifications will be available.

    :param openerp.sql_db.Cursor cr:
        Database cursor.

    :param openerp.modules.registry.RegistryManager registry:
        Database registry, using v7 api.
    """
    raise NotImplementedError


def uninstall_hook(cr, registry):
    """Loaded before uninstalling the module.

    This module's DB modifications will still be available. Raise an exception
    to abort uninstallation.

    :param openerp.sql_db.Cursor cr:
        Database cursor.

    :param openerp.modules.registry.RegistryManager registry:
        Database registry, using v7 api.
    """
    raise NotImplementedError
