# Inventory Quality Check

This module customizes the Odoo Inventory (`stock.picking`) model by adding a new feature, enhancing the workflow, improving the user interface, and implementing security and access control mechanisms.

## Features

1. **New Field Addition:**
   - Adds a custom boolean field `is_quality_checked` to the `stock.picking` model to track whether a quality check has been performed.

2. **Workflow Enhancement:**
   - Introduces a new `quality_check` state in the `state` field of `stock.picking`.
   - Adds a button to transition to the `quality_check` state.
   - Implements automated actions based on the new state.

3. **User Interface Improvements:**
   - Enhances the appearance of the custom field and the workflow button with custom CSS.

4. **Security and Access Control:**
   - Defines new security groups (Stock Manager).
   - Configures access control for the new feature and workflow based on user roles.

## Installation

1. Clone the repository or download the module.
2. Place the `Inventory Quality Check` folder in your Odoo `addons` directory.
3. Update the Odoo module list by navigating to **Apps** > **Update Apps List**.
4. Search for `Inventory Quality Check` and click **Install**.

## Configuration

### Security Groups

This module defines one security groups:
- **Stock Manager**: Has full access (read, write, create) to the stock.picking model.

### Custom Field

The `is_quality_checked` field is added to the `stock.picking` model and displayed in the form view under the **Other Information** section.

### Workflow Enhancement

- A new state `quality_check` is added to the `state` field.
- A button labeled `Quality Check` is added to the form view to transition to the `quality_check` state.
- When the `Quality Check` button is clicked, the state of the record changes to `quality_check`.

## Usage

1. Navigate to **Inventory** > **Operations** > **Transfers**.
2. Open any existing transfer or create a new one.
3. Fill in the required details.
4. Click on the `Quality Check` button to transition the state to `quality_check`.
5. The `is_quality_checked` field can be checked to mark that the quality check has been performed.

## License

This module is licensed under the MIT License. See the LICENSE file for more details.
