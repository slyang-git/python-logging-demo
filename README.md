# python-logging-demo

logging is a built-in package in Python. There are only **Three** files in this package.

![logging](docs/images/logging.svg)

1. `__init__.py`
2. `config.py`
3. `handlers.py`

![logginghandler](docs/images/Handler.svg)

The logging library takes a modular approach and offers several categories of components: loggers, handlers, filters, and formatters.

* Loggers expose the interface that application code directly uses.
* Handlers send the log records (created by loggers) to the appropriate destination.
* Filters provide a finer grained facility for determining which log records to output.
* Formatters specify the layout of log records in the final output.

![logging-flow](docs/images/logging_flow.png)

A good convention to use when naming loggers is to use a module-level logger, in each module which uses logging, named as follows:

```
logger = logging.getLogger(__name__)
```

上面的一句创建logger的代码，调用了 logging库中`__init__.py`中的`getLogger()`函数, 它的实现如下：

```python
def getLogger(name=None):
    """
    Return a logger with the specified name, creating it if necessary.

    If no name is specified, return the root logger.
    """
    if name:
        return Logger.manager.getLogger(name)
    else:
        return root
```
通过代码可以看到，如果`getLogger()`有传入name字段，则查找manager是否已经有这个name的logger，若没有传入name字段，则返回root logger

root logger是什么呢？在什么时候创建的呢？

在logging库的`__init__.py`中，我们可以找到如下代码：

```python

root = RootLogger(WARNING)
Logger.root = root
Logger.manager = Manager(Logger.root)
```

可以看到，当我们在某一个地方 `import logging`时，上述代码就被执行了，也就是说 root logger就已经生成了。root logger其实本质上也是 Logger类的一个实例，只是它是一个特殊的logger。

以上代码不仅仅创建了root logger，还给Logger类新增了两个类变量——root（用户新创建的root实例初始化）和manager（直接实例化一个Manager类）




# Logging from multiple modules

a common practice is to create different loggers for every module.


<https://docs.python.org/3/howto/logging.html>