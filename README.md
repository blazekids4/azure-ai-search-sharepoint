# SharePoint Online Indexer

## Introduction

The SharePoint Online Indexer is a robust tool designed for efficient data extraction and indexing from SharePoint Online to Azure Cognitive Search. This guide provides an overview of CRUD operations, setup instructions, and the usage of variables and tests.

## Getting Started

### Requirements

- Azure Subscription
- SharePoint Online access
- Postman (for API interaction)

### Configuration

Before you begin, ensure you have the following:

- API key for Azure Cognitive Search
- SharePoint Online endpoint details
- Access to the Azure portal

### Installation

1. Clone this repository or download the provided Postman collection JSON.
2. Import the collection into Postman.

## How to Use This Template

### Step 1: Send Requests

Perform CRUD operations using the HTTP methods GET, POST, PUT, and DELETE. Each request type is detailed within the Postman collection. Simply select a request and click "Send".

### Step 2: View Responses

After sending a request, check the response tab to view the status code, response time, and size of the response.

### Step 3: Send New Body Data

Modify or add new data in the "Body" tab in the POST and PUT requests to alter data as needed.

### Step 4: Update Variables

Variables such as `base_url` and `api-key` are essential for customizing the requests to your environment. Update these variables within Postman to match your configuration.

### Step 5: Add Tests

Add tests in the "Tests" tab to verify the API's functionality. This helps ensure your setup is correctly interacting with Azure Cognitive Search.

## API Requests Documentation

Here are the key operations you can perform with this setup:

### Create DataSource

- **Method**: POST
- **Description**: Creates a data source in Azure Cognitive Search for SharePoint Online.
- **Endpoint**: `{{endpoint}}/datasources`

### Create Index

- **Method**: PUT
- **Description**: Creates an index in Azure Cognitive Search to store and manage the data extracted from SharePoint Online.
- **Endpoint**: `{{endpoint}}/indexes('{{index-name}}')`

### Create Indexer

- **Method**: POST
- **Description**: Creates an indexer that automatically pulls data from SharePoint Online into the Azure Cognitive Search index.
- **Endpoint**: `{{endpoint}}/indexers`

### Check Indexer Status

- **Method**: GET
- **Description**: Retrieves the current status of the indexer, providing insights into its operational state and activity.
- **Endpoint**: `{{endpoint}}/indexers/{{indexer-name}}/status`

## Pro Tips

- Organize requests into folders in Postman for better management.
- Extend testing scripts to cover more scenarios and ensure robustness.

## Related Links

- [Index data from SharePoint document libraries](https://learn.microsoft.com/en-us/azure/search/search-howto-index-sharepoint-online)
