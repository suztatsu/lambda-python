import base64
import gzip
import json

### This function is sample for following architecture.
### CloudWatch Logs (Subscription Filter) -> Kinesis Data Streams -> Lambda

def lambda_handler(event, context):
    for record in event['Records']:
        gzip_data = base64.b64decode(record["Data"])
        uncompressed_data = json.loads(gzip.decompress(gzip_data))
        for log_event in uncompressed_data["logEvents"]:
            print(log_event["message"])
