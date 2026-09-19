/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { DateTimeField } from "@web/views/fields/datetime/datetime_field";
import { ListRenderer } from "@web/views/list/list_renderer";

// ── 1. Patch ListRenderer.getFormattedValue ────────────────────
patch(ListRenderer.prototype, {
    getFormattedValue(column, record) {
        const fieldName = column.name;
        const field = this.fields[fieldName];
        if (!field) return super.getFormattedValue(column, record);
        
        // For date/datetime fields, use direct luxon formatting
        if (field.type === "date" || field.type === "datetime") {
            const value = record.data[fieldName];
            if (!value) return "";
            if (field.type === "date") {
                return value.toFormat("dd/MM/yyyy");
            }
            return value.toFormat("dd/MM/yyyy HH:mm:ss");
        }
        return super.getFormattedValue(column, record);
    },
});

// ── 2. Patch DateTimeField for form view ───────────────────────
patch(DateTimeField.prototype, {
    getFormattedValue(valueIndex, numeric) {
        return super.getFormattedValue(valueIndex, true);
    },
});


