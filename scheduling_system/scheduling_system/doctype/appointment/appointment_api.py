import frappe

#Read all appointments
@frappe.whitelist(allow_guest=True)
def get_all_appointments():
    appointments = frappe.get_all(
        "Appointment",
        fields=["name", "client_name", "start_date", "end_date", "duration", "description", "seller", "status"]
    )
    return appointments

#read a single appointment
@frappe.whitelist(allow_guest=True)
def get_appointment(name):
    appointment = frappe.get_doc(
        "Appointment", 
        name,
        )
    return appointment

#Create an appointment
@frappe.whitelist(allow_guest=True)
def create_appointment(name, client_name, start_date, duration, description, seller):
    appointment = frappe.new_doc("Appointment")
    appointment.name = name
    appointment.client_name = client_name
    appointment.start_date = start_date
    appointment.duration = duration
    appointment.description = description
    appointment.seller = seller
    appointment.save()
    return appointment

#Update an appointment
@frappe.whitelist(allow_guest=True)
def update_appointment(name, client_name, start_date, duration, description, seller):
    appointment = frappe.get_doc("Appointment", name)
    appointment.client_name = client_name
    appointment.start_date = start_date
    appointment.duration = duration
    appointment.description = description
    appointment.seller = seller
    appointment.save()
    return appointment

#Delete an appointment
@frappe.whitelist(allow_guest=True)
def delete_appointment(name):
    appointment = frappe.get_doc("Appointment", name)
    appointment.delete()
    return appointment

