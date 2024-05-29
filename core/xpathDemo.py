from lxml import etree

def useEtree():
    tree = etree.parse("xpathDemo.html")
    # 路径查询
    li_list1 = tree.xpath("//body/ul/li")
    # 谓词查询
    li_list2 = tree.xpath("//ul/li[@id]")
    # 谓词查询查找 id 为 test 的标签
    li_list3 = tree.xpath("//ul/li[@id='test']/text()")
    #属性查询查找 class 为 a 的标签
    li_list4 = tree.xpath("//ul/li[@class='a']/text()")

    #获取标签中的内容
    li_value = tree.xpath("//ul/li[@id]/text()")


    print(li_list4)


if __name__ == '__main__':
    useEtree()