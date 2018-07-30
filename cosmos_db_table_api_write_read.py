from azure.cosmosdb.table import TableService
the_connection_string = "DefaultEndpointsProtocol=https;AccountName=njesptable;AccountKey=SbXCFNzDS0gZGFlNMAQ6kPoIWZp1hvFFLIGAqMwdRLdgC4N7NMj6NAb8vOwOWnFA9APrPBDLXJXaskYg1Kb2hA==;TableEndpoint=https://njesptable.table.cosmosdb.azure.com:443/;"
TableService(endpoint_suffix="table.cosmosdb.azure.com",
             connection_string=the_connection_string)
