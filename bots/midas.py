import asyncio, os, time
from playwright.async_api import async_playwright, TimeoutError as PTimeoutError

cookies = {
    'UUID': '027681750677636763168597536459451067',
    'country': 'tr',
    'midasbuyDeviceId': '067176547893401711685975364590',
    'shopcode': 'midasbuy',
    'x-trace-id': 'trace_E2tr5m7sQ1g6YHX',
    'cookie_control': '1|1',
    'tencent_tdrc': 'SCroMh4QBKS9tPwlp8b6g595recLpLUNjI',
    'tKeplerToken': 'tid0BsfsBqaK0lHYKt6mBXy8Ahio0MzFHtJp7u62edfzBso*',
    'kepler_fp': 'kfp1KWt6odq2WYYfBrZSvrQLWRzAOoIYfPo3xOknha4_R645pZISJ5EKUw**',
    'shield_FPC': 'SCJRCJNGPLUbrD2Mkk3jzFLvTpLGea1Pga',
    'lastRskxRun': '1685975407272',
    'rskxRunCookie': '0',
    'rCookie': 'aqsear6v4ttgdl2r4xjprliiy8622',
    'ftr_blst_1h': '1685975408318',
    'forterToken': '4ddc891186dc44ad8386706521fcc264_1685975389192__UDF43-mnf-a4_13ck',
    'session_token': '3d26be29f4f566dc0c42dfbac7125e9af90655c159d5ca5b8fbf7478f0121f49',
    'platform_temp_token': '',
    'select_country': 'tr',
    '_fbp': 'fb.1.1685975433360.563049308',
    '_gid': 'GA1.2.1631422335.1685975435',
    'daily_landing_pop_tr': '1',
    'kepler_ticket': 'wt2Jqr1GlxpTkvDQBuyU6yZA2K8a5WmkeDXs2q1jOCnAzeSfMqFffHz2vVxIqdFI9OdVfog0gI6ri464ya0I0FdPIwrqFkPFWvufx5dJB_QW4rc_SozQRYiCpRZ-YadG8vp8gkAlIv5-30ZVwLwf3CS1RXCVnutFnfv',
    '_ga_PNR34BM5B9': 'GS1.1.1685975436.1.1.1685975458.38.0.0',
    '_ga': 'GA1.1.1324207411.1685975435',
}

headers = {
    'authority': 'www.midasbuy.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'UUID=027681750677636763168597536459451067; country=tr; midasbuyDeviceId=067176547893401711685975364590; shopcode=midasbuy; x-trace-id=trace_E2tr5m7sQ1g6YHX; cookie_control=1|1; tencent_tdrc=SCroMh4QBKS9tPwlp8b6g595recLpLUNjI; tKeplerToken=tid0BsfsBqaK0lHYKt6mBXy8Ahio0MzFHtJp7u62edfzBso*; kepler_fp=kfp1KWt6odq2WYYfBrZSvrQLWRzAOoIYfPo3xOknha4_R645pZISJ5EKUw**; shield_FPC=SCJRCJNGPLUbrD2Mkk3jzFLvTpLGea1Pga; lastRskxRun=1685975407272; rskxRunCookie=0; rCookie=aqsear6v4ttgdl2r4xjprliiy8622; ftr_blst_1h=1685975408318; forterToken=4ddc891186dc44ad8386706521fcc264_1685975389192__UDF43-mnf-a4_13ck; session_token=3d26be29f4f566dc0c42dfbac7125e9af90655c159d5ca5b8fbf7478f0121f49; platform_temp_token=; select_country=tr; _fbp=fb.1.1685975433360.563049308; _gid=GA1.2.1631422335.1685975435; daily_landing_pop_tr=1; kepler_ticket=wt2Jqr1GlxpTkvDQBuyU6yZA2K8a5WmkeDXs2q1jOCnAzeSfMqFffHz2vVxIqdFI9OdVfog0gI6ri464ya0I0FdPIwrqFkPFWvufx5dJB_QW4rc_SozQRYiCpRZ-YadG8vp8gkAlIv5-30ZVwLwf3CS1RXCVnutFnfv; _ga_PNR34BM5B9=GS1.1.1685975436.1.1.1685975458.38.0.0; _ga=GA1.1.1324207411.1685975435',
    'if-none-match': 'W/"563ab-MBHDFFCE6dlOObEYRKRUPRKML/8"',
    'referer': 'https://www.midasbuy.com/midasbuy/tr',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

async def midas():
    async with async_playwright() as p:
        # browser = await p.chromium.launch(
        #     headless=False
        # )
        try:
            browser = await p.chromium.connect_over_cdp("http://localhost:8989")#, headless=False)
        except:
            os.system("start chrome --remote-debugging-port=8989 &")
            time.sleep(5)
            browser = await p.chromium.connect_over_cdp("http://localhost:8989")
        # device = p.devices["Desktop Chrome HiDPI"]
        context = await browser.new_context(
            # locale='en-TR',
            # geolocation={'longitude': 28.9784, 'latitude': 41.0082},
            # timezone_id="Europe/Istanbul",
            # permissions=['geolocation'],
            # extra_http_headers=headers,
            # **device
        )
        # await context.add_cookies([{"name":x, "value":cookies[x], "url":"https://www.midasbuy.com/"} for x in cookies])
        page = await context.new_page()
        try:
            await page.goto('https://www.midasbuy.com/midasbuy/tr/', timeout=1)
        except:
            pass
        input('Press any key to continue...')
        await context.storage_state(path="cookies.json")
        
        await browser.close()
        
asyncio.run(midas())