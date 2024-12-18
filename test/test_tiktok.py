# 测试修改一下指纹
import unittest
from time import sleep
from playwright.async_api import async_playwright
from test.stealth import stealth_async

class TestTiktok(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        # 初始化代码
        playwright = await async_playwright().start()
        # 创建浏览器上下文，每个上下文是独立的登录环境
        self.browser = await playwright.chromium.launch(headless=False, devtools=True)
        # 尝试加载之前保存的状态
        try:
            self.context = await self.browser.new_context(
                storage_state="../data/tiktok_us.json",
                timezone_id='America/Los_Angeles',
                locale='en-US',
                viewport={'width': 1920, 'height': 720},
            )
        except FileNotFoundError:
            self.context = await self.browser.new_context(
                timezone_id='America/Los_Angeles',
                locale='en-US',
                viewport={'width': 1920, 'height': 720},
            )
        # 每个 context 就是一个会话窗口，可以创建自己的页面，也就是浏览器上的 tab 栏
        self.page = await self.context.new_page()
        # 修改页面指纹
        await stealth_async(self.page)
        print('准备完成')

    async def asyncTearDown(self):
        # 保存登录态
        await self.context.storage_state(path="../data/tiktok_us.json")
        # 使用完成关闭上下文（也就是会话窗口）
        await self.context.close()
        # 关闭浏览器
        await self.browser.close()

    # 监听QRCODE返回
    async def check_qrcode(self, response):
        await response.finished()
        if "tiktok.com/passport/web/get_qrcode" in response.url:
            res = await response.json()
            print(res['data']['qrcode'])

    # 登录tiktok
    async def test_click_login(self):
        # 页面打开指定网址
        await self.page.goto('https://www.tiktok.com')

        # 监听二维码返回
        self.page.on('response', self.check_qrcode)

        # 点击 内容为 Log in 的按钮
        await self.page.click('text="Log in"')
        # 点击 内容为 Use QR code 的按钮
        await self.page.click('text="Use QR code"')

        # 延迟关闭
        sleep(5)


if __name__ == '__main__':
    unittest.main()