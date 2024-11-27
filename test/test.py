import unittest
from playwright.sync_api import Playwright, sync_playwright

class TestExample(unittest.TestCase):
    def setUp(self):
        # 初始化代码
        pass

    def tearDown(self):
        # 清理代码
        pass

    def test_example(self):
        def run(playwright: Playwright) -> None:
            # 创建浏览器
            browser = playwright.chromium.launch(headless=False)

            # 使用 selenium 如果要打开多个网页，需要创建多个浏览器，但是 playwright 中只需要创建多个上下文即可
            content = browser.new_context()

            # 每个 content 就是一个会话窗口，可以创建自己的页面，也就是浏览器上的 tab 栏
            page = content.new_page()

            # 页面打开指定网址
            page.goto('https://www.baidu.com')

            # 找到百度输入框并填入内容
            page.fill('//input[@id="kw"]', '周杰伦')

            # 点击百度一下进行搜索
            page.click('//input[@id="su"]')

            # 延迟关闭
            page.wait_for_timeout(10000)

            # 使用完成关闭上下文（也就是会话窗口）
            content.close()

            # 关闭浏览器
            browser.close()

        # 调用
        with sync_playwright() as playwright:
            run(playwright)


if __name__ == '__main__':
    unittest.main()