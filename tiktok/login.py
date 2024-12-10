import asyncio
import time
from playwright.async_api import async_playwright
from utils.browser import create_browser

async def login():
    """
    获取Tiktok登录二维码
    """
    browser = await create_browser('tiktok')

    await browser['page'].goto('https://www.browserscan.net/zh/')

    input("Press Enter to exit...")

if __name__ == '__main__':
    asyncio.run(login())