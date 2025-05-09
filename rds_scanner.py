import boto3
import sys
import json

def list_rds_instances(region):
    rds = boto3.client('rds', region_name=region)
    response = rds.describe_db_instances()
    
    result = []
    for db in response['DBInstances']:
        info = {
            "DBInstanceIdentifier": db['DBInstanceIdentifier'],
            "Engine": db['Engine'],
            "Status": db['DBInstanceStatus'],
            "Endpoint": db['Endpoint']['Address']
        }
        result.append(info)
    
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rds_scanner.py <aws-region>")
        sys.exit(1)

    region = sys.argv[1]
    rds_data = list_rds_instances(region)
    print(json.dumps(rds_data, indent=2))

