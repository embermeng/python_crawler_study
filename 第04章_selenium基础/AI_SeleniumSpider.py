import time
from typing import List, Dict
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# selenium的错误类型
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class SeleniumSpider:
    """
    Selenium 4.40 爬虫类（适配Python 3.13）
    示例：爬取百度热搜榜信息
    """
    chrome_options = None
    service = None
    driver = None
    wait = None

    def __init__(self):
        """初始化浏览器驱动和配置"""
        # 配置Chrome选项
        self.set_chrome_options()
        # 初始化驱动服务（Selenium 4.40自动管理驱动，无需指定executable_path）
        self.service = Service(executable_path='./chromedriver.exe')
        # 声明驱动对象
        self.driver = None
        # 显式等待对象（全局复用）
        self.wait = None

    def set_chrome_options(self):
        """设置Chrome浏览器选项（私有方法）"""
        options = Options()
        # 基础配置
        options.add_argument("--no-sandbox")  # 解决沙箱问题
        options.add_argument("--disable-dev-shm-usage")  # 解决内存不足问题
        options.add_argument("--disable-blink-features=AutomationControlled")  # 避免被检测为自动化工具

        # 可选：无头模式（不显示浏览器窗口），注释掉则显示窗口
        # options.add_argument("--headless=new")

        # 禁用图片加载（提升爬取速度）
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # options.add_experimental_option("prefs", prefs)

        self.chrome_options = options

    def start_driver(self):
        """启动浏览器驱动"""
        try:
            self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
            # 设置隐式等待（全局，查找元素时最多等待10秒）
            self.driver.implicitly_wait(10)
            # 初始化显式等待（更灵活的等待方式）
            self.wait = WebDriverWait(self.driver, 10)
            print("浏览器驱动启动成功")
        except Exception as e:
            print(f"驱动启动失败：{str(e)}")
            raise

    def visit_url(self, url: str):
        """访问指定URL"""
        if not self.driver:
            raise RuntimeError("请先调用start_driver()启动驱动")

        try:
            self.driver.get(url)
            # 当前网页的标题
            print(self.driver.title)
            # 当前响应的URL
            print(self.driver.current_url)
            # 浏览器驱动名称
            print(self.driver.name)
            # 页面源码
            print(len(self.driver.page_source))

            # 等待页面标题加载完成（验证页面是否正常打开）
            self.wait.until(EC.title_contains("百度"))
            # print(f"成功访问URL：{url}")
        except TimeoutException:
            print(f"访问URL超时：{url}")
            raise
        except Exception as e:
            print(f"访问URL失败：{str(e)}")
            raise

    def extract_data(self) -> List[Dict]:
        """提取页面数据（示例：百度热搜榜）"""
        if not self.driver:
            raise RuntimeError("请先调用start_driver()启动驱动")

        data_list = []
        try:
            # 等待热搜榜元素加载完成
            hot_list = self.wait.until(
                EC.presence_of_element_located((By.ID, "hotsearch-content-wrapper"))
            )
            # 提取热搜条目
            hot_items = hot_list.find_elements(By.CLASS_NAME, "hotsearch-item")

            for index, item in enumerate(hot_items, 1):
                try:
                    # 提取排名、标题、热度
                    rank = index
                    title = item.find_element(By.CLASS_NAME, "title-content-title").text
                    heat = item.find_element(By.CLASS_NAME, "hot-index").text

                    data = {
                        "rank": rank,
                        "title": title,
                        "heat": heat
                    }
                    data_list.append(data)
                except NoSuchElementException:
                    print(f"第{index}条热搜数据提取失败，跳过")
                    continue

            print(f"共提取到{len(data_list)}条热搜数据")
            return data_list

        except TimeoutException:
            print("热搜榜元素加载超时")
            return []
        except Exception as e:
            print(f"数据提取失败：{str(e)}")
            return []

    def save_data(self, data: List[Dict]):
        """保存提取的数据到文件"""
        if not data:
            print("无数据可保存")
            return

        try:
            # 打开文件，保存数据
            print(self)
            pass
        except Exception as e:
            print(f"数据保存失败：{str(e)}")
            raise

    def close_driver(self):
        """关闭浏览器驱动，释放资源"""
        if self.driver:
            self.driver.quit()
            print("浏览器驱动已关闭")

    def run(self, url: str):
        """爬虫主执行流程"""
        try:
            # 1. 启动驱动
            self.start_driver()
            # 2. 访问页面
            self.visit_url(url)
            # 3. 等待页面完全加载（额外等待，可选）
            time.sleep(10)
            # 4. 提取数据
            # data = self.extract_data()
            # 5. 保存数据
            # self.save_data(data)
        except Exception as e:
            print(f"爬虫执行失败：{str(e)}")
        finally:
            # 无论是否异常，都关闭驱动
            self.close_driver()


# 程序入口
if __name__ == "__main__":
    # 初始化爬虫实例
    spider = SeleniumSpider()
    # 执行爬虫（爬取百度首页热搜）
    spider.run("https://www.baidu.com")
