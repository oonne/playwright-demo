from playwright.async_api import async_playwright, Page
import random
import string

async def stealth_webdriver(page: Page):
    """
    机器人控制 navigator.webdriver
    """
    await page.add_init_script("delete Object.getPrototypeOf(navigator).webdriver")

async def create_browser(contextName=None, timezone_id='Asia/Singapore', locale='zh-CN'):
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
        user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        viewport={'width': 1440, 'height': 900},
    )
    pages = context.pages
    if len(pages)==0:
        page = await context.new_page()
    else:
        page = pages[0]

    # 指纹
    await stealth_webdriver(page)

    # 返回
    return {
        'playwright': playwright,
        'context': context,
        'page': page,
    }

