# Copyright (c) 2024, Thiago Cardoso and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
import json
from datetime import datetime, timedelta
from frappe import _
from datetime import datetime, timedelta

class Appointment(Document):
    def validate(self):
        self.end_date = calculate_end_date(self.start_date, self.duration)
        self.check_for_seller_availability()
        
    def check_for_seller_availability(self):
        from frappe.utils import flt
        
        # Query the database using Frappe ORM
        conflicting_appointments = frappe.get_all(
            'Appointment',
            filters={
                'seller': self.seller,
                'status': ['!=', 'Canceled'],
                'name': ['!=', self.name or ''],
                'start_date': ['<', self.end_date],
                'end_date': ['>', self.start_date],
                'docstatus': ['<', 2]
            },
            fields=['name']
        )

        # Check if there are any conflicting appointments
        if conflicting_appointments:
            frappe.throw(_(f"The seller {self.seller} is not available during the selected time slot."))



def calculate_end_date(start_date, duration):
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')

    hours, minutes, seconds = map(int, duration.split(':'))
    duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)

    end_date = start_date + duration

    return end_date.strftime('%Y-%m-%d %H:%M:%S')

@frappe.whitelist()
def get_events(start, end, filters=None):
    events = []
    start = frappe.utils.getdate(start)
    end = frappe.utils.getdate(end)

    filters = json.loads(filters) if filters else {}

    events_list = frappe.get_all(
        "Appointment",
        fields=["name", "start_date", "end_date", "client_name", "status"],
        filters=[
            ["start_date", ">=", start],
            ["end_date", "<=", end]
        ] + filters,
    )
        
    for events in events_list:
        title = events.start_date.strftime('%H:%M') + " - " + events.name
        events.append({
            "name": events.name,
            "start": events.start_date.strftime('%Y-%m-%d %H:%M:%S'),
            "end": events.end_date.strftime('%Y-%m-%d %H:%M:%S'),
            "title": title,
            "status": events.status,
            "allDay": False,
        })
    return events


