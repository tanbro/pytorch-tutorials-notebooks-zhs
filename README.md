# pytorch-tutorials-notebooks-zhs

[PyTorch tutorials](https://github.com/pytorch/tutorials/) 的中文翻译笔记。

点击这个链接直接访问其Web文档：<https://tanbro.github.io/pytorch-tutorials-notebooks-zhs/>

官方教程以*带有[Sphinx-Doc][]扩展[rST][]格式注释的Python源代码*的形式制作了Web文档并导出[Jupyter][]笔记。

而这个项目除了翻译，修改还有:

- 使用 Jupyter Notebook 保存说明和代码片段
- 由 Jupyter Notebook 导出Markdown文件，并在其基础上构建Web文档

这是个人的翻译笔记，用于个人学习 PyTorch。

目前只翻译和转换了部分 `*.py`文件(用 Sphinx-Gallery 制作了 Jupyter Notebook) ，没有处理任何 `*.rst`(单纯的 Sphinx-Doc 文档)

## 环境

这个工程采在 Ubuntu 1604, 1804 下，使用 Python 3.6 运行和构建，没有测试过其它环境。

**强烈**建议为这个项目单独新建一个专用的 [venv][] 或 [Conda][] 环境

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
  conda install -y jupyter tqdm pandas matplotlib scikit-image pygments
  conda install -y pytorch torchvision cudatoolkit=9.0 -c pytorch
  pip install pymdown-extensions mkdocs-material
  ```

## 运行 Jupyter Notebook

入门指南的翻译以[Jupyter][]笔记的形式保存在`notebooks`目录，启动[Jupyter][] notebooks:

```console
jupyter-notebook
```

在 `notebooks` 目录可以找到所有笔记。

## 构建 Web 文档

这个项目使用 [MkDocs][] 将多个由笔记本导出 Markdown 文档生成一个 Web 文档。

1. 把笔记导出为Markdown文件:

   ```console
   python tools/nb_export_mk.py
   ```

1. 构建Web文档

   ```console
   mkdocs build
   ```

1. 运行Web文档服务器，访问 <http://localhost:8000/> 查看

   ```console
   mkdocs serve
   ```

## Jupyter Notebook 无法导出含有中文 latex/pdf 的问题

采用来自 <https://github.com/jupyter/notebook/issues/2848#issuecomment-372736199> 的方法：

1. 安装 texlive

   ```console
   sudo apt install texlive-xetex
   ```

1. 安装 pandoc

   ```console
   sudo apt install pandoc
   ```

1. 修改 Aritcal tex 模板

   找到文件 `site-packages/nbconvert/templates/latex/article.tplx`,

   在 `\documentclass[11pt]{article}` 之后加上中文字体定义:

   ```latex
   ((* block docclass *))
   \documentclass[11pt]{article}
       % 中文问题: https://github.com/jupyter/notebook/issues/2848#issuecomment-372736199
       \usepackage{xeCJK}
       \setCJKmainfont{Noto Sans CJK SC}
       \setCJKmonofont{Noto Sans Mono CJK SC}
   ((* endblock docclass *))
   ```

具体采用哪个的字体应以实际情况为准

[Jupyter]: https://jupyter.org/
[Conda]: https://packaging.python.org/key_projects/#conda
[pip]: https://packaging.python.org/key_projects/#pip
[Pipenv]: https://packaging.python.org/key_projects/#pipenv
[venv]: https://packaging.python.org/key_projects/#venv
[Sphinx-Doc]: http://www.sphinx-doc.org/
[MkDocs]: https://www.mkdocs.org
[rST]: reStructuredText "reStructuredText (reST)"
