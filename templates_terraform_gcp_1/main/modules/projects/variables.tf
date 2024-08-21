variable "project_id" {
  description = "The ID of the project to be created"
  type = string
}

variable "billing_account" {
  description = "The ID of the billing account to be used"
  type = string
}

variable "project_parent_folder" {
  description = "The ID of the parent folder where the project will be created."
  type = string
  nullable = true
}

variable "project_services_list" {
  description = "The list of the servifces other than the CRM to be enabled on the project"
  type = list(string)
}

variable "budget_amount" {
  description = "The amount of the budget to be created with the project budget"
  type = string
}

variable "budget_currency" {
  description = "The symbol of the currency to be used with the budget alert"
  type = string
  default = "USD"
}

# Budget rules:
# budget_rules
# threshold_percent: double, ex: 0.25 (25%)...
# spend_basis: either CURRENT_SPEND or FORECASTED_SPEND
variable "budget_rules" {
  description = "The rules of the budget that will be created."
  type = map(object({
    threshold_percent = number
    spend_basis = string
  }))
}

variable "notification_emails" {
  description = "The list of the notification emails to be created as notification channels"
  type = list(string)
}
