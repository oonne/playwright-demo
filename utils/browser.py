from playwright.async_api import async_playwright
import random
import string

async def create_browser(contextName=None, timezone_id='Asia/Shanghai', locale='zh-CN'):
    """
    创建一个浏览器实例，并做指纹处理
    """
    if not contextName:
        contextName = ''.join(random.sample(string.ascii_letters + string.digits, 16))

    playwright = await async_playwright().start()
    context = await playwright.chromium.launch_persistent_context("../data/"+contextName,
        headless=False,
        devtools=True,
        timezone_id=timezone_id,
        locale=locale,
        viewport={'width': 1440, 'height': 900},
    )
    pages = context.pages
    if len(pages)==0:
        page = await context.new_page()
    else:
        page = pages[0]

    return {
        'playwright': playwright,
        'context': context,
        'page': page,
    }

