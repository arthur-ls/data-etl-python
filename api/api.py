import pip._vendor.requests as req


def get_api_data(url, headers, parameters):
    response = req.get(url, headers=headers, params=parameters)
    return response
