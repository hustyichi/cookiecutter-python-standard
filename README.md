# 美折 Python 项目开发规范

## 管理虚拟环境

不限于`pyenv`,`pipenv`或者`poetry`

(杜老师推荐`poetry`)

## 配置文件

统一使用`pyproject.toml`来配置各个工具。

使用统一的`gitignore`模板

## Lint

使用`pylint`

### 配置

在`pyproject.toml`中配置

```toml
[tool.pylint.master]
job = 0 # 默认多进程
suggestion-mode = "yes" # 显示建议

[tool.pylint.format]
max-line-length = 120 # 每行宽度限制

[tool.pylint.basic] # 名称规范
argument-naming-style = "any" # 参数名称
attr-naming-style = "any" # 类属性名称
function-naming-style = "any" # 函数名称
method-naming-style = "any" # 方法名称
variable-naming-style = "any" # 变量名称

[tool.pylint.message_control]
# 不检查项目，尽量不要随意添加
disable = ["missing-docstring", # 缺少docstring
 "logging-fstring-interpolation, # 允许在log语句中使用f-string语法
 "]

[tool.pylint.design]
min-public-methods = 0 #类公共方法数目最小限制放宽为0
```

## Formater

使用`black`

### 配置

在`pyproject.toml`中配置

```toml
[tool.black]
line-length = 120 # 每行代码宽度限制，需要和pylint配置匹配
```

## Sort Imports

使用`isort`

## type

使用`mypy`

## 测试

使用`pytest`

### 配置

在`pyproject.toml`中配置

```toml
[tool.pytest.ini_options]
addopts = " -svv --cov=app"
testpaths = [
  "tests",
]
```

## 测试覆盖

使用 `pytest-cov`插件和`coverage`

### 配置

在`pyproject.toml`中配置

```toml
[tool.coverage.report]
exclude_lines = [ # 哪些代码块不进行覆盖率检查
  "pragma: no cover",
  "def __repr__",
  "raise AssertionError",
  "raise NotImplementedError",
  "if __name__ == .__main__.:",
]
fail_under = 60.0 # 覆盖率指标
show_missing = true # 在报告中显示未覆盖的代码行号
skip_covered = true # 报告中不显示满足覆盖率要求的文件
skip_empty = true # 报告中不显示空文件
sort = "miss" # 按代码覆盖率从低到高排序

[tool.coverage.path]
source = "app" # 代码覆盖检查目录

```

## CI 检查

```bash
make lint # pylint 和 mypy
make test # pytest 和覆盖率检查
```
