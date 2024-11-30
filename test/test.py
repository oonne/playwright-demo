import unittest
from unittest.async_case import IsolatedAsyncioTestCase
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
            browser = playwright.chromium.launch(headless=False)
            content = browser.new_context()
            # 每个 content 就是一个会话窗口，可以创建自己的页面，也就是浏览器上的 tab 栏
            page = content.new_page()

            # 页面打开指定网址
            page.goto('https://www.baidu.com')
            # 找到百度输入框并填入内容
            page.fill('//input[@id="kw"]', 'SaleChaty')
            # 点击百度一下进行搜索
            page.click('//input[@id="su"]')
            # 延迟关闭
            page.wait_for_timeout(10000)

            # 使用完成关闭上下文（也就是会话窗口）
            content.close()
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
        browser = await playwright.chromium.launch(headless=False)
        content = await browser.new_context()
        # 每个 content 就是一个会话窗口，可以创建自己的页面，也就是浏览器上的 tab 栏
        page = await content.new_page()

        # 页面打开指定网址
        await page.goto('https://tiktok.com')
        # 延迟关闭
        await page.wait_for_timeout(10000)

        # 使用完成关闭上下文（也就是会话窗口）
        await content.close()
        # 关闭浏览器
        await browser.close()

if __name__ == '__main__':
    unittest.main()