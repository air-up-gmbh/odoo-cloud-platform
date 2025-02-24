# Copyright 2016-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)


{
    "name": "Monitoring: Prometheus Metrics",
    "version": "16.0.1.0.0",
    "author": "Camptocamp,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "category",
    "depends": [
        "base",
        "web",
        "server_environment",
    ],
    "website": "http://www.camptocamp.com",
    "data": [],
    "external_dependencies": {
        "python": ["prometheus_client"],
    },
    "installable": True,
}
