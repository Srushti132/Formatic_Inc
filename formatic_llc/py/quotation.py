import frappe
from frappe.utils import now_datetime
from erpnext.accounts.utils import get_fiscal_year
from frappe.model.naming import make_autoname



def custom_autoname(doc, method):
    fiscal_year = str(get_fiscal_year(now_datetime())[0])[-2:]  # Extract last 2 digits
    if doc.owner:
        employee = frappe.get_value("Employee", {"user_id": doc.owner}, "name")
        if not employee:
            frappe.throw("Employee code not found for the document owner.")
    else:
        frappe.throw("Document must have an owner.")

    pattern = f"{fiscal_year}{employee}"

    doc.name = make_autoname(pattern+".###","",doc)