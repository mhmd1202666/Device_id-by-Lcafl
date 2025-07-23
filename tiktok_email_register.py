#!/usr/bin/env python3
import requests

import SignerPy

def xor(string):
    return "".join([hex(ord(c) ^ 5)[2:] for c in string])

url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/"

params = {
    "passport-sdk-version": "6031990",
    "device_platform": "android",
    "os": "android",
    "ssmix": "a",
    "_rticket": "1752875703408",
    "cdid": "a90f0ed5-8028-413e-a00d-77e931779d00",
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "370805",
    "version_name": "37.8.5",
    "manifest_version_code": "2023708050",
    "update_version_code": "2023708050",
    "ab_version": "37.8.5",
    "resolution": "900*1600",
    "dpi": "240",
    "device_type": "NE2211",
    "device_brand": "OnePlus",
    "language": "en",
    "os_api": "28",
    "os_version": "9",
    "ac": "wifi",
    "is_pad": "0",
    "current_region": "TW",
    "app_type": "normal",
    "sys_region": "US",
    "last_install_time": "1752871588",
    "mcc_mnc": "46692",
    "timezone_name": "Asia/Baghdad",
    "carrier_region_v2": "466",
    "residence": "TW",
    "app_language": "en",
    "carrier_region": "TW",
    "timezone_offset": "10800",
    "host_abi": "arm64-v8a",
    "locale": "en-GB",
    "ac2": "wifi",
    "uoo": "0",
    "op_region": "TW",
    "build_number": "37.8.5",
    "region": "GB",
    "ts": "1752875702",
    "iid": "7528525992324908807",
    "device_id": "7528525775047132680",
    "openudid": "7a59d727a58ee91e",
    "support_webview": "1",
    "reg_store_region": "tw",
    "user_selected_region": "0",
    "okhttp_version": "4.2.210.6-tiktok",
    "use_store_region_cookie": "1",
    "app_version":"37.8.5"
}

client = requests.session()

cookies = {
    "install_id": "7528525992324908807",
    "passport_csrf_token": "13e1ddab691a6a5ed7cd70592d960fe7",
    "passport_csrf_token_default": "13e1ddab691a6a5ed7cd70592d960fe7",
}

client.cookies.update(cookies)

email = input("enter email :")
password = input("enter password :")

payload = {
    'rules_version': "v2",
    'password': xor(password),
    'account_sdk_source': "app",
    'mix_mode': "1",
    'multi_login': "1",
    'type': "34",
    'email': xor(email),
    'email_theme': "2"
}

print(payload)

m = SignerPy.sign(params=params, payload=payload, cookie=cookies)
print(m)

headers = {
    'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_GB; NE2211; Build/SKQ1.220617.001;tt-ok/3.12.13.16)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'X-SS-STUB': m['x-ss-stub'],
    'x-tt-pba-enable': "1",
    'x-bd-kmsv': "0",
    'x-tt-dm-status': "login=1;ct=1;rt=8",
    'X-SS-REQ-TICKET': m['x-ss-req-ticket'],
    'x-bd-client-key': "#yEjw14J8W9l4SfT9U1TO60CXVvhTKWlciV4wIs/yJvoJp9e6R85bFU+QLZlj2NzfUISVioYXoQrs9gx6",
    'x-tt-passport-csrf-token': "13e1ddab691a6a5ed7cd70592d960fe7",
    'tt-ticket-guard-public-key': "BHxT6qq83FTRAnJYjUgFDzwxX14GDgGVWmXnZftx8oJntWW03KYyAqdengSdAMgufFURdqiqF23x6RFV+F4593I=",
    'sdk-version': "2",
    'tt-ticket-guard-iteration-version': "0",
    'tt-ticket-guard-client-data': "eyJyZXFfY29udGVudCI6InRpY2tldCxwYXRoLHRpbWVzdGFtcCIsInJlcV9zaWduIjoiTUVZQ0lRRExiZVFWOHVVUFlYaGRPWHpseEJ2VG5YdUtXUisxQm9WVmtYdW1oa1lQbEFJaEFNdjlNeEdadlR4d3ovc2lrQUNWaFZlSmRISm1wcTR2QkFGMm5nS0JybW1SIiwidGltZXN0YW1wIjoxNzUyODc1NzAxLCJ0c19zaWduIjoidHMuMS4zNWJlNDgzYzc5NGYxMzkyMjA1NTZlODFiMTdkY2UxYzlkZjBjODQ0OGYwYzVjMmY0NmRkMjZjZjdmODU5ODkyMGU3MGI0YmRhODJjMTM4MzZlNWNmYTE4Mzk0ZDcwMjQwZjhhZjE2MzFmMTY1YWU5NjAxMjJlZWZmZDQ1MzNkZCJ9",
    'tt-ticket-guard-version': "3",
    'passport-sdk-settings': "x-tt-token",
    'passport-sdk-sign': "x-tt-token",
    'passport-sdk-version': "6031990",
    'x-tt-bypass-dp': "1",
    'oec-vc-sdk-version': "3.0.5.i18n",
    'x-vc-bdturing-sdk-version': "2.3.8.i18n",
    'x-tt-request-tag': "n=0;nr=011;bg=0",
    'x-tt-pba-enable': "1",
    'X-Ladon': m['x-ladon'],
    'X-Khronos': m['x-khronos'],
    'X-Argus': m['x-argus'],
    'X-Gorgon': m['x-gorgon'],
}

response = client.post(url, data=payload, headers=headers, params=params)
print(response.text)

if "email_ticket" in response.text:
    print("success")
else:
    print("error")

url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/register_verify_login/"
params = {
    "passport-sdk-version": "6031990",
    "device_platform": "android",
    "os": "android",
    "ssmix": "a",
    "_rticket": "1752875715998",
    "cdid": "a90f0ed5-8028-413e-a00d-77e931779d00",
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "370805",
    "version_name": "37.8.5",
    "manifest_version_code": "2023708050",
    "update_version_code": "2023708050",
    "ab_version": "37.8.5",
    "resolution": "900*1600",
    "dpi": "240",
    "device_type": "NE2211",
    "device_brand": "OnePlus",
    "language": "en",
    "os_api": "28",
    "os_version": "9",
    "ac": "wifi",
    "is_pad": "0",
    "current_region": "TW",
    "app_type": "normal",
    "sys_region": "US",
    "last_install_time": "1752871588",
    "mcc_mnc": "46692",
    "timezone_name": "Asia/Baghdad",
    "carrier_region_v2": "466",
    "residence": "TW",
    "app_language": "en",
    "carrier_region": "TW",
    "timezone_offset": "10800",
    "host_abi": "arm64-v8a",
    "locale": "en-GB",
    "ac2": "wifi",
    "uoo": "0",
    "op_region": "TW",
    "build_number": "37.8.5",
    "region": "GB",
    "ts": "1752875714",
    "iid": "7528525992324908807",
    "device_id": "7528525775047132680",
    "openudid": "7a59d727a58ee91e",
    "support_webview": "1",
    "reg_store_region": "tw",
    "user_selected_region": "0",
    "okhttp_version": "4.2.210.6-tiktok",
    "use_store_region_cookie": "1",
    "app_version":"37.8.5"
}

code = input("enter code :")

payload = {
    'birthday': "2002-02-24",
    'fixed_mix_mode': "1",
    'code': xor(code),
    'account_sdk_source': "app",
    'mix_mode': "1",
    'multi_login': "1",
    'type': "34",
    'email': payload["email"]
}

m = SignerPy.sign(params=params, payload=payload, cookie=cookies)

headers = {
    'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_GB; NE2211; Build/SKQ1.220617.001;tt-ok/3.12.13.16)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'X-SS-STUB': m['x-ss-stub'],
    'x-tt-pba-enable': "1",
    'x-bd-kmsv': "0",
    'x-tt-dm-status': "login=1;ct=1;rt=8",
    'X-SS-REQ-TICKET':  m['x-ss-req-ticket'],
    'x-bd-client-key': "#yEjw14J8W9l4SfT9U1TO60CXVvhTKWlciV4wIs/yJvoJp9e6R85bFU+QLZlj2NzfUISVioYXoQrs9gx6",
    'x-tt-passport-csrf-token': "13e1ddab691a6a5ed7cd70592d960fe7",
    'tt-ticket-guard-public-key': "BHxT6qq83FTRAnJYjUgFDzwxX14GDgGVWmXnZftx8oJntWW03KYyAqdengSdAMgufFURdqiqF23x6RFV+F4593I=",
    'sdk-version': "2",
    'tt-ticket-guard-iteration-version': "0",
    'X-Tt-Token': "0370c890e123ee06efe9bfd83298e202d701f5742061f9f4abf220abb27fdc3f7d8a2389a8db93c3ea4e1a4e24cdf19e194ed15acffd5e582ca1177dc53e71281973c50f7f5a498c43e00a210bb650575fb5c2488922fbbc51cdb25cdb4b960d90767--0a4e0a2088aefe8e956071b58d7e88474a1b08e4021225bcf93fb9044dc0b2164e4680d71220e811fecf461dd5e810309dae1c0fa532912e69b7449d6ce777d95fe44c8dc8b41801220674696b746f6b-3.0.0",
    'tt-ticket-guard-version': "3",
    'passport-sdk-settings': "x-tt-token",
    'passport-sdk-sign': "x-tt-token",
    'passport-sdk-version': "6031990",
    'x-tt-bypass-dp': "1",
    'oec-vc-sdk-version': "3.0.5.i18n",
    'x-vc-bdturing-sdk-version': "2.3.8.i18n",
    'x-tt-request-tag': "n=0;nr=011;bg=0",
    'x-tt-pba-enable': "1",
    'X-Ladon': m['x-ladon'],
    'X-Khronos': m['x-khronos'],
    'X-Argus': m['x-argus'],
    'X-Gorgon': m['x-gorgon'],
}

response = client.post(url, data=payload, headers=headers, params=params)
print(response.text)

if "session_key" in response.text:
    with open("account.txt", "a") as m:
        m.write(f"email : {email} | password : {password} | sessionid : {response.json()['data']['session_key']} | username : {response.json()['data']['name']}\n")
    sessionid = response.json()["data"]["session_key"]
    print(sessionid)
    with open("session.txt", "a") as f:
        f.write(sessionid + "\n")
else:
    print("IP Band")