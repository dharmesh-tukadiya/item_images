import frappe

def execute():
    """Ensure Item.image is visible in list view via Property Setter."""
    if not frappe.db.exists("Property Setter", {
        "doc_type": "Item",
        "field_name": "image",
        "property": "in_list_view"
    }):
        frappe.get_doc({
            "doctype": "Property Setter",
            "doctype_or_field": "DocField",
            "doc_type": "Item",
            "field_name": "image",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        }).insert(ignore_permissions=True)