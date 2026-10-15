/** @odoo-module **/

import { registry } from "@web/core/registry";
import { patch } from "@web/core/utils/patch";
import { DateTimeField } from "@web/views/fields/datetime/datetime_field";

// Force numeric date formatting in list views and other formatter-based views.
const formatters = registry.category("formatters");

const originalDateFormatter = formatters.get("date");
const numericDateFormatter = (value, options = {}) => {
    return originalDateFormatter(value, { ...options, numeric: true });
};
numericDateFormatter.extractOptions = originalDateFormatter.extractOptions;

const originalDateTimeFormatter = formatters.get("datetime");
const numericDateTimeFormatter = (value, options = {}) => {
    return originalDateTimeFormatter(value, { ...options, numeric: true });
};
numericDateTimeFormatter.extractOptions = originalDateTimeFormatter.extractOptions;

formatters.add("date", numericDateFormatter, { force: true });
formatters.add("datetime", numericDateTimeFormatter, { force: true });

// Force numeric date formatting inside form views.
patch(DateTimeField.prototype, {
    getFormattedValue(valueIndex, numeric = true) {
        return super.getFormattedValue(valueIndex, true);
    },
});
