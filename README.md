# Azure_Class

## Understanding Azure Service Tools for Data Engineers

(kindly note that this will be updated on each milestone)

## Tools Used
- Terminal/iTerm for the CLI
- Terraform
- Azure Console

## Steps to Create a Resource Group and Storage Account Using the CLI

In your terminal:

### 1. Log in to Azure
Before you start, ensure your Azure CLI is set up and you have the necessary permissions to create resources in your subscription. To log in:

```bash
az login
```

### 2. Create a New Resource Group
A resource group is a container that holds related resources for an Azure solution. To create a new resource group:

```bash
az group create --name musiliazuredec_rg --location southafricanorth
```

### 3. Confirm the Resource Group Exists
To verify that your resource group was successfully created:

```bash
az group show --name musiliazuredec_rg
```

### 4. Create a New Storage Account
A storage account provides a unique namespace for your Azure Storage data that is accessible from anywhere in the world. To create a new storage account:

```bash
az storage account create --name mystorageaccount --resource-group MyResourceGroup --location southafricannorth --sku Standard_LRS --kind StorageV2
```

### 5. Confirm the Storage Account Exists
To verify that your storage account was successfully created:

```bash
az storage account show --name mystorageaccount --resource-group musiliazuredec_rg
```

---

## Understanding the Key Clients in Azure Data Lake

While the initial steps were straightforward, the real challenge was understanding the various clients used in Azure Data Lake. Once I understood their roles, the process became much clearer. Here’s a brief overview:

### 1. Service Client (`DataLakeServiceClient`)
This is your entry point for interacting with the Data Lake service. The service client is responsible for authenticating your requests and establishing a connection to your Azure storage account.

### 2. File System Client (`FileSystemClient`)
Operating under the service client, the file system client allows you to create, manage, and delete file systems, which are similar to containers in Blob storage. This client is essential for managing your file structure within the Data Lake.

### 3. Directory Client (`DataLakeDirectoryClient`)
The directory client is created from the file system client. It helps you manage directories within the file system, enabling you to create, delete, and manage both directories and files. This is the client you use when you need to interact with specific folders and files in your Data Lake.

### Process Flow
The workflow typically follows this sequence:

`DataLakeServiceClient >> FileSystemClient >> DataLakeDirectoryClient >> Upload`

Each client is crucial for the next step in the process:
- **Service Client**: Connects to Azure.
- **File System Client**: Manages your containers (file systems).
- **Directory Client**: Handles your directory and file operations, leading to the final step of uploading your files.
