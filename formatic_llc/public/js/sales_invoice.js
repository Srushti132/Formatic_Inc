frappe.ui.form.on('Sales Invoice Item', {
    item_code: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        
        if (row.item_code) {
            frappe.db.get_value('Item', row.item_code, 'custom_hs_code')
                .then(r => {
                    if (r && r.message) {
                        frappe.model.set_value(cdt, cdn, 'custom_hs_code', r.message.custom_hs_code);
                    }
                });
        }
    }
});



