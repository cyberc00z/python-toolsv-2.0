# 'By by april'

from apiclient.discovery imoort build
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = '<YOU_KEY_FILE>'
VIEW_ID = '<REPLACE_WITH_VIEW_ID>'

def initialize_analyticsreporting():
    """ Initializes an Analytics Reporting API v4 service object
    Returns:
        An authorized Analytics Reporting API v4 service object.

    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            KEY_FILE_LOCATION, SCOPES
            )
    # Build the service object
    analytics = build('analyticsreporting', 'v4', credentials=credentials)

    return analytics


def get_report(analytics):
    """ Queries the Analytics Reporting API v4
    Returns:
        The analytics response
    
    """
    return analytics.reports().batchGet(
            body= {
                'reportRequests': [
                    {
                        'viewId':VIEW_ID,
                        'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                        'metrics': [{'expression': 'ga:session'}],
                        'dimensions': [{'name':'ga:country'}]
                        }
                    ]

                }

            ).excute()

def print_response(response):
    """ Parses and prints the Analtics Reporting API V4 response
    Args:
        response: An analytics Reporting API v4 response
    
    """
    for report in response.get('reports', []):
        columnHeader = report.get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries ', [])
        for row in report.get('data', {}).get('rows', []):
            dimensions = row.get('dimensions',[])
            dataRangeValues = row.get('metrics', [])

            for header, dimension in zip(dimensionsHeaders , dimensions):
                print( header +  ": " ,  dimension)

            for i , values in enumerate(dateRangeValues):
                print('Data range: ', str(i))
                for metricHeader, value in zip(metricHeaders, values.get('values')):
                    print(metricHeader.get('name') + ": " , value)

def main():
    analytics = initialize_analyitcsreporting()
    response = get_report(analytics)
    print_response(response)

if __name__ == '__main__':
    main()
