// Copyright (c) 2024, Thiago Cardoso and contributors
// For license information, please see license.txt

frappe.ui.form.on('Appointment', {
  refresh: function(frm) {
      if (frm.doc.__islocal) {
          frm.layout.make_view_switcher();
          frm.layout.switch_view('calendar');
      }
  }
});

