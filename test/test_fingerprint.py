# 测试修改一下指纹

import unittest
from time import sleep
from playwright.async_api import async_playwright
from test.stealth import stealth_async

class TestFingerprint(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        # 初始化代码
        playwright = await async_playwright().start()
        # 创建浏览器上下文，每个上下文是独立的登录环境
        self.context = await playwright.chromium.launch_persistent_context("../data/fingerprint", headless=False, devtools=True,
                timezone_id='America/Los_Angeles',
                locale='en-US',
                viewport={'width': 1920, 'height': 720},)

        # 每个 context 就是一个会话窗口，可以创建自己的页面，也就是浏览器上的 tab 栏
        self.page = await self.context.new_page()

        # 修改页面指纹
        await stealth_async(self.page)

    async def asyncTearDown(self):
        # 保存登录态
        await self.context.storage_state(path="../data/fingerprint.json")
        # 使用完成关闭上下文（也就是会话窗口）
        await self.context.close()

    # 访问普通网站
    async def test_web(self):
        # 页面打开指定网址
        await self.page.goto('https://www.baidu.com')

        # 延迟关闭
        sleep(10)

    # 识别指纹
    async def test_scan(self):
        # 页面打开指定网址
        await self.page.goto('https://www.browserscan.net/zh/')

        # 延迟关闭
        sleep(20)

    # 判断是否是机器人
    async def test_bot(self):
        # 页面打开指定网址
        await self.page.goto('https://www.browserscan.net/zh/bot-detection#google_vignette')

        # 延迟关闭
        sleep(10)

if __name__ == '__main__':
    unittest.main()