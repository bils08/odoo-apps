# -*- coding: utf-8 -*-
from odoo import http, _, exceptions
# from odoo.http import content_disposition, request
import io
import xlsxwriter
from odoo.tests import Form
import json
import requests
import werkzeug.wrappers

class MyModule(http.Controller):

    @http.route('/my_module/my_module', auth='public', csrf=False)
    def index(self, **kw):
        return "Hello, world"

    # @http.route('/my_module/my_module/objects', auth='public')
    # def list(self, **kw):
    #     return http.request.render('my_module.listing', {
    #         'root': '/my_module/my_module',
    #         'objects': http.request.env['my_module.my_item'].search([]),
    #     })
    #
    # @http.route('/my_module/my_module/objects/<model("my_module.my_module"):obj>', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('my_module.object', {
    #         'object': obj
    #     })
