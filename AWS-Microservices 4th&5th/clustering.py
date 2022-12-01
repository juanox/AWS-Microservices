import json


def lambda_handler(event, context):

    zoom_level = event["queryStringParameters"]["level"]

    if 4 == int(zoom_level):
        clusters = {
            "cluster_size": 9,
            "latitude": -21.391303,
            "longitude": -69.185811
        }

    elif 5 == int(zoom_level):
        clusters = [
            {
                'cluster_size': 4,
                "latitude": -22.84111,
                "longitude": -68.169106
            },
            {
                'cluster_size': 3,
                "latitude": -21.205897,
                "longitude": -69.80718
            },
            {
                'cluster_size': 2,
                "latitude": -18.769965,
                "longitude": -69.787169
            }
        ]

    elif 6 == int(zoom_level):
        clusters = [
            {
                'cluster_size': 1,
                "latitude": -23.060296,
                "longitude": -67.241466
            },
            {
                'cluster_size': 3,
                "latitude": -22.768051,
                "longitude": -68.478319
            },
            {
                'cluster_size': 1,
                "latitude": -22.915622,
                "longitude": -70.290275
            },
            {
                'cluster_size': 1,
                "latitude": -20.491570,
                "longitude": -69.329696
            },
            {
                'cluster_size': 1,
                "latitude": -20.21015,
                "longitude": -69.801569
            },
            {
                'cluster_size': 1,
                "latitude": -19.060498,
                "longitude": -69.250661
            },
            {
                'cluster_size': 1,
                "latitude": -18.479432,
                "longitude": -70.323676
            },
        ]
    else:
        clusters = [
            {
                'cluster_size': 1,
                "latitude": -23.060296,
                "longitude": -67.241466
            },
            {
                'cluster_size': 1,
                "latitude": -22.924155,
                "longitude": -68.288103
            },
            {
                'cluster_size': 1,
                "latitude": -22.316964,
                "longitude": -68.933477
            },
            {
                'cluster_size': 1,
                "latitude": -23.063035,
                "longitude": -68.213378
            },
            {
                'cluster_size': 1,
                "latitude": -22.915622,
                "longitude": -70.290275
            },
            {
                'cluster_size': 1,
                "latitude": -20.491570,
                "longitude": -69.329696
            },
            {
                'cluster_size': 1,
                "latitude": -20.21015,
                "longitude": -69.801569
            },
            {
                'cluster_size': 1,
                "latitude": -19.060498,
                "longitude": -69.250661
            },
            {
                'cluster_size': 1,
                "latitude": -18.479432,
                "longitude": -70.323676
            },
        ]

    return({
        'isBase64Encoded': True,
        'statusCode': 200,
        'headers': {"Access-Control-Allow-Origin": "*"},
        'body': json.dumps(clusters)
    })
