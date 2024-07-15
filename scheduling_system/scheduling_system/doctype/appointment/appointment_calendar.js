frappe.views.calendar['Appointment'] = {
  field_map: {
      start: 'start',
      end: 'end',
      id: 'name',
      title: 'title',
      status: 'status',
      alldata: 'allDay',
  },
  get_events_method: 'scheduling_system.scheduling_system.doctype.appointment.appointment.get_events',
  get_css_class: function (data) {
    console.log(data.status);
   if (data.status == "Scheduled") {
			return "info";
		} else if (data.status == "Finished") {
			return "success";
		} else if (data.status == "Canceled") {
			return "danger";
		}
  }
}