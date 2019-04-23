# pytorch-tutorials-notebooks-zhs

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tanbro/pytorch-tutorials-notebooks-zhs/master)

[PyTorch tutorials](https://github.com/pytorch/tutorials/) 的中文翻译笔记。
点击下面的链接可直接访问该项目生成的 Web 文档站点：

<https://tanbro.github.io/pytorch-tutorials-notebooks-zhs/>

## 概述

官方教程以 *带有 [Sphinx-Doc][] 扩展 [reST][] 格式注释的 Python 源代码* 的形式制作了Web文档并导出 [Jupyter][] 笔记。

而这个项目除了翻译，修改还有:

- 使用 [Jupyter][] 笔记文件保存说明和代码片段
- 从 [Jupyter][] 笔记导出 [Markdown][] 文件，并在其基础上构建Web文档站点

这是个人的翻译笔记，用于个人学习 PyTorch。

目前只翻译和转换了部分`*.py`文件(官方使用Sphinx-Gallery将它们转成[Sphinx-Doc][]文档并导出 [Jupyter][] 笔记) ，没有处理任何 `*.rst`(单纯的 [Sphinx-Doc][] 文档)

## 环境

这个工程在 Ubuntu 1604, 1804下，使用 Python3.6 运行和构建，没有测试过其它环境。

**强烈**建议为这个项目使用单独的 [venv][] 或 [Conda][] 环境

### 包依赖

可用 [pip][], [Pipenv] 或 [Conda][] 为这个项目安装所需的包：

- [pip][]:

  ```console
  pip install -r requirements.txt
  ```

- [Pipenv][]:

  ```console
  pipenv install
  ```

- [Conda][]:

  ```console
  conda install -y jupyter nbconvert tqdm pandas matplotlib scikit-image pillow=4.1.1 pygments
  conda install -y -c conda-forge jupyterlab
  conda install -y pytorch torchvision cudatoolkit=9.0 -c pytorch
  pip install mkdocs pymdown-extensions mkdocs-material mkdocs-pdf-export-plugin
  ```

## 运行 Jupyter Lab/Notebook

入门指南的翻译以 [Jupyter][] 笔记的形式保存在 `notebooks` 子目录中。

要启动 [Jupyter][] lab/notebook web 服务程序，运行：

```console
jupyter-lab
```

或

```console
jupyter-notebook
```

在 Web 界面中进入 `notebooks` 子目录，可以找到所有笔记。

## 构建 Web 文档站点

这个项目使用[MkDocs][]将多个由笔记导出的Markdown文件合并生成一个Web文档站点。

1. 把笔记导出为Markdown文件:

   ```console
   python tools/nbtomd.py
   ```

1. 构建 Web 文档

   ```console
   mkdocs build
   ```

1. 启动 Web 文档服务器：

   ```console
   mkdocs serve
   ```

   然后在浏览器中访问 <http://localhost:8000/>

## 其它

### Jupyter 无法以 LaTeX/PDF 格式导出含有中文的笔记

采用来自 <https://github.com/jupyter/notebook/issues/2848#issuecomment-372736199> 的方法：

1. 安装 texlive 和 pandoc

   ```console
   sudo apt install texlive-xetex pandoc
   ```

1. 修改 `nbconvert` `Article` 的 `LaTeX` 模板文件

   找到文件 `site-packages/nbconvert/templates/latex/article.tplx`,

   在 `\documentclass[11pt]{article}` 之后加上中文字体定义，修改后的内容形如:

   ```latex
   ((* block docclass *))
   \documentclass[11pt]{article}
       % 中文问题: https://github.com/jupyter/notebook/issues/2848#issuecomment-372736199
       \usepackage{xeCJK}
       \setCJKmainfont{Noto Sans CJK SC}
       \setCJKmonofont{Noto Sans Mono CJK SC}
   ((* endblock docclass *))
   ```

具体采用哪个的字体应以实际情况为准。

[Jupyter]: https://jupyter.org/
[Conda]: https://packaging.python.org/key_projects/#conda
[pip]: https://packaging.python.org/key_projects/#pip
[Pipenv]: https://packaging.python.org/key_projects/#pipenv
[venv]: https://packaging.python.org/key_projects/#venv
[Sphinx-Doc]: http://www.sphinx-doc.org/
[reST]: http://www.sphinx-doc.org/en/master/usage/restructuredtext/ "reStructuredText (reST)"
[Sphinx-Gallery]: https://sphinx-gallery.github.io/
[MkDocs]: https://www.mkdocs.org
[Markdown]: https://www.markdownguide.org/
