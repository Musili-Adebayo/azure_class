
# Creare a resource group
resource "azurerm_resource_group" "musiliazuredec_rg" {
  name     = "musiliazuredec-rg"
  location = "South Africa North"
}

# Create a storage account
resource "azurerm_storage_account" "musiliazuredec_rg" {
  name                     = "musilistorageaccount"
  resource_group_name      = azurerm_resource_group.musiliazuredec_rg.name
  location                 = azurerm_resource_group.musiliazuredec_rg.location
  account_tier             = "Standard"
  account_replication_type = "GRS"
  account_kind             = "StorageV2"
  is_hns_enabled           = "true"

  tags = {
    environment = "staging"
  }
}

#Creating a Conatiner
resource "azurerm_storage_container" "musiliazuredec_rg" {
  name                  = "raw"
  storage_account_name  = azurerm_storage_account.musiliazuredec_rg.name
  container_access_type = "private"
}

# # Ingesting A file in in the container
# resource "azurerm_storage_blob" "musiliazuredec_rg" {
#   name                   = "musili_test_file"
#   storage_account_name   = azurerm_storage_account.musiliazuredec_rg.name
#   storage_container_name = azurerm_storage_container.musiliazuredec_rg.name
#   type                   = "Block"
#   source                 = "C:/Users/SURECHILL COMPANY/Downloads/musili-test-file.xlsx"
# }



