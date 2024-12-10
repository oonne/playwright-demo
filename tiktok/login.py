import asyncio
import time
from playwright.async_api import async_playwright
from utils.browser import create_browser

async def login():
    """
    获取Tiktok登录二维码
    """
    browser = await create_browser('tiktok')

    # await browser['page'].goto('https://www.browserscan.net/zh/bot-detection#google_vignette')
    await browser['page'].goto('https://www.browserscan.net/zh')

    # 关闭
    input("Press Enter to exit...")
    await browser['context'].close()
    await browser['playwright'].stop()
    print('已关闭')

if __name__ == '__main__':
    asyncio.run(login())