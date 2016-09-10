#!/user/bin/env python
#encoding:utf-8

'''
现有一个单向链表dataList，链表的每个节点dataNode都有个不固定大小的buf来存储字符串数据。
比如，String为“123456789abcdefg”，dataList为：[12]->[34567]->[8]->[9ab]->[cdefg]。
要求实现一个查找算法，给出链表dataList的对象实例，查找某个子字符串，返回dataNode的结点及字符串首字符在该结点中的索引位置
eg:在如上dataList查找“bcd”，返回[9ab]和2（假设以0为起始下标）


String =  '123456789abcdefg'
dataList = ['12','234567','8','9ab','cdefg']

dict = {} #创建一个空字典
'''
class Node(object): #创建Node的数据类型，包括data和nextdata
    def __init__(self,data):
        self.data = data
        self.next = None

def __init__(self): #初始化链表
        self.head =None 
        
def __len__(self): #获取链表长度
    pre = self.head
    length = 0
    while pre:
        length += 1
        pre = pre.next
    return length

def append(self, data): #追加节点
    node = Node(data)
    if self.head is None:
        self.head = node
    else:
        pre = self.head
        while pre.next:
            pre = pre.next
        pre.next = node


def insert(self, index, data):#插入节点
    node = Node(data)
    if abs(index + 1) > len(self):
        return False
    index = index if index >= 0 else len(self) + index + 1
    if index == 0:
        node.next = self.head
        self.head = node
    else:
        pre = self.get(index - 1)
        if pre:
            next = pre.next
            pre.next = node
            node.next = next
        else:
            return False
    return node

def delete(self, index):#删除节点
    f = index if index > 0 else abs(index + 1)
    if len(self) <= f:
        return False
    pre = self.head
    index = index if index >= 0 else len(self) + index
    prep = None
    while index:
        prep = pre
        pre = pre.next
        index -= 1
    if not prep:
        self.head = pre.next
    else:
        prep.next = pre.next
    return pre.data

def __reversed__(self): #反转链表
    def reverse(pre_node, node):
        if pre_node is self.head:
            pre_node.next = None
        if node:
            next_node = node.next
            node.next = pre_node
            return reverse(node, next_node)
        else:
            self.head = pre_node

    return reverse(self.head, self.head.next)

def clear(self): #清空链表
    self.head = None