import asyncio
import time
from playwright.async_api import async_playwright
from utils.browser import create_browser

async def login():
    """
    获取Tiktok登录二维码
    """
    browser = await create_browser(contextName='tiktok',
                                   timezone_id='Asia/Singapore',
                                   locale='en-US',
                                   user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')

    # 指纹检测
    # await browser['page'].goto('https://www.browserscan.net/zh/bot-detection#google_vignette')
    # await browser['page'].goto('https://www.browserscan.net/zh')

    await browser['page'].goto('https://www.tiktok.com')

    # 关闭
    input("Press Enter to exit...")
    await browser['context'].close()
    await browser['playwright'].stop()
    print('已关闭')

if __name__ == '__main__':
    asyncio.run(login())