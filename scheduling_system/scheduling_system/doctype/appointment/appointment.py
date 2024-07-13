# Copyright (c) 2024, Thiago Cardoso and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
from frappe.utils import getdate
import json
from datetime import datetime, timedelta
from frappe import _

class Appointment(Document):
    def validate(self):
        self.end_date = calculate_end_date(self.start_date, self.duration)
        self.check_for_seller_availability()
        
    def check_for_seller_availability(self):
        
        existing_appointment = frappe.db.sql("""
            SELECT
                name
            FROM
                `tabAppointment`
            WHERE
                seller = %(seller)s
                AND status != 'Canceled'
                AND name != %(name)s
                AND (
                    start_date < %(end_date)s AND end_date > %(start_date)s
                )
                AND docstatus < 2
        """, {
            'seller': self.seller,
            'name': self.name or '',
            'start_date': self.start_date,
            'end_date': self.end_date
        })
        
        if existing_appointment:
            frappe.throw(f"The seller {self.seller} is not available during the selected time slot.")

				



from datetime import datetime, timedelta

def calculate_end_date(start_date, duration):
    # Ensure start_date is a datetime object
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')

    # Convert duration to timedelta
    hours, minutes, seconds = map(int, duration.split(':'))
    duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)

    # Calculate end date
    end_date = start_date + duration

    return end_date.strftime('%Y-%m-%d %H:%M:%S')

@frappe.whitelist()
def get_events(start, end, filters=None):
    events = []
    start = frappe.utils.getdate(start)
    end = frappe.utils.getdate(end)

    filters = json.loads(filters) if filters else {}

    event_list = frappe.get_all(
        "Appointment",
        fields=["name", "start_date", "end_date", "client_name", "status"],
        filters=[
            ["start_date", ">=", start],
            ["end_date", "<=", end]
        ] + filters,
    )
        
    for event in event_list:
        color = {
            'Scheduled': '#28a745',  # green
            'Finished': '#007bff',   # blue
            'Canceled': '#dc3545',   # red
        }.get(event.status, '#6c757d')  # grey for other statuses

        events.append({
            "name": event.name,
            "start": event.start_date.strftime('%Y-%m-%d %H:%M:%S'),
            "end": event.end_date.strftime('%Y-%m-%d %H:%M:%S'),
            "title": event.client_name,
            "status": event.status,
            "allDay": False,  # add this line
        })
    return events