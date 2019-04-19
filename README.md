# pytorch-tutorials-notebooks-zhs

[PyTorch tutorials](https://github.com/pytorch/tutorials/) 的中文翻译笔记。

点击这个链接直接访问这个项目生成的Web文档站点：<https://tanbro.github.io/pytorch-tutorials-notebooks-zhs/>

官方教程以*带有[Sphinx-Doc][]扩展[reST][]格式注释的Python源代码*的形式制作了Web文档并导出[Jupyter][]笔记。

而这个项目除了翻译，修改还有:

- 使用[Jupyter][]笔记文件保存说明和代码片段
- 从[Jupyter][]笔记导出[Markdown][]文件，并在其基础上构建Web文档站点

这是个人的翻译笔记，用于个人学习 PyTorch。

目前只翻译和转换了部分`*.py`文件(官方使用Sphinx-Gallery将它们转成[Sphinx-Doc][]文档并导出[Jupyter][]笔记) ，没有处理任何 `*.rst`(单纯的[Sphinx-Doc][]文档)

## 环境

这个工程采在Ubuntu1604,1804下，使用Python3.6运行和构建，没有测试过其它环境。

**强烈**建议为这个项目单独新建一个专用的[venv][]或[Conda][]环境

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
  conda install -y jupyter nbconvert tqdm pandas matplotlib scikit-image pygments
  conda install -y -c conda-forge jupyterlab
  conda install -y pytorch torchvision cudatoolkit=9.0 -c pytorch
  pip install mkdocs pymdown-extensions mkdocs-material mkdocs-pdf-export-plugin
  ```

## 运行 Jupyter Lab/Notebook

入门指南的翻译以[Jupyter][]笔记的形式保存在`notebooks`目录，启动[Jupyter][] lab/notebook:

```console
jupyter-lab
```

或者

```console
jupyter-notebook
```

在Web界面中进入`notebooks`目录可以找到所有笔记。

## 构建Web文档站点

这个项目使用[MkDocs][]将多个由笔记导出的Markdown文件合并生成一个Web文档站点。

1. 把笔记导出为Markdown文件:

   ```console
   python tools/nbtomd.py
   ```

1. 构建Web文档

   ```console
   mkdocs build
   ```

1. 运行Web文档服务器，访问 <http://localhost:8000/> 查看

   ```console
   mkdocs serve
   ```

## Jupyter Notebook 无法导出含有中文 LaTeX/PDF 的问题

采用来自 <https://github.com/jupyter/notebook/issues/2848#issuecomment-372736199> 的方法：

1. 安装 texlive 和 pandoc

   ```console
   sudo apt install texlive-xetex pandoc

1. 修改 Article 的 LaTeX 模板

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
[reST]: http://www.sphinx-doc.org/en/master/usage/restructuredtext/ "reStructuredText (reST)"
[Sphinx-Gallery]: https://sphinx-gallery.github.io/
[MkDocs]: https://www.mkdocs.org
[Markdown]: https://www.markdownguide.org/
