import base64
import gzip
import json

### This function is sample for following architecture.
### CloudWatch Logs (Subscription Filter) -> Lambda

def lambda_handler(event, context):
    gzip_data = base64.b64decode(event["awslogs"]["data"])
    uncompressed_data = json.loads(gzip.decompress(gzip_data))
    for log_event in uncompressed_data["logEvents"]:
        print(log_event["message"])
