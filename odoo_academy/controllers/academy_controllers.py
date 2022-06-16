# -*- coding:'utf-8' -*-

from odoo import http

class Academy(http.Controller):
    @http.route('/academy/', auth='public', website=True, sitemap=True)
    def index(self,**kw):
        return "Hello World!"
    
    @http.route('/academy/courses/', auth='public', website=True, sitemap=False)
    def courses(self,**kw):
        courses = http.request.env['academy.course'].search([])
        return http.request.render('odoo_academy.course_website',{
            'courses': courses,
        })
    
    @http.route('/academy/<model("academy.session"):session>/', auth='public', website=True, sitemap=False)
    def session(self, session):
        return http.request.render('odoo_academy.session_website', {
            'session': session,
        })