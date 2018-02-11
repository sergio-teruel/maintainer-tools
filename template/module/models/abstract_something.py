# -*- coding: utf-8 -*-
# Copyright 2018 Carlos Dauden - Tecnativa <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class AbstractSomething(models.AbstractModel):
    _name = "abstract.something"
    _description = "Abstract Somethings"
