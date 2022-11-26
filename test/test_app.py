import unittest
import requests


class TestGeoipFlask(unittest.TestCase):

    def test_app_json_ipv4(self):
        geoip_response = requests.get("http://127.0.0.1:8888/api/v1.0/ip/200.42.143.3")
        geoip_response = geoip_response.json()
        self.assertEqual(geoip_response['country']['iso_code'], "AR")

    def test_app_ipv4(self):
        geoip_response = requests.get("http://127.0.0.1:8888/200.42.143.3")
        self.assertRegex(geoip_response.text, "IP: <b>200.42.143.3</b>")

    def test_app_json_ipv6(self):
        geoip_response = requests.get("http://127.0.0.1:8888/api/v1.0/ip/2001:4860:4860::8888")
        geoip_response = geoip_response.json()
        self.assertEqual(geoip_response['country']['iso_code'], "US")

    def test_app_ipv6(self):
        geoip_response = requests.get(
            "http://127.0.0.1:8888/2001:4860:4860::8888")
        self.assertRegex(geoip_response.text,
                         "IP: <b>2001:4860:4860::8888</b>")

    def test_app_ip_null(self):
        geoip_response = requests.get("http://127.0.0.1:8888/23.155.53.186")
        self.assertRegex(geoip_response.text, "<b>23.155.53.186</b>")

    def test_app_json_with_proxy_header(self):
        geoip_response = requests.get("http://127.0.0.1:8888/api/v1.0/ip/", headers={"X-Real-IP": "200.42.143.3"})
        geoip_response = geoip_response.json()
        self.assertEqual(geoip_response['country']['iso_code'], "AR")


if __name__ == '__main__':
    unittest.main()
