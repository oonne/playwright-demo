import os
import time
from playwright.async_api import async_playwright, Page
import random
import string

current_dir = os.path.dirname(__file__)

async def stealth_webdriver(page: Page):
    """
    机器人控制 navigator.webdriver
    """
    await page.add_init_script("delete Object.getPrototypeOf(navigator).webdriver")

async def stealth_js(page: Page):
    """stealth.min.js脚本"""
    script_path = os.path.join(current_dir, "stealth.min.js")
    await page.add_init_script(path=script_path)

async def create_browser(contextName=None, timezone_id=None, locale=None, user_agent=None):
    """
    创建一个浏览器实例，并做指纹处理
    """
    if not contextName:
        contextName = ''.join(random.sample(string.ascii_letters + string.digits, 16))

    playwright = await async_playwright().start()
    context = await playwright.chromium.launch_persistent_context("../data/"+contextName,
        headless=False,
        devtools=False,
        timezone_id=timezone_id,
        locale=locale,
        user_agent=user_agent,
        viewport={'width': 1440, 'height': 900}
    )
    pages = context.pages
    if len(pages)==0:
        page = await context.new_page()
    else:
        page = pages[0]

    # 指纹
    await stealth_webdriver(page)
    await stealth_js(page)

    time.sleep(1)

    # 返回
    return {
        'playwright': playwright,
        'context': context,
        'page': page,
    }

