# coding=utf-8
from common.getYaml import getyaml
from common.baseOperate import BaseOperate

class Operate:
    def __init__(self, path, driver):
        self.path = path
        self.driver = driver
        self.yaml = getyaml(self.path)
        self.baseoperate = BaseOperate(driver)

    def check_operate_type(self):
        '''
        读取yaml信息并执行
        element_info：定位元素信息
        find_type：属性，id、xpath、text、ids
        operate_type: click、exist、sendkeys、back、swipe_up exist判断元素在页面是否存在

        上面三个必填，operate_type必填!!!!!!

        send_content：send_keys 时用到
        index：ids时用到
        times:
        :return:
        '''

        for i in range(self.yaml.caselen()):
            if self.yaml.get_operate_type(i) == 'click':
                self.driver.implicitly_wait(3)
                if self.yaml.get_findtype(i) == 'text':
                    self.baseoperate.get_name(self.yaml.get_elementinfo(i)).click()
                elif self.yaml.get_findtype(i) == 'id':
                    self.baseoperate.get_id(self.yaml.get_elementinfo(i)).click()
                elif self.yaml.get_findtype(i) == 'xpath':
                    self.baseoperate.get_xpath(self.yaml.get_elementinfo(i)).click()
                elif self.yaml.get_findtype(i) == 'ids':
                    self.baseoperate.get_ids(self.yaml.get_elementinfo(i))[self.yaml.get_index(i)].click()

            elif self.yaml.get_operate_type(i) == 'exist':
                self.driver.implicitly_wait(3)
                if self.yaml.get_findtype(i) == 'text':
                    self.baseoperate.get_name(self.yaml.get_elementinfo(i))
                elif self.yaml.get_findtype(i) == 'id':
                    self.baseoperate.get_id(self.yaml.get_elementinfo(i))
                elif self.yaml.get_findtype(i) == 'xpath':
                    self.baseoperate.get_xpath(self.yaml.get_elementinfo(i))
                elif self.yaml.get_findtype(i) == 'ids':
                    self.baseoperate.get_ids(self.yaml.get_elementinfo(i))[self.yaml.get_index(i)].is_displayed()

            elif self.yaml.get_operate_type(i) == 'send_keys':
                self.driver.implicitly_wait(3)
                if self.yaml.get_findtype(i) == 'text':
                    self.baseoperate.get_name(self.yaml.get_elementinfo(i)).send_keys(self.yaml.get_send_content(i))
                elif self.yaml.get_findtype(i) == 'id':
                    self.baseoperate.get_id(self.yaml.get_elementinfo(i)).send_keys(self.yaml.get_send_content(i))
                elif self.yaml.get_findtype(i) == 'xpath':
                    self.baseoperate.get_xpath(self.yaml.get_elementinfo(i)).send_keys(self.yaml.get_send_content(i))
                elif self.yaml.get_findtype(i) == 'ids':
                    self.baseoperate.get_ids(self.yaml.get_elementinfo(i))[self.yaml.get_index(i)].send_keys(self.yaml.get_send_content(i))

            elif self.yaml.get_operate_type(i) == 'back':
                for n in range(self.yaml.get_backtimes(i)):
                    self.baseoperate.back()

            elif self.yaml.get_operate_type(i) == 'swipe_up':
                for n in range(self.yaml.get_backtimes(i)):
                    self.baseoperate.swipeUp()

            elif self.yaml.get_operate_type(i) == 'swipe_down':
                for n in range(self.yaml.get_backtimes(i)):
                    self.baseoperate.swipeDown()


    def back_home(self):
        '''
        返回至首页
        :return:
        '''
        self.baseoperate.page('推荐')
