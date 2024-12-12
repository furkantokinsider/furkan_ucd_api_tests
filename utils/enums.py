test_partner = "ucdtest_13"
UCD_ENDPOINT = "http://atrium.insidethekube.com/api"
opt_taskId = "opt-153835"

HEADERS = {
    "Content-Type": "application/json",
    "x-ins-namespace": opt_taskId
}


class ENDPOINTS:
    ATTRIBUTE_V2_UPDATE = "/attribute/v2/update"
    CONTACT_API = "/contact/v1/profile"
    VERTICAL_API = "/vertical/v2/get"
