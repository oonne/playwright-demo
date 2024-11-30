import unittest
from time import sleep
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright

class TestExample(unittest.TestCase):
    def setUp(self):
        # 初始化代码
        pass

    def tearDown(self):
        # 清理代码
        pass

    # 测试用例1：同步 打开浏览器并搜索
    def test_1(self):
        with sync_playwright() as playwright:
            # 创建浏览器上下文，每个上下文是独立的登录环境
            browser = playwright.chromium.launch(headless=False, devtools=True)
            context = browser.new_context()
            # 每个 context 就是一个会话窗口，可以创建自己的页面，也就是浏览器上的 tab 栏
            page = context.new_page()

            # 页面打开指定网址
            page.goto('https://www.baidu.com')
            # 找到百度输入框并填入内容
            page.fill('//input[@id="kw"]', 'SaleChaty')
            # 点击百度一下进行搜索
            page.click('//input[@id="su"]')
            # 延迟关闭
            page.wait_for_timeout(10000)

            # 使用完成关闭上下文（也就是会话窗口）
            context.close()
            # 关闭浏览器
            browser.close()

class AsyncTestExample(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        # 初始化代码
        pass

    def tearDown(self):
        # 清理代码
        pass

    # 测试用例2：获取user_agent
    async def test_2(self):
        playwright = await async_playwright().start()
        # 创建浏览器上下文，每个上下文是独立的登录环境
        browser = await playwright.chromium.launch(headless=False, devtools=True)
        context = await browser.new_context()
        # 每个 context 就是一个会话窗口，可以创建自己的页面，也就是浏览器上的 tab 栏
        page = await context.new_page()

        # 页面打开指定网址
        await page.goto('https://www.tiktok.com')

        user_agent = await page.evaluate("() => navigator.userAgent")
        language = await page.evaluate("() => navigator.language || navigator.userLanguage")
        platform = await page.evaluate("() => navigator.platform")
        print(user_agent, language, platform)

        # 延迟关闭
        await page.wait_for_timeout(10000)

        # 使用完成关闭上下文（也就是会话窗口）
        await context.close()
        # 关闭浏览器
        await browser.close()

    # 测试用例3：测试登录
    async def test_3(self):
        playwright = await async_playwright().start()
        # 创建浏览器上下文，每个上下文是独立的登录环境
        browser = await playwright.chromium.launch(headless=False, devtools=True)
        # 尝试加载之前保存的状态
        try:
            context = await browser.new_context(storage_state="../data/test_3.json")
        except FileNotFoundError:
            context = await browser.new_context()
        # 每个 context 就是一个会话窗口，可以创建自己的页面，也就是浏览器上的 tab 栏
        page = await context.new_page()

        # 页面打开指定网址
        await page.goto('https://link-ai.tech/home')

        # 此处先手动登录，没有做自动化

        # 延迟关闭
        sleep(20)

        # 保存登录态
        await context.storage_state(path="../data/test_3.json")

        # 使用完成关闭上下文（也就是会话窗口）
        await context.close()
        # 关闭浏览器
        await browser.close()

if __name__ == '__main__':
    unittest.main()