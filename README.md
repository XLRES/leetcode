# leetcode
打算开始在leetcode上刷题了嗯。  
希望不要因为各种各样的原因半途而废……   
2015.3.28

---

在这里贴一下写过的题解和思路。
长期更新。

---

## \#19 Remove Nth Node From End of List
> Given a linked list, 
> remove the nth node from the end of list and return its head. 
>
> For example,  
>>  Given linked list: 1-\>2-\>3-\>4-\>5, and n = 2.  
>>  After removing the second node from the end, 
>>  the linked list becomes 1-\>2-\>3-\>5.  
>
> Note:  
> Given n will always be valid. 
> Try to do this in one pass.  

大体上来说就是删除链表中倒数第n个元素，
并没有任何难度。  
这种程度的题也不管你内存回收什么的所以说随便写就好了。
唯一要注意的地方是 n 等于链表长度的情况，
即要删除的结点就是头结点，在最开始应该新建一个空结点指向头结点，
当然针对这种情况做特殊处理也行。  
——没错这和我过去习惯写的链表不一样，我以为空的头结点是链表标配呢……  

一开始的想法是先把链表过一遍数一数元素个数，
然后再从头到Len-n个结点的地方完成删除操作。  
然而总是报internal error，现在想想大概就是头结点没处理好？  
翻了翻别人的题解，才发现可以用两个指针，
p1走n个结点之后p1p2开始同时走，这样p1到底了p2也就到位置了。  
时间缩短了一半，
不过一半 O(n) 时间的意义也就在于满足一下我这种强迫症，大概。

顺便说一句这题的 Tags上挂了 Two Pointers，然而Tags默认不显示，
大概是为了防剧透。我是写完才发现的。  

最后的代码：

```python
def removeNthFromEnd(self, head, n):
    h = ListNode(0)
    h.next = head
    p1 = p2 = head.next
    for i in range(n):
        p1 = p1.next
    while (p1.next != None):
        p1 = p1.next
        p2 = p2.next
    p2.next = p2.next.next
    return  h.next
```

---

## \#205 Isomorphic Strings
> Given two strings s and t, determine if they are isomorphic. 
>
> Two strings are isomorphic if the characters in s>
> can be replaced to get t.  
>
> All occurrences of a character must be replaced 
> with another character while preserving the order of characters.
> No two characters may map to the same character
> but a character may map to itself.  
>
> For example,  
> Given "egg", "add", return true.  
>
> Given "foo", "bar", return false.  
>
> Given "paper", "title", return true.  
>
> Note:  
> You may assume both s and t have the same length.  

Tags 上挂了 Hash Table 把我吓了个半死，这刚第二题呢……不过其实没有用到。
其实只要记录下 s 到 t 的每个字母的映射，看看有没有矛盾就行。  
我在这里用了dict，其实只要用list就行，
内存开销要小一点，不过处理逻辑可能要稍微复杂一些。  
（其实是dict太简单了……）  
另外对于如何方便的按顺序遍历s和t两个字符串，
这里使用了 itertools.izip()。

```python
def isIsomorphic(self, s, t):
    import itertools
    maptable={}
    for c1,c2 in itertools.izip(s,t):
        if c1 in maptable :
            if maptable[c1] != c2: return False
        else: maptable[c1] = c2
    return True

```
不过这么写其实是有问题的，对于诸如
>s = 'ab'  
>t = 'aa'

这类问题无法正确判断，因为没有对两个字符映射到同一个字符的情况做出检查。  
然而将s和t交换再检查一次就没有问题了。  
所以提交的代码是将现有 isIsomorophic() 的内容写成子函数，
而真正的 isIsomorophic()里只有一句:

```python
    print isisomorophic(s, t) and isisomorophic(t, s)
```

---

## \#202 Happy Number
> Write an algorithm to determine if a number is "happy".  
>
> A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.  
>
> Example: 19 is a happy number  
> 1<sup>2</sup> + 9<sup>2</sup> = 82  
> 8<sup>2</sup> + 2<sup>2</sup> = 68  
> 6<sup>2</sup> + 8<sup>2</sup> = 100  
> 1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1  
>
> Credits:  
> Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.  

够简单，够 happy。  
简单的数字处理，感谢Python提供了 in 这么好用的办法来判断包含。  
另外原来leetcode并不存在一个固定的难度排列？那顺序就随便排了……

```python
def isHappy(self, n):
    s = 0
    numlist = []
    while (n != 1 and not n in numlist):
        numlist.append (n)
        while (n > 0):
            s += (n % 10)**2
            n /= 10
        n = s
        s = 0
    if n == 1: return True
    else: return False
```

---

## \#20 Valid Parentheses
>Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.  

>The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.  

经典的括号匹配问题，解决方法也是经典的栈结构。  
因为知道 Python 有队列模块（Queue），以为栈（Stack）也有封装好的模块，
没想到其实没有……  
不过列表（list）本身实现栈很方便，甚至已经提供了 append 和 pop 方法，
top 可以用 list[-1] 实现，isEmpty 这种也很好处理，所以也没关系。  
我在这里对于三种括号的判断应该有更优雅的写法，不过只有三种括号无所谓了。
括号种类多的话用上索引，或者直接上 dict 更方便。  
重复两次 stk:append(c) 是为了避免诸如第一个字符就是‘}’时stk[-1]报错的情况，
不过总觉得应该有更好的处理方式才对。  

```python
def isValid(self, s):
    stk = []
    for c in s:
        if len(stk) > 0:
            if c == ')' and stk[-1] == '(' : stk.pop()
            elif c == ']' and stk[-1] == '[': stk.pop()
            elif c == '}' and stk[-1] == '{': stk.pop()
            else: stk.append(c);
        else: stk.append(c)
        print stk
    if len(stk) == 0: return True
    else : return False
```

---

## \#204 Count Primes
> Description:
>
> Count the number of prime numbers less than a non-negative number, n

求小于n的数中素数的个数。  
Tags里也是有 Hash Table 不过并不明白为什么……  
这里用的是某种线性筛法。
作者说这个易于理解，时空效率都还不错，我倒觉得相比同类算法完全不好理解呢……

首先这里只算了奇数部分，2和2一下的情况要单独处理。  
若p[i] 为 True，代表的是 2\*i+3 是素数。  
筛法起点 2\*i^2+6\*i+3 是 ((2*i+3)^2-3)/2，
也就是对应真实值的平方再回推出的数组下标。  
最后统计的时候从i到 range(half - 1) 也是考虑到数组下标 i=(k-3)/2。   
而count从1开始是加上2这个偶数素数。

```python
def countPrimes(self, n):
    import math
    if n <= 2 : return 0
    half = n / 2;
    sn = (int)(math.sqrt(n))
    p = []
    for i in range (half):
        p.append (True)
    for i in range (sn):
        if p[i]:
            for j in range(2 * i * i + 6 * i + 3 , half , 2 * i + 3):
                p[j] = False
    
    count = 1
    for i in range(half - 1):
        if p[i]:
            count += 1
    return count

```

---

## \#141 Linked List Cycle
> Given a linked list, determine if it has a cycle in it.   
> 
> Follow up:  
> Can you solve it without using extra space?  

这还是个 Media 难度的题呢……  
Tags 里被机智地写上了 Two Pointers所以……  
想法很简单，两个指针，一个一次走一步，一个一次走两步，
如果两个能再次相遇就存在循环。  
值得注意的是各种边界条件，因为这个跪了好几次。  
包括空链表，只有一个元素的链表所以不能有p.next.next 之类之类的。  
不过都处理完了之后也就完全没难度了。  

```python
def hasCycle(self, head):
    if head == None : return False
    p1 = p2 = head
    flag = 0
    while(p1 != None and p2 != None and p2.next != None):
        p1 = p1.next
        p2 = p2.next.next
        if (p1 == p2 ): 
            flag = 1 
            break
    if flag : return True
    else: return False
```

---

## \#199 Binary Tree Right Side View
> Given a binary tree, 
> imagine yourself standing on the right side of it, 
> return the values of the nodes you can see ordered from top to bottom.  
> 

因为懒得排版就不贴example了。  
这题其实没想出来解法……  
看题目给出的example还以为是一直找右子树就可以了，
结果对于左子树高度大于右子树的情况也需要考虑。  
本来觉得对这棵树做一个层序遍历就可以了，
每一层的最后一个节点记录一下数据，
但是给出的TreeNode定义里并没有高度，
除非有办法在遍历的过程中记录高度。  
然而并没有想到有什么优雅的解法。  
暂且搁置吧。  

## \#191 Number of 1 Bits
> Write a function that takes an unsigned integer 
> and returns the number of ’1' bits it has 
> (also known as the Hamming weight).  
> 
> For example,   
> the 32-bit integer ’11' has binary representation 
> 00000000000000000000000000001011, 
> so the function should return 3.  

求一个数字转换成二进制后有多少位是1.  
↑↑↑其实这是个有引导性的说法，数值本身是无所谓几进制的。  
一种思路是进行“进制转换”，对n每次减半然后数模2的余数。  
另一种思路是直接把n当作二进制，
每次看一眼最后一位是1还是0然后整串数字右移。  
当然这两种思路是完全相同的，
只是突然让我写个进制转换之类的东西说不定我还得真好好想想边界条件什么的……  
略水。  

```python
def hammingWeight(self, n):
    s = 0
    while n > 0:
        s += n % 2
        n = n >> 1
    return s
```

## \# 110 Balanced Binary Tree

> Given a binary tree, determine if it is height-balanced.  
> 
> For this problem, 
> a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

判断给定的二叉树是否平衡。   
理论上是挺简单的可是这段时间忙于考试代码生疏了这么多遍才过……   
首先，二叉树不平衡的条件是
树及其任一子树的左右子树高度差大于等于2   
所以写了treeDepth用了递归的方式求高度（深度）。   
然后是isBalanced 当中除了判断当前节点是否平衡以外，
在最后还要递归地考虑左右子树是否平衡。   
这么一来程序非常间接，逻辑也很清晰，
然而时间复杂度和空间复杂度都相当差……  
无论是 treeDepth 还是 isBalanced 递归时都用上了表达式
而不能被编译器优化，
isBalanced 递归过程中对于各点的深度计算也有严重重复。  
解决方法也有，尾递归优化做不了的话，
手动操作出入栈改成循环即可；  
各结点深度能写进 TreeNode 最好，
不能的话临时开个表记录也成。  

然而非常令我惊讶的是我这种时间空间都不合格的算法
排名居然并不是很靠后……  
看来大家水leetcode的时候都用的是好写的渣算法233

```python
def treeDepth (self, root):
    if root == None :
        return -1
    ldepth = self.treeDepth (root.left)
    rdepth = self.treeDepth (root.right)
    if ldepth > rdepth :
        return ldepth + 1
    else :
        return rdepth + 1

def isBalanced (self, root):
    if root == None :
        return True
    ldepth = self.treeDepth(root.left)
    rdepth = self.treeDepth(root.right)
    if ldepth - rdepth > 1 or rdepth - ldepth > 1 :
        return False
    else:
        return self.isBalanced(root.left) and isisBalanced(root.right)
```

