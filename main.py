from json import dump, loads
import requests


def get_json_prices():
    cookies = {
        "MVID_GUEST_ID": "21261106415",
        "BIGipServeratg-ps-prod_tcp80": "2416237578.20480.0000",
        "_ym_d": "1661789718",
        "_ym_uid": "1661789718497798801",
        "_ga": "GA1.3.1661789718.1661789718",
        "_gid": "GA1.3.1661789718.1661789718",
        "sub_id1_c": "91778",
        "sub_id2_c": "1faafedecf322635e9a0245da27adfd6e5dbc5db",
        "partnerSrc": "advcake",
        "advcake_click_id": "1faafedecf322635e9a0245da27adfd6e5dbc5db",
        "advcake_utm_partner": "91778",
        "advcake_utm_webmaster": "gdeslon",
        "__cpatrack": "advcake_cpa",
        "__SourceTracker": "advcake__cpa",
        "admitad_deduplication_cookie": "advcake__cpa",
        "__allsource": "advcake",
        "__sourceid": "advcake",
        "advcake_track_url": "https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_content%3Dgdeslon%26utm_medium%3Dcpa%26utm_source%3Dadvcake%26utm_campaign%3D91778%26advcake_params%3D1faafedecf322635e9a0245da27adfd6e5dbc5db%26sub_id1%3D91778%26sub_id2%3D1faafedecf322635e9a0245da27adfd6e5dbc5db",
        "advcake_track_id": "1da84184-4fd7-170c-6e4d-25b30133a8f4",
        "advcake_session_id": "2b788c42-8405-5236-f101-0ca55ee421fd",
        "st_uid": "4cfdda6c68bfa15487a4bd7032742d3b",
        "__lhash_": "54c2abe7b64d95200a6ffe227ec72d09",
        "__hash_": "712f70241fe2fb49d10b6c6a77cff89b",
        "CACHE_INDICATOR": "false",
        "COMPARISON_INDICATOR": "false",
        "HINTS_FIO_COOKIE_NAME": "2",
        "JSESSIONID": "sRyKjPtJk4lhbQ2QNX8wyBnPLdhLhJ2pCTS9rSkD3LytJcdtlmzF!-1609380260",
        "MVID_AB_SERVICES_DESCRIPTION": "var2",
        "MVID_ADDRESS_COMMENT_AB_TEST": "2",
        "MVID_BLACK_FRIDAY_ENABLED": "true",
        "MVID_CALC_BONUS_RUBLES_PROFIT": "false",
        "MVID_CART_MULTI_DELETE": "false",
        "MVID_CATALOG_STATE": "1",
        "MVID_CHECKOUT_REGISTRATION_AB_TEST": "2",
        "MVID_CITY_ID": "CityCZ_2128",
        "MVID_EXP_NEW_RANKING": "0",
        "MVID_FILTER_CODES": "true",
        "MVID_FILTER_TOOLTIP": "1",
        "MVID_FLOCKTORY_ON": "true",
        "MVID_GEOLOCATION_NEEDED": "true",
        "MVID_GET_LOCATION_BY_DADATA": "DaData",
        "MVID_GIFT_KIT": "true",
        "MVID_GTM_DELAY": "true",
        "MVID_HANDOVER_SUMMARY": "true",
        "MVID_IS_NEW_BR_WIDGET": "true",
        "MVID_KLADR_ID": "2300000100000",
        "MVID_LAYOUT_TYPE": "1",
        "MVID_LP_HANDOVER": "0",
        "MVID_LP_SOLD_VARIANTS": "2",
        "MVID_MCLICK": "true",
        "MVID_MINI_PDP": "true",
        "MVID_MOBILE_FILTERS": "true",
        "MVID_NEW_ACCESSORY": "true",
        "MVID_NEW_DESKTOP_FILTERS": "true",
        "MVID_NEW_LK_CHECK_CAPTCHA": "true",
        "MVID_NEW_LK_OTP_TIMER": "true",
        "MVID_NEW_MBONUS_BLOCK": "true",
        "MVID_REGION_ID": "11",
        "MVID_REGION_SHOP": "S911",
        "MVID_SERVICES": "111",
        "MVID_SERVICES_MINI_BLOCK": "var2",
        "MVID_TAXI_DELIVERY_INTERVALS_VIEW": "new",
        "MVID_TIMEZONE_OFFSET": "3",
        "MVID_WEBP_ENABLED": "true",
        "NEED_REQUIRE_APPLY_DISCOUNT": "true",
        "PRESELECT_COURIER_DELIVERY_FOR_KBT": "true",
        "PROMOLISTING_WITHOUT_STOCK_AB_TEST": "2",
        "SENTRY_ERRORS_RATE": "0.1",
        "SENTRY_TRANSACTIONS_RATE": "0.5",
        "bIPs": "1949759381",
        "flacktory": "no",
        "searchType2": "3",
        "_ga": "GA1.2.1661789718.1661789718",
        "_gid": "GA1.2.1661789718.1661789718",
        "_dc_gtm_UA-1873769-1": "1",
        "_sp_ses.d61c": "*",
        "_sp_id.d61c": "dbf6dacf-ddb8-4a0b-b74d-b49b8063567f.1661939088.1.1661939088..974de565-8a70-453d-b945-dff869e7b434..438773ef-93f7-4ff6-9779-3f0376aa9f28.1661939087920.1",
        "_ym_isad": "2",
        "_dc_gtm_UA-1873769-37": "1",
        "SMSError": "",
        "authError": "",
        "uxs_uid": "8ffcddd0-2911-11ed-b587-358f1db446ac",
        "gdeslon.ru.__arc_domain": "gdeslon.ru",
        "gdeslon.ru.user_id": "99001f7d-b62c-4e5b-838f-6e7f61fef1e9",
        "tmr_lvid": "682ffa8a51537af8521930ae844df8cd",
        "tmr_lvidTS": "1661939092786",
        "flocktory-uuid": "b6180cc2-7b3d-4d7b-a99a-68356c2a9ff0-1",
        "afUserId": "9b5aaea3-c31c-4432-85c3-136ccb15d0ca-p",
        "AF_SYNC": "1661939094397",
        "tmr_detect": "0%7C1661939095095",
        "MVID_CART_AVAILABILITY": "true",
        "MVID_CREDIT_AVAILABILITY": "true",
        "MVID_SMART_BANNER_BOTTOM": "true",
        "tmr_reqNum": "216",
        "MVID_ENVCLOUD": "prod2",
        "_ga_BNX5WPP3YK": "GS1.1.1661939087.6.1.1661939102.45.0.0",
        "_ga_CFMZTSS5FM": "GS1.1.1661939087.6.1.1661939102.0.0.0",
        "mindboxDeviceUUID": "ee867241-034c-4b2e-ac3a-4d9e0180b4d2",
        "directCrm-session": "%7B%22deviceGuid%22%3A%22ee867241-034c-4b2e-ac3a-4d9e0180b4d2%22%7D",
    }

    headers = {
        "authority": "www.mvideo.ru",
        "accept": "application/json",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "baggage": "sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=d11ccffd42534466b37dd40a4bed3324,sentry-sample_rate=0%2C5",
        # Requests sorts cookies= alphabetically
        # 'cookie': 'MVID_GUEST_ID=21261106415; BIGipServeratg-ps-prod_tcp80=2416237578.20480.0000; _ym_d=1661789718; _ym_uid=1661789718497798801; _ga=GA1.3.1661789718.1661789718; _gid=GA1.3.1661789718.1661789718; sub_id1_c=91778; sub_id2_c=1faafedecf322635e9a0245da27adfd6e5dbc5db; partnerSrc=advcake; advcake_click_id=1faafedecf322635e9a0245da27adfd6e5dbc5db; advcake_utm_partner=91778; advcake_utm_webmaster=gdeslon; __cpatrack=advcake_cpa; __SourceTracker=advcake__cpa; admitad_deduplication_cookie=advcake__cpa; __allsource=advcake; __sourceid=advcake; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_content%3Dgdeslon%26utm_medium%3Dcpa%26utm_source%3Dadvcake%26utm_campaign%3D91778%26advcake_params%3D1faafedecf322635e9a0245da27adfd6e5dbc5db%26sub_id1%3D91778%26sub_id2%3D1faafedecf322635e9a0245da27adfd6e5dbc5db; advcake_track_id=1da84184-4fd7-170c-6e4d-25b30133a8f4; advcake_session_id=2b788c42-8405-5236-f101-0ca55ee421fd; st_uid=4cfdda6c68bfa15487a4bd7032742d3b; __lhash_=54c2abe7b64d95200a6ffe227ec72d09; __hash_=712f70241fe2fb49d10b6c6a77cff89b; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; JSESSIONID=sRyKjPtJk4lhbQ2QNX8wyBnPLdhLhJ2pCTS9rSkD3LytJcdtlmzF!-1609380260; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CHECKOUT_REGISTRATION_AB_TEST=2; MVID_CITY_ID=CityCZ_2128; MVID_EXP_NEW_RANKING=0; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GTM_DELAY=true; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=2300000100000; MVID_LAYOUT_TYPE=1; MVID_LP_HANDOVER=0; MVID_LP_SOLD_VARIANTS=2; MVID_MCLICK=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_REGION_ID=11; MVID_REGION_SHOP=S911; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; bIPs=1949759381; flacktory=no; searchType2=3; _ga=GA1.2.1661789718.1661789718; _gid=GA1.2.1661789718.1661789718; _dc_gtm_UA-1873769-1=1; _sp_ses.d61c=*; _sp_id.d61c=dbf6dacf-ddb8-4a0b-b74d-b49b8063567f.1661939088.1.1661939088..974de565-8a70-453d-b945-dff869e7b434..438773ef-93f7-4ff6-9779-3f0376aa9f28.1661939087920.1; _ym_isad=2; _dc_gtm_UA-1873769-37=1; SMSError=; authError=; uxs_uid=8ffcddd0-2911-11ed-b587-358f1db446ac; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=99001f7d-b62c-4e5b-838f-6e7f61fef1e9; tmr_lvid=682ffa8a51537af8521930ae844df8cd; tmr_lvidTS=1661939092786; flocktory-uuid=b6180cc2-7b3d-4d7b-a99a-68356c2a9ff0-1; afUserId=9b5aaea3-c31c-4432-85c3-136ccb15d0ca-p; AF_SYNC=1661939094397; tmr_detect=0%7C1661939095095; MVID_CART_AVAILABILITY=true; MVID_CREDIT_AVAILABILITY=true; MVID_SMART_BANNER_BOTTOM=true; tmr_reqNum=216; MVID_ENVCLOUD=prod2; _ga_BNX5WPP3YK=GS1.1.1661939087.6.1.1661939102.45.0.0; _ga_CFMZTSS5FM=GS1.1.1661939087.6.1.1661939102.0.0.0; mindboxDeviceUUID=ee867241-034c-4b2e-ac3a-4d9e0180b4d2; directCrm-session=%7B%22deviceGuid%22%3A%22ee867241-034c-4b2e-ac3a-4d9e0180b4d2%22%7D',
        "referer": "https://www.mvideo.ru/product-list-page?q=%D0%BD%D0%B0%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B8&category=noutbuki-118",
        "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sentry-trace": "d11ccffd42534466b37dd40a4bed3324-ae1aa96148bf26bb-0",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        "x-set-application-id": "aaa33529-1c9e-4709-99aa-a93f8c0fdfa8",
    }

    params = {
        "productIds": "30063389,30063862,30063386,30063387,30063680,30063385,30063388,30063860,30062106,30056687,30059533,30062056,30061223,30062329,30056685,30062055,30056686,30061113,30062325,30061887,30061888,30061553,30061244,30058344",
        "addBonusRubles": "true",
        "isPromoApplied": "true",
    }

    response = requests.get(
        "https://www.mvideo.ru/bff/products/prices",
        params=params,
        cookies=cookies,
        headers=headers,
    )
    return response.json()


def get_json_description():
    cookies = {
        "MVID_GUEST_ID": "21261106415",
        "BIGipServeratg-ps-prod_tcp80": "2416237578.20480.0000",
        "_ym_d": "1661789718",
        "_ym_uid": "1661789718497798801",
        "_ga": "GA1.3.1661789718.1661789718",
        "_gid": "GA1.3.1661789718.1661789718",
        "sub_id1_c": "91778",
        "sub_id2_c": "1faafedecf322635e9a0245da27adfd6e5dbc5db",
        "partnerSrc": "advcake",
        "advcake_click_id": "1faafedecf322635e9a0245da27adfd6e5dbc5db",
        "advcake_utm_partner": "91778",
        "advcake_utm_webmaster": "gdeslon",
        "__cpatrack": "advcake_cpa",
        "__SourceTracker": "advcake__cpa",
        "admitad_deduplication_cookie": "advcake__cpa",
        "__allsource": "advcake",
        "__sourceid": "advcake",
        "advcake_track_url": "https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_content%3Dgdeslon%26utm_medium%3Dcpa%26utm_source%3Dadvcake%26utm_campaign%3D91778%26advcake_params%3D1faafedecf322635e9a0245da27adfd6e5dbc5db%26sub_id1%3D91778%26sub_id2%3D1faafedecf322635e9a0245da27adfd6e5dbc5db",
        "advcake_track_id": "1da84184-4fd7-170c-6e4d-25b30133a8f4",
        "advcake_session_id": "2b788c42-8405-5236-f101-0ca55ee421fd",
        "st_uid": "4cfdda6c68bfa15487a4bd7032742d3b",
        "__lhash_": "54c2abe7b64d95200a6ffe227ec72d09",
        "__hash_": "712f70241fe2fb49d10b6c6a77cff89b",
        "CACHE_INDICATOR": "false",
        "COMPARISON_INDICATOR": "false",
        "HINTS_FIO_COOKIE_NAME": "2",
        "JSESSIONID": "sRyKjPtJk4lhbQ2QNX8wyBnPLdhLhJ2pCTS9rSkD3LytJcdtlmzF!-1609380260",
        "MVID_AB_SERVICES_DESCRIPTION": "var2",
        "MVID_ADDRESS_COMMENT_AB_TEST": "2",
        "MVID_BLACK_FRIDAY_ENABLED": "true",
        "MVID_CALC_BONUS_RUBLES_PROFIT": "false",
        "MVID_CART_MULTI_DELETE": "false",
        "MVID_CATALOG_STATE": "1",
        "MVID_CHECKOUT_REGISTRATION_AB_TEST": "2",
        "MVID_CITY_ID": "CityCZ_2128",
        "MVID_EXP_NEW_RANKING": "0",
        "MVID_FILTER_CODES": "true",
        "MVID_FILTER_TOOLTIP": "1",
        "MVID_FLOCKTORY_ON": "true",
        "MVID_GEOLOCATION_NEEDED": "true",
        "MVID_GET_LOCATION_BY_DADATA": "DaData",
        "MVID_GIFT_KIT": "true",
        "MVID_GTM_DELAY": "true",
        "MVID_HANDOVER_SUMMARY": "true",
        "MVID_IS_NEW_BR_WIDGET": "true",
        "MVID_KLADR_ID": "2300000100000",
        "MVID_LAYOUT_TYPE": "1",
        "MVID_LP_HANDOVER": "0",
        "MVID_LP_SOLD_VARIANTS": "2",
        "MVID_MCLICK": "true",
        "MVID_MINI_PDP": "true",
        "MVID_MOBILE_FILTERS": "true",
        "MVID_NEW_ACCESSORY": "true",
        "MVID_NEW_DESKTOP_FILTERS": "true",
        "MVID_NEW_LK_CHECK_CAPTCHA": "true",
        "MVID_NEW_LK_OTP_TIMER": "true",
        "MVID_NEW_MBONUS_BLOCK": "true",
        "MVID_REGION_ID": "11",
        "MVID_REGION_SHOP": "S911",
        "MVID_SERVICES": "111",
        "MVID_SERVICES_MINI_BLOCK": "var2",
        "MVID_TAXI_DELIVERY_INTERVALS_VIEW": "new",
        "MVID_TIMEZONE_OFFSET": "3",
        "MVID_WEBP_ENABLED": "true",
        "NEED_REQUIRE_APPLY_DISCOUNT": "true",
        "PRESELECT_COURIER_DELIVERY_FOR_KBT": "true",
        "PROMOLISTING_WITHOUT_STOCK_AB_TEST": "2",
        "SENTRY_ERRORS_RATE": "0.1",
        "SENTRY_TRANSACTIONS_RATE": "0.5",
        "bIPs": "1949759381",
        "flacktory": "no",
        "searchType2": "3",
        "_ga": "GA1.2.1661789718.1661789718",
        "_gid": "GA1.2.1661789718.1661789718",
        "_dc_gtm_UA-1873769-1": "1",
        "_sp_ses.d61c": "*",
        "_sp_id.d61c": "dbf6dacf-ddb8-4a0b-b74d-b49b8063567f.1661939088.1.1661939088..974de565-8a70-453d-b945-dff869e7b434..438773ef-93f7-4ff6-9779-3f0376aa9f28.1661939087920.1",
        "_ym_isad": "2",
        "_dc_gtm_UA-1873769-37": "1",
        "SMSError": "",
        "authError": "",
        "uxs_uid": "8ffcddd0-2911-11ed-b587-358f1db446ac",
        "gdeslon.ru.__arc_domain": "gdeslon.ru",
        "gdeslon.ru.user_id": "99001f7d-b62c-4e5b-838f-6e7f61fef1e9",
        "tmr_lvid": "682ffa8a51537af8521930ae844df8cd",
        "tmr_lvidTS": "1661939092786",
        "flocktory-uuid": "b6180cc2-7b3d-4d7b-a99a-68356c2a9ff0-1",
        "afUserId": "9b5aaea3-c31c-4432-85c3-136ccb15d0ca-p",
        "AF_SYNC": "1661939094397",
        "tmr_detect": "0%7C1661939095095",
        "MVID_CART_AVAILABILITY": "true",
        "MVID_CREDIT_AVAILABILITY": "true",
        "MVID_SMART_BANNER_BOTTOM": "true",
        "tmr_reqNum": "216",
        "MVID_ENVCLOUD": "prod2",
        "_ga_BNX5WPP3YK": "GS1.1.1661939087.6.1.1661939102.45.0.0",
        "_ga_CFMZTSS5FM": "GS1.1.1661939087.6.1.1661939102.0.0.0",
        "mindboxDeviceUUID": "ee867241-034c-4b2e-ac3a-4d9e0180b4d2",
        "directCrm-session": "%7B%22deviceGuid%22%3A%22ee867241-034c-4b2e-ac3a-4d9e0180b4d2%22%7D",
    }

    headers = {
        "authority": "www.mvideo.ru",
        "accept": "application/json",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "baggage": "sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=d11ccffd42534466b37dd40a4bed3324,sentry-sample_rate=0%2C5",
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'MVID_GUEST_ID=21261106415; BIGipServeratg-ps-prod_tcp80=2416237578.20480.0000; _ym_d=1661789718; _ym_uid=1661789718497798801; _ga=GA1.3.1661789718.1661789718; _gid=GA1.3.1661789718.1661789718; sub_id1_c=91778; sub_id2_c=1faafedecf322635e9a0245da27adfd6e5dbc5db; partnerSrc=advcake; advcake_click_id=1faafedecf322635e9a0245da27adfd6e5dbc5db; advcake_utm_partner=91778; advcake_utm_webmaster=gdeslon; __cpatrack=advcake_cpa; __SourceTracker=advcake__cpa; admitad_deduplication_cookie=advcake__cpa; __allsource=advcake; __sourceid=advcake; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_content%3Dgdeslon%26utm_medium%3Dcpa%26utm_source%3Dadvcake%26utm_campaign%3D91778%26advcake_params%3D1faafedecf322635e9a0245da27adfd6e5dbc5db%26sub_id1%3D91778%26sub_id2%3D1faafedecf322635e9a0245da27adfd6e5dbc5db; advcake_track_id=1da84184-4fd7-170c-6e4d-25b30133a8f4; advcake_session_id=2b788c42-8405-5236-f101-0ca55ee421fd; st_uid=4cfdda6c68bfa15487a4bd7032742d3b; __lhash_=54c2abe7b64d95200a6ffe227ec72d09; __hash_=712f70241fe2fb49d10b6c6a77cff89b; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; JSESSIONID=sRyKjPtJk4lhbQ2QNX8wyBnPLdhLhJ2pCTS9rSkD3LytJcdtlmzF!-1609380260; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CHECKOUT_REGISTRATION_AB_TEST=2; MVID_CITY_ID=CityCZ_2128; MVID_EXP_NEW_RANKING=0; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GTM_DELAY=true; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=2300000100000; MVID_LAYOUT_TYPE=1; MVID_LP_HANDOVER=0; MVID_LP_SOLD_VARIANTS=2; MVID_MCLICK=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_REGION_ID=11; MVID_REGION_SHOP=S911; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; bIPs=1949759381; flacktory=no; searchType2=3; _ga=GA1.2.1661789718.1661789718; _gid=GA1.2.1661789718.1661789718; _dc_gtm_UA-1873769-1=1; _sp_ses.d61c=*; _sp_id.d61c=dbf6dacf-ddb8-4a0b-b74d-b49b8063567f.1661939088.1.1661939088..974de565-8a70-453d-b945-dff869e7b434..438773ef-93f7-4ff6-9779-3f0376aa9f28.1661939087920.1; _ym_isad=2; _dc_gtm_UA-1873769-37=1; SMSError=; authError=; uxs_uid=8ffcddd0-2911-11ed-b587-358f1db446ac; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=99001f7d-b62c-4e5b-838f-6e7f61fef1e9; tmr_lvid=682ffa8a51537af8521930ae844df8cd; tmr_lvidTS=1661939092786; flocktory-uuid=b6180cc2-7b3d-4d7b-a99a-68356c2a9ff0-1; afUserId=9b5aaea3-c31c-4432-85c3-136ccb15d0ca-p; AF_SYNC=1661939094397; tmr_detect=0%7C1661939095095; MVID_CART_AVAILABILITY=true; MVID_CREDIT_AVAILABILITY=true; MVID_SMART_BANNER_BOTTOM=true; tmr_reqNum=216; MVID_ENVCLOUD=prod2; _ga_BNX5WPP3YK=GS1.1.1661939087.6.1.1661939102.45.0.0; _ga_CFMZTSS5FM=GS1.1.1661939087.6.1.1661939102.0.0.0; mindboxDeviceUUID=ee867241-034c-4b2e-ac3a-4d9e0180b4d2; directCrm-session=%7B%22deviceGuid%22%3A%22ee867241-034c-4b2e-ac3a-4d9e0180b4d2%22%7D',
        "origin": "https://www.mvideo.ru",
        "referer": "https://www.mvideo.ru/product-list-page?q=%D0%BD%D0%B0%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B8&category=noutbuki-118",
        "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sentry-trace": "d11ccffd42534466b37dd40a4bed3324-9a7fe7aceb388a8d-0",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        "x-set-application-id": "aaa33529-1c9e-4709-99aa-a93f8c0fdfa8",
    }

    json_data = {
        "productIds": [
            "30063389",
            "30063862",
            "30063386",
            "30063387",
            "30063680",
            "30063385",
            "30063388",
            "30063860",
            "30062106",
            "30056687",
            "30059533",
            "30062056",
            "30061223",
            "30062329",
            "30056685",
            "30062055",
            "30056686",
            "30061113",
            "30062325",
            "30061887",
            "30061888",
            "30061553",
            "30061244",
            "30058344",
        ],
        "mediaTypes": [
            "images",
        ],
        "category": True,
        "status": True,
        "brand": True,
        "propertyTypes": [
            "KEY",
        ],
        "propertiesConfig": {
            "propertiesPortionSize": 5,
        },
        "multioffer": False,
    }

    response = requests.post(
        "https://www.mvideo.ru/bff/product-details/list",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    return response.json()


def save_to_json_file(name, data):
    with open(name, "w", encoding="utf-8") as file:
        dump(data, file, indent=4, ensure_ascii=False)


def get_data_from_json(name):
    with open(name, "r", encoding="utf-8") as file:
        return loads(file.read())


def join_prices_and_descriptions():
    prices = get_data_from_json("prices.json")
    descriptions = get_data_from_json("descriptions.json")

    cite_product_info = descriptions["body"]["products"]
    products_descriprions = []
    for product_info in cite_product_info:
        info = {
            "productId": product_info["productId"],
            "name": product_info["name"],
            "images": product_info["images"],
        }
        products_descriprions.append(info)

    material_prices = prices["body"]["materialPrices"]
    products_prices = []
    for material in material_prices:
        product_price = {
            "product_id": material["productId"],
            "basePrice": material["price"]["basePrice"],
            "salePrice": material["price"]["salePrice"],
            "basePromoPrice": material["price"]["basePromoPrice"],
        }
        products_prices.append(product_price)

    # теперь объединяем products_descriptions и products_prices по ключу product_id
    result_data = []
    for description in products_descriprions:
        product_id = description["productId"]
        # теперь ищем элмент с таким productId в products_prices
        for price in products_prices:
            price_id = price["product_id"]
            if product_id == price_id:
                product_description = {
                    "name": description["name"],
                    "images": description["images"],
                    "price": {
                        "basePrice": price["basePrice"],
                        "salePrice": price["salePrice"],
                        "basePromoPrice": price["basePromoPrice"],
                    },
                }
                result_data.append(product_description)
            continue
    return result_data


def main():
    prices = get_json_prices()  # from get_json_prices() get list(prices)
    descriptions = get_json_description()  # from get_json_descriptions() get list(descriptions)
    save_to_json_file("prices.json", prices)  # save to json
    save_to_json_file("descriptions.json", descriptions)  # save to json
    prices = get_data_from_json("prices.json")  # ...
    result = join_prices_and_descriptions()  # ...
    save_to_json_file("result_data.json", result)  # ...
    print(join_prices_and_descriptions())


if __name__ == "__main__":
    main()
