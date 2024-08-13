terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.115.0"
    }
  }

}

#Setting up my provider
provider "azurerm" {
  features {
    # app_configuration {
    #   purge_soft_delete_on_destroy = true
    #   recover_soft_deleted         = true
    # }
  }
}
